#!/usr/bin/env python3
"""Render _valuation_result.json into the deliverable markdown file."""
import json
ROOT='/home/john/repos/leaps'
r=json.load(open(f'{ROOT}/_valuation_result.json'))
p=r['params']

def table(rows):
    out=["| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |",
         "|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|"]
    for i,x in enumerate(rows,1):
        g=f"{x['g']*100:.0f}%" if x['g'] is not None else "—"
        intr=f"${x['intrinsic']}" if x['intrinsic'] is not None else "—"
        pct="no earnings" if x['flag']=='no_earnings' else f"{x['pct']:+.0f}%"
        nm=(x['name'] or '')[:26]
        out.append(f"| {i} | {x['ticker']} | {nm} | ${x['price']} | {x['ttm_eps']} | {g} | {intr} | {pct} | {x['flag'] or ''} |")
    return "\n".join(out)

def section(s):
    L=[f"## {s['label']}",
       f"Valued {s['total_valued']} holdings · **{s['n_each']} most undervalued (BULLISH)** vs "
       f"**{s['n_each']} most overvalued (BEARISH)** · {len(s['neutral'])} near-median (neutral, excluded).",""]
    L.append(f"### 🟢 BULLISH — {s['n_each']} most undervalued (price most below Brandon-intrinsic)")
    L.append(table(s['bullish'])); L.append("")
    L.append(f"### 🔴 BEARISH — {s['n_each']} most overvalued (price most above Brandon-intrinsic)")
    L.append(table(s['bearish'])); L.append("")
    if s['neutral']:
        L.append(f"<details><summary>Neutral / near-median ({len(s['neutral'])}) — excluded from the split</summary>\n")
        L.append(table(s['neutral'])); L.append("\n</details>\n")
    return "\n".join(L)

hdr=f"""# QQQ, SPY & Russell 1000 — Brandon Valuation Screen (Bullish vs Bearish)

**Generated:** 2026-06-07 · **Method:** Brandon's valuation rules (see `wiki/strategy/valuation-method.md`).
Data: yfinance (price, trailing-12-month EPS, forward EPS). This is an **estimate/guess**, exactly as
Brandon frames his own calculator — the growth input is a best-guess and drives everything.

## How each stock was scored
`intrinsic = TTM_EPS × (1+g)^5 × {p['FAIR_PE']:.0f} ÷ (1+{p['DISCOUNT']:.2f})^5`, where conservative growth
`g = median(analyst current-year est, next-year est, TTM YoY earnings growth)`, floored at 0 and
capped at {p['GCAP']*100:.0f}% (Brandon's conservatism). Using a multi-year growth signal — not just
next-year's analyst bump — is what keeps fast compounders (e.g. GOOGL) from being mislabeled.
A stock is **undervalued (bullish)** when price is below intrinsic, **overvalued (bearish)** when above.
Stocks are ranked by under/over %, then split into equal halves (the {p['FAIR_PE']:.0f}× multiple and
{p['DISCOUNT']*100:.0f}% discount are identical for every stock, so they don't affect which half a stock
lands in — only the reported %). Companies with **no positive trailing earnings can't be valued this
way** and are forced to the bearish side, flagged `no_earnings` (Brandon: "if you can't value it
conservatively, skip it").

> Caveat: a single fixed fair multiple and a mechanical growth proxy stand in for Brandon's per-company
> judgment. He would hand-tune the growth rate and skip names he can't value (e.g. Tesla). Treat this as
> a systematic first-pass screen in his style, not his exact hand-built call on each name.
>
> Index-proxy note: SPY/QQQ use official constituent lists. "Russell 1000" and "Global" are built from
> market-cap rankings (largest ~1000 US-listed / largest ~1000 worldwide), so they include a few ADRs and
> closed-end funds (e.g. CET) that the official Russell 1000 excludes, and some names show odd EPS. The
> ranking method is unchanged; treat these two as faithful proxies, not the exact official membership.
>
> Data note: a few tickers (e.g. BKNG) show a scaled/incorrect absolute price from the yfinance feed.
> This does **not** affect the bullish/bearish split — the score is driven by the price-to-earnings
> ratio (EPS/price), which stays correct under a uniform scaling of both, so the ranking is robust.

---
"""
body=hdr+section(r['qqq'])+"\n---\n"+section(r['spy'])
if 'russell' in r: body+="\n---\n"+section(r['russell'])
if 'global' in r: body+="\n---\n"+section(r['global'])
open(f'{ROOT}/QQQ_SPY_valuation_bullish_bearish.md','w').write(body+"\n")
print("report written:", f'{ROOT}/QQQ_SPY_valuation_bullish_bearish.md')
