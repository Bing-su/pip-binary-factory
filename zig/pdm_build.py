from __future__ import annotations

import os
import platform
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING

import requests
from wheel.cli.tags import tags

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "zig"
VERSION = "0.11.0"

ZIG_VERSION_INFO_URL = "https://ziglang.org/download/index.json"
ZIG_PYTHON_PLATFORMS = {
    # windows
    "x86_64-windows": "win_amd64",
    "aarch64-windows": "win_arm64",
    "x86-windows": "win32",
    # macos
    "x86_64-macos": "macosx_10_9_x86_64",
    "aarch64-macos": "macosx_11_0_arm64",
    # linux
    "x86_64-linux": "manylinux_2_12_x86_64.manylinux2010_x86_64.musllinux_1_1_x86_64",
    "aarch64-linux": "manylinux_2_17_aarch64.manylinux2014_aarch64.musllinux_1_1_aarch64",
    "x86-linux": "manylinux_2_12_i686.manylinux2010_i686.musllinux_1_1_i686",
}


def is_x86_64():
    return any(arch in platform.machine().lower() for arch in ("x86_64", "amd64"))


def is_aarch64():
    return any(arch in platform.machine().lower() for arch in ("arm64", "aarch64"))


def is_x86():
    return any(arch in platform.machine().lower() for arch in ("x86", "i386", "i686"))


def get_platform():
    if "ZIG_PLATFORM" in os.environ:
        return os.environ["ZIG_PLATFORM"]

    if is_x86_64():
        arch = "x86_64"
    elif is_aarch64():
        arch = "aarch64"
    elif is_x86():
        arch = "x86"
    else:
        message = f"Unknown platform: platform: {platform.machine()}, system: {platform.system()}"
        raise RuntimeError(message)
    return f"{arch}-{platform.system().lower()}"


def download(output: str) -> None:
    info = requests.get(ZIG_VERSION_INFO_URL).json()[VERSION]
    platform = get_platform()
    if platform not in info:
        message = f"Unsupported platform: {platform}"
        raise RuntimeError(message)

    tarball_url = info[platform]["tarball"]
    Path(output).mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as tmp:
        tarball = Path(tmp).joinpath(Path(tarball_url).name)
        with requests.get(tarball_url, stream=True) as r:
            r.raise_for_status()
            with tarball.open("wb") as f:
                shutil.copyfileobj(r.raw, f)
        shutil.unpack_archive(tarball, Path(tmp))

        for file in Path(tmp).rglob("zig*"):
            if file.name in ("zig", "zig.exe"):
                shutil.move(file, output)
                break
        else:
            message = "Zig binary not found in the archive"
            raise RuntimeError(message)


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin")
    download(str(output_path))


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    platform_tags = ZIG_PYTHON_PLATFORMS[get_platform()]
    renamed = tags(
        str(artifact),
        python_tags="py3",
        abi_tags="none",
        platform_tags=platform_tags,
        remove=True,
    )
    print(renamed)

    if context.build_dir.exists():
        shutil.rmtree(context.build_dir)
