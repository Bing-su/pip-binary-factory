from __future__ import annotations

import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

try:
    import tomllib
except ImportError:
    import tomli as tomllib

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "act"

pwd = Path(__file__).parent
with pwd.joinpath("pyproject.toml").open("rb") as f:
    pyproject = tomllib.load(f)
VERSION: str = pyproject["project"]["version"]


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return platform.system() == "Windows"


def build(output: str) -> None:
    go = shutil.which("go")
    if go is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    if "GOPATH" in os.environ:
        gopath = os.environ["GOPATH"]
    else:
        # https://go.dev/wiki/GOPATH
        gopath = str(Path.home().joinpath("go"))
        os.environ["GOPATH"] = gopath

    binary = Path(gopath, "bin", NAME)
    if is_windows():
        binary = binary.with_suffix(".exe")
    os.environ.setdefault("CGO_ENABLED", "0")

    args = [
        go,
        "install",
        "-trimpath",
        "-ldflags",
        f"-s -w -X main.version={VERSION}",
        f"github.com/nektos/act@v{VERSION}",
    ]

    cwd = Path(__file__).parent
    subprocess.run(args, check=True, cwd=cwd)  # noqa: S603

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    shutil.move(binary, output)
    Path(output).chmod(0o777)


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    setting = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**setting, **context.builder.config_settings}

    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path))
