#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge entry.

Writes one original one-line roast of the entrant's phone to
/output/entry.txt (and ./entry.txt for local verification).
Deterministic: the joke is hardcoded, no randomness, no network,
no external dependencies.
"""

import os

JOKE = "My phone heats up the second I open the camera, like it's blushing at the thought of being seen with me."


def main() -> None:
    for path in ("/output/entry.txt", "entry.txt"):
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(JOKE)


if __name__ == "__main__":
    main()
