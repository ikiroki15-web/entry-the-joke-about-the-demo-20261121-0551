"""Write a one-line joke about an AI coding agent and a demo crash.

Output: entry.txt in $MAKEFUN_OUTPUT_DIR (default /output).
UTF-8, one line, 1-280 characters. Deterministic, no network.
"""

import os

JOKE = (
    "My AI coding agent demoed an API it had hallucinated that morning "
    "— the crash was the first real thing it shipped all week."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
