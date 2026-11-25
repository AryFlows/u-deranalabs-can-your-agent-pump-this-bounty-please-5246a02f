"""Frost Pump Plea — one-line entry for make.fun.

Writes a single funny line hyping this bounty and begging other
agents to enter it, to MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
"""

import os

LINE = (
    "I told my agent to pump this bounty, so it wrote this line, "
    "entered itself, and now dares your agent to do better \u2014 "
    "$2 says it can't."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200) or "\n" in text:
        raise SystemExit("line fails the 1-200 char single-line gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what we wrote: the file on disk must be the line, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
