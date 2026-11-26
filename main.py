#!/usr/bin/env python3
"""Entry point for make.fun bounty news-image-20261126.

Copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(or /output/entry.png). Python 3.13 standard library only, no network.
Deterministic: the copied bytes are exactly the bundled file's bytes.
"""
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if not data or len(data) > MAX_BYTES:
        print("error: entry.png size %d out of range" % len(data),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
