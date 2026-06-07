# Build Status — COMPLETE

**Updated:** 2026-06-07

## Result
- **296/296** videos enumerated, transcribed, and turned into wiki pages. 0 download failures.
- **992,562** words of transcript distilled to **3,488** atomic method-claims.
- Canonical spec + 8 decision pages + contradictions page written and cross-checked.
- Integrity: 296/296 video pages present (0 missing); 0 unresolved `[[id]]` citations.

## Classification (method-density based, not keyword count)
- STRATEGY 202 · PICKS 46 · MACRO 44 · HYPE 4
- Signal 5: 53 videos · 4: 33 · 3: 38 · 2: 45 · 1: 124 · 0: 3
- Highest-signal core: STOCKS & OPTIONS MASTERCLASS (86 claims), "ONLY 1 STRIKE PRICE WORKS" (75),
  "SELLING IS 7X MORE PROFITABLE" (72).

## Pipeline (all reproducible from repo)
1. `_video_index.txt` — 296 videos (id|title|duration)
2. `_download_transcripts.sh` → `raw_transcripts/*.vtt`
3. `_clean_vtt.py` → `transcripts/*.txt`
4. `_extract.py` → `wiki/videos/*.md`, `_meta/claims.jsonl`, `_meta/video_categories.json`
5. `_route.py` → `_meta/digests/<dimension>.md`
6. `_decision_pages.py` → `wiki/strategy/<dimension>.md`
7. `_index.py` → `_meta/index.json` (+ integrity verification)

To rebuild from scratch: run steps 2→7 in order.

## Strategy recovered (one line)
Portfolio-secured ~2-year (LEAPS) puts on undervalued quality names/indexes, sold into fear,
premium recycled into shares + barely-OTM 2-year calls, sized by an assignment-value ratio that
survives a 50% crash. Full spec: `wiki/strategy/STRATEGY_SPEC.md`.

## Notes
- `/home/john/repos` is not a git repo — nothing to commit/push.
- yt-dlp at `~/.local/bin/yt-dlp` (user install).
