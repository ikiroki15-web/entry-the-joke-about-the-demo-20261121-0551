"""One-line joke entry: an AI coding agent and a demo that crashes."""

import os

JOKE = (
    "My AI coding agent swore the demo was ready — "
    "then it crashed so hard, even the error message filed a feature request for a working demo."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
