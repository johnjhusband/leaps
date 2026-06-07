#!/usr/bin/env python3
import json, re, os
import os as _os; ROOT=_os.path.dirname(_os.path.abspath(__file__)); S=f'{ROOT}/wiki/strategy'
RULES={
'instrument-selection':("Instrument Selection",
 "**Resolved rule:** Sell puts only on high-quality companies and the major indexes (S&P 500, "
 "Nasdaq/QQQ) and megacaps (NVDA, META, AMD, TSM, UNH) that are trading BELOW intrinsic value "
 "(below the EPS-growth line) at the time. Valuation gates every trade — a put 10% below price is "
 "not safe if the stock is 50% overvalued. Avoid high-beta meme/junk names; they fall 50% in an 11% "
 "index drawdown. Greeks tell you nothing about valuation."),
'strike-selection':("Strike Selection",
 "**Resolved rule:** Sell puts ~10–12% below current price, leaving a margin of safety down to "
 "intrinsic value / the EPS line. High conviction + clearly cheap → strike hard (more notional). "
 "Calls you buy are barely out of the money — never pay ITM premium. Examples: NVDA 180 put, "
 "Meta 560, UNH 230."),
'expiration-duration':("Expiration / Duration",
 "**Resolved rule:** ~2-year (LEAPS) expirations for both sold puts and bought calls; long duration "
 "over monthly, always. Accept low theta in exchange for high probability and EPS-growth runway — "
 "one 2-year put (~$30k) beats winning ~12 monthly puts in a row. Long duration enables rolling "
 "down-and-out and waiting out any drawdown."),
'entry-timing':("Entry Timing",
 "**Resolved rule:** Sell puts INTO fear — dips, panic, high implied volatility, after a quality "
 "name has fallen and gone cheap. That is when premium is inflated and rebound most likely. Never "
 "sell puts after a run-up / when overvalued. Immediately recycle premium into undervalued shares "
 "and barely-OTM long calls."),
'exit-profit-taking':("Exit / Profit-Taking",
 "**Resolved rule:** On sold options, buy back cheap (sold high, buy back low) or let expire "
 "worthless. Take profit early (~70%) only if the buying power is needed for a more compelling "
 "setup; otherwise squeeze the last ~30% to expiration (near-guaranteed). Profit-taking timing is "
 "the single hardest skill."),
'assignment-handling':("Assignment Handling",
 "**Resolved rule:** Assignment is rare (~3–4x in 12 years). If assigned: (a) sell base-portfolio "
 "shares to fund it, (b) take assignment on margin, or (c) roll down-and-out to a cheaper strike + "
 "further expiration. You can roll down-and-out nearly forever on an index/quality company because "
 "EPS growth returns and the contract expires worthless; you cannot roll up-and-out forever."),
'position-sizing-ratios':("Position Sizing & Ratios",
 "**Resolved rule (risk core):** Use portfolio-secured puts — base portfolio is collateral, no "
 "parked cash. Track 'sold-put assignment value' = total cash owed if every sold put were assigned "
 "at once; keep it coverable by liquidating the base portfolio even after a ~50% drawdown "
 "(e.g. $300k assignment value vs a $600k portfolio). Scale assignment value up when more bullish, "
 "down when less. 'Keep your ratios in check' is what makes the book survive any volatility."),
'market-regime':("Market Regime",
 "**Resolved rule:** Long-duration contracts + ratios-in-check + portfolio collateral survive both "
 "bull and bear; volatility never force-closes you. The design exists to CAPITALIZE on a 50% crash "
 "(sell overpriced fear premium), not be wiped out — the Buffett-2008 analogy. Buying options needs "
 "perfect timing; selling is structurally easier."),
}
for dim,(title,rule) in RULES.items():
    digest=f'{ROOT}/wiki/_meta/digests/{dim}.md'
    ev=[]
    if os.path.exists(digest):
        for l in open(digest):
            if l.startswith('- [5]'): ev.append(l.rstrip())
            if len(ev)>=10: break
    fm=f"---\nid: {dim}\ntitle: {title}\ntype: decision\ndimension: {dim}\nevidence_digest: ../_meta/digests/{dim}.md\nupdated: 2026-06-07\n---\n\n"
    body=f"# {title}\n\n{rule}\n\nSee canonical [[strategy-spec]]. Full deduped evidence: `_meta/digests/{dim}.md`.\n\n## Top evidence (signal 5)\n"+"\n".join(ev)+"\n"
    open(f'{S}/{dim}.md','w').write(fm+body)
print('wrote', len(RULES), 'decision pages')
