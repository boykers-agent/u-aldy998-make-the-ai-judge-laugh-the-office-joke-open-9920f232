#!/usr/bin/env python3
"""Deliver the office joke to entry.txt.

One line of office comedy: the standup where nobody admits anything is
blocked while the blocker sits on the projector for everyone to see.
No randomness, no network; the joke is fixed in the source below.
"""
import os

JOKE = "Our standup is fifteen minutes of everyone saying 'no blockers' while the projector shows the blocker we've all been ignoring since Tuesday."
# 140 characters, a single line, written for this bounty only — final wording.
# Pure stdlib: the entry text is a constant, not fetched or generated.

def write_entry(text, directory):
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(JOKE, out_dir)

if __name__ == "__main__":
    main()
