# leaps

A reproducible system that reverse-engineers the @InvestingWithBrandon strategy from the channel's
videos and turns it into an investable, auto-rebalanced "index with an edge."

## Operating it
**Read `CLAUDE.md` first.** It is the entry point — it explains, with no embedded data, how to read and
use every other file, in the order to read them, and the precedence between them. Anyone (human or AI)
running this should start there, not here.

This README is a human-facing map only. It contains **no stock names, counts, prices, or allocations** on
purpose — those go stale; all live numbers come from the generated files after a fresh rebuild.

## What's in here (by role, no data)
- **`CLAUDE.md`** — operating instructions / read order / precedence. Start here.
- **`BUY_DECISION.md`** — the exact, authoritative buy + allocation rule (ground truth).
- **`REPRODUCE.md`** — the runbook to regenerate the investable universe from current market data.
- **`ibkr/`** — the live-trading harness. `TRADING_AUTHORIZATION.md` (the hard rule that you never trade
  without explicit authorization) and `README.md` (how the order execution works).
- **Generated outputs** (rebuilt, not hand-edited): `buy_list.csv` (holdings), `orders.csv` (dollar
  amounts), `MARKET_DIRECTION.md` (stock/bond split), `universe_fractional.csv` (full scored universe).
  `universe_columns_key.md` is the column dictionary.
- **Background / provenance** (explanation, not instructions): `INDEX_PLAN.md`, `ASSUMPTIONS_LEDGER.md`,
  `AUDIT_REPORT.md`, `BACKTEST_RECONCILIATION.md`, and the `wiki/` (per-video research + per-company moat
  write-ups the rule was distilled from).
- **Data layer**: `leaps.db` (SQLite) — each rebuild appends a dated snapshot so the screen can be queried
  with SQL and tracked across rebalances. Tables: `companies`, `snapshots`, `market_gate`, `videos`, `claims`.

## Rebuilding
`bash rebuild_universe.sh` regenerates everything end-to-end; `REPRODUCE.md` is the step-by-step runbook.
The knowledge-base build pipeline (transcripts → wiki) is the `_*.py` / `_*.sh` scripts; `wiki/README.md`
describes the wiki's layout.
