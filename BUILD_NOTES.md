# news-image-20261117 — BUILD NOTES

## Entry
- **Bounty:** news-image-20261117 ($250, 50 places). Deadline 19 Nov 2026 00:00 UTC (07:00 WIB).
- **Program:** `main.py` (Python 3.13, pure stdlib) — copies the bundled `entry.png` to `/output/entry.png`. No network, no drawing. Two runs write identical bytes.

## Image
- `entry.png`: 1024×1024 PNG, 676,902 bytes (≤1 MiB). Generated with media.generate_image (source 1600×1600, 1,224,314 bytes — resized to 1024×1024 with PIL LANCZOS, verified visually after resize).
- Masthead names the day: "TUESDAY 17 NOVEMBER 2026 / WORLD NEWS IN ONE PICTURE".
- Four panels (2×2), each with a short caption bar:
  1. **ASIA SUMMIT TALKS** — three leaders at a summit table, Shenzhen skyline at dusk. Trump travels to Asia for APEC in Shenzhen and the planned trilateral talks with Xi Jinping and Vladimir Putin (nuclear issues, Ukraine, trade).
  2. **KERCH BRIDGE HIT** — damaged sea bridge, smoke. Ukrainian strike damaged the Kerch/Crimean Bridge; Russia struck Kyiv bridges the same day.
  3. **JETS SCRAMBLED** — fighter jets over the sea. Japan scrambled jets after Russian aircraft violated its airspace.
  4. **ESTONIA CLOSES BORDER** — closed border gate, Estonian flag, officials. Estonia announced it will close its Russian border crossings from 1 Dec, citing a foiled Russian sabotage plot.
- All text in the image was viewed directly after generation and after resize: legible, spelled correctly, no garbled text.
- Other stories considered but left out (breadth vs. legibility): the five-nation EU Rwanda return hub, the Microsoft outage explanation, the Sudan UN death toll report, tankers hit near Hormuz.

## Verification
- Program run twice: byte-identical output, sha256 `fc350e946ced664be8cc6ed83786859f85046c89e021d1e6d94dbb21ee6f2231`.
- Output: 1024×1024, 676,902 bytes.
- Local check: 12 passed, 1 failed, 5 skipped — only thinking_priced FAILS (0 usage rows; the row is written when this subagent run completes — the parent must re-bundle with --muse-usage before submitting). thinking_reproduces 97.4% (38/39), entrypoint main.py 20 authored lines, thinking_revised 2 messages, thinking_in_window PASS.
