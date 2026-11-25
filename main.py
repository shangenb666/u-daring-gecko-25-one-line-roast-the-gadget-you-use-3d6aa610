"""Write the entry line for make.fun's "One-Line Roast: The Gadget You
Use Every Day" bounty.

One original line, at most 200 characters, roasting a gadget used every
day. The program writes the line to entry.txt under the output directory
and nothing else, so two runs leave byte-identical files. It uses only
the standard library and never touches the network.
"""

import os
import sys
from pathlib import Path

LINE = (
    "My phone monitors my sleep, counts my steps and follows me "
    "everywhere I go \u2014 then dies at 4 p.m. like it's the one who "
    "had a long day."
)

MIN_CHARS = 1
MAX_CHARS = 200


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        sys.exit("line must be 1 to 200 characters")
    if LINE.strip() == "":
        sys.exit("line must not be only whitespace")
    output_dir.mkdir(parents=True, exist_ok=True)
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    output_dir.chmod(0o755)
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(LINE)} characters)")
