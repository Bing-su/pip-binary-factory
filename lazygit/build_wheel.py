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

linux_platform_map = {
    "manylinux_2_28_x86_64": "manylinux_2_28_x86_64.musllinux_1_2_x86_64",
    "manylinux_2_28_aarch64": "manylinux_2_28_aarch64.musllinux_1_2_aarch64",
    "manylinux_2_28_s390x": "manylinux_2_28_s390x.musllinux_1_2_s390x",
    "manylinux_2_28_ppc64le": "manylinux_2_28_ppc64le.musllinux_1_2_ppc64le",
    "manylinux_2_28_riscv64": "manylinux_2_28_riscv64.musllinux_1_2_riscv64",
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

    platform_tag = linux_platform_map.get(platform, platform)

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
        ("darwin", "amd64", "macosx_12_0_x86_64"),
        ("darwin", "arm64", "macosx_12_0_arm64"),
        ("linux", "amd64", "manylinux_2_28_x86_64"),
        ("linux", "arm64", "manylinux_2_28_aarch64"),
        ("linux", "s390x", "manylinux_2_28_s390x"),
        ("linux", "ppc64le", "manylinux_2_28_ppc64le"),
        ("linux", "riscv64", "manylinux_2_28_riscv64"),
        ("android", "arm64", "android_33_arm64_v8a"),
    ]

    for os_, arch, platform in matrix:
        build(os_, arch, platform)


if __name__ == "__main__":
    main()
