# leaps

Knowledge base reverse-engineering the @InvestingWithBrandon options strategy from all 296 of the
channel's videos, structured so an LLM can query and **implement** it.

## Start here
- **`INDEX_PLAN.md`** — OUR "index with an edge" construction plan & buy rule (read this for what we invest in).
- **`wiki/strategy/STRATEGY_SPEC.md`** — the canonical Brandon strategy (read this for the source method).

> **Buy rule vs analysis split:** the 50/50 bullish/bearish split in the per-index screens is an *analysis
> ranking only*. The actual buy rule is **undervalued names only** — we never buy an overvalued stock even
> if it's in the better half. See `INDEX_PLAN.md`. The current buy list is `buy_list.csv`.

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
`MARKET_DIRECTION.md`. **Clean buy list = golden_verdict=bullish AND golden_valid=Y (~332 names: 269 valid + 63 forward-confirmed skewed e.g. NVDA).**
Still not computed: the full company scorecard's qualitative inputs (sentiment, execution risk) → can't hit ">75".

## Data layer: `leaps.db` (SQLite) + rebalance history
Decision (2026-06-07): **narrative strategy pages stay markdown** (prose to reason from); **the data layer
is SQLite.** `build_db.py` loads each rebuild into `leaps.db` and **appends a dated snapshot**, so you can
query the screen with SQL and track how it changes across rebalances (Brandon's "trend across rebalances"
signal). Tables: `companies`, `snapshots`, `market_gate`, `videos`, `claims`. `sqlite3 leaps.db` to query.

## Rebuilding the investable universe (periodic task)
**`bash rebuild_universe.sh`** regenerates everything end-to-end; see **`REPRODUCE.md`** for the runbook.
Final output: **`universe_fractional.csv`** — 1,150 IBKR-fractional-tradable companies (448 undervalued),
the buy-list source for the "synthetic index with an edge." OTC/pink ADRs and non-fractional listings
are filtered out.

## Valuation screen (applies the strategy to live holdings)
`QQQ_SPY_valuation_bullish_bearish.md` — every SPY (503) and QQQ (101) holding scored with Brandon's
valuation method and split into bullish (undervalued) vs bearish (overvalued) halves: 250/250 for SPY,
50/50 for QQQ. Rebuild:
```bash
python3 -c "..."              # _constituents.json  (SPY+QQQ from Wikipedia)
python3 _fetch_fundamentals.py # _fundamentals.json (yfinance: price, TTM/fwd EPS) — slow, cached/resumable
python3 _valuate.py            # _valuation_result.json (Brandon intrinsic value + rank split)
python3 _write_report.py       # QQQ_SPY_valuation_bullish_bearish.md
```
Score is P/E-driven so it's robust to per-ticker feed scale glitches. Data is a point-in-time snapshot
(2026-06-07); re-run to refresh. Covers four baskets: SPY (250/250), QQQ (50/50), Russell 1000 proxy
(500/500), and a Global top-1000 basket (companiesmarketcap.com, ~496/496). Growth input = median of
analyst current-yr, next-yr, and TTM YoY earnings growth (capped 30%) — the forward-EPS-only proxy
mislabeled compounders like GOOGL and was fixed.

`master_company_list.csv` — the unified de-duplicated universe across all four baskets: 1,431 publicly
traded companies (after dropping 58 with no usable price/EPS data → `dropped_no_data.csv`), each tagged
with index membership, market cap, and bullish/bearish verdict. Includes all ~1,000 largest public
companies worldwide that have data, plus 459 smaller US names ($6–24B, below the global top-1000 floor,
sourced from SPY/Russell — note: the sub-$24B tier is US-only, no foreign mid-caps).

`tradable_master_list.csv` — the master list filtered to IBKR-fractional-tradable only (US + Canada +
Europe + ADRs; drops 269 Asian/Gulf local listings + sanctioned). **1,162 tradable companies → 455
undervalued (the investable "index-with-an-edge" universe), 597 overvalued, 110 no-earnings.** 65% US.

`global_100k_holdings_answer.md` — answers "how many securities can $100k hold" using IBKR fractional
rules (min = greater of 0.0001 shares or ~$1; US/Canada/Europe eligible, Asian local listings not):
~332 IBKR-eligible bullish global names (~281 if strictly undervalued).

## Rebuild from scratch
```bash
./_download_transcripts.sh      # raw_transcripts/
python3 _clean_vtt.py           # transcripts/
python3 _extract.py             # video pages + claims.jsonl + categories
python3 _route.py               # _meta/digests/
python3 _decision_pages.py      # strategy decision pages
python3 _index.py               # index.json + integrity check
```
