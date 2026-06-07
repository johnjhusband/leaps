# Moat Research — per-company wiki + the moat gate

**Purpose:** the golden line scores price-vs-earnings; it has no moat judgment. Moat is qualitative
("will competition wipe them out?" — see `wiki/strategy/moat.md`), so we **research each buy-list company**
and record a verdict. No-moat names are value traps and get pruned, exactly as Brandon rejects them.

## How it works
- One article per security here: `wiki/moats/<TICKER>.md` — verdict + reasoning + sources.
- The machine-readable verdicts live in `../../moat_verdicts.csv` (ticker, moat, basis, source).
- `build_universe.py` reads that file: a verdict of **`no`** or **`weak`** removes the name from the buy
  list (the **moat gate**). Names **not yet researched stay** (pending) — we only remove confirmed bad ones.

## Verdict values
- `yes` — durable competitive advantage + pricing power.
- `weak` — moat in doubt (e.g. AI/disruption question mark) → treated as a no, per Brandon ("not confident → pass").
- `no` — no moat; cheap is a trap.

## Status
Seeded with names Brandon judged on-camera (ground truth). The remaining buy-list names need research —
one article each. As articles land, update `moat_verdicts.csv` and rerun `build_universe.py`; the buy list
re-prunes automatically and `backtest.py`'s agree-count should climb.
