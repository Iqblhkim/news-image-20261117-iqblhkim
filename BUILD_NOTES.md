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
