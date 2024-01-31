import shutil
import subprocess
import sys

if __name__ == "__main__":
    zig = shutil.which("zig")
    if zig is None:
        msg = "Not found 'zig' in $PATH"
        raise RuntimeError(msg)

    subprocess.run([zig, *sys.argv[1:]])
