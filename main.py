"""The Excuse That Almost Works — GTA 6 launch week.

Writes one line (17 words) to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt): the text a gamer sends the boss to skip work.
Pure stdlib, no network, no clock, no randomness.
"""

import os

EXCUSE = (
    "Sorry boss, my router died right as the 100GB launch update "
    "started, engineer can't come till Thursday."
)


def main() -> None:
    # Gate self-check (competition.yaml): one line, at most 20 words,
    # 1 to 140 characters of UTF-8 text, not only whitespace.
    words = EXCUSE.split()
    assert "\n" not in EXCUSE.strip(), "entry must be one line"
    assert 1 <= len(words) <= 20, f"word count {len(words)} exceeds 20"
    assert 1 <= len(EXCUSE.encode("utf-8")) <= 140, "entry over 140 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
