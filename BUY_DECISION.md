# The Buy Decision — exact, reproducible spec (ground truth)

This is the single authoritative definition of how a stock gets `buy=Y` and how the stock/bond split is set.
Every threshold here matches `build_universe.py` / `goldenline.py` exactly. If a doc disagrees with this
file, this file wins. (Written 2026-06-07 to close the "thresholds only live in code" gaps.)

## REBALANCING — never place fresh; reconcile HOLDINGS to TARGET (sell first, then buy)
Trading is **never** "buy the whole list from scratch." Every time we trade, we **compare what's in the
portfolio to the ideal target state, then sell what's overbought and buy what's underbought — sells first,
then buys.** (John, 2026-06-27.) Algorithm:

1. **Target state** = the freshly regenerated `orders.csv` — each buy-list name at its target dollar weight,
   plus the SGOV/cash sleeve. Regenerate from current prices first (§ Cache freshness) so the target is live.
2. **Current state** = the account's **actual positions** (shares × current price = current $ per name) + cash.
   Read it from the broker, never assume it.
3. **Per-name diff** `delta = target_$ − current_$`:
   - **Held but NOT in target** (a name that left the buy list, or is now excluded — Swiss, restricted, a
     dropped foreign name) → **SELL the entire position.**
   - **delta < 0** (overweight) → **SELL** the excess.
   - **delta > 0** (underweight) → **BUY** the shortfall.
   - **In target but not held** → **BUY**.
   - Whole-share rounding + cash-remainder policy applies to each leg.
4. **ORDER OF OPERATIONS (hard rule): execute ALL SELLS first, let them fill, THEN do the BUYS.** Why: the
   sale proceeds fund the buys (no extra cash or margin needed), and you never attempt a buy before the cash
   exists. Selling first also realizes the exits cleanly before re-deploying.
5. This makes trading **idempotent toward the target** — re-running converges the book to `orders.csv` from
   any starting state, and does nothing if already aligned.

> Implementation: **`ibkr/rebalance_orders.py`** does the full reconcile — reads `orders.csv` (ideal) vs the
> account's live positions, normalizes tickers (e.g. `BF-B`↔`BF B`) so a name isn't double-counted, derives
> per-name sell/buy deltas (whole shares), places **all sells first then all buys**, and trims/exits anything
> not in the ideal (Swiss, restricted, dropped names, the SGOV overweight). `place_orders.py` remains the
> simpler buy-only batch placer for an initial build.

## A′. Tradable-universe gate (listing & country — applied before §A)
We only hold names a US retail investor can **cleanly and paper-testably** trade. Enforced in
`build_universe.py` `fractional()`:
- **US-listed names** (NYSE/Nasdaq, incl. ADRs that trade as a plain US ticker like TSM/ASML) → tradable.
- **Foreign LOCAL listings** (ticker has an exchange suffix, e.g. `.PA`/`.DE`/`.SW`) → **dropped**, UNLESS
  the company has a **clean exchange-listed US ADR** (NYSE/Nasdaq, not OTC/pink). Those are swapped to the
  ADR ticker via `ADR_MAP`. Verified 2026-06-27: of 22 foreign names only **Ferrovial** qualifies
  (`FER.MC`→`FER`); the other 21 have OTC-only ADRs → dropped. OTC/pink ADRs are excluded (illiquid,
  not paper-testable, withholding/data friction).
- **Switzerland is excluded ENTIRELY** (`EXCLUDE_COUNTRIES`), regardless of listing — even Swiss-domiciled
  US-listed names (ALC, AMRZ). Rationale: the portfolio is too small to justify the 35% Swiss dividend
  withholding + manual reclaim complexity. (John, 2026-06-27.)
- To re-enable foreign breadth later: add the foreign market-data subscriptions (so they're paper-testable),
  extend `ADR_MAP`, or relax `EXCLUDE_COUNTRIES`.

## A. Per-stock buy decision (`buy=Y`)
A name is on the buy list **iff ALL of these pass**, evaluated in order:

0. **Restricted gate (compliance — checked FIRST).** If the ticker is in `restricted_tickers.txt`, it is
   **never `buy=Y`** and never tradable in any form (shares, puts, calls). Currently **MSFT** (John is a
   Microsoft insider). Enforced in `build_universe.py` `buy_eligible()` and every order builder; it also
   overrides any human "buy everything" instruction. See `ibkr/TRADING_AUTHORIZATION.md`.

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
   - The `stock_weight` is spread across these moat-quality names. Bonds = SGOV (see §C.3).

3. **The bond sleeve instrument = SGOV (0–3mo US Treasuries). Settled 2026-06-26.**
   The sleeve is **collateral + dry powder**, not a yield play — it backs the sold puts (assignment ÷
   7-day liquidity) and is the cash deployed into dips. Its only job is to stay stable & liquid *when
   stocks crash*. So: **US T-bills (SGOV)**, which are uncorrelated/negatively-correlated with equities in
   a panic, ~zero duration/credit risk. **NOT corporates** (credit spreads widen with equity crashes — they
   fall exactly when you need them). **Munis deferred:** at the current curve the after-tax pickup over
   SGOV is only ~0.2–0.4% for real duration/drawdown risk (taxable, high-bracket assumed); revisit a small
   short-muni (SUB) tranche on the *parked* portion only after Fed rate cuts widen the muni edge.

> Why split them: the moat gate removing value traps shouldn't fool the portfolio into thinking the market
> got more expensive and piling into bonds. The market is exactly as hot as the *valuation* says (pre-moat);
> we just hold that stock allocation in a smaller, higher-quality set.

## D. Live numbers (no hardcoded counts — they go stale)
The per-run counts (universe size, undervalued count, stock/bond split, holdings) are **regenerated every
build** and written to **`MARKET_DIRECTION.md`** + printed by `build_universe.py`. Do not hardcode them here.
The durable facts: the allocation denominator is the IBKR-fractional set **with a golden verdict**; the
split is `stock = min(100%, undervalued% ÷ 50%)`; holdings = the post-moat `buy=Y` names in `buy_list.csv`.
The moat gate is backed by `moat_verdicts.csv` + `wiki/moats/`. Known back-test gap: a few names Brandon
avoids purely on PRICE (e.g. WM, PANW, AMZN, COST — moats but expensive) — the still-open
absolute-valuation-ceiling gate, not a moat issue.

## E0. Two-layer portfolio architecture (index + concentration) — mirrors Brandon
Brandon runs a broad index base (SPY/QQQ) PLUS concentration on **10–20 high-conviction names**. Ours:
- **Layer 1 — the index-with-an-edge:** the full `buy_list.csv` (all undervalued + reliable + moat names).
  This REPLACES a plain SPY/QQQ index — same broad-base role, but valuation-filtered. It is the collateral.
- **Layer 2 — the concentration sleeve:** the top ~10–20 high-conviction names (`build_conviction.py`),
  **overweighted** and the **targets of the put/call overlay** (`build_puts.py`).
- **High conviction =** on the buy list AND `moat=yes` AND largest market cap (liquidity/quality/table-pounder),
  EXCLUDING (a) price-ceiling names Brandon avoids (WM, PANW, COST) and (b) EPS-base-artifact golden reads
  (`golden_pct > 300`). Raw `golden_pct` is shown but not the ranker (tiny-base years spike it to artifacts).
- Top of the current sleeve — NVDA, GOOG, AMZN, META — are exactly the names Brandon is buying now.
  (Brandon also names MSFT, but MSFT is **restricted** for us — §A.0 — so it never enters our sleeve.)

## E. Instrument layer — HOW each holding is expressed (puts / shares / calls)
§A picks **which** names; this section picks **how** to hold each, per Brandon's actual options method.
Source: `wiki/strategy/STRATEGY_SPEC.md` + the 2026-06-26 video re-investigation (J_KCO3hhf24
"tested every options strategy 12 yrs", flzw3xQ4_9E, -ayim8zd7BY, O9Xv6w6FbXE, 18WBQZ9JiBM).
**Status (partial implementation):** `build_orders.py` emits the **shares + SGOV collateral base** (the
long-only book — Brandon's foundation). `build_puts.py` now generates the **put-selling overlay** with
**real LEAPS quotes**: it ranks the table-pounders by market cap, pulls ~2yr put chains (~10% below spot),
sizes contracts so total assignment value ≤ a regime cap (`ASSIGN_CAP_FRAC` of 7-day liquidity), reports
premium collected, and the recycle (≈50% shares / 50% barely-OTM ~2yr calls). Still TODO: wiring the
overlay into live IBKR option orders and a full call-leg builder.

### E.1 The bullish-only hierarchy (the ONLY instruments used)
- **Long shares** — the base / collateral; the floor for any qualifying name.
- **Short puts (SELL puts)** — bullish; sold into fear/high-IV on undervalued names. **Portfolio-secured, NEVER cash-secured.**
- **Long calls (BUY calls)** — leverage; only on the deepest-value, highest-conviction names, funded by put premium.
- **Bonds (SGOV)** — dry powder when the market is rich; the only "hedge."
- **NEVER:** short stock, buy puts, covered/naked calls (except to exit assigned shares or a name gone extremely overvalued), spreads, the wheel, short-duration (<6mo), active margin, high-beta junk.

### E.2 Expression by conviction depth (a name that already passes §A)
| Undervaluation (depth below the EPS line) | How to express it |
|---|---|
| **Extremely** undervalued + "table-pounder" conviction (beaten down in fear) | shares **+ sell ~2yr put ~10% below spot + buy 1–2 barely-OTM ~2yr calls** |
| **Good price** (moderately undervalued) | shares **+ sell ~2yr put**; no calls |
| **Fair value** | shares only (or wait) |
| **Overvalued / deteriorating** | **avoid** (no bullish exposure); covered call only to exit existing/assigned shares |

### E.3 Options parameters (from his real trades)
- **Duration ~1–2 yr (LEAPS)**, 6-month floor, never monthly. (NVDA example: puts & calls out to 6/16/2028.)
- **Put strike ~10% below spot**, deeper below the EPS/intrinsic line; deeper when cheaper.
- **Calls barely OTM, same long expiry, bought AFTER a dip** (cheaper), capped ~3–5%/name, funded by recycled put premium — not fresh cash.
- **Worked example (flzw3xQ4_9E, 2026-06):** NVDA — sell 5× $180 put exp 6/16/2028 (~$31/sh ≈ $15k premium, ~10% below ~$204 spot) → recycle into NVDA shares + 1–2× $205 calls same expiry.

### E.4 Sizing & risk (the ratio core)
- **Portfolio-secured:** base portfolio is collateral. Track **assignment value** = total cash owed if every sold put were assigned at once.
- **Cap = assignment value ÷ 7-day liquidity**, regime-scaled: **0–50% when lofty, up to ~75% cheap** (≈100% only COVID-cheap). Raise the cap as the market falls. Survives a 50–70% crash.
- **Never actively on margin** (zero margin interest).

### E.5 Trim / exit order
- Sold puts: take profit **~70–95%** (by valuation + buying-power need).
- Shares & calls: **no % rule** — exit only when the story changes / meaningfully overvalued.
- **Trim order when reducing risk: calls first → puts → shares last.**

### E.6 Hard rules added by the 2026-06-26 re-investigation
- **NEVER cash-secured puts — ever, even in a retirement account** (J_KCO3hhf24). Portfolio-secured only.
- **Buy the LEAP call AFTER the dip, not at initiation** — cheaper entry (J_KCO3hhf24).
- **Calls only on a "table-pounder" buy** (ultra-high conviction AND extremely cheap) (J_KCO3hhf24).
- **No active margin** (J_KCO3hhf24).
- He confirmed (does NOT short, does NOT buy puts, rejects covered calls / CSP / spreads / short-duration) across all 5 latest videos — the bullish-only doctrine is reinforced, not changed.
