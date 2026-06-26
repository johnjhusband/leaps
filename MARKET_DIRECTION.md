# Market Direction — Deploy Gauge

Brandon deploys aggressively only when the overall market is favorable (his bull-bear scale / economic scorecard). This is our computable version: where each index sits vs intrinsic value.

| Index | Median under/over | Cap-weighted under/over | Breadth (% undervalued) |
|-------|------------------:|------------------------:|------------------------:|
| SPY | -17% | +5% | 37% |
| QQQ | -26% | +7% | 32% |
| Global1000 | -9% | +17% | 46% |

**Read it as:** higher numbers = cheaper market = more bullish to deploy. The absolute level is model-tilted, so the real signal is the **trend across rebalances** — if breadth and medians fall month over month, the market is getting expensive (be selective); if they rise, deploy more.

## Deploy gate (golden line on the S&P — Brandon's >20% rule)
- Median golden-line read across 284 valid S&P names: **-4%** (breadth 47% undervalued).
- **OK to deploy (market roughly fair).** (Gate trips when the market is >20% overvalued, i.e. price ran >20% ahead of earnings. Uses apples-to-apples valid names only — skewed mega-caps excluded.)

## Capital allocation (stocks vs bonds)
- **Sizing (market hotness, PRE-moat):** 308/908 = **34%** undervalued → rule `stock = min(100%, undervalued% ÷ 50%)` → **68% stocks / 32% bonds.**
- **Holdings (POST-moat):** that 68% stock sleeve is spread across the **178** moat-quality names in `buy_list.csv` (the moat gate removed 130 undervalued-but-no/weak-moat names).
