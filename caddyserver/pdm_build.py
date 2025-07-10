from __future__ import annotations

import os
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path
from typing import TYPE_CHECKING

try:
    import tomllib
except ImportError:
    import tomli as tomllib

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "caddy"
pwd = Path(__file__).parent
with pwd.joinpath("pyproject.toml").open("rb") as f:
    pyproject = tomllib.load(f)
VERSION: str = pyproject["project"]["version"]


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def build(output: str, plugins: list[str] | None = None) -> None:
    go = shutil.which("go")
    if go is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    # 1. Install xcaddy
    args = ["eget", "https://github.com/caddyserver/xcaddy", "--asset=^deb"]
    xcaddy = Path.cwd().joinpath("xcaddy").with_suffix(sysconfig.get_config_var("EXE"))
    subprocess.run(args, check=True)

    # 2. Build caddy
    os.environ.setdefault("CGO_ENABLED", "0")
    if not plugins:
        plugins = []

    args = [
        str(xcaddy),
        "build",
        f"v{VERSION}",
        "--output",
        output,
    ]

    for plugin in plugins:
        args.extend(["--with", plugin])

    subprocess.run(args, check=True)
    Path(output).chmod(0o777)


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    config = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**config, **context.builder.config_settings}

    plugins = context.builder.config_settings.get("--caddy-plugins", "")
    if not isinstance(plugins, str):
        msg = "Expected --caddy-plugins to be a string"
        raise TypeError(msg)
    plugins = [p.strip() for p in plugins.split(",") if p.strip()]
    if not plugins:
        plugins = [
            "github.com/greenpau/caddy-security",
            "github.com/sjtug/caddy2-filter",
            "github.com/mholt/caddy-webdav",
            "github.com/abiosoft/caddy-exec",
            "github.com/aksdb/caddy-cgi/v2",
            "github.com/ggicci/caddy-jwt",
        ]

    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path), plugins)


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    if Path(context.build_dir).exists():
        shutil.rmtree(context.build_dir)
