"""Write this entry's image to the make.fun output directory."""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def check_source() -> int:
    """Return the source size, or exit with a message if it is not a valid entry."""
    size = os.path.getsize(SOURCE)
    with open(SOURCE, "rb") as f:
        signature = f.read(8)
    if signature != PNG_SIGNATURE:
        raise SystemExit(f"{SOURCE} is not a PNG file (bad signature)")
    if size > MAX_BYTES:
        raise SystemExit(f"{SOURCE} is {size} bytes, over the {MAX_BYTES} byte limit")
    return size


def main() -> None:
    check_source()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print(os.path.getsize(target))


if __name__ == "__main__":
    main()
