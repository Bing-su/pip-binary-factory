from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

try:
    import tomllib
except ImportError:
    import tomli as tomllib

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "weed"
pwd = Path(__file__).parent
with pwd.joinpath("pyproject.toml").open("rb") as f:
    pyproject = tomllib.load(f)
VERSION: str = pyproject["project"]["version"]


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def build(output: str, tags: str = "") -> None:
    go = shutil.which("go")
    if go is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    os.environ.setdefault("CGO_ENABLED", "0")
    os.environ.setdefault("GODEBUG", "http2client=0")

    args = [
        go,
        "build",
        "-o",
        output,
        "-trimpath",
        "-ldflags",
        "-s -w -extldflags -static -X github.com/seaweedfs/seaweedfs/weed/util.COMMIT=pypi",
    ]

    if tags:
        args.extend(["-tags", tags])

    args.append("./weed")

    submodule = Path(__file__).parent.joinpath("seaweedfs")
    subprocess.run(args, check=True, cwd=submodule)
    Path(output).chmod(0o777)


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    setting = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**setting, **context.builder.config_settings}

    tags: str = context.builder.config_settings.get("--seaweedfs-tags", "")

    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path), tags)


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    if Path(context.build_dir).exists():
        shutil.rmtree(context.build_dir)
