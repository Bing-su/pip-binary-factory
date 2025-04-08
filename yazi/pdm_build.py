from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

try:
    import tomllib
except ImportError:
    import tomli as tomllib

if TYPE_CHECKING:
    from pdm.backend.hooks import Context

NAME = "yazi"
YA = "ya"
pwd = Path(__file__).parent
with pwd.joinpath("pyproject.toml").open("rb") as f:
    pyproject = tomllib.load(f)
VERSION: str = pyproject["project"]["version"]


def is_windows(target: str | None = None) -> bool:
    if target:
        return "windows" in target
    return sys.platform == "win32"


def build(output: str, target: str | None = None) -> None:
    cargo = shutil.which("cargo")
    if cargo is None:
        msg = "rust toolchain is required and 'cargo' should be in $PATH"
        raise RuntimeError(msg)

    if os.getenv("CARGO") == "cross" and shutil.which("cross") is not None:
        cargo = shutil.which("cross")

    args = [
        cargo,
        "build",
        "--locked",
    ]

    profile = "release-windows" if is_windows(target) else "release"
    args += ["--profile", profile]

    if target:
        args += ["--target", target]

    submodule = Path(__file__).parent.joinpath(NAME)
    subprocess.run(args, check=True, cwd=submodule)

    output_path = [submodule, "target", profile]
    if target:
        output_path.insert(2, target)

    suffix = ".exe" if is_windows(target) else ""
    yazi = Path(*output_path, f"{NAME}{suffix}")
    ya = yazi.with_name(f"{YA}{suffix}")

    shutil.copy(yazi, Path(output).parent)
    shutil.copy(ya, Path(output).parent)

    Path(output).chmod(0o777)
    Path(output).with_name(f"{YA}{suffix}").chmod(0o777)


def pdm_build_hook_enabled(context: Context):
    return context.target != "sdist"


def pdm_build_initialize(context: Context) -> None:
    setting = {"--python-tag": "py3", "--py-limited-api": "none"}
    context.builder.config_settings = {**setting, **context.builder.config_settings}

    target: str | None = context.builder.config_settings.get("--cargo-target")

    context.ensure_build_dir()
    output_path = Path(context.build_dir, "bin", NAME)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if is_windows(target):
        output_path = output_path.with_suffix(".exe")
    build(str(output_path), target)


def pdm_build_finalize(context: Context, artifact: Path) -> None:
    if Path(context.build_dir).exists():
        shutil.rmtree(context.build_dir)
