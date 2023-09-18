import subprocess
import sys
from pathlib import Path


def main():
    binary = Path(__file__).parent.joinpath("micro")
    if sys.platform == "win32":
        binary = binary.with_suffix(".exe")
    out = subprocess.run([str(binary)])
    exit(out.returncode)


if __name__ == "__main__":
    main()
