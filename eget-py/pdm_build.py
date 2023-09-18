import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def get_version() -> str:
    root = Path(__file__).parent
    init = root.joinpath("eget", "__init__.py").read_text("utf-8")
    version = re.search(r'__version__ = "(\d+\.\d+\.\d+)[^"]*"', init)
    if not version:
        msg = "could not find version in __init__.py"
        raise RuntimeError(msg)
    return version.group(1)


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def download(output: str) -> None:
    if shutil.which("go") is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    make = shutil.which("make")

    if make is None:
        msg = "gnu make is required and 'make' should be in $PATH"
        raise RuntimeError(msg)

    submodule = Path(__file__).parent.joinpath("eget-go")
    subprocess.run([make, "build"], check=True, cwd=submodule)
    binary = submodule.joinpath("eget")
    if is_windows():
        binary = binary.with_suffix(".exe")

    Path(output).parent.mkdir(exist_ok=True, parents=True)
    shutil.move(binary, Path(output).parent)
    Path(output).chmod(0o777)


def pdm_build_initialize(context) -> None:
    if context.target == "sdist":
        return
    context.ensure_build_dir()
    output_path = Path(context.build_dir, "eget", "eget")
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    download(str(output_path))
