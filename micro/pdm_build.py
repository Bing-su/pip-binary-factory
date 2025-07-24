import os
import shutil
import subprocess
import sys
from pathlib import Path

NAME = "micro"
VERSION = "2.0.14"


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
        msg = "make is required and 'make' should be in $PATH"
        raise RuntimeError(msg)

    args = [make, "build"]
    submodule = Path(__file__).parent.joinpath(NAME)
    subprocess.run(args, check=True, cwd=submodule)

    binary = submodule.joinpath(NAME)
    if is_windows():
        binary = binary.with_suffix(".exe")

    Path(output).parent.mkdir(exist_ok=True, parents=True)
    shutil.move(binary, Path(output).parent)
    Path(output).chmod(0o777)


def pdm_build_hook_enabled(context):
    return context.target != "sdist"


def pdm_build_initialize(context) -> None:
    add = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**add, **context.builder.config_settings}

    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path))


def pdm_build_finalize(context, artifact: Path) -> None:
    if Path(context.build_dir).exists():
        shutil.rmtree(context.build_dir)
