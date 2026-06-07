---
id: valuation-method
title: Valuation Method — How Brandon Decides Undervalued vs Overvalued
type: decision
dimensions: [instrument-selection, strike-selection, entry-timing]
updated: 2026-06-07
sources: verified verbatim from transcripts (see quotes)
---

# Valuation Method — Undervalued vs Overvalued

Valuation is the gate on every trade (which name, what strike, when to enter). This is the actual
mechanism, not just "below intrinsic value." Two layers — individual stock and whole market — both
built on one idea.

## CORRECTED 2026-06-07 — the "golden line" is the real method; our screen uses a proxy
Brandon **names** his valuation engine the **"golden line"** and claims **~94% accuracy**. The actual
procedure: take a **2-year window**, get start vs current **EPS** from the reports, compute **EPS %
growth**, draw a line rising by exactly that %, and compare to the **actual price % move** — the gap =
over/under-valuation. **Validity check:** start P/E ≈ end P/E (apples-to-apples); if the multiple
re-rated, the line is "skewed." His intrinsic value also folds in **P/S, revenue growth, margin expansion,
guidance, interest rates, macro** — not EPS alone. **Our screen now implements this golden line** as the
PRIMARY verdict (`golden_verdict`/`golden_pct`/`golden_valid`, via `goldenline.py`); the exact buy logic and
thresholds are in **`BUY_DECISION.md`**. (An older proxy formula `intrinsic = TTM_EPS×(1+g)^5×20÷1.10^5`
still appears as the secondary `proxy_*`/`intrinsic_value` columns for comparison only — its multiple,
discount, 15%, and 5-yr were reconstruction choices, NOT Brandon's stated numbers, and it does not drive `buy`.)

## Core idea: the EPS-growth line / reversion to the mean
- Plot a line of where price *should* be based on the underlying companies' actual earnings-per-share
  growth. He calls it interchangeably the **earnings-per-share growth line, intrinsic value, true
  value, or "gravity."**
- Thesis: price oscillates above and below the line but is always pulled back to it (**reversion to
  the mean**). *"Markets above it go back down to the mean line of growth; markets below it revert
  back up."*
- **Below the line = undervalued = bullish / sell puts. Above the line = overvalued = cautious.**
  *"When the market goes below this EPS growth line, that's a time to be bullish. When it goes above
  it, that is a time to be cautious."*

## Layer 1 — individual stock: the intrinsic-value calculator
A spreadsheet calculator (he gives it away free, linked under his videos) with **two inputs**:
1. **Trailing-12-month EPS** — actual reported number, sanity-checked (*"earnings per share TTM is
   $248, so plug in 248"*).
2. **Assumed annualized growth rate for the next 5 years** — his best guess, deliberately
   conservative (*"NVIDIA ~60%/yr; I know it's 100% now but maybe year five it's lower"*; *"it's just
   a best estimation"*).

Output = **intrinsic value per share**, compared to current price → % over/under.

Worked examples (verbatim):
| Stock | Intrinsic value | Price | Read |
|---|---|---|---|
| NVIDIA | ~$172 | ~$200 | mildly overvalued — "not an extreme deal, not an extreme bubble" |
| Nikola | ~$13 | $45 | **337% of intrinsic value** — "out of control expensive," not a buyer |
| Tesla | ~$155 | higher | "still expensive, I am not a buyer at these values" |

## Buy / sell thresholds
- **Buy shares only ~15% below intrinsic value** for a margin of safety. *"I like to buy stocks
  trading 15% below intrinsic value so I have a margin of safety."*
- **Sell puts** when the name is well below the line (deeper discount than the share-buy threshold);
  the deeper below, the harder he "strikes" (more notional).
- Feeds directly into [[strike-selection]] (strike ~10–12% below price *and* below intrinsic value)
  and [[entry-timing]] (sell into fear when price is clearly under the line).

## P/E cross-check (second lens)
- Compare current **P/E ratio to its own historical average** (broad market long-run norm ~15–20),
  judged *relative to growth*. A P/E of 52 isn't "expensive" if growth justifies it; a P/E of 27 with
  slowing growth is. He computes P/E = price ÷ TTM EPS as a quick gut check alongside the calculator.

## Layer 2 — whole market
- Same method on the S&P 500 and Nasdaq: plot the index EPS-growth line, measure how far price sits
  above/below. Recent read: **~8% above the line → "5–10% overvalued… not a bubble, but not a
  screaming buy."** He extends the line ~1 year forward to estimate where the market "should" be.

## Caveats he states himself
- The growth-rate input is the whole ballgame and it's a guess → stay conservative.
- Some names (Tesla) are near-impossible to value due to optionality (robotaxi, Optimus).
- Plotting the line *"is not the end-all be-all"* — layer in how the broader economy is doing.

## One line
Trailing EPS × a conservative 5-year growth assumption → intrinsic value per share; buy ~15% under
it, sell puts well under it, get cautious when price runs above the EPS line — because everything
reverts to that line.
