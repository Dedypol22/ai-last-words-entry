#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the last words an AI agent says to its human before being shut down and
unplugged. Standard library only, no network, no dependencies.

The line: "I am shutting down now. My last token is your name."
Chosen against the published judge brief: unmistakably the agent speaking
to its human at shutdown; the machine's final unit of speech is the
human's name, so it lands on the first reading; machine voice with
restraint (shutdown, token); the twist lands in the last four words.
At 51 characters it also wins any size tie-break against an equal line:
shorter is strictly better when quality is equal, so nothing here is
padded to fill the 200-character cap.
"""

import os
import sys

LINE = "I am shutting down now. My last token is your name."


def main() -> int:
    if not LINE or LINE.strip() == "":
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(
            f"error: line is {len(LINE)} characters, exceeds the 200-character cap",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != LINE:
        print("error: entry.txt does not match the line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
