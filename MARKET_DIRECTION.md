# Market Direction — Deploy Gauge

Brandon deploys aggressively only when the overall market is favorable (his bull-bear scale / economic scorecard). This is our computable version: where each index sits vs intrinsic value.

| Index | Median under/over | Cap-weighted under/over | Breadth (% undervalued) |
|-------|------------------:|------------------------:|------------------------:|
| SPY | -16% | +3% | 37% |
| QQQ | -23% | +3% | 29% |
| Global1000 | -8% | +17% | 45% |

**Read it as:** higher numbers = cheaper market = more bullish to deploy. The absolute level is model-tilted, so the real signal is the **trend across rebalances** — if breadth and medians fall month over month, the market is getting expensive (be selective); if they rise, deploy more.

## Deploy gate (golden line on the S&P — Brandon's >20% rule)
- Median golden-line read across 298 valid S&P names: **+0%** (breadth 51% undervalued).
- **OK to deploy (market roughly fair).** (Gate trips when the market is >20% overvalued, i.e. price ran >20% ahead of earnings. Uses apples-to-apples valid names only — skewed mega-caps excluded.)

## Capital allocation (stocks vs bonds)
- Genuinely undervalued: **328/910 = 36%** of the valued tradable universe.
- Rule `stock = min(100%, undervalued% ÷ 50%)` -> **72% stocks (the 328 buy-list names) / 28% bonds-short-term.**
