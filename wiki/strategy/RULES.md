---
id: rules
title: Brandon Strategy — Executable Ruleset
type: spec
dimensions: [instrument-selection, valuation-method, strike-selection, expiration-duration, entry-timing, exit-profit-taking, assignment-handling, position-sizing-ratios, market-regime, scorecard]
updated: 2026-06-07
note: Operational distillation of [[strategy-spec]]. CORRECTED 2026-06-07 after the full-transcript audit (AUDIT_REPORT.md).
---

# Brandon Strategy — Executable Ruleset

## Top-down funnel (do the gates IN ORDER) — [[scorecard]]
1. Gate 1 — **Market valuation:** if S&P/Nasdaq are **>20% overvalued**, do NOT deploy; park in bonds/CDs/SGOV and wait for price to fall below the EPS line. Otherwise proceed.
2. Gate 2 — **Economic scorecard** (his /200 macro read; "four needle movers" = economy, market valuation, EPS growth, interest rates) must be favorable.
3. Gate 3 — **Company score** (Valuation, Growth, Moat, Execution risk, Sentiment, Macro — weighted, out of 100): only act on names scoring **>75**.
4. Gate 4 — only then pick **strike & expiration**.

## Setup
5. Build the base portfolio first (hold horizon **≥5 years**): ~70–80% split across S&P 500 + Nasdaq, ~10–20% individual quality names, and **bonds (SGOV/BLV) as dry powder** when the market is rich. Calls are NOT a base allocation — they come from recycled premium, capped ~3–5% per name.
6. The base portfolio is collateral for every sold put. Quality/indexes only — never meme/high-beta junk.

## Valuation — the "golden line" — [[valuation-method]]
7. Value via the golden line: over a ~2-year window, draw a line rising by the company's **EPS % growth**, compare to the **actual price % move**; the gap = under/over-valuation (he claims ~94% accuracy).
8. Validity check: start P/E ≈ end P/E (apples-to-apples) or the line is skewed/unreliable.
9. Fold in P/S, revenue growth, margin expansion, guidance, macro — not EPS alone. Undervalued = price below the line. Only act on quality you'd be glad to own; if you can't value it, skip it (95–99% are a "no").

## Entry — [[entry-timing]] [[strike-selection]] [[expiration-duration]]
10. Sell puts only when the name is undervalued AND fear/IV is high. Never after a run-up / above intrinsic.
11. Strike: as deep below the **forward EPS line** as premium still makes worth collecting — typically **~19–44% below spot**, scaled by conviction (NOT a fixed 10–12%); deeper when cheaper.
12. Duration: **~1 year on average** (range 1 to ~2.5yr, longer when cheaper; 6-month floor). Never short-duration.
13. Confirm the entry technically (oversold: near lower Bollinger band, low RSI). Never sell puts on anything you're not OK owning. Add MORE on further dips — don't try to call the bottom.

## Recycle the premium
14. Immediately deploy premium into undervalued **shares + barely-OTM long-dated calls**; split ~**80/20 shares/calls** low-conviction → up to **50/50** high-conviction. Never buy ITM or short-duration calls. Premium may also be withdrawn as income.
15. Bullish hierarchy: bullish → buy shares; ultra → sell puts; ultra-ultra → buy calls.

## Risk cap — [[position-sizing-ratios]]
16. Portfolio-secured puts only (no cash-secured). Track total assignment value = cash owed if every sold put were assigned.
17. Size it as **assignment value ÷ 7-day liquidity** (cash raisable in 7 days). Max ratio is regime-dependent: **0–50% in a lofty market, up to 75% (≈100% COVID-cheap)**; raise the cap as the market falls. If a trade breaches the cap, don't sell it.
18. Sized this way the book survives a **50–70%** crash (assigned only ~4× in ~10 years).

## Exit (instrument-specific) — [[exit-profit-taking]]
19. Sold puts: close around **70–95%** profit, gated by valuation + need for buying power; the real metric is profit-per-month-held.
20. Shares & bought calls: **no % rule** — exit only when the story changes / it's meaningfully overvalued.
21. Trim order when de-risking: calls first → sold puts → shares last.

## Assignment — [[assignment-handling]]
22. Rare (~4× in ~10 years). If assigned, in order: **roll down-and-out** (also harvests a tax loss — change strike/expiry to dodge wash-sale, often for a net credit) → sell bonds/base shares → margin last.
23. You can roll down-and-out almost indefinitely on an index/quality name; never count on rolling up-and-out.

## Calls you SELL & the trap list — [[contradictions]]
24. Banned: cash-secured puts, the wheel, spreads, poor-man's covered calls, short-duration anything, and **naked calls**. Covered calls are NOT banned — sell calls deliberately when a name/market is **overvalued** (stretched above the EPS line) for cash flow, or to exit assigned shares when premium > margin interest. The trap is writing them on cheap stock.

## Mindset — [[market-regime]]
25. Selling beats buying (theta is the seller's tailwind; delta is a near-useless strike picker). Beat the S&P/Nasdaq or you're wasting your time. The strategy is built to PROFIT from a 50% crash, not die in it — fear is the inventory you sell.
