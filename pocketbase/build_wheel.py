import os
import subprocess
import sys
from pathlib import Path
from platform import machine, system

linux_platform_map = {
    "manylinux_2_28_x86_64": "manylinux_2_28_x86_64",
    "musllinux_1_1_x86_64": "manylinux_2_17_x86_64.manylinux2014_x86_64.musllinux_1_1_x86_64",
    "manylinux2014_aarch64": "manylinux_2_17_aarch64.manylinux2014_aarch64.musllinux_1_1_aarch64",
    "manylinux2014_s390x": "manylinux_2_17_s390x.manylinux2014_s390x.musllinux_1_1_s390x",
    "manylinux2014_ppc64le": "manylinux_2_17_ppc64le.manylinux2014_ppc64le.musllinux_1_1_ppc64le",
}


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
        os.environ["CC"] = "zig cc -target x86_64-linux-gnu"
        os.environ["CXX"] = "zig c++ -target x86_64-linux-gnu"
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

    if "linux" not in platform:
        return

    platform_tag = linux_platform_map[platform]

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
        ("linux", "amd64", "manylinux_2_28_x86_64"),
        ("linux", "amd64", "musllinux_1_1_x86_64"),
        ("linux", "arm64", "manylinux2014_aarch64"),
        ("linux", "s390x", "manylinux2014_s390x"),
        ("linux", "ppc64le", "manylinux2014_ppc64le"),
    ]

    for os_, arch, platform in matrix:
        build(os_, arch, platform)


if __name__ == "__main__":
    main()
