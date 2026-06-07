# The Buy Decision — exact, reproducible spec (ground truth)

This is the single authoritative definition of how a stock gets `buy=Y` and how the stock/bond split is set.
Every threshold here matches `build_universe.py` / `goldenline.py` exactly. If a doc disagrees with this
file, this file wins. (Written 2026-06-07 to close the "thresholds only live in code" gaps.)

## A. Per-stock buy decision (`buy=Y`)
A name is on the buy list **iff ALL of these pass**, evaluated in order:

1. **Moat gate.** Look up the ticker in `moat_verdicts.csv`. If its `moat` value is **`no`** or **`weak`**,
   it is **rejected**. A ticker not present in that file (not yet researched) **passes** (pending).
   → This gate, not the `moat_proxy_20` column, is what removes value traps (PayPal, Netflix). The
   `moat_proxy_20` column is informational only and is **not used** in the decision.

2. **Golden-line bullish.** Compute over a 2-year window:
   - `eps_growth = eps_now / eps_2y − 1`  (annual diluted EPS; `eps_2y` = 2 fiscal years before the latest;
     if fewer than 3 years of EPS exist, fall back to the oldest available year).
   - `price_growth = price_now / price_2y − 1`  (`price_2y` = close ~24 months ago).
   - `fair_price = price_2y × (1 + eps_growth)`;  `golden_pct = (fair_price/price_now − 1) × 100`.
   - **Bullish iff `golden_pct >= 0`** (EPS outgrew price → price sits below the EPS line). Else rejected.
   - If `eps_2y`, `eps_now`, `price_2y`, or `price_now` is missing or ≤ 0, the name is **unvalued** → not buyable.

3. **Reliability** — one of:
   - **Valid:** `|pe_now/pe_then − 1| <= 0.5` (start vs end P/E within 50% = apples-to-apples) → `golden_valid='Y'` → pass.
   - **Forward-confirmed (for skewed names):** if `|pe_now/pe_then − 1| > 0.5` (`golden_valid='skewed'`),
     the name still passes **iff** `fwd_pe <= 1.5 × max(growth_pct, 8)`, where
     `fwd_pe = price / forward_eps` (forward EPS must be > 0) and
     `growth_pct = g_used × 100` (`g_used` = median of {analyst current-yr, next-yr, TTM YoY earnings
     growth}, floored at 0, capped at 0.30). If `fwd_pe` is unavailable → rejected.

**Worked examples:** NVDA — golden bullish, *skewed* (P/E 104→42), but `fwd_pe≈16 ≤ 1.5×max(30,8)=45` →
**buy**. Tesla — golden **bearish** (`golden_pct<0`) → never reaches reliability → **no**. PayPal — golden
bullish + valid, but moat=`no` → **rejected by gate 1**.

## B. Market deploy gate (portfolio-level, does not change per-stock `buy`)
- Take the S&P 500 members that are golden-**valid** (`golden_valid='Y'`); compute the **median** of their
  `golden_pct`. If that median **< −20** → market is >20% overvalued → **do not deploy; sit in bonds**
  (Brandon's >20% rule). Else OK to deploy. (This median-of-constituents is a documented *proxy* for the
  index's own EPS line — see `ASSUMPTIONS_LEDGER.md` #3.)

## C. Stock / bond allocation (John's capital rule)
- `undervalued_share = (# buy-eligible names) ÷ (# names with a golden verdict)`, over the fractional-tradable set.
- `stock_weight = min(1.0, undervalued_share / 0.50)`;  `bond_weight = 1 − stock_weight`.
  (50% of the universe undervalued = 100% stocks; 25% = 50/50; 0% = all bonds.) Bonds = SGOV/short-term.

## D. Current snapshot (2026-06-07) — the numbers, reconciled
| Quantity | Value |
|---|---|
| Total universe across the 4 baskets (unique) | 1,489 |
| With usable data (price + EPS) | 1,431 |
| IBKR-fractional **tradable** | **1,150** |
| Tradable **with a golden verdict** (the allocation denominator) | **910** |
| **Buy list** (`buy=Y`: golden-bullish + reliable + passes moat gate) | **328** |
| └ of which `golden_valid='Y'` | 266 |
| └ of which skewed-but-forward-confirmed | 62 |
| Removed by the moat gate (PYPL, NFLX, NKE, CRM) | 4 |
| Allocation: 328/910 = 36% → `min(100%, 36%/50%)` | **72% stocks / 28% bonds** |

> Note on older counts: earlier docs cited 269 (valid-only, pre-forward-confirm) and 332 (pre-moat-gate).
> The current, correct buy-list count is **328**. `build_universe.py` prints these every run and writes the
> allocation to `MARKET_DIRECTION.md`.
