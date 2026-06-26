# leaps

Knowledge base reverse-engineering the @InvestingWithBrandon options strategy from all 296 of the
channel's videos, structured so an LLM can query and **implement** it.

## Start here
- **`INDEX_PLAN.md`** — OUR "index with an edge" construction plan & buy rule (read this for what we invest in).
- **`wiki/strategy/STRATEGY_SPEC.md`** — the canonical Brandon strategy (read this for the source method).

> **Buy rule vs analysis split:** the 50/50 bullish/bearish split in the per-index screens (the
> `QQQ_SPY_*` report) is an *analysis ranking only* and uses an OLD proxy formula. The **actual buy
> decision** — exact thresholds, the moat gate, the allocation formula, and the current reconciled
> counts — is in **`BUY_DECISION.md`** (ground truth). The current buy list is `buy_list.csv` (185 names).

- `wiki/README.md` — how the wiki is organized and why (5-layer design for LLM utility).
- `wiki/_meta/BUILD_STATUS.md` — what was built, classification stats, how to rebuild.

## The strategy in one line
Sell ~2-year (LEAPS) puts on undervalued quality names/indexes, collateralized by a stock portfolio
("portfolio-secured puts"), into fear/high-IV dips; recycle premium into shares + barely-OTM 2-year
calls; cap total assignment exposure with a ratio that survives a 50% crash.

## Layout
```
_video_index.txt            296 videos (id|title|duration)
raw_transcripts/            yt-dlp .vtt captions (source)
transcripts/                cleaned plain text
wiki/strategy/              L1 spec + L2 decision pages + contradictions
wiki/videos/<id>.md         L3 one page per video (extracted claims)
wiki/_meta/                 L5 claims.jsonl, index.json, video_categories.json, digests/
_*.py / _*.sh               reproducible build pipeline
```

## AUDIT (2026-06-07) + golden-line implementation
`AUDIT_REPORT.md` — full reconciliation vs the videos; found real errors (base allocation, covered-calls,
strike depth, duration, profit-taking, assignment sizing) now corrected in the wiki.
**Brandon's actual "golden line" valuation is now implemented** (`goldenline.py`): over a 2-year window,
EPS growth vs price growth, with his P/E apples-to-apples validity check. `universe_fractional.csv` now
leads with `golden_verdict`/`golden_pct`/`golden_valid` (the faithful method); the old proxy columns are
kept for comparison. The **>20% market deploy gate** (golden line on the S&P, valid names only) writes to
`MARKET_DIRECTION.md`. **Buy list = `BUY_DECISION.md` rule (golden-bullish + reliable + passes moat gate) = 185 names** (164 valid
+ 21 forward-confirmed; ~147 removed by the moat gate after full per-company research). The moat gate is
now backed by `moat_verdicts.csv` + `wiki/moats/` (189 yes / 118 weak / 30 no). Earlier counts (269/328)
predate that research. Still not computed: the scorecard's qualitative inputs (sentiment, execution risk).

## Data layer: `leaps.db` (SQLite) + rebalance history
Decision (2026-06-07): **narrative strategy pages stay markdown** (prose to reason from); **the data layer
is SQLite.** `build_db.py` loads each rebuild into `leaps.db` and **appends a dated snapshot**, so you can
query the screen with SQL and track how it changes across rebalances (Brandon's "trend across rebalances"
signal). Tables: `companies`, `snapshots`, `market_gate`, `videos`, `claims`. `sqlite3 leaps.db` to query.

## Rebuilding the investable universe (periodic task)
**`bash rebuild_universe.sh`** regenerates everything end-to-end; see **`REPRODUCE.md`** for the runbook
and **`BUY_DECISION.md`** for the exact buy/allocation rules and current counts. Primary outputs:
- **`universe_fractional.csv`** — the 1,150 IBKR-fractional-tradable companies (910 scoreable), every column.
- **`buy_list.csv`** — the 185 buy-eligible names (the investable "index with an edge").
- **`MARKET_DIRECTION.md`** — the deploy gate + the stock/bond allocation (currently 72/28).

### Other / historical artifacts (superseded by the above — kept for reference)
- `QQQ_SPY_valuation_bullish_bearish.md`, `master_company_list.csv`, `tradable_master_list.csv`,
  `global_100k_holdings_answer.md` — earlier per-index screens built on the **old proxy formula** and a
  50/50 median split. Their counts (332/448/455/281 etc.) predate the golden-line + moat-gate buy rule;
  trust `BUY_DECISION.md` for current numbers, not these.

## Rebuild from scratch
```bash
./_download_transcripts.sh      # raw_transcripts/
python3 _clean_vtt.py           # transcripts/
python3 _extract.py             # video pages + claims.jsonl + categories
python3 _route.py               # _meta/digests/
python3 _decision_pages.py      # strategy decision pages
python3 _index.py               # index.json + integrity check
```
