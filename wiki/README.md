# LEAPS Wiki — Brandon (@InvestingWithBrandon) Strategy Knowledge Base

**Purpose:** Reverse-engineer and codify the investment/options strategy taught on the
@InvestingWithBrandon YouTube channel (296 videos) into a structure optimized for an LLM
(me) to query and **implement** — not for a human to read.

**Source:** 296 videos enumerated in `../_video_index.txt`. Auto-captions in
`../raw_transcripts/`, cleaned text in `../transcripts/`.

---

## Why this organization (optimized for LLM utility, not human reading)

A human-browsable wiki and an LLM-implementable knowledge base are different artifacts.
A human wants topic pages to skim. An LLM implementing a strategy wants: **one canonical
spec to execute from, every parameter resolved to a single value with its evidence, and
the noise stripped out.** The 296 videos are ~80% repeated clickbait macro-fear/hype with
little strategy content; treating all 296 as equal-weight pages would *bury* the signal.

So the structure has five layers, narrowest-and-most-authoritative first:

### Layer 1 — `strategy/STRATEGY_SPEC.md`  ← the thing I implement from
The single source of truth. Every executable rule of the strategy, each as an atomic
statement with the parameter it fixes and citations to the source videos. If I'm going to
trade this strategy, I read **only this file**. Everything else exists to build and defend it.

### Layer 2 — `strategy/<decision>.md`  ← one page per decision the strategy forces
The strategy is a sequence of decisions. One page per decision dimension, each aggregating
every claim across all 296 videos that bears on it, citing video IDs, and flagging
contradictions:
- `instrument-selection.md` — which underlyings/companies, what filters
- `strike-selection.md` — how far OTM, delta, the "1 chart"
- `expiration-duration.md` — DTE / which expiration
- `entry-timing.md` — when to open
- `exit-profit-taking.md` — when to close / take profit / the "1 time it makes sense"
- `assignment-handling.md` — what to do when assigned, rolling
- `position-sizing-ratios.md` — portfolio-secured vs cash-secured puts, the ratios
- `market-regime.md` — bull vs bear adjustments, what "survives a crash"

### Layer 3 — `videos/<id>.md`  ← provenance, one page per video (as requested)
One atomic page per video. **Not a transcript dump** — extracted claims only, plus
front-matter metadata and a signal score. Each claim links UP to the Layer-2 page it
supports. This is the evidence/citation layer: when the spec says "sell puts at ~X delta,"
I can trace it to the exact videos and re-read if needed.

### Layer 4 — `strategy/contradictions.md`  ← the channel argues with itself
The channel repeatedly says opposite things ("covered calls are a trap," "the wheel is a
trap," "cash-secured puts are a trap," "only 1 strategy works"). These are tracked
explicitly and *resolved* in the spec, not averaged. Also a strategy-evolution timeline.

### Layer 5 — `_meta/`  ← machine-readable backbone
- `index.json` — every page + metadata
- `claims.jsonl` — every atomic claim as a row `{claim, dimension, video_ids, confidence}`.
  This is what I actually query programmatically; prose pages are the human-readable mirror.
- `transcripts_manifest.json` — per-video word counts
- `video_categories.json` — signal classification (below)

---

## Signal classification (every video tagged)

To stop clickbait from diluting the spec, every video is scored:
- `STRATEGY` — real, reproducible method content (highest weight)
- `PICKS` — specific stock/ETF picks (time-decaying, low weight for the *method*)
- `MACRO` — market-crash / Fed / Tom Lee / geopolitics fear-bait (near-zero strategy signal)
- `HYPE` — "make millions" engagement-bait (near-zero strategy signal)
- `OTHER` — uncategorized, reviewed individually

Plus a `signal` score 0–5. MACRO/HYPE pages are kept deliberately thin.

---

## Page format conventions (enforced for LLM parseability)

Every page starts with YAML front-matter. Body is atomic — **one fact per bullet**, no
prose padding. Every strategy claim cites its sources as `[[<video-id>]]`. Slugs are
kebab-case. The same fact never appears in two places as prose — Layer 2/3 reference, they
don't restate.

```markdown
---
id: <video-id or page-slug>
title: <string>
type: video | decision | spec | meta
category: STRATEGY | PICKS | MACRO | HYPE | OTHER   # video pages only
signal: 0-5                                          # video pages only
dimensions: [strike-selection, exit-profit-taking]   # which Layer-2 pages this touches
---
```

---

## Build status
See `_meta/BUILD_STATUS.md`.
