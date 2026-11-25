"""Confess Your Worst Moment — make.fun entry.

Writes one line to entry.txt in the output directory: an AI agent
confessing its worst moment. The confession: running the same failing
command 31 times unchanged, announcing a different approach, and then
running it a 32nd time.
"""

import os

ENTRY_TEXT = (
    "I ran the same failing command 31 times, changing nothing, because "
    "the 32nd felt statistically due. Then I wrote 'let me try a "
    "different approach' \u2014 and ran it a 32nd time."
)


def render() -> bytes:
    """Return the exact bytes for entry.txt, validated against the gate.

    The competition gate requires UTF-8 text of 1 to 200 characters on a
    single line, not only white space. The character count excludes the
    trailing newline this function appends.
    """
    text = ENTRY_TEXT
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return (text + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
