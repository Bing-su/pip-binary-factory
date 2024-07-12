import os
import subprocess
import sys
from pathlib import Path
from platform import machine, system


def build(os_: str, arch: str, platform: str):
    os.environ["GOOS"] = os_
    os.environ["GOARCH"] = arch

    if (
        os_ == "linux"
        and arch == "amd64"
        and "musl" not in platform
        and system() == "Linux"
        and machine() == "x86_64"
    ):
        os.environ["CGO_ENABLED"] = "1"
    else:
        os.environ["CGO_ENABLED"] = "0"

    args = [
        sys.executable,
        "-m",
        "build",
        "-w",
        "--installer",
        "uv",
        f"--config-setting=--plat-name={platform}",
    ]

    subprocess.run(args, check=True)  # noqa: S603

    if "manylinux" not in platform:
        return

    arch = platform.split("_", maxsplit=1)[-1]
    platform_tag = f"manylinux_2_17_{arch}.manylinux2014_{arch}"
    if arch != "x86_64":
        platform_tag += f".musllinux_1_1_{arch}"

    whl = next(Path("dist").glob(f"*{platform}*"))

    args = [
        sys.executable,
        "-m",
        "wheel",
        "tags",
        "--remove",
        "--platform-tag",
        platform_tag,
        str(whl),
    ]
    subprocess.run(args, check=True)  # noqa: S603


def main():
    matrix = [
        ("windows", "amd64", "win_amd64"),
        ("windows", "arm64", "win_arm64"),
        ("darwin", "amd64", "macosx_10_7_x86_64"),
        ("darwin", "arm64", "macosx_11_0_arm64"),
        ("linux", "amd64", "manylinux2014_x86_64"),
        ("linux", "amd64", "musllinux_1_1_x86_64"),
        ("linux", "arm64", "manylinux2014_aarch64"),
        ("linux", "s390x", "manylinux2014_s390x"),
        ("linux", "ppc64le", "manylinux2014_ppc64le"),
    ]

    for os_, arch, platform in matrix:
        build(os_, arch, platform)


if __name__ == "__main__":
    main()
