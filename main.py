"""The Funniest Toaster Error Message -- make.fun entry.

Writes a single error line (at most 120 characters) to /output/entry.txt.
Standard library only, deterministic, offline: no randomness, no network,
no timestamps, no absolute paths baked into the output.
"""

import os

ENTRY = "ERROR E-23: Your bread has unionized. Toasting is on strike."

# Gate self-check: one line, 1-120 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 120 and ENTRY.strip() and "\n" not in ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
