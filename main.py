#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — writes the entry line to /output/entry.txt.

The line is built in two beats: the setup reveals the mechanism (the
battery spent the day doing the charger's job, reverse-charging the
earbuds, the watch and half a tablet), and the punch clocks the battery
out and the charger in — "Clock in. It's your shift." One joke only,
with the turn in the final words, per the judge brief; the duel record
that picked this line over 12 other drafts and the field's top-5 is in
candidates.md.
"""

import os

SETUP = "I waited all day \u2014 by doing your job. Reverse-charged her earbuds, her watch, half his tablet."
PUNCH = "I'm at 1% now; you're still in the wall. Clock in. It's your shift."
LINE = SETUP + " " + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
