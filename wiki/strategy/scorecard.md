---
id: scorecard
title: Brandon's Full 100-Point Scorecard (Moat, Execution, Macro)
type: decision
dimensions: [valuation-method, instrument-selection, market-regime]
updated: 2026-06-07
note: The valuation screen we built captures only Valuation+Growth (~40 pts). This page documents the
      full method so the rest can be added.
---

# Brandon's Full Company Scorecard — 100 points

Brandon does not buy on valuation alone. Each company gets a score out of 100 across five components;
he buys the "cream of the crop" (most names score a no — "95 out of 100 are going to be a no").

| Component | Max pts | What it measures | In our screen? |
|-----------|--------:|------------------|----------------|
| **Valuation** | ~20 | price vs intrinsic value (the "golden line", below) | ✅ proxy |
| **Growth** | ~20 | earnings-growth rate | ✅ (in `g_used`) |
| **Moat** | ~20 | durable competitive advantage — pricing power, can competition wipe them out? | ⚠ proxy added |
| **Execution risk** | ~10 | how hard is their plan to actually pull off (humanoid robots = high risk) | ❌ qualitative |
| **Sentiment** | weighted | crowd positioning / fear-greed on the name | ❌ not yet |
| **Economy / macro** | ~30 | overall economic & market direction (from his economic scorecard) | ⚠ MARKET_DIRECTION.md |

He grades on **valuation, growth, moat, execution risk, sentiment, and macro**, **weighted** by importance
(the exact point weights above are from spoken examples, not a stated fixed rubric). **He allocates only to
names scoring over ~75/100.** Real examples: Meta = Val 20/20, Growth 18/20, Moat 16/20, Exec 8/10, Economy
21/30; NVDA stock-sheet score **85**; CoreWeave ≈ 64 ("valuation level is bad"); "95 out of 100 are a no."

## The "golden line" (his valuation engine — what Valuation /20 really measures)
He names it the **golden line** and claims a **94% accuracy** at predicting direction. Plotted by: take a
**2-year window**, get start vs current **EPS** from the reports, compute the **EPS % growth**, draw a line
rising by exactly that %, and compare to the **actual price % move** — the gap is over/under-valuation.
**Validity check:** the start and end **P/E must be similar** (apples-to-apples); if the multiple
re-rated a lot, the line is "skewed" and unreliable. (Our screen uses a growth-adjusted proxy, NOT this —
see [[valuation-method]].)

## Moat /20
- A moat = "any competition that could come in and wipe their business out." He asks: **do they have a
  durable competitive advantage? pricing power? will competition wipe them out?**
- Examples: Apple ("durable moat — we all have iPhones"), UnitedHealth ("biggest health insurer in the
  world"), Amazon. "Crap companies at crap prices with no moat" are the reject pile.
- **Mechanizable proxy (approximate):** quality/profitability metrics — gross margin, operating margin,
  return on equity / invested capital, low debt. High sustained margins + high ROE ≈ pricing power /
  moat. Not identical to his qualitative call, but a usable systematic stand-in.

## Execution risk /10
- How likely the company actually delivers its plan. High when the plan is moonshot-y (Tesla humanoid
  robots, robotaxi). Low for steady operators.
- **Largely qualitative** — no clean mechanical proxy. Could approximate inversely with earnings
  stability / how speculative the growth assumption is.

## Economy / macro /30 + market direction
- Driven by a separate **economic scorecard (/200)** — e.g. "economy is 151/200" / "146/200" / "143/200
  = good economy category" — gauging where the economy, valuations, and corporate profits sit. Maps into
  the /30 of each company score. The **four needle movers**: economy, market valuations, EPS growth,
  interest rates.
- **Hard market GATE:** if the S&P/Nasdaq are **>20% overvalued**, stop buying base portfolio — park in
  **bonds / CDs / SGOV** and wait until price falls back below the EPS line, then rotate back in (uses an
  IRA for tax-free reallocation). Other Discord tabs: **bull-bear scale, assignment-value sheet,
  intrinsic-value sheet (NOT an implied-volatility sheet), intrinsic-value calculator.**
- Plus a **bull-bear scale / market-direction gauge**: a single read on whether it's a good time to
  deploy. Example: "the overall market is at **67 out of 100** right now — it's **not** a bullish time
  to buy stocks." Low gauge → hold back / be selective; high gauge → deploy aggressively.
- This is the [[market-regime]] / [[entry-timing]] overlay: even great companies wait for the macro to
  be favorable, and the whole-market read (S&P/Nasdaq above or below its EPS-growth line) sets how
  aggressive to be.
- **Mechanizable:** the market-direction piece is computable at the index level — where SPY/QQQ sit
  vs their earnings-growth line (the "market is ~5–10% overvalued" read), as a single deploy-or-wait signal.

## What this means for our screen
Our `universe_fractional.csv` ranks on Valuation+Growth only. To match Brandon we should add:
1. **Moat proxy** — quality columns (margins, ROE) so low-quality "value traps" are visible/penalized.
2. **Market-direction indicator** — one market-level bull/bear read to decide *when* to deploy.
3. (Execution risk stays qualitative — flagged, not scored.)
See [[valuation-method]] and [[market-regime]].
