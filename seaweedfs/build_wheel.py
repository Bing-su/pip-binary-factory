# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "wheel",
# ]
# ///
import os
import subprocess
import sys
from pathlib import Path


def build(os_: str, arch: str, platform: str):
    os.environ["GOOS"] = os_
    os.environ["GOARCH"] = arch
    os.environ["CGO_ENABLED"] = "0"

    args = [
        "uv",
        "build",
        "--wheel",
        "--config-setting=--seaweedfs-tags=5BytesOffset,sqlite",
        f"--config-setting=--plat-name={platform}",
    ]

    subprocess.run(args, check=True)

    if "manylinux" not in platform:
        return

    arch = platform.split("_", maxsplit=1)[-1]

    whl = next(Path("dist").glob(f"*{platform}*"))

    args = [
        sys.executable,
        "-m",
        "wheel",
        "tags",
        "--remove",
        "--platform-tag",
        f"manylinux_2_17_{arch}.manylinux2014_{arch}.musllinux_1_1_{arch}",
        str(whl),
    ]
    subprocess.run(args, check=True)


def main():
    matrix = [
        ("windows", "amd64", "win_amd64"),
        ("windows", "arm64", "win_arm64"),
        ("darwin", "arm64", "macosx_11_0_arm64"),
        ("linux", "amd64", "manylinux2014_x86_64"),
        ("linux", "arm64", "manylinux2014_aarch64"),
    ]

    for os_, arch, platform in matrix:
        build(os_, arch, platform)


if __name__ == "__main__":
    main()
