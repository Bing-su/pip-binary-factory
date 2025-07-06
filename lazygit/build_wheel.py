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

plat_map = {
    "manylinux2014_x86_64": "manylinux_2_17_x86_64.manylinux2014_x86_64.musllinux_1_1_x86_64",
    "manylinux2014_aarch64": "manylinux_2_17_aarch64.manylinux2014_aarch64.musllinux_1_1_aarch64",
    "manylinux2014_s390x": "manylinux_2_17_s390x.manylinux2014_s390x.musllinux_1_1_s390x",
    "manylinux2014_ppc64le": "manylinux_2_17_ppc64le.manylinux2014_ppc64le.musllinux_1_1_ppc64le",
}


def build(os_: str, arch: str, platform: str):
    os.environ["GOOS"] = os_
    os.environ["GOARCH"] = arch
    os.environ["CGO_ENABLED"] = "0"

    args = [
        "uv",
        "build",
        "--wheel",
        f"--config-setting=--plat-name={platform}",
    ]

    subprocess.run(args, check=True)  # noqa: S603

    if os_ != "linux":
        return

    platform_tag = plat_map.get(platform, platform)

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
        ("darwin", "amd64", "macosx_11_0_x86_64"),
        ("darwin", "arm64", "macosx_11_0_arm64"),
        ("linux", "amd64", "manylinux2014_x86_64"),
        ("linux", "arm64", "manylinux2014_aarch64"),
        ("linux", "s390x", "manylinux2014_s390x"),
        ("linux", "ppc64le", "manylinux2014_ppc64le"),
    ]

    for os_, arch, platform in matrix:
        build(os_, arch, platform)


if __name__ == "__main__":
    main()
