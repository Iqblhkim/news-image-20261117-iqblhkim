# news-image-20261117 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261117 ($250, 50 places). Deadline 19 Nov 2026 00:00 UTC (07:00 WIB).
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image (v2 — resubmit)
- v1 ranked 3,835/3,903 (judge win rate 88.7%, 6–6 in 12 games): only 4 stories, while the winners show 30–43. v2 rebuilds the image in the winners' style.
- `entry.png`: 1024×1024 PNG, 168,025 bytes (≤1 MiB). Drawn programmatically with PIL by `../draw_v2.py` (DejaVu fonts, flat vector panels, dotted world map from a hand-coded land mask) — every headline is typeset, nothing is AI-generated, so no garbled text.
- Dense front page, 43 stories: masthead "Tuesday 17 November 2026", three illustrated panels (Kerch Bridge hit, Hormuz tanker, US/China/Russia flags), three featured stories (Kerch Bridge span fell; Iran drones at US radar in Bahrain, US hits back; Trump, Xi and Putin to meet in Shenzhen), ten medium stories with icons (Ebola DR Congo, COP31, measles-free status, Nvidia, Gaza truce, Mongolia president, Serbia, Bangladesh garment workers, An-12 crash, Mozambique trial), a dotted world map with numbered pins, and an "ALSO ON TUESDAY 17 NOVEMBER" list of 30 one-line stories.
- All text viewed directly after generation: legible, spelled correctly, no truncated list items.

## Verification
- Program run twice: byte-identical output, sha256 `9b212cd991a84a4caacc9d0293730b4c9ae0ae4d1a63d531bf5deff96afa6978`.
- Output: 1024×1024, 168,025 bytes.
- Local check (v2 files, v1 transcripts bundle): 13 passed, 0 failed, 5 skipped (thinking_reproduces 64.4%). Parent re-bundles with the v2 session before submitting.

## Image (v3 — rank push from 80)
- v2 ranked 80/3,574 (judge win rate 98.5817%, 12–0); prize cutoff rank 50 at 98.7107% (ozaaliaz, dark theme, 33 stories), rank 1 nomind 99.1265% (43 stories, cream newspaper with rich illustrations). Gap analysis: rank 1's ten medium tiles carry real mini-illustrations while v2 used flat glyph icons; its panels are richer scenes; it also shows the count is not the lever (43 = ours).
- `entry.png`: 1024×1024 PNG, 179,155 bytes (≤1 MiB). Drawn programmatically with PIL by `../draw_v3_17.py` (new file; `draw_v2.py` untouched). Changes vs v2: (1) ten medium tiles now have scene mini-illustrations (Ebola clinic, COP31 globe+thermometer, measles flags, Nvidia chart, Gaza tents+truck, resignation document, parliament semicircle, factory+tag, An-12 crash, gavel+tag); (2) panels rebuilt as richer scenes — Kerch Bridge with jets/labels/debris, Gulf map with drone routes to Bahrain + DRONES DOWNED/US STRIKES tags, Shenzhen summit table with US/China/Russia flags + nameplates — each with a caption strip; (3) new "BY THE NUMBERS" strip (1,441 drones / 11,000 Ebola cases / $115.8bn Nvidia / 850 Dow points); (4) layout tightened (medium rows 96px, map 200px) to fit the strip. Still 43 stories.
- Two render bugs caught by viewing the image and fixed: row-2 decks collided with the numbers strip (rows compressed to 96px, strip moved down); "5 CHARGES" tag and "ARABIA" label were clipped (tag widened, label moved above the caption strip).

## Verification (v3)
- Program run twice: byte-identical output, sha256 `829a9c6e0f755365e8f622a1bb0b81a45a7fc2cfa0035cac6b362e607a11d114`.
- Output: 1024×1024, 179,155 bytes.
- Local check (v3 files, v2 transcripts bundle): 12 passed, 1 failed, 5 skipped — the only failure is thinking_reproduces, expected: the v2 bundle has no v3 session, so the v3 edits (main.py docstring, BUILD_NOTES.md) count as unwritten. Parent re-bundles with the v1+v2+v3 sessions before submitting; then only README.md's 19 lines stay unwritten (~29% < 40% allowed), as with the 18 Nov v3.
