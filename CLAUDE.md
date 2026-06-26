# CLAUDE.md — operating instructions for the leaps investor (read this first)

You are operating an automated equity-investing system. This file tells you **how to read and use the
other files**, in the order to read them. It deliberately contains **no data** — no stock names, no
counts, no prices, no allocations. Data goes stale; instructions do not. Every number lives in a
generated file you regenerate before you act (see step 3). If you ever see a count or ticker written
into this file or the README, it is a bug — remove it.

## 0. Before you place ANY order — the authorization gate
Read **`ibkr/TRADING_AUTHORIZATION.md`** and obey it. You may **not** place an order (paper or live)
without explicit, specific human authorization for **that** order. A question ("can you make a trade?")
is not an instruction — answer it, do not act. This rule outranks everything else in this repo.

## 0a. RESTRICTED tickers — NEVER trade, in any way
**Never trade any ticker listed in `restricted_tickers.txt` — no shares, no puts, no calls, nothing.**
Currently: **MSFT** (John is a Microsoft employee / insider — trading it is prohibited). This is enforced
in code (every builder excludes them) AND is a hard rule here: even on an explicit "buy everything" order,
a restricted ticker is skipped. If you ever see a restricted ticker in an actionable file, that is a bug —
stop and fix it. See `ibkr/TRADING_AUTHORIZATION.md`.

## What this system does (one line, no data)
Screens a broad global universe of stocks by one fixed valuation rule (the "golden line"), holds the
undervalued + quality subset, and sizes that stock sleeve against short-term bonds by how cheap the
overall market is.

## How to operate — read these in THIS order
You know nothing at start. Follow the sequence; do not wander into other files first.

1. **`ibkr/TRADING_AUTHORIZATION.md`** — may I act at all? (the gate; always first)
2. **`BUY_DECISION.md`** — **THE RULE.** The exact, authoritative definition of what counts as a buy and
   how the stock-vs-bond split is set. This is ground truth: if any other file disagrees with it, it wins.
3. **`REPRODUCE.md`** — the runbook. Run it to **regenerate the investable list from current market
   data.** Never act on the committed output files as-found — they are dated snapshots and go stale.
   Regenerate first, every time.
4. **The freshly regenerated outputs you then act on:**
   - `buy_list.csv` — what to hold (one row per holding).
   - `MARKET_DIRECTION.md` — the stock-vs-bond split and the market deploy gate.
   - `orders.csv` — what to buy and the dollar amount each (produced by `build_orders.py`).
   - `universe_columns_key.md` — the dictionary for every column in those files.
5. **`ibkr/README.md`** — the execution harness: how to actually place the authorized orders (runs on a
   dedicated VPS, never a laptop).

## The rule lives in code, not prose
`BUY_DECISION.md` is the spec; the **executable** rule is `build_universe.py` + `goldenline.py`, with the
moat-gate data in `moat_verdicts.csv`. Spec and code are kept identical — if they ever differ, that is a
bug to fix, not a judgment call. Read the spec to understand; run the code to decide.

## Precedence (highest wins)
1. `ibkr/TRADING_AUTHORIZATION.md` — may I act
2. `BUY_DECISION.md` — the rule
3. the code (`build_universe.py`, `goldenline.py`) — must match the rule
4. the regenerated outputs (`buy_list.csv`, `orders.csv`, `MARKET_DIRECTION.md`)
5. everything else below — background only

## Background — only if you must understand or audit WHY the rule is what it is
**Never trade from these. They are explanation and provenance, not instructions, and some are superseded.**
- `INDEX_PLAN.md` — the design narrative; how this deliberately differs from the source options strategy.
- `ASSUMPTIONS_LEDGER.md` — every threshold, where it came from, and which ones are uncertain/invented.
- `AUDIT_REPORT.md`, `BACKTEST_RECONCILIATION.md` — how the rule was validated and corrected.
- `wiki/` — the original source strategy (per-video research) and per-company moat write-ups. This is the
  raw material the rule was distilled from. You do **not** need it to operate, and you would never start
  here. `README.md` and `wiki/README.md` describe its layout if you ever need to trace a claim.
- `QQQ_SPY_valuation_bullish_bearish.md`, `global_100k_holdings_answer.md`, and other `*_list.csv` from
  earlier passes — **superseded** analyses on an old formula. Ignore for any trading decision.

## Standing rules for whoever operates this
- No stock names or counts in this file or the README — ever. Data lives only in the generated files.
- Always regenerate (step 3) before trading. Never trade a stale snapshot.
- Obey the authorization gate (step 0). When unsure whether you were authorized, do not trade.
