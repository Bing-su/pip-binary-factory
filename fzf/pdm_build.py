import os
import shutil
import subprocess
import sys
from pathlib import Path

NAME = "fzf"


def is_windows():
    if "GOOS" in os.environ:
        return os.environ["GOOS"] == "windows"
    return sys.platform == "win32"


def build(output: str) -> None:
    go = shutil.which("go")
    if go is None:
        msg = "golang is required and 'go' should be in $PATH"
        raise RuntimeError(msg)

    args = [go, "build", "-trimpath", "-ldflags", "-s -w", "."]

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
    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    if is_windows():
        output_path = output_path.with_suffix(".exe")
    build(str(output_path))
