# Audit Report — What I Got Wrong vs What Brandon Actually Said

**Date:** 2026-06-07
**Method:** Re-read the 28 highest-signal strategy transcripts in full (6 parallel deep reads), compared
every claim I made and every working assumption against Brandon's actual words, quote-checked the
high-impact items by hand. Sources are video IDs under `transcripts/`.

## Honest headline
I built the valuation screen from a **partial** reading of the method and pattern-matched the rest. The
core skeleton I captured (portfolio-secured long-dated puts on undervalued quality, recycle premium into
shares + calls, assignment-value sizing) is correct. But Brandon's actual method is a **top-down funnel
with a 100-point company scorecard and a macro/market-direction gate**, and I shipped roughly the
valuation+growth slice of it. Below is everything wrong or missing, with corrections.

---

## A. CONFIRMED ERRORS (things I stated that are wrong or over-precise)

### A1. Base-portfolio allocation — I presented one variant as canonical, and missed bonds
- **I said:** 40% S&P / 40% Nasdaq / 15% individual / 5% long-dated calls.
- **Reality:** Brandon gives **different splits in different videos** — "40/40/**20**" (56GQISel_iY,
  5upcZf1sEJ0), "40/40/**15**" + a 5% calls line (the one I cited, -3fgTkSJs2E), "40/40/**10**", and
  most recently "**~35/35**, rest singles" (J930c1BgrnU). More importantly he repeatedly includes
  **BONDS** (SGOV / BLV) as dry powder: *"my base portfolio is heavily in the S&P and the NASDAQ, and
  then there's some bonds in there too."* The 5% calls "sleeve" is not a fixed allocation — **calls are
  funded from recycled put premium and capped ~3–5% per name** (qSMJShRLDv8: "UNH 1%, Nvidia 3%, Meta 4%").
- **Correct version:** ~70–80% split between S&P 500 and Nasdaq, ~10–20% individual quality names,
  **bonds as the parking spot when the market is rich**; calls are per-trade, ~3–5%/name, not a base bucket.

### A2. "Covered calls are a trap" — wrong as a flat statement
- **I said (contradictions.md):** covered calls are a rejected trap.
- **Reality:** Brandon **sells calls deliberately at market tops for cash flow** (*"I'm going to sell
  them those call options for top dollar… generate cash flow when the market's getting expensive"*),
  ranks covered calls as a usable strategy, and uses them to exit assigned shares when premium > margin
  interest. What he actually bans is **naked calls** (*"I will never sell naked calls"*) and **mindless
  wheel-style covered-call writing regardless of valuation**. 
- **Correct version:** selling calls is a sanctioned *bearish/overvalued-market* tactic; the trap is
  doing it on cheap stocks / capping upside on names you're bullish on.

### A3. Strike "~10–12% below price" — badly understated
- **Reality:** real strikes run from at-the-money to **~19–44% below spot**, scaled by conviction;
  the true anchor is **margin of safety vs the forward EPS line**, which he extrapolates to **~27–50%**.
  Examples: NVDA 145 strike at $180 (~19%), 150 at $189 (~21%); a 110 strike at "25% below intrinsic …
  almost a 50% margin of safety" forward. "10–12%" was a single one-month example.
- **Correct version:** strike = as deep below the (forward) EPS line as premium still makes worth
  collecting; deeper when cheaper. Not a fixed percent.

### A4. Duration "~2 years" — it's ~1 year on average
- **Reality:** *"I sell longer duration puts roughly call it one year on average"* (B8dFMZfOV6I); range
  1 year to ~2.5 years (2028 contracts), longer when cheaper; 6-month floor.
- **Correct version:** "1+ year, ~1yr typical, up to ~2.5yr when very undervalued."

### A5. Profit-taking "~70%, squeeze last 30%" — over-generalized
- **Reality:** it's **instrument-specific**. Sold puts: close around **70–95%**, gated by valuation +
  whether buying power is needed elsewhere; the real metric is **profit captured per month held**
  (he closed at 70–75% after only 4 of 24 months). **Shares and bought calls have NO % threshold** —
  you exit only when *the story changes* / it's meaningfully overvalued (*"it has nothing to do with
  percent profit and everything to do with the fundamental value"*). Trim order: **calls first, then
  sold puts, then shares last.**
- **Correct version:** per-instrument rule above; my single 70/30 rule only loosely fits sold puts.

### A6. Assignment-value sizing — missing the actual denominator and the bands
- **I said:** keep assignment value coverable by liquidating the portfolio through a 50% crash.
- **Reality:** the denominator is **"7-day liquidity"** — cash you can raise in 7 days across accounts
  (*"$490,000 … 7-day liquidity"*; *"come up with $2 million in seven days"*). The **max ratio is
  regime-dependent**: ~30–40% now, **0–50% in a lofty market, up to 75–100% in a cheap market / COVID**;
  he raises the cap as the market falls. Survives **50–70%** crashes. Assigned **~4× in ~10 years** (not 12).
- **Correct version:** assignment value ÷ 7-day liquidity; cap scales inversely with market richness.

### A7. The intrinsic-value formula I implemented is NOT Brandon's actual method
- **I built:** `intrinsic = TTM_EPS × (1+g)^5 × 20 ÷ 1.10^5`, with g capped 30%, "buy 15% below."
- **Reality:** his actual method is the **"golden line"** (he names it): take a **2-year window**, compute
  **EPS % growth** from the reports, draw a line rising by that exact %, and compare to the **actual price
  % move** — the gap is the over/under-valuation. He claims a **94% accuracy** ("94% chance of accurately
  predicting"). He **validates** it with a P/E apples-to-apples check (start P/E ≈ end P/E, or the line is
  "skewed"). His intrinsic value also folds in **P/S, revenue growth, margin expansion, guidance, macro,
  interest rates** — not just EPS. The fixed "20 multiple," "10% discount," "15% below," and "5-year"
  are **my inventions/inferences**, never stated.
- **Impact:** my screen is a *defensible growth-adjusted proxy* but it is **not** Brandon's golden-line
  method. This is the single most important thing to be honest about. (More in section C.)

### A8. Scorecard — I had 5 components; there are more, and they're weighted
- **Reality:** the company score (out of 100, **allocate when >75**) grades **Valuation, Growth, Moat,
  Execution risk, Sentiment, and Macro** — **"Sentiment" is a 6th named input I omitted**, and the
  components are explicitly **weighted**. The 20/20/20/10/30 point split I wrote is from real examples but
  is not stated as the fixed weighting.
- **"IV sheet" was my misread:** there is **no implied-volatility sheet**; it's the **Intrinsic-Value
  sheet** (separate from the intrinsic-value *calculator*). I'll fix that wording.

---

## B. MAJOR OMISSIONS (in the videos, absent from everything I prepared)

1. **The top-down funnel (the actual workflow):** market valuation → economic scorecard → company score
   → strike/expiration. Each gate must pass before the next. (kgfGRlRO25Y)
2. **The >20%-overvalued market GATE:** if S&P/Nasdaq get >20% overvalued, **stop buying** and park in
   **bonds/CDs/SGOV**; rotate back when price falls below the EPS line. (56GQISel_iY, m9w8T0qW1s8) —
   this is the "current market direction" you said was missing.
3. **The "four needle movers"** for market direction: economy, market valuations, EPS growth, interest
   rates. (m9w8T0qW1s8)
4. **Bonds + IRA tax-free rotation** as the macro overlay engine. (m9w8T0qW1s8, kgfGRlRO25Y)
5. **Bullish hierarchy:** bullish→buy shares, ultra→sell puts, ultra-ultra→buy calls; trim in reverse.
6. **Moat / pricing power / "will competition wipe them out"** — the quality gate (now a proxy; see C).
7. **Execution risk** (moonshot plans score low) — qualitative.
8. **Sentiment** as a scored input + **sell into fear/high IV** for richer premium.
9. **Technical confirmation:** Bollinger Bands + RSI to confirm an oversold entry (`/chart` in Discord).
10. **Premium reinvest split by conviction:** ~80/20 shares/calls low-conviction → up to 50/50 high.
11. **Greeks stance:** delta is rejected as a strike picker ("1–2% of the puzzle"); theta is the seller's
    tailwind; gamma/vega/rho ignored.
12. **Roll-for-tax-loss** (wash-sale workaround: change strike/expiry) and **roll for a net credit**;
    roll-down-and-out is the *first* defense before selling base shares.
13. **Gating rules:** never sell puts on anything you're not OK owning; "beat the S&P/Nasdaq or you're
    wasting your time"; **95–99% of candidates are a 'no'**; add more on further dips (don't call the bottom).
14. **Tax:** LEAPS held >1yr = long-term capital gains; uses an IRA for tax-free reallocation.
15. **Triple-whammy on calls:** profit from price + theta/time + IV/sentiment recovery.
16. **Access:** Level-3 options + margin required.

---

## C. Impact on the stock list / screen specifically

What this means for `universe_fractional.csv`, concretely:

- **The verdict (bullish/bearish) is a growth-adjusted-earnings-yield proxy, NOT Brandon's golden line.**
  His golden line is a 2-year EPS%-vs-price%-divergence read. Mine ranks similarly in spirit (cheap = lots
  of earnings/growth per dollar of price) and is fine as a *first-pass filter*, but it is not his method
  and will disagree on individual names. **I should rebuild the valuation column on the actual golden-line
  method** (2yr EPS growth vs 2yr price move, with the P/E-validity check) to be faithful — that's the
  biggest correctable gap and I recommend doing it next.
- **Moat is now in the list** (this turn) as `moat_proxy_20` from margins/ROE/debt — an approximation of
  his qualitative moat, plus a **MARKET_DIRECTION.md** deploy gauge for the macro overlay. But the full
  scorecard (Sentiment, Execution risk, weighted Macro, >75-to-allocate) is still not computed.
- **The screen has no market GATE yet:** Brandon would not deploy at all if the market is >20% overvalued.
  The market-direction file now reports the read, but the list doesn't act on it.
- **"Bullish" ≠ "buy" in Brandon's world:** a name must clear the company score (>75) AND the market gate.
  My list flags undervaluation only — one of five-plus inputs.

---

## D. Corrections applied this turn
- Added `wiki/strategy/scorecard.md` documenting the full 100-pt scorecard (now being corrected for the
  Sentiment input and the IV-sheet→intrinsic-value-sheet fix).
- Added moat proxy + quality columns and `MARKET_DIRECTION.md` to the pipeline (market-direction overlay).
- The wiki strategy pages are being corrected for: base allocation + bonds (A1), covered calls (A2),
  strike depth (A3), duration (A4), profit-taking (A5), 7-day-liquidity + bands (A6), the golden line +
  its plotting/validity (A7), and the funnel + market gate (B1–B4).

## E. Recommended next step (your call)
Rebuild the valuation column on Brandon's **actual golden-line method** (2-yr EPS-growth vs price-move,
P/E-validity-checked) instead of my proxy formula, and add the **>20% market gate** + **company-score
(>75) filter** so the list reflects his real funnel, not just the valuation slice. This is the honest fix
for the "60% was missing" problem.
