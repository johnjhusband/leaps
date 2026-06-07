---
id: instrument-selection
title: Instrument Selection
type: decision
dimension: instrument-selection
evidence_digest: ../_meta/digests/instrument-selection.md
updated: 2026-06-07
---

# Instrument Selection

**Resolved rule:** Sell puts only on high-quality companies and the major indexes (S&P 500, Nasdaq/QQQ) and megacaps (NVDA, META, AMD, TSM, UNH) that are trading BELOW intrinsic value (below the EPS-growth line) at the time. Valuation gates every trade — a put 10% below price is not safe if the stock is 50% overvalued. Avoid high-beta meme/junk names; they fall 50% in an 11% index drawdown. Greeks tell you nothing about valuation.

**How "below intrinsic value" is actually computed:** see [[valuation-method]] — trailing EPS × a conservative 5-year growth rate → intrinsic value per share; buy ~15% under it; the market/index version plots the EPS-growth line and watches for reversion to the mean.

See canonical [[strategy-spec]]. Full deduped evidence: `_meta/digests/instrument-selection.md`.

## Top evidence (signal 5)
- [5] Typically, the base portfolio is going to be somewhere along the lines of 40% in the S&amp;P 500, 40% in the NASDAQ, maybe 15% in individual companies, and then 5% in long-term call options.  ([[-3fgTkSJs2E]])
- [5] There's no surprise that they try to overtrade buying crap companies with crap option strategies like cover calls suck, cash puts suck, the wheel sucks, spread suck, poorman cover calls suck.  ([[-3fgTkSJs2E]])
- [5] You can't roll up and out forever, but you could theoretically roll down and out forever on an index like the S&amp;P or the NASDAQ or a good company because eventually the earnings per share growth is going to come back and eventually that contract is going to expire worthless.  ([[-3fgTkSJs2E]])
- [5] And all the margin of safety is is basically you're just buying a great company for less than what it's worth.  ([[1Ct_EGrYBZU]])
- [5] I would do portfolio secured puts, have my money invested in my base portfolio, which you know is like S&amp;P, Nasdaq, various good companies at good prices, and I'm capturing that bullish tailwind going up into the right, not having that cash dragged by cash secured puts.  ([[1Ct_EGrYBZU]])
- [5] Take the money that you sell the put on and go invest it because if you're selling the put, you're bullish on the company.  ([[3NjaSgq-MtM]])
- [5] I'd probably sell like a 130 strike price put if I feel like the company was trading below intrinsic value at the time.  ([[4n0IUuy0_UI]])
- [5] So, let's flip it the other way and say that somehow you happen to time the bottom of the market perfectly and you bought a call option on Nvidia right here when the share price was roughly 96 bucks a share.  ([[4n0IUuy0_UI]])
- [5] Well, the pro is going to sell put options, take the cash flow, and then go buy call options with the premium because as Nvidia stock is falling and getting a little bit cheaper, it's becoming more compelling to buy call options.  ([[4n0IUuy0_UI]])
- [5] Like does it make sense to sell put options on Nvidia when the stock just ran up a lot?  ([[4n0IUuy0_UI]])
