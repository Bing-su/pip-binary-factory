import os
import shutil
import subprocess
import sys
from pathlib import Path


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def build(output: str) -> None:
    if shutil.which("go") is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    make = shutil.which("make")

    if make is None:
        msg = "gnu make is required and 'make' should be in $PATH"
        raise RuntimeError(msg)

    submodule = Path(__file__).parent.joinpath("micro")
    subprocess.run([make, "build"], check=True, cwd=submodule)
    binary = submodule.joinpath("micro")
    if is_windows():
        binary = binary.with_suffix(".exe")

    Path(output).parent.mkdir(exist_ok=True, parents=True)
    shutil.move(binary, Path(output).parent)
    Path(output).chmod(0o777)


def pdm_build_hook_enabled(context):
    return context.target != "sdist"


def pdm_build_initialize(context) -> None:
    context.ensure_build_dir()
    output_path = Path(context.build_dir, "micro_editor", "micro")
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path))
