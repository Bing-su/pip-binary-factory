from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "task"
VERSION = "3.42.1"


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def build(output: str) -> None:
    go = shutil.which("go")
    if go is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    args = [
        go,
        "build",
        "-o",
        output,
        "-trimpath",
        "-ldflags",
        f"-s -w -X github.com/go-task/task/v3/internal/version.version={VERSION} -X github.com/go-task/task/v3/internal/version.sum=pypi",
        "./cmd/task",
    ]

    submodule = Path(__file__).parent.joinpath(NAME)
    subprocess.run(args, check=True, cwd=submodule)
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
