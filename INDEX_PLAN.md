# The "Index With an Edge" — Construction Plan

**What this is:** our synthetic index. Instead of blindly buying a cap-weighted index, we buy a broad,
globally-diversified basket **filtered to only the genuinely undervalued names** (Brandon's golden line),
giving an index-like feel with the possibility of an edge. Rebuilt and rebalanced periodically.

**Status:** John's design (2026-06-07). Deviates from Brandon where noted — he runs a concentrated
options book; we run a long-only diversified stock+bond index on the same valuation engine.

---

## THE KEY DISTINCTION (the thing we hadn't documented)
**The 50/50 bullish/bearish split is an ANALYSIS device, NOT the investment rule.** Ranking the universe
and cutting it in half was only ever a way to *study* relative valuation. It is **not** what we buy.

**The investment rule:** we buy **only genuinely undervalued names** (golden line bullish AND the read is
valid/apples-to-apples). **We never buy an overvalued stock — even if it sits in the "better half" of the
ranking.** Being the least-overvalued of a rich bunch is still overvalued; it does not get bought.

**Consequence — the holdings count floats with the market:**
- It is NOT fixed at 50%. If 75% of the market is overvalued, only ~25% qualifies and we hold ~25%.
- Right now (2026-06-07): of 910 valued tradable names, **328 make the buy list** — that is the entire
  stock buy list. The other names are not bought. (See `BUY_DECISION.md` for the exact rule + reconciled counts.)

**Where the rest of the money goes:** the capital we do NOT put into undervalued stocks goes into
**bonds / short-term securities (e.g. SGOV)** — exactly as Brandon parks in bonds when the market is rich.
So the portfolio is `undervalued stocks + bonds`, never `undervalued stocks + least-bad overvalued stocks`.

---

## Allocation rule (stocks vs bonds) — THE CAPITAL ALLOCATION FORMULA (John, 2026-06-07)
The stock sleeve scales off opportunity breadth, with **50% of the universe undervalued = fully invested**:

```
stock_weight = min(100%, undervalued_share ÷ 50%)
bond_weight  = 100% − stock_weight
```
where `undervalued_share = (# genuinely undervalued) ÷ (# valued tradable names)`.

- **50% undervalued → 100% stocks, 0% bonds.**
- **25% undervalued → 50% stocks, 50% bonds.** (25/50 = half invested; the other half to bonds.)
- **>50% undervalued → still 100% stocks** (capped — you can't be more than fully invested).
- **0% undervalued → 100% bonds.**

This is essentially **capital allocation**: the richer the market, the fewer names qualify, the more of
the portfolio sits in bonds/short-term — automatic de-risking (mirrors Brandon's bond rotation).

**Current reading (2026-06-07):** 328 buy-eligible ÷ 910 valued = **36% → 72% stocks / 28% bonds.**
(Computed by `build_universe.py`, written to `MARKET_DIRECTION.md` each rebuild. Ground truth: `BUY_DECISION.md`.)

**Invariant that never changes:** no money in overvalued names — bonds, never least-bad stocks.

## The buy rule (CORRECTED 2026-06-07 — forward-confirmation)
A name is **buy-eligible** if it is **golden-bullish AND a reliable read**, where reliable =
- `valid` (apples-to-apples trailing golden line), **OR**
- `skewed` BUT **forward-confirmed**: forward P/E is justified by growth (PEG-forward ≤ 1.5).

**Why the second path exists:** the trailing golden line breaks when a multiple re-rates (skewed). A hard
exclude was *stricter than Brandon* — it threw out NVDA, which **Brandon actually holds**. NVDA's trailing
line is skewed (P/E compressed 104→42 as earnings 4x'd), but its **forward P/E is ~16** — cheap for the
growth — so Brandon buys it and so do we. Tesla stays out: it's golden-*bearish* (forward P/E 156), never
eligible. This recovered 63 quality growers (incl. NVDA, LLY) that the blunt skewed-exclude wrongly dropped
— **62 remain on the buy list after the moat gate** removes one. (Counts: `BUY_DECISION.md`.)

## Within the stock sleeve
- Hold the buy-eligible names (`buy_list.csv`), broadly diversified (index-like). Each row tags the
  `reason` (valid vs fwd-confirmed).
- Globally represented but IBKR-fractional-tradable only (US/Canada/Europe + listed ADRs).
- Weighting is a separate choice (equal-weight vs market-cap-weight) — TBD by John.

## Rebalance cadence
- Re-run `rebuild_universe.sh` periodically (monthly is sensible). Each run appends a dated snapshot to
  `leaps.db`, so we can track the trend across rebalances (which names flipped, is the market getting
  richer) — Brandon's "trend across rebalances" signal.
- At each rebalance: drop names that are no longer undervalued, add newly-undervalued names, and shift the
  stock/bond split to the new breadth.

## Run frequency & automation (the next phase)
**Measured timing:**
- A **price-only refresh of all ~1,500 names = ~36 seconds** (batched), and recomputing the golden line +
  verdicts + allocation is seconds. So the whole screen **re-scores in under a minute.**
- EPS / financials / quality only change on **earnings (quarterly)** — those slow fetches (the ~30–45 min
  cold rebuild) only need to run ~weekly/monthly, not daily.

**So "how often can we run the numbers?"** — effectively as often as we want; compute is not the constraint:
- **Intraday / daily:** price-refresh + re-score (<1 min). Cheap enough to run continuously.
- **Weekly:** also refresh fundamentals so new earnings flow in.
- **Quarterly:** full cold rebuild + re-pull constituents.

**But running ≠ trading.** The strategy is valuation-driven and slow (Brandon thinks in 1–2-year theses);
undervaluation does not flip daily. So **re-score often, but rebalance the actual portfolio ~monthly** to
avoid churn, bid/ask, and tax friction. Each run already appends a dated snapshot to `leaps.db`, so we can
see exactly how much actually changed before deciding to trade.

**Automation build-out (next phase of our work):**
1. Scheduled job (cron) → price refresh → recompute golden line + allocation → diff vs the last `leaps.db`
   snapshot (names that flipped, new allocation %).
2. Generate the target portfolio (buy-list names at chosen weights + bond sleeve from the allocation rule).
3. Compute the order delta vs current IBKR positions.
4. Execute via the **IBKR API** (ib_insync / Client Portal API) — with guardrails (dry-run preview,
   max-order-size, only-on-meaningful-drift) before any live order.
Steps 1–2 are pure extensions of the current pipeline; step 4 (live trading) is where we add the controls.

## How this differs from Brandon (explicit)
| | Brandon | Our index-with-an-edge |
|---|---|---|
| Vehicle | concentrated options (sell puts, buy calls) on a few names | long-only diversified stocks + bonds |
| Valuation engine | golden line | same golden line |
| Overvalued names | never sold puts on them | **never bought** (the distinction above) |
| Rich-market move | park in bonds, stop deploying | stock sleeve shrinks, bonds grow (same spirit) |
| Selectivity | 95% are a "no" | only the genuinely-undervalued ~30% qualify |
