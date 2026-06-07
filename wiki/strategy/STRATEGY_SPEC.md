---
id: strategy-spec
title: Brandon Strategy — Canonical Implementable Spec
type: spec
dimensions: [instrument-selection, strike-selection, expiration-duration, entry-timing, exit-profit-taking, assignment-handling, position-sizing-ratios, market-regime]
sources: 296 videos; synthesized from high-signal (4-5) claims in _meta/digests/
updated: 2026-06-07
---

# Brandon Strategy — Canonical Spec

**One sentence:** Sell long-dated (~1yr avg, up to ~2.5yr / LEAPS) put options on undervalued, high-quality
companies and indexes — collateralized by a stock *portfolio* instead of cash ("portfolio-secured
puts") — into fear/high-IV dips, and recycle the premium into undervalued shares and barely-OTM
long-dated call options, while keeping a hard cap on total assignment exposure so the book survives
a 50% crash.

This file is the source of truth. Everything below is an executable rule. Citations point to the
strongest source videos `[[id]]`; full evidence is in the per-dimension digests and video pages.

---

## 0. The edge (why it works)
- A sold put is the trade. When fear is high, retail overpays for downside protection, so puts are
  sold for **more than they're worth**; the underlying is simultaneously cheap (below intrinsic
  value). You collect inflated premium on a stock that is statistically likely to rebound. [[4n0IUuy0_UI]] [[56GQISel_iY]]
- Option Greeks (delta/theta) know nothing about valuation. Valuation, not Greeks, is the engine.
  Over a long horizon price follows the EPS-growth line; short-term volatility is noise. [[5_PbEUZDdEA]] [[VKnGRB016o8]]
- Buying options (calls or puts) needs perfect direction AND timing and is structurally hard;
  selling options is structurally easier. Buying puts also means betting against the entire
  company/CEO/board. [[5upcZf1sEJ0]]

## ★ The top-down funnel (CORRECTED 2026-06-07 — run this FIRST, before everything below)
Every trade passes gates in order: **(1) overall market valuation** → **(2) economic scorecard** →
**(3) company score (>75/100)** → **(4) strike & expiration**. Skipping a gate is the mistake. The
market gate is hard: **if S&P/Nasdaq are >20% overvalued, stop buying — park in bonds/CDs/SGOV** and
rotate back when price falls below the EPS line. See [[scorecard]] and [[market-regime]].

## 1. Base portfolio (the collateral engine — build this FIRST)
- Target allocation **varies across his videos**: split ~70–80% between S&P 500 and Nasdaq (stated as
  40/40, 35/35), **~10–20% individual quality names**, and **BONDS (SGOV/BLV) as dry powder** when the
  market is rich. The "5% calls" I cited earlier is NOT a fixed sleeve — **calls are funded from recycled
  put premium and capped ~3–5% per name.** [[-3fgTkSJs2E]] [[56GQISel_iY]] [[J930c1BgrnU]] [[m9w8T0qW1s8]]
- Only build it if you can hold **≥5 years**. [[56GQISel_iY]]
- This portfolio is the **collateral / buying power** for selling puts. You sell puts against it,
  not against parked cash. It keeps capturing the market's upward tailwind instead of dragging in cash. [[1Ct_EGrYBZU]]
- Example sizing: $100k → $40k SPY, $40k QQQ, $20k individual companies. [[56GQISel_iY]]

## 2. Instrument selection — what to sell puts on
- Only **high-quality companies and the major indexes** (S&P, Nasdaq) and megacaps trading
  **below intrinsic value** (below the EPS-growth line). Named examples: NVDA, META, AMD, TSM, UNH. [[56GQISel_iY]] [[3NjaSgq-MtM]]
- Valuation gates everything: only sell the put if the company is undervalued *at that time*; a put
  10% below price on a stock that is 50% overvalued is not safe. [[4n0IUuy0_UI]]
- **How undervalued/overvalued is decided** — trailing-12-month EPS × a conservative 5-year growth
  assumption → intrinsic value per share (his free calculator); buy shares ~15% under it, sell puts
  well under it, cautious when price runs above the EPS-growth line (reversion to the mean). Full
  method (calculator inputs, thresholds, P/E cross-check, worked examples): [[valuation-method]].
- **Avoid** high-beta meme/junk names (the SOFI/PLTR/EOS bucket) — they fall 50% in an 11% Nasdaq
  drawdown and destroy short-duration sellers. [[HOmunMw1Fvw]]
- See [[instrument-selection]].

## 3. Strike selection
- **CORRECTED:** sell puts as deep below the **forward EPS line** as premium still makes worth
  collecting — in practice **~19–44% below spot**, scaled by conviction (deeper when cheaper), NOT a
  fixed 10–12%. Long duration enables the deeper strike. [[1Ct_EGrYBZU]] [[4n0IUuy0_UI]] [[B8dFMZfOV6I]]
- High conviction + clearly cheap → **"strike hard"** (more contracts / more notional). [[3NjaSgq-MtM]]
- Long calls you buy: **barely out of the money** — never pay ITM premium. [[4n0IUuy0_UI]]
- Worked example: NVDA 1-year 180 put → ~$2,500 premium; Meta 560 strike out to 2028; UNH 230 strike
  → $42,000 premium. [[7xoiZMwFhdo]] [[-3fgTkSJs2E]] [[3NjaSgq-MtM]]
- See [[strike-selection]].

## 4. Expiration / duration
- **CORRECTED: ~1 year on average** (range 1 to ~2.5yr, longer when cheaper; 6-month floor) for both
  sold puts and bought calls. Long duration over monthly, always. [[B8dFMZfOV6I]] [[32pMRko-uHA]] [[1Ct_EGrYBZU]]
- Theta objection rebutted: one 2-year put collecting ~$30k beats needing to win ~12 monthly puts in
  a row to collect the same; long duration also gives EPS growth time to bail out the strike. [[56GQISel_iY]]
- Long duration is what lets you roll down-and-out and wait out any drawdown. [[HOmunMw1Fvw]]
- See [[expiration-duration]].

## 5. Entry timing
- **Sell puts into fear** — dips, panic, high implied volatility, after a stock has fallen and gone
  cheap. That is when premium is inflated and the rebound is most likely. [[4n0IUuy0_UI]] [[56GQISel_iY]]
- Do **not** sell puts after a big run-up / when the name is overvalued. [[4n0IUuy0_UI]]
- "When opportunity comes, you have to strike and strike hard." [[3NjaSgq-MtM]]
- Immediately recycle the premium: buy undervalued shares + barely-OTM long calls. [[1Ct_EGrYBZU]] [[32pMRko-uHA]]
- See [[entry-timing]].

## 6. Position sizing & ratios (THE risk core — do not skip)
- Use **portfolio-secured puts (PSP)**: base portfolio is collateral; do not park cash for
  cash-secured puts. [[1Ct_EGrYBZU]] [[-3fgTkSJs2E]]
- Track **"sold-put assignment value"** = total cash you'd owe if *every* sold put were assigned at
  once. Keep it **coverable by liquidating the base portfolio even after a large drawdown.** [[-3fgTkSJs2E]] [[32pMRko-uHA]]
- **CORRECTED:** the denominator is **"7-day liquidity"** (cash raisable in 7 days), not portfolio
  value. Max ratio is regime-dependent: **0–50% lofty, up to 75% (≈100% COVID-cheap)**; raise the cap
  as the market falls. Survives a **50–70%** crash. Scale up when cheap, down when lofty. [[-3fgTkSJs2E]] [[RxPLOvlPHfE]]
- "Keep your ratios in check" is repeated as the thing that makes the strategy survive any
  volatility. [[CY-vbMx5k4g]] [[1Ct_EGrYBZU]]
- See [[position-sizing-ratios]].

## 7. Assignment handling
- Assignment is rare: **~4 times in ~10 years** (COVID, 2022, etc.). Rolling down-and-out also harvests
  a tax loss (change strike/expiry to dodge wash-sale, often for a net credit). [[1Ct_EGrYBZU]] [[CY-vbMx5k4g]]
- If assigned, three levers: (a) **sell shares from the base portfolio** to fund the assignment,
  (b) **take assignment on margin**, or (c) **roll down-and-out** to a cheaper strike + further
  expiration. [[-3fgTkSJs2E]] [[32pMRko-uHA]]
- You can roll **down-and-out almost indefinitely** on an index or quality company — EPS growth
  eventually returns and the contract expires worthless. You **cannot** roll up-and-out forever. [[-3fgTkSJs2E]]
- See [[assignment-handling]].

## 8. Exit / profit-taking (CORRECTED — instrument-specific)
- Sold puts: close around **70–95%** profit, gated by valuation + need for buying power; real metric is
  profit-per-month-held. [[reuZrvt1P4M]] [[m9w8T0qW1s8]]
- **Shares & bought calls: no % rule** — exit only when the story changes / it's meaningfully
  overvalued. Trim order: calls → sold puts → shares last. [[JXdSkRGoiXE]] [[m9w8T0qW1s8]]
- Knowing when to take profit is the single hardest part for most people. [[m9w8T0qW1s8]]
- See [[exit-profit-taking]].

## 9. Market-regime behavior
- Long-duration contracts + ratios-in-check + portfolio collateral = **survives bull and bear**;
  volatility never force-closes you. [[CY-vbMx5k4g]] [[HOmunMw1Fvw]]
- The whole point of the design is to **capitalize on a 50% crash** (sell overpriced fear premium),
  not be wiped out by it — the Buffett-in-2008 analogy. [[VVeIZNTCOZ4]] [[JXdSkRGoiXE]]
- See [[market-regime]].

---

## Execution checklist (CORRECTED 2026-06-07)
1. **Market gate first:** if S&P/Nasdaq >20% overvalued, don't deploy — sit in bonds/SGOV. Build base
   portfolio (~70–80% SPY+QQQ, ~10–20% quality singles, bonds as dry powder) only if holding ≥5 years.
2. Score candidates with the golden line (2yr EPS% vs price%, P/E-validity-checked) + the company
   scorecard; only act on names scoring **>75**.
3. On a fear-driven dip in a qualifying name: sell a ~1yr (up to ~2.5yr) put **deep below the forward
   EPS line** (~19–44% below spot, conviction-scaled), sized so **assignment value ÷ 7-day liquidity**
   stays under the regime cap (0–50% lofty, up to 75% cheap).
4. Immediately recycle premium → undervalued shares + barely-OTM long calls (~80/20 → 50/50 by conviction;
   calls capped ~3–5%/name). Add more on further dips.
5. Manage exits per instrument: sold puts close ~70–95% (by valuation/buying-power); shares & calls exit
   only when the story changes. Trim order: calls → puts → shares.
6. If assigned: roll down-and-out (harvest tax loss) → sell bonds/base shares → margin last.
7. Never: cash-secured puts, the wheel, poor-man's covered calls, spreads, short-duration, high-beta junk,
   **naked calls**. Covered calls are OK only when overvalued / to exit assigned shares. See [[contradictions]].
