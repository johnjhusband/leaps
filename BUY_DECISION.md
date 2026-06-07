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

## C. Stock / bond allocation — TWO separate data points (do not conflate)
The moat challenge changes *which* stocks we hold, NOT *how hot the market is*. So sizing and selection
use different numbers:

1. **SIZING the stock/bond split = PRE-moat "undervalued" count** (market hotness):
   - `undervalued_share = (# names passing §A.2+§A.3, i.e. golden-bullish + reliable, BEFORE the moat gate) ÷ (# names with a golden verdict)`, over the fractional set.
   - `stock_weight = min(1.0, undervalued_share / 0.50)`;  `bond_weight = 1 − stock_weight`.
   - (50% undervalued = 100% stocks; 25% = 50/50; 0% = all bonds.) The moat gate does not move this.
2. **SELECTING the holdings = POST-moat buy list** (`buy=Y`, §A in full incl. the moat gate):
   - The `stock_weight` is spread across these moat-quality names. Bonds = SGOV/short-term.

> Why split them: the moat gate removing value traps shouldn't fool the portfolio into thinking the market
> got more expensive and piling into bonds. The market is exactly as hot as the *valuation* says (pre-moat);
> we just hold that stock allocation in a smaller, higher-quality set.

## D. Current snapshot (2026-06-07) — the numbers, reconciled
| Quantity | Value |
|---|---|
| Total universe across the 4 baskets (unique) | 1,489 |
| With usable data (price + EPS) | 1,431 |
| IBKR-fractional **tradable** | **1,150** |
| Tradable **with a golden verdict** (the allocation denominator) | **910** |
| **Undervalued (PRE-moat — sizes the split)** | **332** (332/910 = 36%) |
| **Allocation sizing:** `min(100%, 36%/50%)` | **73% stocks / 27% bonds** |
| **Buy list / holdings (POST-moat: + moat gate)** | **185** |
| └ of which `golden_valid='Y'` | 164 |
| └ of which skewed-but-forward-confirmed | 21 |
| Removed by the **moat gate** (moat=`no`/`weak`, ~324 researched) | 147 |
| → the **73% stock sleeve is spread across the 185** moat-quality names | ~$73k/185 ≈ $395 each on $100k |

> The moat gate is now backed by per-company research (`moat_verdicts.csv` + `wiki/moats/`): 189 `yes`,
> 118 `weak`, 30 `no`. Removing the no/weak names cut the *holdings* from 332 → 185 (Brandon-level
> selectivity) — but **NOT** the stock/bond split: sizing stays on the pre-moat 332 (=73% stocks) per §C.
> Earlier counts (269/328) predate full moat research.
> `build_universe.py` prints these every run and writes the allocation to `MARKET_DIRECTION.md`.
> Remaining back-test gap: ~4 names Brandon avoids on PRICE (WM, PANW, AMZN, COST) — they have moats but
> are expensive; that's the still-open absolute-valuation-ceiling gate, not a moat issue.
