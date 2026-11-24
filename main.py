"""Write one line of honest, funny error copy to /output/entry.txt.

Pure stdlib, fully deterministic: the same line every run.
"""

import os

LINE = (
    "Our server ran out of disk space mid-save, so your file exists "
    "only as a rumor. Clear some room and try again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
