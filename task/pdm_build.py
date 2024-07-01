from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from wheel.cli.tags import tags

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "task"
VERSION = "3.38.0"


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
        f"-s -w -X main.Version={VERSION}",
        "./cmd/task",
    ]

    submodule = Path(__file__).parent.joinpath(NAME)
    subprocess.run(args, check=True, cwd=submodule)
    Path(output).chmod(0o777)


@contextmanager
def fix_task_version():
    target = Path(__file__).parent.joinpath(NAME, "internal/version/version.go")
    content = target.read_text(encoding="utf-8")

    new = re.sub(r"return version", f'return "{VERSION}"', content)
    new = re.sub(
        r'return fmt.Sprintf\("%s \(%s\)", version, sum\)',
        f'return fmt.Sprintf("%s (%s)", "{VERSION}", "pypi")',
        new,
    )
    target.write_text(new, encoding="utf-8")

    try:
        yield
    finally:
        target.write_text(content, encoding="utf-8")


def pdm_build_hook_enabled(context):
    return context.target != "sdist"


def pdm_build_initialize(context) -> None:
    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    with fix_task_version():
        build(str(output_path))


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    renamed = tags(str(artifact), python_tags="py3", abi_tags="none", remove=True)
    print(renamed)
