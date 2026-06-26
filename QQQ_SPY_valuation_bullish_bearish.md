# QQQ, SPY & Russell 1000 — Brandon Valuation Screen (Bullish vs Bearish)

**Generated:** 2026-06-07 · **Method:** Brandon's valuation rules (see `wiki/strategy/valuation-method.md`).
Data: yfinance (price, trailing-12-month EPS, forward EPS). This is an **estimate/guess**, exactly as
Brandon frames his own calculator — the growth input is a best-guess and drives everything.

## How each stock was scored
`intrinsic = TTM_EPS × (1+g)^5 × 20 ÷ (1+0.10)^5`, where conservative growth
`g = median(analyst current-year est, next-year est, TTM YoY earnings growth)`, floored at 0 and
capped at 30% (Brandon's conservatism). Using a multi-year growth signal — not just
next-year's analyst bump — is what keeps fast compounders (e.g. GOOGL) from being mislabeled.
A stock is **undervalued (bullish)** when price is below intrinsic, **overvalued (bearish)** when above.
Stocks are ranked by under/over %, then split into equal halves (the 20× multiple and
10% discount are identical for every stock, so they don't affect which half a stock
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
## QQQ (Nasdaq-100)
Valued 101 holdings · **50 most undervalued (BULLISH)** vs **50 most overvalued (BEARISH)** · 1 near-median (neutral, excluded).

### 🟢 BULLISH — 50 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | CHTR | Charter Communications, In | $129.65 | 36.96 | 10% | $727.51 | +461% |  |
| 2 | CMCSA | Comcast Corporation | $22.69 | 5.1 | 0% | $63.33 | +179% |  |
| 3 | GILD | Gilead Sciences, Inc. | $123.84 | 7.36 | 30% | $339.36 | +174% |  |
| 4 | CTSH | Cognizant Technology Solut | $39.15 | 4.61 | 8% | $83.03 | +112% |  |
| 5 | ADBE | Adobe Inc. | $193.41 | 17.48 | 13% | $395.36 | +104% |  |
| 6 | NFLX | Netflix, Inc. | $70.9 | 3.1 | 30% | $142.94 | +102% |  |
| 7 | GOOG | Alphabet Inc. | $342.19 | 13.11 | 30% | $604.49 | +77% |  |
| 8 | GOOGL | Alphabet Inc. | $343.71 | 13.1 | 30% | $604.02 | +76% |  |
| 9 | BKR | Baker Hughes Company | $56.94 | 3.13 | 21% | $99.66 | +75% |  |
| 10 | MSFT | Microsoft Corporation | $352.83 | 16.79 | 23% | $594.44 | +68% |  |
| 11 | MU | Micron Technology, Inc. | $1213.56 | 44.29 | 30% | $2042.16 | +68% |  |
| 12 | PDD | PDD Holdings Inc. | $73.3 | 9.5 | 0% | $117.98 | +61% |  |
| 13 | INTU | Intuit Inc. | $255.07 | 16.4 | 15% | $403.44 | +58% |  |
| 14 | CEG | Constellation Energy Corpo | $268.69 | 11.5 | 24% | $424.1 | +58% |  |
| 15 | PYPL | PayPal Holdings, Inc. | $42.38 | 5.33 | 0% | $66.19 | +56% |  |
| 16 | NVDA | NVIDIA Corporation | $195.74 | 6.54 | 30% | $301.55 | +54% |  |
| 17 | NXPI | NXP Semiconductors N.V. | $298.64 | 10.45 | 25% | $401.61 | +34% |  |
| 18 | DXCM | DexCom, Inc. | $68.65 | 2.33 | 24% | $85.0 | +24% |  |
| 19 | BKNG | Booking Holdings Inc. Comm | $177.05 | 7.58 | 18% | $212.54 | +20% |  |
| 20 | APP | Applovin Corporation | $445.93 | 11.5 | 30% | $530.25 | +19% |  |
| 21 | PCAR | PACCAR Inc. | $121.68 | 4.7 | 19% | $141.4 | +16% |  |
| 22 | ADSK | Autodesk, Inc. | $189.73 | 6.85 | 21% | $220.18 | +16% |  |
| 23 | META | Meta Platforms, Inc. | $542.87 | 27.52 | 13% | $619.7 | +14% |  |
| 24 | WDC | Western Digital Corporatio | $675.39 | 16.68 | 30% | $769.09 | +14% |  |
| 25 | GEHC | GE HealthCare Technologies | $64.94 | 4.17 | 6% | $69.99 | +8% |  |
| 26 | AMZN | Amazon.com, Inc. | $227.01 | 7.17 | 21% | $233.15 | +3% |  |
| 27 | CSX | CSX Corporation | $47.44 | 1.63 | 19% | $48.35 | +2% |  |
| 28 | ADP | Automatic Data Processing, | $216.31 | 10.73 | 10% | $219.52 | +2% |  |
| 29 | REGN | Regeneron Pharmaceuticals, | $620.14 | 40.93 | 4% | $629.49 | +2% |  |
| 30 | CCEP | Coca-Cola Europacific Part | $99.6 | 4.85 | 10% | $94.95 | -5% |  |
| 31 | ROP | Roper Technologies, Inc. | $332.42 | 16.02 | 10% | $316.05 | -5% |  |
| 32 | ROST | Ross Stores, Inc. | $215.13 | 7.16 | 18% | $200.42 | -7% |  |
| 33 | PAYX | Paychex, Inc. | $96.72 | 4.89 | 8% | $90.01 | -7% |  |
| 34 | TRI | Thomson Reuters Corp | $81.01 | 3.48 | 11% | $73.25 | -10% |  |
| 35 | ABNB | Airbnb, Inc. | $141.88 | 4.04 | 20% | $125.94 | -11% |  |
| 36 | TXN | Texas Instruments Incorpor | $311.81 | 5.86 | 30% | $270.2 | -13% |  |
| 37 | KDP | Keurig Dr Pepper Inc. | $32.52 | 1.35 | 10% | $27.53 | -15% |  |
| 38 | AEP | American Electric Power Co | $137.0 | 6.75 | 7% | $115.93 | -15% |  |
| 39 | EXC | Exelon Corporation | $46.75 | 2.73 | 3% | $39.47 | -16% |  |
| 40 | TMUS | T-Mobile US, Inc. | $181.57 | 9.41 | 6% | $152.58 | -16% |  |
| 41 | AAPL | Apple Inc. | $275.15 | 8.25 | 17% | $228.0 | -17% |  |
| 42 | WDAY | Workday, Inc. | $113.77 | 3.21 | 18% | $90.39 | -21% |  |
| 43 | XEL | Xcel Energy Inc. | $81.75 | 3.47 | 8% | $63.93 | -22% |  |
| 44 | VRTX | Vertex Pharmaceuticals Inc | $480.18 | 16.85 | 12% | $371.25 | -23% |  |
| 45 | PEP | Pepsico, Inc. | $139.52 | 6.38 | 6% | $107.23 | -23% |  |
| 46 | CPRT | Copart, Inc. | $30.05 | 1.61 | 2% | $22.4 | -26% |  |
| 47 | ADI | Analog Devices, Inc. | $417.93 | 6.73 | 30% | $310.31 | -26% |  |
| 48 | ORLY | O'Reilly Automotive, Inc. | $86.9 | 3.07 | 11% | $64.47 | -26% |  |
| 49 | AMAT | Applied Materials, Inc. | $668.0 | 10.62 | 30% | $489.67 | -27% |  |
| 50 | AVGO | Broadcom Inc. | $378.91 | 6.02 | 30% | $277.57 | -27% |  |

### 🔴 BEARISH — 50 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | ASML | ASML Holding N.V. - New Yo | $1841.18 | 29.46 | 28% | $1256.55 | -32% |  |
| 2 | VRSK | Verisk Analytics, Inc. | $177.04 | 6.57 | 7% | $114.81 | -35% |  |
| 3 | ALNY | Alnylam Pharmaceuticals, I | $293.17 | 3.99 | 30% | $183.97 | -37% |  |
| 4 | AMGN | Amgen Inc. | $352.82 | 14.36 | 4% | $221.17 | -37% |  |
| 5 | QCOM | QUALCOMM Incorporated | $204.9 | 9.3 | 2% | $125.09 | -39% |  |
| 6 | LRCX | Lam Research Corporation | $401.82 | 5.3 | 30% | $244.38 | -39% |  |
| 7 | CTAS | Cintas Corporation | $169.09 | 4.73 | 11% | $98.71 | -42% |  |
| 8 | SNDK | Sandisk Corporation | $2335.0 | 29.19 | 30% | $1345.91 | -42% |  |
| 9 | LIN | Linde plc | $522.28 | 15.09 | 10% | $299.2 | -43% |  |
| 10 | MAR | Marriott International | $378.91 | 9.55 | 13% | $216.67 | -43% |  |
| 11 | FAST | Fastenal Company | $46.92 | 1.13 | 14% | $26.78 | -43% |  |
| 12 | WMT | Walmart Inc. | $115.78 | 2.84 | 13% | $65.12 | -44% |  |
| 13 | IDXX | IDEXX Laboratories, Inc. | $554.94 | 13.6 | 13% | $310.21 | -44% |  |
| 14 | CSCO | Cisco Systems, Inc. | $118.97 | 3.0 | 12% | $66.42 | -44% |  |
| 15 | ISRG | Intuitive Surgical, Inc. | $399.69 | 8.23 | 17% | $221.03 | -45% |  |
| 16 | MNST | Monster Beverage Corporati | $95.83 | 2.07 | 15% | $52.02 | -46% |  |
| 17 | SBUX | Starbucks Corporation | $103.16 | 1.31 | 26% | $52.55 | -49% |  |
| 18 | ODFL | Old Dominion Freight Line, | $220.12 | 4.8 | 13% | $109.0 | -50% |  |
| 19 | FER | Ferrovial N.V. | $70.2 | 1.42 | 14% | $34.15 | -51% |  |
| 20 | HON | Honeywell International In | $231.24 | 6.27 | 8% | $112.15 | -52% |  |
| 21 | COST | Costco Wholesale Corporati | $942.24 | 19.88 | 13% | $452.85 | -52% |  |
| 22 | MRVL | Marvell Technology, Inc. | $281.26 | 2.9 | 30% | $133.72 | -52% |  |
| 23 | STX | Seagate Technology Holding | $1025.36 | 10.56 | 30% | $486.91 | -52% |  |
| 24 | MPWR | Monolithic Power Systems,  | $1438.3 | 13.95 | 30% | $643.22 | -55% |  |
| 25 | FTNT | Fortinet, Inc. | $149.93 | 2.58 | 14% | $62.72 | -58% |  |
| 26 | SHOP | Shopify Inc. | $111.62 | 1.02 | 28% | $43.05 | -61% |  |
| 27 | EA | Electronic Arts Inc. | $204.73 | 3.5 | 13% | $78.85 | -62% |  |
| 28 | PLTR | Palantir Technologies Inc. | $107.27 | 0.89 | 30% | $41.04 | -62% |  |
| 29 | CDNS | Cadence Design Systems, In | $368.23 | 4.31 | 18% | $122.97 | -67% |  |
| 30 | MELI | MercadoLibre, Inc. | $1619.25 | 37.89 | 3% | $535.23 | -67% |  |
| 31 | LITE | Lumentum Holdings Inc. | $861.97 | 5.69 | 30% | $262.36 | -70% |  |
| 32 | KLAC | KLA Corporation | $258.8 | 3.52 | 12% | $76.35 | -70% |  |
| 33 | AMD | Advanced Micro Devices, In | $532.57 | 2.98 | 30% | $137.4 | -74% |  |
| 34 | AXON | Axon Enterprise, Inc. | $444.73 | 2.49 | 30% | $114.81 | -74% |  |
| 35 | DASH | DoorDash, Inc. | $176.91 | 2.11 | 10% | $42.62 | -76% |  |
| 36 | SNPS | Synopsys, Inc. | $455.02 | 4.37 | 15% | $107.08 | -76% |  |
| 37 | ARM | Arm Holdings plc | $347.71 | 0.83 | 30% | $38.27 | -89% |  |
| 38 | MCHP | Microchip Technology Incor | $94.12 | 0.22 | 30% | $10.14 | -89% |  |
| 39 | TSLA | Tesla, Inc. | $375.12 | 1.09 | 21% | $35.68 | -90% |  |
| 40 | PANW | Palo Alto Networks, Inc. | $293.09 | 1.14 | 11% | $23.89 | -92% |  |
| 41 | FANG | Diamondback Energy, Inc. | $182.55 | 0.99 | 0% | $12.29 | -93% |  |
| 42 | DDOG | Datadog, Inc. | $220.94 | 0.4 | 18% | $11.42 | -95% |  |
| 43 | CRWD | CrowdStrike Holdings, Inc. | $678.65 | -0.14 | — | — | no earnings | no_earnings |
| 44 | INSM | Insmed Incorporated | $104.47 | -5.76 | — | — | no earnings | no_earnings |
| 45 | INTC | Intel Corporation | $132.87 | -0.6 | — | — | no earnings | no_earnings |
| 46 | KHC | The Kraft Heinz Company | $23.47 | -4.86 | — | — | no earnings | no_earnings |
| 47 | MSTR | Strategy Inc | $85.33 | -36.99 | — | — | no earnings | no_earnings |
| 48 | TTWO | Take-Two Interactive Softw | $238.72 | -1.62 | — | — | no earnings | no_earnings |
| 49 | WBD | Warner Bros. Discovery, In | $26.98 | -0.7 | — | — | no earnings | no_earnings |
| 50 | ZS | Zscaler, Inc. | $123.8 | -0.48 | — | — | no earnings | no_earnings |

<details><summary>Neutral / near-median (1) — excluded from the split</summary>

| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | MDLZ | Mondelez International, In | $61.2 | 2.02 | 11% | $42.0 | -31% |  |

</details>

---
## SPY (S&P 500)
Valued 503 holdings · **250 most undervalued (BULLISH)** vs **250 most overvalued (BEARISH)** · 3 near-median (neutral, excluded).

### 🟢 BULLISH — 250 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | EXE | Expand Energy Corporation | $88.44 | 13.44 | 27% | $553.92 | +526% |  |
| 2 | APA | APA Corporation | $33.42 | 4.29 | 30% | $197.81 | +492% |  |
| 3 | CHTR | Charter Communications, In | $129.65 | 36.96 | 10% | $727.51 | +461% |  |
| 4 | CF | CF Industries Holdings, In | $105.49 | 11.1 | 30% | $511.81 | +385% |  |
| 5 | EQT | EQT Corporation | $51.65 | 5.27 | 30% | $242.99 | +370% |  |
| 6 | EG | Everest Group, Ltd. | $343.02 | 49.12 | 17% | $1337.95 | +290% |  |
| 7 | UAL | United Airlines Holdings,  | $134.6 | 11.19 | 30% | $515.96 | +283% |  |
| 8 | NEM | Newmont Corporation | $95.35 | 7.71 | 30% | $355.5 | +273% |  |
| 9 | AES | The AES Corporation | $14.66 | 1.92 | 18% | $54.09 | +269% |  |
| 10 | EOG | EOG Resources, Inc. | $133.59 | 10.17 | 30% | $468.93 | +251% |  |
| 11 | UHS | Universal Health Services, | $144.46 | 23.95 | 8% | $434.59 | +201% |  |
| 12 | SYF | Synchrony Financial | $78.52 | 9.66 | 14% | $227.35 | +190% |  |
| 13 | FSLR | First Solar, Inc. | $248.64 | 15.49 | 30% | $714.22 | +187% |  |
| 14 | CMCSA | Comcast Corporation | $22.69 | 5.1 | 0% | $63.33 | +179% |  |
| 15 | MPC | Marathon Petroleum Corpora | $253.56 | 15.19 | 30% | $700.39 | +176% |  |
| 16 | CFG | Citizens Financial Group,  | $70.66 | 4.22 | 30% | $194.58 | +175% |  |
| 17 | GILD | Gilead Sciences, Inc. | $123.84 | 7.36 | 30% | $339.36 | +174% |  |
| 18 | FIS | Fidelity National Informat | $37.86 | 5.16 | 9% | $99.27 | +162% |  |
| 19 | T | AT&T Inc. | $22.42 | 3.04 | 9% | $58.41 | +160% |  |
| 20 | C | Citigroup, Inc. | $144.98 | 8.09 | 30% | $373.02 | +157% |  |
| 21 | UBER | Uber Technologies, Inc. | $72.25 | 4.03 | 30% | $185.82 | +157% |  |
| 22 | VLO | Valero Energy Corporation | $255.06 | 13.7 | 30% | $631.69 | +148% |  |
| 23 | ALL | Allstate Corporation (The) | $231.6 | 45.21 | 0% | $561.44 | +142% |  |
| 24 | SMCI | Super Micro Computer, Inc. | $31.68 | 1.9 | 26% | $75.05 | +137% |  |
| 25 | ACGL | Arch Capital Group Ltd. | $94.33 | 13.0 | 7% | $221.71 | +135% |  |
| 26 | KEY | KeyCorp | $23.41 | 1.63 | 22% | $53.71 | +129% |  |
| 27 | DAL | Delta Air Lines, Inc. | $92.11 | 6.85 | 20% | $209.87 | +128% |  |
| 28 | SCHW | Charles Schwab Corporation | $89.44 | 5.03 | 26% | $202.1 | +126% |  |
| 29 | VICI | VICI Properties Inc. | $26.53 | 2.92 | 10% | $59.85 | +126% |  |
| 30 | DVA | DaVita Inc. | $213.36 | 10.39 | 30% | $479.07 | +124% |  |
| 31 | HIG | The Hartford Insurance Gro | $130.37 | 14.21 | 10% | $287.44 | +120% |  |
| 32 | CTSH | Cognizant Technology Solut | $39.15 | 4.61 | 8% | $83.03 | +112% |  |
| 33 | TEL | TE Connectivity plc | $200.07 | 9.78 | 28% | $422.55 | +111% |  |
| 34 | CBOE | Cboe Global Markets, Inc. | $244.98 | 11.71 | 29% | $516.47 | +111% |  |
| 35 | ADBE | Adobe Inc. | $193.41 | 17.48 | 13% | $395.36 | +104% |  |
| 36 | NFLX | Netflix, Inc. | $70.9 | 3.1 | 30% | $142.94 | +102% |  |
| 37 | INCY | Incyte Corporation | $107.53 | 7.08 | 20% | $216.6 | +101% |  |
| 38 | AMP | Ameriprise Financial, Inc. | $453.29 | 40.12 | 12% | $897.82 | +98% |  |
| 39 | NTRS | Northern Trust Corporation | $175.97 | 9.56 | 24% | $348.18 | +98% |  |
| 40 | GDDY | GoDaddy Inc. | $79.35 | 6.31 | 15% | $156.04 | +97% |  |
| 41 | CPAY | Corpay, Inc. | $325.81 | 16.71 | 25% | $638.87 | +96% |  |
| 42 | BAC | Bank of America Corporatio | $58.19 | 4.03 | 18% | $112.37 | +93% |  |
| 43 | NUE | Nucor Corporation | $248.89 | 10.08 | 30% | $464.78 | +87% |  |
| 44 | SOLV | Solventum Corporation | $77.92 | 8.17 | 7% | $143.97 | +85% |  |
| 45 | HAL | Halliburton Company | $34.67 | 1.81 | 23% | $63.95 | +84% |  |
| 46 | TFC | Truist Financial Corporati | $50.67 | 4.04 | 13% | $93.34 | +84% |  |
| 47 | MKC | McCormick & Company, Incor | $48.35 | 6.1 | 3% | $88.33 | +83% |  |
| 48 | RF | Regions Financial Corporat | $29.98 | 2.41 | 12% | $53.07 | +77% |  |
| 49 | GOOG | Alphabet Inc. | $342.19 | 13.11 | 30% | $604.49 | +77% |  |
| 50 | GOOGL | Alphabet Inc. | $343.71 | 13.1 | 30% | $604.02 | +76% |  |
| 51 | CINF | Cincinnati Financial Corpo | $177.73 | 17.5 | 8% | $312.14 | +76% |  |
| 52 | AIG | American International Gro | $74.85 | 5.68 | 13% | $131.23 | +75% |  |
| 53 | BKR | Baker Hughes Company | $56.94 | 3.13 | 21% | $99.66 | +75% |  |
| 54 | ACN | Accenture plc | $125.82 | 12.52 | 7% | $219.7 | +75% |  |
| 55 | WFC | Wells Fargo & Company | $84.74 | 6.47 | 13% | $147.64 | +74% |  |
| 56 | UDR | UDR, Inc. | $39.1 | 1.47 | 30% | $67.78 | +73% |  |
| 57 | IT | Gartner, Inc. | $126.63 | 10.12 | 12% | $219.02 | +73% |  |
| 58 | BIIB | Biogen Inc. | $201.96 | 9.29 | 25% | $348.85 | +73% |  |
| 59 | STLD | Steel Dynamics, Inc. | $251.0 | 9.34 | 30% | $430.66 | +72% |  |
| 60 | PNC | PNC Financial Services Gro | $245.28 | 17.22 | 14% | $413.91 | +69% |  |
| 61 | MSFT | Microsoft Corporation | $352.83 | 16.79 | 23% | $594.44 | +68% |  |
| 62 | MU | Micron Technology, Inc. | $1213.56 | 44.29 | 30% | $2042.16 | +68% |  |
| 63 | CI | The Cigna Group | $281.87 | 23.59 | 10% | $472.66 | +68% |  |
| 64 | CB | Chubb Limited | $330.82 | 28.29 | 9% | $548.02 | +66% |  |
| 65 | VST | Vistra Corp. | $167.77 | 5.97 | 30% | $275.27 | +64% |  |
| 66 | PTC | PTC Inc. | $112.55 | 10.41 | 7% | $184.47 | +64% |  |
| 67 | USB | U.S. Bancorp | $61.21 | 4.77 | 11% | $99.14 | +62% |  |
| 68 | MTB | M&T Bank Corporation | $236.77 | 17.81 | 12% | $382.7 | +62% |  |
| 69 | WTW | Willis Towers Watson Publi | $257.69 | 17.03 | 14% | $410.42 | +59% |  |
| 70 | RJF | Raymond James Financial, I | $150.52 | 10.6 | 13% | $239.65 | +59% |  |
| 71 | INTU | Intuit Inc. | $255.07 | 16.4 | 15% | $403.44 | +58% |  |
| 72 | CEG | Constellation Energy Corpo | $268.69 | 11.5 | 24% | $424.1 | +58% |  |
| 73 | GEN | Gen Digital Inc. | $23.31 | 1.57 | 14% | $36.74 | +58% |  |
| 74 | LDOS | Leidos Holdings, Inc. | $100.0 | 10.93 | 3% | $156.21 | +56% |  |
| 75 | PYPL | PayPal Holdings, Inc. | $42.38 | 5.33 | 0% | $66.19 | +56% |  |
| 76 | HST | Host Hotels & Resorts, Inc | $24.98 | 1.47 | 16% | $38.64 | +55% |  |
| 77 | NVDA | NVIDIA Corporation | $195.74 | 6.54 | 30% | $301.55 | +54% |  |
| 78 | EIX | Edison International | $74.75 | 9.2 | 0% | $114.25 | +53% |  |
| 79 | BNY | The Bank of New York Mello | $145.43 | 8.06 | 17% | $221.42 | +52% |  |
| 80 | ICE | Intercontinental Exchange  | $124.49 | 6.87 | 17% | $188.01 | +51% |  |
| 81 | BEN | Franklin Resources, Inc. | $32.65 | 1.31 | 25% | $48.92 | +50% |  |
| 82 | PCG | Pacific Gas & Electric Co. | $17.08 | 1.29 | 10% | $25.55 | +50% |  |
| 83 | PFG | Principal Financial Group  | $105.44 | 6.97 | 13% | $157.3 | +49% |  |
| 84 | HBAN | Huntington Bancshares Inco | $17.9 | 1.3 | 11% | $26.66 | +49% |  |
| 85 | GL | Globe Life Inc. | $176.4 | 14.45 | 8% | $260.75 | +48% |  |
| 86 | BR | Broadridge Financial Solut | $136.26 | 9.35 | 12% | $200.91 | +47% |  |
| 87 | HCA | HCA Healthcare, Inc. | $386.94 | 29.02 | 10% | $570.18 | +47% |  |
| 88 | HPQ | HP Inc. | $22.92 | 2.7 | 0% | $33.53 | +46% |  |
| 89 | GEV | GE Vernova Inc. | $1085.47 | 34.19 | 30% | $1576.46 | +45% |  |
| 90 | TRV | The Travelers Companies, I | $318.29 | 33.52 | 2% | $460.49 | +45% |  |
| 91 | EXPE | Expedia Group, Inc. | $250.95 | 11.32 | 21% | $360.72 | +44% |  |
| 92 | JPM | JP Morgan Chase & Co. | $335.12 | 20.88 | 13% | $481.13 | +44% |  |
| 93 | GIS | General Mills, Inc. | $35.4 | 4.09 | 0% | $50.79 | +44% |  |
| 94 | VZ | Verizon Communications Inc | $46.07 | 4.1 | 5% | $65.67 | +42% |  |
| 95 | TRGP | Targa Resources, Inc. | $273.45 | 9.79 | 26% | $388.1 | +42% |  |
| 96 | DELL | Dell Technologies Inc. | $409.45 | 12.57 | 30% | $579.59 | +42% |  |
| 97 | ZTS | Zoetis Inc. | $77.82 | 6.1 | 8% | $109.16 | +40% |  |
| 98 | HSY | The Hershey Company | $176.68 | 5.37 | 30% | $247.6 | +40% |  |
| 99 | BXP | BXP, Inc. | $65.67 | 1.99 | 30% | $91.76 | +40% |  |
| 100 | FCX | Freeport-McMoRan, Inc. | $62.8 | 1.89 | 30% | $87.15 | +39% |  |
| 101 | LULU | lululemon athletica inc. | $112.06 | 12.35 | 0% | $153.37 | +37% |  |
| 102 | MET | MetLife, Inc. | $84.63 | 5.17 | 12% | $114.26 | +35% |  |
| 103 | NXPI | NXP Semiconductors N.V. | $298.64 | 10.45 | 25% | $401.61 | +34% |  |
| 104 | GS | Goldman Sachs Group, Inc.  | $1065.09 | 54.75 | 16% | $1426.2 | +34% |  |
| 105 | AFL | AFLAC Incorporated | $118.23 | 8.75 | 8% | $158.19 | +34% |  |
| 106 | MS | Morgan Stanley | $221.04 | 11.03 | 17% | $295.85 | +34% |  |
| 107 | LUV | Southwest Airlines Company | $52.09 | 1.5 | 30% | $69.16 | +33% |  |
| 108 | CRM | Salesforce, Inc. | $150.19 | 8.64 | 13% | $196.38 | +31% |  |
| 109 | PLD | Prologis, Inc. | $140.53 | 3.98 | 30% | $183.51 | +31% |  |
| 110 | MRK | Merck & Company, Inc. | $125.45 | 3.55 | 30% | $163.69 | +30% |  |
| 111 | RCL | Royal Caribbean Cruises Lt | $322.65 | 16.39 | 16% | $418.37 | +30% |  |
| 112 | AIZ | Assurant, Inc. | $260.77 | 19.51 | 7% | $336.18 | +29% |  |
| 113 | PODD | Insulet Corporation | $153.82 | 4.28 | 30% | $197.35 | +28% |  |
| 114 | BALL | Ball Corporation | $61.37 | 3.43 | 13% | $78.65 | +28% |  |
| 115 | BBY | Best Buy Co., Inc. | $76.89 | 5.4 | 8% | $98.4 | +28% |  |
| 116 | ORCL | Oracle Corporation | $152.46 | 5.82 | 22% | $194.54 | +28% |  |
| 117 | FICO | Fair Isaac Corporation | $1143.48 | 31.56 | 30% | $1455.19 | +27% |  |
| 118 | LVS | Las Vegas Sands Corp. | $46.28 | 2.71 | 12% | $58.55 | +26% |  |
| 119 | AON | Aon plc | $315.95 | 18.23 | 12% | $398.97 | +26% |  |
| 120 | DIS | Walt Disney Company (The) | $98.05 | 6.25 | 10% | $123.81 | +26% |  |
| 121 | HII | Huntington Ingalls Industr | $279.09 | 15.38 | 13% | $352.36 | +26% |  |
| 122 | WRB | W.R. Berkley Corporation | $69.29 | 4.72 | 8% | $85.85 | +24% |  |
| 123 | AMT | American Tower Corporation | $168.72 | 6.19 | 22% | $208.87 | +24% |  |
| 124 | DXCM | DexCom, Inc. | $68.65 | 2.33 | 24% | $85.0 | +24% |  |
| 125 | SPG | Simon Property Group, Inc. | $225.49 | 14.39 | 9% | $274.83 | +22% |  |
| 126 | FITB | Fifth Third Bancorp | $56.41 | 2.97 | 13% | $68.41 | +21% |  |
| 127 | ULTA | Ulta Beauty, Inc. | $485.52 | 26.7 | 12% | $589.05 | +21% |  |
| 128 | TXT | Textron Inc. | $89.06 | 5.24 | 11% | $107.69 | +21% |  |
| 129 | STT | State Street Corporation | $169.51 | 9.85 | 11% | $204.82 | +21% |  |
| 130 | BKNG | Booking Holdings Inc. Comm | $177.05 | 7.58 | 18% | $212.54 | +20% |  |
| 131 | FOXA | Fox Corporation | $48.86 | 3.8 | 4% | $58.64 | +20% |  |
| 132 | APP | Applovin Corporation | $445.93 | 11.5 | 30% | $530.25 | +19% |  |
| 133 | MCK | McKesson Corporation | $763.81 | 38.34 | 14% | $905.93 | +19% |  |
| 134 | DPZ | Domino's Pizza Inc | $285.44 | 17.38 | 9% | $332.85 | +17% |  |
| 135 | DECK | Deckers Outdoor Corporatio | $102.59 | 7.02 | 6% | $119.5 | +16% |  |
| 136 | AXP | American Express Company | $342.46 | 16.03 | 15% | $397.79 | +16% |  |
| 137 | PCAR | PACCAR Inc. | $121.68 | 4.7 | 19% | $141.4 | +16% |  |
| 138 | ADSK | Autodesk, Inc. | $189.73 | 6.85 | 21% | $220.18 | +16% |  |
| 139 | NOC | Northrop Grumman Corporati | $499.33 | 31.91 | 8% | $578.49 | +16% |  |
| 140 | CDW | CDW Corporation | $128.02 | 8.21 | 8% | $147.74 | +15% |  |
| 141 | LLY | Eli Lilly and Company | $1127.69 | 28.19 | 30% | $1299.81 | +15% |  |
| 142 | TROW | T. Rowe Price Group, Inc. | $106.34 | 9.32 | 1% | $122.25 | +15% |  |
| 143 | META | Meta Platforms, Inc. | $542.87 | 27.52 | 13% | $619.7 | +14% |  |
| 144 | FDS | FactSet Research Systems I | $208.84 | 15.54 | 4% | $238.08 | +14% |  |
| 145 | WDC | Western Digital Corporatio | $675.39 | 16.68 | 30% | $769.09 | +14% |  |
| 146 | OKE | ONEOK, Inc. | $89.52 | 5.61 | 8% | $101.75 | +14% |  |
| 147 | OTIS | Otis Worldwide Corporation | $73.63 | 3.76 | 12% | $83.66 | +14% |  |
| 148 | DG | Dollar General Corporation | $117.56 | 7.07 | 9% | $133.49 | +14% |  |
| 149 | PGR | Progressive Corporation (T | $215.54 | 19.66 | 0% | $244.15 | +13% |  |
| 150 | JKHY | Jack Henry & Associates, I | $128.71 | 7.16 | 10% | $145.3 | +13% |  |
| 151 | PRU | Prudential Financial, Inc. | $107.03 | 9.71 | 0% | $120.58 | +13% |  |
| 152 | EFX | Equifax, Inc. | $151.93 | 5.68 | 19% | $170.89 | +12% |  |
| 153 | KKR | KKR & Co. Inc. | $92.65 | 2.94 | 23% | $103.77 | +12% |  |
| 154 | BSX | Boston Scientific Corporat | $44.2 | 2.39 | 11% | $49.16 | +11% |  |
| 155 | KMI | Kinder Morgan, Inc. | $33.01 | 1.49 | 14% | $36.27 | +10% |  |
| 156 | ES | Eversource Energy (D/B/A) | $72.08 | 4.67 | 6% | $78.09 | +8% |  |
| 157 | GEHC | GE HealthCare Technologies | $64.94 | 4.17 | 6% | $69.99 | +8% |  |
| 158 | ATO | Atmos Energy Corporation | $173.67 | 8.13 | 13% | $186.02 | +7% |  |
| 159 | RMD | ResMed Inc. | $198.6 | 10.37 | 10% | $212.16 | +7% |  |
| 160 | FOX | Fox Corporation | $44.39 | 3.8 | 0% | $47.19 | +6% |  |
| 161 | DLTR | Dollar Tree, Inc. | $118.21 | 6.23 | 10% | $125.39 | +6% |  |
| 162 | HPE | Hewlett Packard Enterprise | $46.72 | 1.07 | 30% | $49.34 | +6% |  |
| 163 | DVN | Devon Energy Corporation | $42.6 | 3.59 | 0% | $44.58 | +5% |  |
| 164 | TPR | Tapestry, Inc. | $146.0 | 3.28 | 30% | $151.24 | +4% |  |
| 165 | JCI | Johnson Controls Internati | $145.49 | 3.27 | 30% | $150.6 | +4% |  |
| 166 | MO | Altria Group, Inc. | $73.21 | 4.79 | 5% | $75.27 | +3% |  |
| 167 | AMZN | Amazon.com, Inc. | $227.01 | 7.17 | 21% | $233.15 | +3% |  |
| 168 | CME | CME Group Inc. | $225.0 | 11.72 | 10% | $230.17 | +2% |  |
| 169 | MAS | Masco Corporation | $79.72 | 4.04 | 10% | $81.35 | +2% |  |
| 170 | CSX | CSX Corporation | $47.44 | 1.63 | 19% | $48.35 | +2% |  |
| 171 | BRK-B | Berkshire Hathaway Inc. Ne | $487.81 | 33.61 | 4% | $495.48 | +2% |  |
| 172 | ADP | Automatic Data Processing, | $216.31 | 10.73 | 10% | $219.52 | +2% |  |
| 173 | REGN | Regeneron Pharmaceuticals, | $620.14 | 40.93 | 4% | $629.49 | +2% |  |
| 174 | CBRE | CBRE Group Inc | $134.58 | 4.37 | 20% | $136.39 | +1% |  |
| 175 | PEG | Public Service Enterprise  | $82.63 | 4.52 | 8% | $82.78 | +0% |  |
| 176 | WY | Weyerhaeuser Company | $25.76 | 0.56 | 30% | $25.82 | +0% |  |
| 177 | GPN | Global Payments Inc. | $68.16 | 2.72 | 15% | $68.06 | -0% |  |
| 178 | BLK | BlackRock, Inc. | $971.92 | 39.75 | 14% | $963.44 | -1% |  |
| 179 | NDAQ | Nasdaq, Inc. | $77.65 | 3.32 | 13% | $76.91 | -1% |  |
| 180 | PNR | Pentair plc. | $76.0 | 3.98 | 9% | $75.04 | -1% |  |
| 181 | ALLE | Allegion plc | $137.0 | 7.32 | 8% | $132.83 | -3% |  |
| 182 | CCL | Carnival Corporation Ltd. | $28.46 | 2.22 | 0% | $27.57 | -3% |  |
| 183 | COR | Cencora, Inc. | $286.95 | 13.06 | 11% | $277.88 | -3% |  |
| 184 | ROP | Roper Technologies, Inc. | $332.42 | 16.02 | 10% | $316.05 | -5% |  |
| 185 | NWSA | News Corporation | $25.03 | 0.79 | 19% | $23.78 | -5% |  |
| 186 | PHM | PulteGroup, Inc. | $135.81 | 10.34 | 0% | $128.41 | -6% |  |
| 187 | ED | Consolidated Edison, Inc. | $110.76 | 5.93 | 7% | $104.5 | -6% |  |
| 188 | TGT | Target Corporation | $139.57 | 7.56 | 7% | $130.57 | -6% |  |
| 189 | TRMB | Trimble Inc. | $50.24 | 1.91 | 15% | $46.92 | -7% |  |
| 190 | ROST | Ross Stores, Inc. | $215.13 | 7.16 | 18% | $200.42 | -7% |  |
| 191 | DRI | Darden Restaurants, Inc. | $212.76 | 10.45 | 9% | $198.12 | -7% |  |
| 192 | PAYX | Paychex, Inc. | $96.72 | 4.89 | 8% | $90.01 | -7% |  |
| 193 | STZ | Constellation Brands, Inc. | $144.45 | 9.61 | 2% | $134.5 | -7% |  |
| 194 | TSCO | Tractor Supply Company | $30.75 | 2.03 | 2% | $28.56 | -7% |  |
| 195 | SPGI | S&P Global Inc. | $395.14 | 15.81 | 13% | $366.72 | -7% |  |
| 196 | CRH | CRH PLC | $113.05 | 5.39 | 9% | $103.84 | -8% |  |
| 197 | CLX | Clorox Company (The) | $95.27 | 6.15 | 3% | $87.26 | -8% |  |
| 198 | MA | Mastercard Incorporated | $488.92 | 17.26 | 16% | $447.67 | -8% |  |
| 199 | JBL | Jabil Inc. | $374.64 | 7.42 | 30% | $342.13 | -9% |  |
| 200 | BMY | Bristol-Myers Squibb Compa | $55.39 | 3.57 | 3% | $50.43 | -9% |  |
| 201 | EVRG | Evergy, Inc. | $86.66 | 3.76 | 11% | $78.79 | -9% |  |
| 202 | DLR | Digital Realty Trust, Inc. | $192.44 | 3.77 | 30% | $173.83 | -10% |  |
| 203 | EXPD | Expeditors International o | $161.67 | 6.19 | 14% | $145.94 | -10% |  |
| 204 | IQV | IQVIA Holdings, Inc. | $186.43 | 8.05 | 11% | $166.94 | -10% |  |
| 205 | ABNB | Airbnb, Inc. | $141.88 | 4.04 | 20% | $125.94 | -11% |  |
| 206 | DUK | Duke Energy Corporation (H | $127.11 | 6.5 | 7% | $112.84 | -11% |  |
| 207 | KVUE | Kenvue Inc. | $18.96 | 0.84 | 10% | $16.84 | -11% |  |
| 208 | AEE | Ameren Corporation | $114.53 | 5.55 | 8% | $101.08 | -12% |  |
| 209 | GD | General Dynamics Corporati | $344.7 | 15.89 | 9% | $304.03 | -12% |  |
| 210 | COIN | Coinbase Global, Inc. | $142.52 | 2.72 | 30% | $125.42 | -12% |  |
| 211 | L | Loews Corporation | $110.9 | 7.86 | 0% | $97.61 | -12% |  |
| 212 | JBHT | J.B. Hunt Transport Servic | $274.68 | 6.43 | 25% | $240.58 | -12% |  |
| 213 | PPG | PPG Industries, Inc. | $122.4 | 6.98 | 4% | $106.48 | -13% |  |
| 214 | BG | Bunge Limited | $111.55 | 3.8 | 15% | $96.7 | -13% |  |
| 215 | TXN | Texas Instruments Incorpor | $311.81 | 5.86 | 30% | $270.2 | -13% |  |
| 216 | YUM | Yum! Brands, Inc. | $151.14 | 6.2 | 11% | $130.74 | -14% |  |
| 217 | AVY | Avery Dennison Corporation | $164.61 | 8.87 | 5% | $142.0 | -14% |  |
| 218 | VLTO | Veralto Corp | $87.99 | 3.88 | 10% | $75.68 | -14% |  |
| 219 | NEE | NextEra Energy, Inc. | $87.7 | 3.94 | 9% | $75.35 | -14% |  |
| 220 | WYNN | Wynn Resorts, Limited | $99.38 | 3.49 | 14% | $85.18 | -14% |  |
| 221 | AZO | AutoZone, Inc. | $3059.04 | 145.3 | 8% | $2614.63 | -14% |  |
| 222 | DGX | Quest Diagnostics Incorpor | $206.24 | 9.05 | 9% | $175.55 | -15% |  |
| 223 | NTAP | NetApp, Inc. | $154.59 | 6.35 | 11% | $131.63 | -15% |  |
| 224 | V | Visa Inc. | $330.52 | 11.47 | 15% | $281.43 | -15% |  |
| 225 | KDP | Keurig Dr Pepper Inc. | $32.52 | 1.35 | 10% | $27.53 | -15% |  |
| 226 | AEP | American Electric Power Co | $137.0 | 6.75 | 7% | $115.93 | -15% |  |
| 227 | CAT | Caterpillar, Inc. | $1057.01 | 20.08 | 29% | $893.56 | -16% |  |
| 228 | MRSH | Marsh | $162.23 | 8.0 | 7% | $137.08 | -16% |  |
| 229 | EXC | Exelon Corporation | $46.75 | 2.73 | 3% | $39.47 | -16% |  |
| 230 | LEN | Lennar Corporation | $93.86 | 6.38 | 0% | $79.23 | -16% |  |
| 231 | CMS | CMS Energy Corporation | $77.1 | 3.62 | 8% | $64.78 | -16% |  |
| 232 | TMUS | T-Mobile US, Inc. | $181.57 | 9.41 | 6% | $152.58 | -16% |  |
| 233 | NWS | News Corporation | $28.34 | 0.79 | 19% | $23.78 | -16% |  |
| 234 | UNP | Union Pacific Corporation | $267.73 | 12.15 | 8% | $223.76 | -16% |  |
| 235 | MDT | Medtronic plc. | $80.52 | 3.73 | 8% | $67.25 | -16% |  |
| 236 | GRMN | Garmin Ltd. | $235.41 | 8.97 | 12% | $195.61 | -17% |  |
| 237 | AAPL | Apple Inc. | $275.15 | 8.25 | 17% | $228.0 | -17% |  |
| 238 | LH | Labcorp Holdings Inc. | $266.34 | 11.29 | 10% | $220.31 | -17% |  |
| 239 | CHRW | C.H. Robinson Worldwide, I | $180.34 | 4.94 | 19% | $149.0 | -17% |  |
| 240 | BRO | Brown & Brown, Inc. | $60.83 | 3.07 | 6% | $49.99 | -18% |  |
| 241 | PNW | Pinnacle West Capital Corp | $107.28 | 5.36 | 6% | $87.95 | -18% |  |
| 242 | EBAY | eBay Inc. | $108.0 | 4.33 | 10% | $87.87 | -19% |  |
| 243 | IBM | International Business Mac | $258.27 | 11.31 | 8% | $206.75 | -20% |  |
| 244 | EME | EMCOR Group, Inc. | $862.66 | 29.76 | 13% | $688.48 | -20% |  |
| 245 | XYZ | Block, Inc. | $74.08 | 1.28 | 30% | $59.02 | -20% |  |
| 246 | MCD | McDonald's Corporation | $264.54 | 12.14 | 7% | $210.46 | -20% |  |
| 247 | PPL | PPL Corporation | $37.0 | 1.63 | 8% | $29.43 | -20% |  |
| 248 | WDAY | Workday, Inc. | $113.77 | 3.21 | 18% | $90.39 | -21% |  |
| 249 | FIX | Comfort Systems USA, Inc. | $2017.57 | 34.7 | 30% | $1599.97 | -21% |  |
| 250 | KEYS | Keysight Technologies Inc. | $360.06 | 6.19 | 30% | $285.41 | -21% |  |

### 🔴 BEARISH — 250 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | TTD | The Trade Desk, Inc. | $17.33 | 0.88 | 4% | $13.63 | -21% |  |
| 2 | AWK | American Water Works Compa | $130.0 | 5.64 | 8% | $102.1 | -22% |  |
| 3 | AVB | AvalonBay Communities, Inc | $186.13 | 8.08 | 8% | $145.53 | -22% |  |
| 4 | XEL | Xcel Energy Inc. | $81.75 | 3.47 | 8% | $63.93 | -22% |  |
| 5 | VEEV | Veeva Systems Inc. | $158.08 | 5.64 | 12% | $122.77 | -22% |  |
| 6 | NI | NiSource Inc | $47.81 | 2.01 | 8% | $37.03 | -22% |  |
| 7 | VRTX | Vertex Pharmaceuticals Inc | $480.18 | 16.85 | 12% | $371.25 | -23% |  |
| 8 | D | Dominion Energy, Inc. | $69.51 | 3.39 | 5% | $53.58 | -23% |  |
| 9 | APH | Amphenol Corporation | $165.15 | 3.48 | 24% | $127.21 | -23% |  |
| 10 | RL | Ralph Lauren Corporation | $410.11 | 15.09 | 11% | $315.77 | -23% |  |
| 11 | PEP | Pepsico, Inc. | $139.52 | 6.38 | 6% | $107.23 | -23% |  |
| 12 | SNA | Snap-On Incorporated | $400.95 | 19.37 | 5% | $306.56 | -24% |  |
| 13 | AOS | A.O. Smith Corporation | $61.13 | 3.75 | 0% | $46.57 | -24% |  |
| 14 | ETR | Entergy Corporation | $115.38 | 3.92 | 12% | $87.88 | -24% |  |
| 15 | ELV | Elevance Health, Inc. | $387.32 | 23.59 | 0% | $292.95 | -24% |  |
| 16 | KO | Coca-Cola Company (The) | $80.42 | 3.18 | 9% | $60.51 | -25% |  |
| 17 | URI | United Rentals, Inc. | $1139.51 | 39.09 | 12% | $857.42 | -25% |  |
| 18 | IFF | International Flavors & Fr | $75.08 | 3.23 | 7% | $56.42 | -25% |  |
| 19 | WEC | WEC Energy Group, Inc. | $117.07 | 4.99 | 7% | $87.97 | -25% |  |
| 20 | AJG | Arthur J. Gallagher & Co. | $217.86 | 6.19 | 16% | $162.85 | -25% |  |
| 21 | NCLH | Norwegian Cruise Line Hold | $20.98 | 1.24 | 0% | $15.65 | -25% |  |
| 22 | NVR | NVR, Inc. | $6814.44 | 409.55 | 0% | $5085.97 | -25% |  |
| 23 | CPRT | Copart, Inc. | $30.05 | 1.61 | 2% | $22.4 | -26% |  |
| 24 | STE | STERIS plc (Ireland) | $210.6 | 7.94 | 10% | $156.72 | -26% |  |
| 25 | VMC | Vulcan Materials Company ( | $312.97 | 8.45 | 17% | $232.73 | -26% |  |
| 26 | ADI | Analog Devices, Inc. | $417.93 | 6.73 | 30% | $310.31 | -26% |  |
| 27 | ORLY | O'Reilly Automotive, Inc. | $86.9 | 3.07 | 11% | $64.47 | -26% |  |
| 28 | PM | Philip Morris Internationa | $178.93 | 7.1 | 8% | $132.15 | -26% |  |
| 29 | AMAT | Applied Materials, Inc. | $668.0 | 10.62 | 30% | $489.67 | -27% |  |
| 30 | AVGO | Broadcom Inc. | $378.91 | 6.02 | 30% | $277.57 | -27% |  |
| 31 | LMT | Lockheed Martin Corporatio | $505.02 | 20.66 | 8% | $370.05 | -27% |  |
| 32 | ZBRA | Zebra Technologies Corpora | $243.39 | 8.28 | 12% | $178.48 | -27% |  |
| 33 | PSX | Phillips 66 | $171.76 | 10.12 | 0% | $125.67 | -27% |  |
| 34 | VRSN | VeriSign, Inc. | $250.85 | 9.06 | 10% | $183.68 | -27% |  |
| 35 | ARES | Ares Management Corporatio | $112.47 | 2.17 | 25% | $82.14 | -27% |  |
| 36 | ADM | Archer-Daniels-Midland Com | $76.54 | 2.24 | 15% | $55.8 | -27% |  |
| 37 | HWM | Howmet Aerospace Inc. | $273.14 | 4.32 | 30% | $199.19 | -27% |  |
| 38 | ITW | Illinois Tool Works Inc. | $270.6 | 10.77 | 8% | $197.16 | -27% |  |
| 39 | LOW | Lowe's Companies, Inc. | $221.93 | 11.83 | 2% | $160.38 | -28% |  |
| 40 | ROK | Rockwell Automation, Inc. | $479.39 | 9.64 | 23% | $342.96 | -28% |  |
| 41 | UNH | UnitedHealth Group Incorpo | $415.53 | 13.3 | 12% | $297.24 | -28% |  |
| 42 | J | Jacobs Solutions Inc. | $124.39 | 3.4 | 16% | $88.76 | -29% |  |
| 43 | GM | General Motors Company | $78.53 | 2.74 | 10% | $55.85 | -29% |  |
| 44 | BF-B | Brown Forman Inc | $27.68 | 1.53 | 1% | $19.64 | -29% |  |
| 45 | HSIC | Henry Schein, Inc. | $83.69 | 3.31 | 8% | $59.29 | -29% |  |
| 46 | TMO | Thermo Fisher Scientific I | $505.75 | 18.21 | 10% | $358.28 | -29% |  |
| 47 | FDX | FedEx Corporation | $329.44 | 18.75 | 0% | $232.85 | -29% |  |
| 48 | ZBH | Zimmer Biomet Holdings, In | $90.96 | 3.86 | 6% | $64.27 | -29% |  |
| 49 | LNT | Alliant Energy Corporation | $76.19 | 3.18 | 6% | $53.83 | -29% |  |
| 50 | MLM | Martin Marietta Materials, | $628.94 | 15.98 | 18% | $444.27 | -29% |  |
| 51 | A | Agilent Technologies, Inc. | $135.51 | 4.99 | 9% | $95.52 | -30% |  |
| 52 | UPS | United Parcel Service, Inc | $109.31 | 6.18 | 0% | $76.75 | -30% |  |
| 53 | WM | Waste Management, Inc. | $223.08 | 6.92 | 13% | $156.31 | -30% |  |
| 54 | HUBB | Hubbell Inc | $536.04 | 16.94 | 12% | $373.23 | -30% |  |
| 55 | CMI | Cummins Inc. | $727.59 | 19.28 | 16% | $505.92 | -30% |  |
| 56 | DOC | Healthpeak Properties, Inc | $21.23 | 0.32 | 30% | $14.75 | -30% |  |
| 57 | CPT | Camden Property Trust | $113.59 | 3.58 | 12% | $78.7 | -31% |  |
| 58 | FE | FirstEnergy Corp. | $48.01 | 1.84 | 8% | $33.26 | -31% |  |
| 59 | XYL | Xylem Inc. | $117.0 | 4.02 | 10% | $81.06 | -31% |  |
| 60 | GWW | W.W. Grainger, Inc. | $1374.78 | 37.26 | 15% | $949.03 | -31% |  |
| 61 | COP | ConocoPhillips | $106.41 | 5.9 | 0% | $73.27 | -31% |  |
| 62 | CNP | CenterPoint Energy, Inc (H | $44.22 | 1.63 | 8% | $30.41 | -31% |  |
| 63 | PFE | Pfizer, Inc. | $23.67 | 1.31 | 0% | $16.27 | -31% |  |
| 64 | MDLZ | Mondelez International, In | $61.2 | 2.02 | 11% | $42.0 | -31% |  |
| 65 | WMB | Williams Companies, Inc. ( | $77.53 | 2.28 | 13% | $53.19 | -31% |  |
| 66 | SO | Southern Company (The) | $95.91 | 3.91 | 6% | $65.41 | -32% |  |
| 67 | MCO | Moody's Corporation | $438.85 | 13.96 | 11% | $297.03 | -32% |  |
| 68 | TJX | TJX Companies, Inc. (The) | $155.19 | 5.14 | 10% | $104.68 | -32% |  |
| 69 | OXY | Occidental Petroleum Corpo | $51.21 | 0.74 | 30% | $34.12 | -33% |  |
| 70 | FLEX | Flex Ltd. | $161.28 | 2.32 | 30% | $106.97 | -34% |  |
| 71 | SWK | Stanley Black & Decker, In | $92.31 | 2.44 | 15% | $61.24 | -34% |  |
| 72 | MTD | Mettler-Toledo Internation | $1243.42 | 42.52 | 9% | $819.17 | -34% |  |
| 73 | DOV | Dover Corporation | $230.73 | 8.01 | 9% | $151.44 | -34% |  |
| 74 | PG | Procter & Gamble Company ( | $148.5 | 6.85 | 3% | $97.47 | -34% |  |
| 75 | KIM | Kimco Realty Corporation ( | $25.52 | 0.87 | 9% | $16.69 | -35% |  |
| 76 | SBAC | SBA Communications Corpora | $180.95 | 9.5 | 0% | $117.98 | -35% |  |
| 77 | ABT | Abbott Laboratories | $93.24 | 3.57 | 6% | $60.66 | -35% |  |
| 78 | VRSK | Verisk Analytics, Inc. | $177.04 | 6.57 | 7% | $114.81 | -35% |  |
| 79 | ALGN | Align Technology, Inc. | $175.71 | 5.96 | 9% | $113.36 | -36% |  |
| 80 | APD | Air Products and Chemicals | $279.93 | 9.49 | 9% | $179.59 | -36% |  |
| 81 | SYY | Sysco Corporation | $80.85 | 3.6 | 3% | $51.4 | -36% |  |
| 82 | FDXF | FedEx Freight Holding Comp | $158.53 | 4.55 | 12% | $100.61 | -36% |  |
| 83 | AMGN | Amgen Inc. | $352.82 | 14.36 | 4% | $221.17 | -37% |  |
| 84 | TDY | Teledyne Technologies Inco | $627.19 | 19.76 | 10% | $393.05 | -37% |  |
| 85 | WSM | Williams-Sonoma, Inc. | $240.06 | 8.93 | 6% | $150.09 | -38% |  |
| 86 | DTE | DTE Energy Company | $152.81 | 6.08 | 5% | $95.36 | -38% |  |
| 87 | IBKR | Interactive Brokers Group, | $92.16 | 2.33 | 15% | $57.52 | -38% |  |
| 88 | LII | Lennox International, Inc. | $570.73 | 22.49 | 5% | $356.11 | -38% |  |
| 89 | TT | Trane Technologies plc | $503.46 | 13.09 | 14% | $314.09 | -38% |  |
| 90 | JNJ | Johnson & Johnson | $244.88 | 8.62 | 7% | $151.62 | -38% |  |
| 91 | WST | West Pharmaceutical Servic | $346.56 | 7.49 | 18% | $213.79 | -38% |  |
| 92 | LHX | L3Harris Technologies, Inc | $288.52 | 9.2 | 9% | $176.43 | -39% |  |
| 93 | QCOM | QUALCOMM Incorporated | $204.9 | 9.3 | 2% | $125.09 | -39% |  |
| 94 | WAB | Westinghouse Air Brake Tec | $282.45 | 7.06 | 14% | $172.47 | -39% |  |
| 95 | ANET | Arista Networks, Inc. | $165.45 | 2.91 | 23% | $100.91 | -39% |  |
| 96 | KMB | Kimberly-Clark Corporation | $108.1 | 5.17 | 0% | $65.79 | -39% |  |
| 97 | TKO | TKO Group Holdings, Inc. | $203.8 | 2.69 | 30% | $124.03 | -39% |  |
| 98 | LRCX | Lam Research Corporation | $401.82 | 5.3 | 30% | $244.38 | -39% |  |
| 99 | TYL | Tyler Technologies, Inc. | $281.09 | 7.25 | 14% | $170.18 | -40% |  |
| 100 | SRE | DBA Sempra | $93.43 | 2.94 | 9% | $56.25 | -40% |  |
| 101 | MSI | Motorola Solutions, Inc. | $397.01 | 12.39 | 9% | $238.15 | -40% |  |
| 102 | EMR | Emerson Electric Company | $145.34 | 4.32 | 10% | $87.11 | -40% |  |
| 103 | CAH | Cardinal Health, Inc. | $234.75 | 6.55 | 11% | $139.61 | -40% |  |
| 104 | SLB | SLB Limited | $47.42 | 2.27 | 0% | $28.19 | -41% |  |
| 105 | SYK | Stryker Corporation | $316.11 | 8.63 | 12% | $185.61 | -41% |  |
| 106 | CTAS | Cintas Corporation | $169.09 | 4.73 | 11% | $98.71 | -42% |  |
| 107 | BX | Blackstone Inc. | $114.18 | 3.9 | 7% | $66.61 | -42% |  |
| 108 | RSG | Republic Services, Inc. | $213.5 | 6.96 | 8% | $124.08 | -42% |  |
| 109 | CCI | Crown Castle Inc. | $79.53 | 2.37 | 9% | $45.95 | -42% |  |
| 110 | SNDK | Sandisk Corporation | $2335.0 | 29.19 | 30% | $1345.91 | -42% |  |
| 111 | FRT | Federal Realty Investment  | $124.55 | 5.77 | 0% | $71.65 | -42% |  |
| 112 | LIN | Linde plc | $522.28 | 15.09 | 10% | $299.2 | -43% |  |
| 113 | MAR | Marriott International | $378.91 | 9.55 | 13% | $216.67 | -43% |  |
| 114 | NDSN | Nordson Corporation | $304.64 | 9.36 | 8% | $174.22 | -43% |  |
| 115 | FAST | Fastenal Company | $46.92 | 1.13 | 14% | $26.78 | -43% |  |
| 116 | CVNA | Carvana Co. | $66.2 | 1.73 | 12% | $37.69 | -43% |  |
| 117 | RTX | RTX Corporation | $186.59 | 5.34 | 10% | $106.22 | -43% |  |
| 118 | MMM | 3M Company | $167.97 | 5.19 | 8% | $94.35 | -44% |  |
| 119 | VRT | Vertiv Holdings, LLC | $325.57 | 3.97 | 30% | $183.05 | -44% |  |
| 120 | WMT | Walmart Inc. | $115.78 | 2.84 | 13% | $65.12 | -44% |  |
| 121 | IDXX | IDEXX Laboratories, Inc. | $554.94 | 13.6 | 13% | $310.21 | -44% |  |
| 122 | CSCO | Cisco Systems, Inc. | $118.97 | 3.0 | 12% | $66.42 | -44% |  |
| 123 | IEX | IDEX Corporation | $228.07 | 6.75 | 9% | $126.92 | -44% |  |
| 124 | O | Realty Income Corporation | $62.04 | 1.22 | 18% | $34.51 | -44% |  |
| 125 | ECL | Ecolab Inc. | $281.2 | 7.4 | 11% | $155.9 | -45% |  |
| 126 | HD | Home Depot, Inc. (The) | $345.0 | 14.08 | 2% | $191.26 | -45% |  |
| 127 | PKG | Packaging Corporation of A | $241.09 | 8.22 | 6% | $133.67 | -45% |  |
| 128 | ISRG | Intuitive Surgical, Inc. | $399.69 | 8.23 | 17% | $221.03 | -45% |  |
| 129 | SHW | Sherwin-Williams Company ( | $339.08 | 10.41 | 8% | $185.59 | -45% |  |
| 130 | MNST | Monster Beverage Corporati | $95.83 | 2.07 | 15% | $52.02 | -46% |  |
| 131 | GE | GE Aerospace | $371.36 | 8.06 | 15% | $200.36 | -46% |  |
| 132 | AME | AMETEK, Inc. | $240.95 | 6.63 | 10% | $129.91 | -46% |  |
| 133 | ROL | Rollins, Inc. | $42.8 | 1.09 | 11% | $23.0 | -46% |  |
| 134 | XOM | Exxon Mobil Corporation | $137.55 | 5.94 | 0% | $73.77 | -46% |  |
| 135 | BA | Boeing Company (The) | $218.12 | 2.53 | 30% | $116.66 | -46% |  |
| 136 | TPL | Texas Pacific Land Corpora | $391.04 | 7.27 | 18% | $209.18 | -46% |  |
| 137 | ON | ON Semiconductor Corporati | $118.74 | 1.37 | 30% | $63.17 | -47% |  |
| 138 | KR | Kroger Company (The) | $57.77 | 1.71 | 8% | $30.59 | -47% |  |
| 139 | TER | Teradyne, Inc. | $471.96 | 5.38 | 30% | $248.07 | -47% |  |
| 140 | AMCR | Amcor plc | $42.86 | 1.24 | 8% | $22.46 | -48% |  |
| 141 | REG | Regency Centers Corporatio | $80.25 | 2.91 | 3% | $41.85 | -48% |  |
| 142 | CHD | Church & Dwight Company, I | $98.15 | 3.04 | 6% | $51.14 | -48% |  |
| 143 | NOW | ServiceNow, Inc. | $89.52 | 1.68 | 18% | $46.65 | -48% |  |
| 144 | PH | Parker-Hannifin Corporatio | $989.91 | 27.12 | 9% | $515.82 | -48% |  |
| 145 | PSA | Public Storage | $320.74 | 9.69 | 7% | $165.88 | -48% |  |
| 146 | TDG | Transdigm Group Incorporat | $1332.56 | 31.98 | 12% | $684.41 | -49% |  |
| 147 | SBUX | Starbucks Corporation | $103.16 | 1.31 | 26% | $52.55 | -49% |  |
| 148 | CASY | Caseys General Stores, Inc | $784.71 | 19.16 | 11% | $398.42 | -49% |  |
| 149 | DHR | Danaher Corporation | $193.21 | 5.16 | 9% | $97.6 | -50% |  |
| 150 | HRL | Hormel Foods Corporation | $26.02 | 0.85 | 4% | $13.15 | -50% |  |
| 151 | GNRC | Generac Holdlings Inc. | $295.16 | 3.19 | 30% | $147.09 | -50% |  |
| 152 | CTVA | Corteva, Inc. | $81.62 | 1.85 | 12% | $40.58 | -50% |  |
| 153 | ETN | Eaton Corporation, PLC | $419.87 | 10.2 | 10% | $208.77 | -50% |  |
| 154 | ODFL | Old Dominion Freight Line, | $220.12 | 4.8 | 13% | $109.0 | -50% |  |
| 155 | Q | Qnity Electronics, Inc. | $167.49 | 3.1 | 16% | $82.79 | -51% |  |
| 156 | CVS | CVS Health Corporation | $104.66 | 2.28 | 13% | $51.64 | -51% |  |
| 157 | FTV | Fortive Corporation | $61.73 | 1.7 | 8% | $30.27 | -51% |  |
| 158 | HLT | Hilton Worldwide Holdings  | $340.55 | 6.54 | 15% | $165.78 | -51% |  |
| 159 | HON | Honeywell International In | $231.24 | 6.27 | 8% | $112.15 | -52% |  |
| 160 | FFIV | F5, Inc. | $386.01 | 12.16 | 4% | $186.48 | -52% |  |
| 161 | COST | Costco Wholesale Corporati | $942.24 | 19.88 | 13% | $452.85 | -52% |  |
| 162 | MRVL | Marvell Technology, Inc. | $281.26 | 2.9 | 30% | $133.72 | -52% |  |
| 163 | STX | Seagate Technology Holding | $1025.36 | 10.56 | 30% | $486.91 | -52% |  |
| 164 | NSC | Norfolk Southern Corporati | $312.06 | 11.86 | 0% | $147.28 | -53% |  |
| 165 | BDX | Becton, Dickinson and Comp | $151.38 | 5.74 | 0% | $71.28 | -53% |  |
| 166 | TSN | Tyson Foods, Inc. | $57.8 | 1.27 | 11% | $27.05 | -53% |  |
| 167 | PWR | Quanta Services, Inc. | $718.59 | 7.26 | 30% | $334.75 | -53% |  |
| 168 | EQR | Equity Residential | $67.17 | 2.5 | 0% | $31.05 | -54% |  |
| 169 | NKE | Nike, Inc. | $40.9 | 1.52 | 0% | $18.88 | -54% |  |
| 170 | WAT | Waters Corporation | $376.89 | 7.88 | 12% | $172.19 | -54% |  |
| 171 | EW | Edwards Lifesciences Corpo | $89.72 | 1.85 | 12% | $40.45 | -55% |  |
| 172 | MPWR | Monolithic Power Systems,  | $1438.3 | 13.95 | 30% | $643.22 | -55% |  |
| 173 | ESS | Essex Property Trust, Inc. | $285.57 | 8.88 | 2% | $122.77 | -57% |  |
| 174 | WELL | Welltower Inc. | $223.73 | 2.08 | 30% | $95.91 | -57% |  |
| 175 | SWKS | Skyworks Solutions, Inc. | $69.94 | 2.4 | 0% | $29.8 | -57% |  |
| 176 | CMG | Chipotle Mexican Grill, In | $32.28 | 1.09 | 0% | $13.54 | -58% |  |
| 177 | GLW | Corning Incorporated | $228.01 | 2.07 | 30% | $95.45 | -58% |  |
| 178 | FTNT | Fortinet, Inc. | $149.93 | 2.58 | 14% | $62.72 | -58% |  |
| 179 | CL | Colgate-Palmolive Company | $91.06 | 2.58 | 3% | $37.72 | -59% |  |
| 180 | CVX | Chevron Corporation | $172.24 | 5.74 | 0% | $71.28 | -59% |  |
| 181 | EQIX | Equinix, Inc. | $1087.61 | 14.47 | 20% | $447.14 | -59% |  |
| 182 | INVH | Invitation Homes Inc. | $29.91 | 0.95 | 0% | $11.8 | -61% |  |
| 183 | EA | Electronic Arts Inc. | $204.73 | 3.5 | 13% | $78.85 | -62% |  |
| 184 | PLTR | Palantir Technologies Inc. | $107.27 | 0.89 | 30% | $41.04 | -62% |  |
| 185 | EXR | Extra Space Storage Inc | $147.19 | 4.45 | 0% | $55.26 | -62% |  |
| 186 | BLDR | Builders FirstSource, Inc. | $88.72 | 2.62 | 0% | $32.54 | -63% |  |
| 187 | CARR | Carrier Global Corporation | $76.0 | 1.5 | 8% | $27.48 | -64% |  |
| 188 | DE | Deere & Company | $630.76 | 17.66 | 0% | $219.31 | -65% |  |
| 189 | APTV | Aptiv PLC | $61.97 | 1.68 | 0% | $20.86 | -66% |  |
| 190 | SW | Smurfit WestRock plc | $46.84 | 0.72 | 12% | $15.76 | -66% |  |
| 191 | COO | The Cooper Companies, Inc. | $70.64 | 1.18 | 10% | $23.76 | -66% |  |
| 192 | CDNS | Cadence Design Systems, In | $368.23 | 4.31 | 18% | $122.97 | -67% |  |
| 193 | AKAM | Akamai Technologies, Inc. | $112.89 | 2.96 | 0% | $36.76 | -67% |  |
| 194 | DD | DuPont de Nemours, Inc. | $137.8 | 1.14 | 26% | $44.96 | -67% |  |
| 195 | HOOD | Robinhood Markets, Inc. | $93.47 | 2.06 | 3% | $29.23 | -69% |  |
| 196 | HUM | Humana Inc. | $376.0 | 9.36 | 0% | $116.24 | -69% |  |
| 197 | IR | Ingersoll Rand Inc. | $81.7 | 1.48 | 6% | $25.18 | -69% |  |
| 198 | LITE | Lumentum Holdings Inc. | $861.97 | 5.69 | 30% | $262.36 | -70% |  |
| 199 | MAA | Mid-America Apartment Comm | $138.08 | 3.3 | 0% | $40.98 | -70% |  |
| 200 | APO | Apollo Global Management,  | $121.51 | 1.59 | 13% | $35.95 | -70% |  |
| 201 | KLAC | KLA Corporation | $258.8 | 3.52 | 12% | $76.35 | -70% |  |
| 202 | MOS | Mosaic Company (The) | $21.73 | 0.14 | 30% | $6.41 | -70% |  |
| 203 | CIEN | Ciena Corporation | $484.69 | 3.01 | 30% | $138.79 | -71% |  |
| 204 | RVTY | Revvity, Inc. | $113.53 | 2.08 | 4% | $30.96 | -73% |  |
| 205 | AMD | Advanced Micro Devices, In | $532.57 | 2.98 | 30% | $137.4 | -74% |  |
| 206 | AXON | Axon Enterprise, Inc. | $444.73 | 2.49 | 30% | $114.81 | -74% |  |
| 207 | DASH | DoorDash, Inc. | $176.91 | 2.11 | 10% | $42.62 | -76% |  |
| 208 | COHR | Coherent Corp. | $407.25 | 2.12 | 30% | $97.75 | -76% |  |
| 209 | SNPS | Synopsys, Inc. | $455.02 | 4.37 | 15% | $107.08 | -76% |  |
| 210 | ABBV | AbbVie Inc. | $243.14 | 2.04 | 14% | $49.57 | -80% |  |
| 211 | COF | Capital One Financial Corp | $204.9 | 3.26 | 0% | $41.38 | -80% |  |
| 212 | MGM | MGM Resorts International | $47.2 | 0.73 | 0% | $9.07 | -81% |  |
| 213 | VTR | Ventas, Inc. | $87.43 | 0.55 | 19% | $16.01 | -82% |  |
| 214 | IRM | Iron Mountain Incorporated | $131.06 | 0.92 | 15% | $22.75 | -83% |  |
| 215 | TECH | Bio-Techne Corp | $70.7 | 0.7 | 7% | $12.16 | -83% |  |
| 216 | NRG | NRG Energy, Inc. | $147.11 | 0.91 | 12% | $20.08 | -86% |  |
| 217 | CSGP | CoStar Group, Inc. | $28.64 | 0.07 | 30% | $3.23 | -89% |  |
| 218 | PSKY | Paramount Skydance Corpora | $9.43 | 0.03 | 23% | $1.05 | -89% |  |
| 219 | MCHP | Microchip Technology Incor | $94.12 | 0.22 | 30% | $10.14 | -89% |  |
| 220 | TSLA | Tesla, Inc. | $375.12 | 1.09 | 21% | $35.68 | -90% |  |
| 221 | PANW | Palo Alto Networks, Inc. | $293.09 | 1.14 | 11% | $23.89 | -92% |  |
| 222 | FANG | Diamondback Energy, Inc. | $182.55 | 0.99 | 0% | $12.29 | -93% |  |
| 223 | GPC | Genuine Parts Company | $112.99 | 0.44 | 5% | $6.83 | -94% |  |
| 224 | DDOG | Datadog, Inc. | $220.94 | 0.4 | 18% | $11.42 | -95% |  |
| 225 | ALB | Albemarle Corporation | $141.05 | -3.41 | — | — | no earnings | no_earnings |
| 226 | ARE | Alexandria Real Estate Equ | $53.29 | -6.27 | — | — | no earnings | no_earnings |
| 227 | BAX | Baxter International Inc. | $21.55 | -1.91 | — | — | no earnings | no_earnings |
| 228 | CAG | ConAgra Brands, Inc. | $13.78 | -0.1 | — | — | no earnings | no_earnings |
| 229 | CNC | Centene Corporation | $64.77 | -13.05 | — | — | no earnings | no_earnings |
| 230 | CRL | Charles River Laboratories | $212.71 | -3.7 | — | — | no earnings | no_earnings |
| 231 | CRWD | CrowdStrike Holdings, Inc. | $678.65 | -0.14 | — | — | no earnings | no_earnings |
| 232 | DOW | Dow Inc. | $29.31 | -4.0 | — | — | no earnings | no_earnings |
| 233 | ECHO |  | $97.19 | None | — | — | no earnings | no_earnings |
| 234 | EL | Estee Lauder Companies, In | $81.5 | -0.7 | — | — | no earnings | no_earnings |
| 235 | F | Ford Motor Company | $14.11 | -1.55 | — | — | no earnings | no_earnings |
| 236 | FISV | Fiserv, Inc. | $47.53 | None | — | — | no earnings | no_earnings |
| 237 | HAS | Hasbro, Inc. | $84.88 | -1.61 | — | — | no earnings | no_earnings |
| 238 | INTC | Intel Corporation | $132.87 | -0.6 | — | — | no earnings | no_earnings |
| 239 | IP | International Paper Compan | $39.02 | -5.19 | — | — | no earnings | no_earnings |
| 240 | IVZ | Invesco Ltd | $25.87 | -1.47 | — | — | no earnings | no_earnings |
| 241 | KHC | The Kraft Heinz Company | $23.47 | -4.86 | — | — | no earnings | no_earnings |
| 242 | LYB | LyondellBasell Industries  | $55.84 | -2.12 | — | — | no earnings | no_earnings |
| 243 | LYV | Live Nation Entertainment, | $175.11 | -1.77 | — | — | no earnings | no_earnings |
| 244 | MRNA | Moderna, Inc. | $59.75 | -8.14 | — | — | no earnings | no_earnings |
| 245 | OMC | Omnicom Group Inc. | $73.43 | -0.37 | — | — | no earnings | no_earnings |
| 246 | SJM | The J.M. Smucker Company | $112.5 | -1.31 | — | — | no earnings | no_earnings |
| 247 | TAP | Molson Coors Beverage Comp | $40.54 | -10.55 | — | — | no earnings | no_earnings |
| 248 | TTWO | Take-Two Interactive Softw | $238.72 | -1.62 | — | — | no earnings | no_earnings |
| 249 | VTRS | Viatris Inc. | $16.07 | -0.3 | — | — | no earnings | no_earnings |
| 250 | WBD | Warner Bros. Discovery, In | $26.98 | -0.7 | — | — | no earnings | no_earnings |

<details><summary>Neutral / near-median (3) — excluded from the split</summary>

| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | DHI | D.R. Horton, Inc. | $166.95 | 10.65 | 0% | $132.26 | -21% |  |
| 2 | ERIE | Erie Indemnity Company | $229.96 | 10.91 | 6% | $180.88 | -21% |  |
| 3 | MSCI | MSCI Inc. | $544.56 | 17.53 | 14% | $428.24 | -21% |  |

</details>

---
## Russell 1000 (top ~1000 US by market cap)
Valued 1000 holdings · **500 most undervalued (BULLISH)** vs **500 most overvalued (BEARISH)** · 0 near-median (neutral, excluded).

### 🟢 BULLISH — 500 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | CET | 11017 | $52.11 | 9.15 | 30% | $421.9 | +710% |  |
| 2 | EXE | Expand Energy Corporation | $88.44 | 13.44 | 27% | $553.92 | +526% |  |
| 3 | APA | APA Corporation | $33.42 | 4.29 | 30% | $197.81 | +492% |  |
| 4 | KEP | Korea Electric Power Corpo | $12.46 | 4.42 | 5% | $70.25 | +464% |  |
| 5 | CHTR | Charter Communications, In | $129.65 | 36.96 | 10% | $727.51 | +461% |  |
| 6 | GFI | Gold Fields Limited | $32.82 | 3.94 | 30% | $181.67 | +454% |  |
| 7 | CF | CF Industries Holdings, In | $105.49 | 11.1 | 30% | $511.81 | +385% |  |
| 8 | EQT | EQT Corporation | $51.65 | 5.27 | 30% | $242.99 | +370% |  |
| 9 | LTM | LATAM Airlines Group S.A. | $56.9 | 5.79 | 30% | $266.97 | +369% |  |
| 10 | B | Barrick Mining Corporation | $36.75 | 3.65 | 30% | $168.3 | +358% |  |
| 11 | DINO | HF Sinclair Corporation | $67.78 | 6.66 | 30% | $307.08 | +353% |  |
| 12 | KGC | Kinross Gold Corporation | $24.04 | 2.35 | 30% | $108.36 | +351% |  |
| 13 | AR | Antero Resources Corporati | $34.5 | 3.09 | 30% | $142.48 | +313% |  |
| 14 | ALLY | Ally Financial Inc. | $46.32 | 4.12 | 30% | $189.97 | +310% |  |
| 15 | RCI | Rogers Communication, Inc. | $34.8 | 9.18 | 4% | $139.84 | +302% |  |
| 16 | TTE | TotalEnergies SE | $78.28 | 6.74 | 30% | $310.77 | +297% |  |
| 17 | AU | AngloGold Ashanti PLC | $79.34 | 6.81 | 30% | $314.0 | +296% |  |
| 18 | EG | Everest Group, Ltd. | $343.02 | 49.12 | 17% | $1337.95 | +290% |  |
| 19 | TM | Toyota Motor Corporation | $166.5 | 18.27 | 23% | $643.96 | +287% |  |
| 20 | UAL | United Airlines Holdings,  | $134.6 | 11.19 | 30% | $515.96 | +283% |  |
| 21 | NEM | Newmont Corporation | $95.35 | 7.71 | 30% | $355.5 | +273% |  |
| 22 | AGI | Alamos Gold Inc. | $31.11 | 2.51 | 30% | $115.73 | +272% |  |
| 23 | AXIA | AXIA Energia | $10.61 | 0.85 | 30% | $39.19 | +269% |  |
| 24 | AES | The AES Corporation | $14.66 | 1.92 | 18% | $54.09 | +269% |  |
| 25 | VG | Venture Global, Inc. | $10.83 | 0.96 | 27% | $38.92 | +259% |  |
| 26 | CDE | Coeur Mining, Inc. | $15.99 | 1.24 | 30% | $57.17 | +258% |  |
| 27 | EOG | EOG Resources, Inc. | $133.59 | 10.17 | 30% | $468.93 | +251% |  |
| 28 | NTR | Nutrien Ltd. | $60.96 | 4.91 | 28% | $209.67 | +244% |  |
| 29 | SHEL | Shell PLC | $77.33 | 6.42 | 27% | $259.28 | +235% |  |
| 30 | SF | Stifel Financial Corporati | $71.47 | 5.13 | 30% | $236.54 | +231% |  |
| 31 | CVE | Cenovus Energy Inc | $24.68 | 1.77 | 30% | $81.61 | +231% |  |
| 32 | AER | AerCap Holdings N.V. | $150.11 | 22.79 | 12% | $496.33 | +231% |  |
| 33 | JEF | Jefferies Financial Group  | $52.64 | 3.76 | 30% | $173.37 | +229% |  |
| 34 | PAAS | Pan American Silver Corp. | $44.99 | 3.17 | 30% | $146.16 | +225% |  |
| 35 | LYG | Lloyds Banking Group Plc | $5.75 | 0.4 | 30% | $18.44 | +221% |  |
| 36 | BABA | Alibaba Group Holding Limi | $95.07 | 6.48 | 30% | $298.78 | +214% |  |
| 37 | AEM | Agnico Eagle Mines Limited | $156.18 | 10.62 | 30% | $489.67 | +214% |  |
| 38 | EQNR | Equinor ASA | $31.56 | 2.21 | 29% | $98.8 | +213% |  |
| 39 | SU | Suncor Energy  Inc. | $54.36 | 3.7 | 30% | $169.95 | +213% |  |
| 40 | MFG | Mizuho Financial Group, In | $9.59 | 0.62 | 30% | $28.59 | +198% |  |
| 41 | RNR | RenaissanceRe Holdings Ltd | $307.14 | 59.34 | 4% | $906.52 | +195% |  |
| 42 | SYF | Synchrony Financial | $78.52 | 9.66 | 14% | $227.35 | +190% |  |
| 43 | BPYPN | Brookfield Property Partne | $13.91 | 2.196 | 8% | $40.07 | +188% |  |
| 44 | FSLR | First Solar, Inc. | $248.64 | 15.49 | 30% | $714.22 | +187% |  |
| 45 | ARW | Arrow Electronics, Inc. | $229.03 | 13.97 | 30% | $644.14 | +181% |  |
| 46 | CMCSA | Comcast Corporation | $22.69 | 5.1 | 0% | $63.33 | +179% |  |
| 47 | TIGO | Millicom International Cel | $88.46 | 7.36 | 22% | $245.71 | +178% |  |
| 48 | MPC | Marathon Petroleum Corpora | $253.56 | 15.19 | 30% | $700.39 | +176% |  |
| 49 | CFG | Citizens Financial Group,  | $70.66 | 4.22 | 30% | $194.58 | +175% |  |
| 50 | WF | Woori Financial Group Inc. | $57.36 | 7.9 | 10% | $157.28 | +174% |  |
| 51 | GILD | Gilead Sciences, Inc. | $123.84 | 7.36 | 30% | $339.36 | +174% |  |
| 52 | SUZ | Suzano S.A. | $8.1 | 1.77 | 0% | $21.98 | +171% |  |
| 53 | MT | Arcelor Mittal NY Registry | $61.82 | 3.82 | 29% | $167.24 | +170% |  |
| 54 | DB | Deutsche Bank AG | $34.38 | 3.6 | 16% | $92.69 | +170% |  |
| 55 | BPOP | Popular, Inc. | $167.19 | 13.53 | 21% | $443.24 | +165% |  |
| 56 | FIS | Fidelity National Informat | $37.86 | 5.16 | 9% | $99.27 | +162% |  |
| 57 | OVV | Ovintiv Inc. (DE) | $53.55 | 3.04 | 30% | $140.17 | +162% |  |
| 58 | MLI | Mueller Industries, Inc. | $134.39 | 7.63 | 30% | $351.81 | +162% |  |
| 59 | BPYPO | Brookfield Property Partne | $15.32 | 2.196 | 8% | $40.07 | +162% |  |
| 60 | BCS | Barclays PLC | $27.3 | 2.29 | 20% | $71.27 | +161% |  |
| 61 | T | AT&T Inc. | $22.42 | 3.04 | 9% | $58.41 | +160% |  |
| 62 | BPYPP | Brookfield Property Partne | $15.47 | 2.196 | 8% | $40.07 | +159% |  |
| 63 | C | Citigroup, Inc. | $144.98 | 8.09 | 30% | $373.02 | +157% |  |
| 64 | UBER | Uber Technologies, Inc. | $72.25 | 4.03 | 30% | $185.82 | +157% |  |
| 65 | SHG | Shinhan Financial Group Co | $61.99 | 6.66 | 14% | $159.24 | +157% |  |
| 66 | BBD | Banco Bradesco Sa | $3.35 | 0.4 | 11% | $8.54 | +155% |  |
| 67 | BCE | BCE, Inc. | $23.2 | 4.76 | 0% | $59.11 | +155% |  |
| 68 | VLO | Valero Energy Corporation | $255.06 | 13.7 | 30% | $631.69 | +148% |  |
| 69 | NWG | NatWest Group plc | $17.35 | 1.84 | 13% | $42.8 | +147% |  |
| 70 | ALL | Allstate Corporation (The) | $231.6 | 45.21 | 0% | $561.44 | +142% |  |
| 71 | FMS | Fresenius Medical Care AG | $23.25 | 1.86 | 19% | $55.98 | +141% |  |
| 72 | NU | Nu Holdings Ltd. | $12.46 | 0.65 | 30% | $29.97 | +140% |  |
| 73 | SMCI | Super Micro Computer, Inc. | $31.68 | 1.9 | 26% | $75.05 | +137% |  |
| 74 | RGA | Reinsurance Group of Ameri | $208.5 | 18.39 | 17% | $492.2 | +136% |  |
| 75 | EVR | Evercore Inc. | $347.31 | 17.78 | 30% | $819.81 | +136% |  |
| 76 | PBR | Petroleo Brasileiro S.A. P | $16.52 | 3.13 | 0% | $38.87 | +135% |  |
| 77 | ACGL | Arch Capital Group Ltd. | $94.33 | 13.0 | 7% | $221.71 | +135% |  |
| 78 | WES | Western Midstream Partners | $42.78 | 3.04 | 21% | $98.71 | +131% |  |
| 79 | KEY | KeyCorp | $23.41 | 1.63 | 22% | $53.71 | +129% |  |
| 80 | SNX | TD SYNNEX Corporation | $277.63 | 13.94 | 30% | $635.13 | +129% |  |
| 81 | DAL | Delta Air Lines, Inc. | $92.11 | 6.85 | 20% | $209.87 | +128% |  |
| 82 | KB | KB Financial Group Inc | $99.99 | 10.42 | 12% | $226.83 | +127% |  |
| 83 | SCHW | Charles Schwab Corporation | $89.44 | 5.03 | 26% | $202.1 | +126% |  |
| 84 | VICI | VICI Properties Inc. | $26.53 | 2.92 | 10% | $59.85 | +126% |  |
| 85 | DVA | DaVita Inc. | $213.36 | 10.39 | 30% | $479.07 | +124% |  |
| 86 | PUK | Prudential Public Limited  | $26.65 | 3.07 | 9% | $59.69 | +124% |  |
| 87 | SBS | Companhia de saneamento Ba | $5.63 | 0.49 | 15% | $12.45 | +121% |  |
| 88 | SUN | Sunoco LP | $64.72 | 3.92 | 24% | $143.17 | +121% |  |
| 89 | HIG | The Hartford Insurance Gro | $130.37 | 14.21 | 10% | $287.44 | +120% |  |
| 90 | GLPI | Gaming and Leisure Propert | $45.06 | 3.17 | 20% | $98.75 | +119% |  |
| 91 | ONB | Old National Bancorp | $25.88 | 1.94 | 18% | $55.37 | +114% |  |
| 92 | CTSH | Cognizant Technology Solut | $39.15 | 4.61 | 8% | $83.03 | +112% |  |
| 93 | TEL | TE Connectivity plc | $200.07 | 9.78 | 28% | $422.55 | +111% |  |
| 94 | CBOE | Cboe Global Markets, Inc. | $244.98 | 11.71 | 29% | $516.47 | +111% |  |
| 95 | HL | Hecla Mining Company | $15.15 | 0.69 | 30% | $31.82 | +110% |  |
| 96 | ITUB | Itau Unibanco Banco Holdin | $8.03 | 0.79 | 11% | $16.83 | +110% |  |
| 97 | VLYPP | Valley National Bancorp -  | $24.6 | 1.11 | 30% | $51.18 | +108% |  |
| 98 | TECK | Teck Resources Ltd | $59.0 | 2.66 | 30% | $122.65 | +108% |  |
| 99 | JLL | Jones Lang LaSalle Incorpo | $303.76 | 18.59 | 22% | $631.39 | +108% |  |
| 100 | EDU | New Oriental Education & T | $44.44 | 2.7 | 22% | $92.12 | +107% |  |
| 101 | VLYPO | Valley National Bancorp -  | $24.71 | 1.11 | 30% | $51.18 | +107% |  |
| 102 | BHP | BHP Group Limited | $81.16 | 4.03 | 27% | $167.11 | +106% |  |
| 103 | ADBE | Adobe Inc. | $193.41 | 17.48 | 13% | $395.36 | +104% |  |
| 104 | TCOM | Trip.com Group Limited | $40.49 | 6.66 | 0% | $82.71 | +104% |  |
| 105 | JD | JD.com, Inc. | $25.19 | 1.36 | 25% | $51.03 | +103% |  |
| 106 | UBS | UBS Group AG Registered | $49.94 | 2.79 | 24% | $100.72 | +102% |  |
| 107 | NFLX | Netflix, Inc. | $70.9 | 3.1 | 30% | $142.94 | +102% |  |
| 108 | INCY | Incyte Corporation | $107.53 | 7.08 | 20% | $216.6 | +101% |  |
| 109 | ZION | Zions Bancorporation N.A. | $69.33 | 6.44 | 12% | $138.75 | +100% |  |
| 110 | AMP | Ameriprise Financial, Inc. | $453.29 | 40.12 | 12% | $897.82 | +98% |  |
| 111 | NTRS | Northern Trust Corporation | $175.97 | 9.56 | 24% | $348.18 | +98% |  |
| 112 | NLY | Annaly Capital Management  | $22.56 | 3.1 | 3% | $44.43 | +97% |  |
| 113 | GDDY | GoDaddy Inc. | $79.35 | 6.31 | 15% | $156.04 | +97% |  |
| 114 | SAN | Banco Santander, S.A. Spon | $13.38 | 1.01 | 16% | $26.26 | +96% |  |
| 115 | CPAY | Corpay, Inc. | $325.81 | 16.71 | 25% | $638.87 | +96% |  |
| 116 | FIVE | Five Below, Inc. | $186.59 | 7.93 | 30% | $365.64 | +96% |  |
| 117 | BAC | Bank of America Corporatio | $58.19 | 4.03 | 18% | $112.37 | +93% |  |
| 118 | ORI | Old Republic International | $40.01 | 4.06 | 9% | $76.51 | +91% |  |
| 119 | UMBF | UMB Financial Corporation | $143.41 | 11.43 | 14% | $271.03 | +89% |  |
| 120 | SNEX | StoneX Group Inc. | $137.28 | 5.59 | 30% | $257.75 | +88% |  |
| 121 | FCNCA | First Citizens BancShares, | $2089.21 | 173.4 | 13% | $3921.98 | +88% |  |
| 122 | COKE | Coca-Cola Consolidated, In | $179.23 | 7.29 | 30% | $336.13 | +88% |  |
| 123 | CM | Canadian Imperial Bank of  | $114.37 | 7.09 | 19% | $213.93 | +87% |  |
| 124 | NUE | Nucor Corporation | $248.89 | 10.08 | 30% | $464.78 | +87% |  |
| 125 | RGLD | Royal Gold, Inc. | $204.62 | 8.27 | 30% | $381.32 | +86% |  |
| 126 | SOLV | Solventum Corporation | $77.92 | 8.17 | 7% | $143.97 | +85% |  |
| 127 | SSB | SouthState Bank Corporatio | $100.77 | 9.28 | 10% | $186.02 | +85% |  |
| 128 | HAL | Halliburton Company | $34.67 | 1.81 | 23% | $63.95 | +84% |  |
| 129 | TFC | Truist Financial Corporati | $50.67 | 4.04 | 13% | $93.34 | +84% |  |
| 130 | TEVA | Teva Pharmaceutical Indust | $33.62 | 1.34 | 30% | $61.79 | +84% |  |
| 131 | KSPI | Joint Stock Company Kaspi. | $86.85 | 11.1 | 3% | $159.33 | +84% |  |
| 132 | FHN | First Horizon Corporation | $25.56 | 1.99 | 14% | $46.9 | +84% |  |
| 133 | ING | ING Group, N.V. | $31.02 | 2.49 | 13% | $56.82 | +83% |  |
| 134 | AMX | America Movil, S.A.B. de C | $26.3 | 1.65 | 19% | $48.18 | +83% |  |
| 135 | MKC | McCormick & Company, Incor | $48.35 | 6.1 | 3% | $88.33 | +83% |  |
| 136 | NBIX | Neurocrine Biosciences, In | $164.18 | 6.5 | 30% | $299.71 | +82% |  |
| 137 | SQM | Sociedad Quimica y Minera  | $73.11 | 2.86 | 30% | $131.87 | +80% |  |
| 138 | PNFP | Pinnacle Financial Partner | $98.7 | 7.19 | 15% | $178.03 | +80% |  |
| 139 | RF | Regions Financial Corporat | $29.98 | 2.41 | 12% | $53.07 | +77% |  |
| 140 | THC | Tenet Healthcare Corporati | $183.94 | 19.22 | 6% | $325.64 | +77% |  |
| 141 | GOOG | Alphabet Inc. | $342.19 | 13.11 | 30% | $604.49 | +77% |  |
| 142 | CIB | Grupo Cibest S.A. | $78.89 | 7.83 | 8% | $139.4 | +77% |  |
| 143 | AFG | American Financial Group,  | $135.89 | 10.53 | 13% | $239.97 | +77% |  |
| 144 | GOOGL | Alphabet Inc. | $343.71 | 13.1 | 30% | $604.02 | +76% |  |
| 145 | CINF | Cincinnati Financial Corpo | $177.73 | 17.5 | 8% | $312.14 | +76% |  |
| 146 | AIG | American International Gro | $74.85 | 5.68 | 13% | $131.23 | +75% |  |
| 147 | BKR | Baker Hughes Company | $56.94 | 3.13 | 21% | $99.66 | +75% |  |
| 148 | ACN | Accenture plc | $125.82 | 12.52 | 7% | $219.7 | +75% |  |
| 149 | RS | Reliance, Inc. | $405.78 | 15.34 | 30% | $707.31 | +74% |  |
| 150 | WFC | Wells Fargo & Company | $84.74 | 6.47 | 13% | $147.64 | +74% |  |
| 151 | WBS | Webster Financial Corporat | $75.52 | 6.1 | 12% | $131.49 | +74% |  |
| 152 | UDR | UDR, Inc. | $39.1 | 1.47 | 30% | $67.78 | +73% |  |
| 153 | BIIB | Biogen Inc. | $201.96 | 9.29 | 25% | $348.85 | +73% |  |
| 154 | STLD | Steel Dynamics, Inc. | $251.0 | 9.34 | 30% | $430.66 | +72% |  |
| 155 | BAP | Credicorp Ltd. | $380.41 | 26.17 | 15% | $652.82 | +72% |  |
| 156 | EWBC | East West Bancorp, Inc. | $130.24 | 10.02 | 12% | $221.06 | +70% |  |
| 157 | PNC | PNC Financial Services Gro | $245.28 | 17.22 | 14% | $413.91 | +69% |  |
| 158 | MSFT | Microsoft Corporation | $352.83 | 16.79 | 23% | $594.44 | +68% |  |
| 159 | MU | Micron Technology, Inc. | $1213.56 | 44.29 | 30% | $2042.16 | +68% |  |
| 160 | BBDO | Banco Bradesco Sa | $2.96 | 0.4 | 0% | $4.97 | +68% |  |
| 161 | CI | The Cigna Group | $281.87 | 23.59 | 10% | $472.66 | +68% |  |
| 162 | JBS | JBS N.V. | $12.03 | 1.62 | 0% | $20.12 | +67% |  |
| 163 | CB | Chubb Limited | $330.82 | 28.29 | 9% | $548.02 | +66% |  |
| 164 | FMX | Fomento Economico Mexicano | $125.37 | 4.5 | 30% | $207.49 | +66% |  |
| 165 | TME | Tencent Music Entertainmen | $8.16 | 0.84 | 5% | $13.45 | +65% |  |
| 166 | GIB | CGI Inc. | $62.24 | 5.39 | 9% | $102.28 | +64% |  |
| 167 | VST | Vistra Corp. | $167.77 | 5.97 | 30% | $275.27 | +64% |  |
| 168 | PTC | PTC Inc. | $112.55 | 10.41 | 7% | $184.47 | +64% |  |
| 169 | ZTO | ZTO Express (Cayman) Inc. | $21.8 | 1.68 | 11% | $35.63 | +64% |  |
| 170 | VIV | Telefonica Brasil S.A. | $13.37 | 0.76 | 18% | $21.78 | +63% |  |
| 171 | PKX | POSCO Holdings Inc. | $52.17 | 1.84 | 30% | $84.84 | +63% |  |
| 172 | USB | U.S. Bancorp | $61.21 | 4.77 | 11% | $99.14 | +62% |  |
| 173 | MTB | M&T Bank Corporation | $236.77 | 17.81 | 12% | $382.7 | +62% |  |
| 174 | WPM | Wheaton Precious Metals Co | $113.08 | 3.96 | 30% | $182.59 | +62% |  |
| 175 | PDD | PDD Holdings Inc. | $73.3 | 9.5 | 0% | $117.98 | +61% |  |
| 176 | BNS | Bank Nova Scotia Halifax P | $86.46 | 5.1 | 17% | $138.5 | +60% |  |
| 177 | WTW | Willis Towers Watson Publi | $257.69 | 17.03 | 14% | $410.42 | +59% |  |
| 178 | RJF | Raymond James Financial, I | $150.52 | 10.6 | 13% | $239.65 | +59% |  |
| 179 | WTFC | Wintrust Financial Corpora | $161.88 | 11.93 | 12% | $256.58 | +58% |  |
| 180 | INTU | Intuit Inc. | $255.07 | 16.4 | 15% | $403.44 | +58% |  |
| 181 | CEG | Constellation Energy Corpo | $268.69 | 11.5 | 24% | $424.1 | +58% |  |
| 182 | GEN | Gen Digital Inc. | $23.31 | 1.57 | 14% | $36.74 | +58% |  |
| 183 | BMO | Bank Of Montreal | $174.8 | 9.16 | 19% | $274.2 | +57% |  |
| 184 | BSAC | Banco Santander - Chile | $31.99 | 2.33 | 12% | $50.09 | +57% |  |
| 185 | PYPL | PayPal Holdings, Inc. | $42.38 | 5.33 | 0% | $66.19 | +56% |  |
| 186 | LDOS | Leidos Holdings, Inc. | $100.0 | 10.93 | 3% | $156.21 | +56% |  |
| 187 | SCCO | Southern Copper Corporatio | $174.73 | 5.91 | 30% | $272.5 | +56% |  |
| 188 | FNV | Franco-Nevada Corporation | $210.0 | 7.1 | 30% | $327.37 | +56% |  |
| 189 | HST | Host Hotels & Resorts, Inc | $24.98 | 1.47 | 16% | $38.64 | +55% |  |
| 190 | NVDA | NVIDIA Corporation | $195.74 | 6.54 | 30% | $301.55 | +54% |  |
| 191 | EIX | Edison International | $74.75 | 9.2 | 0% | $114.25 | +53% |  |
| 192 | BNY | The Bank of New York Mello | $145.43 | 8.06 | 17% | $221.42 | +52% |  |
| 193 | BP | BP p.l.c. | $37.72 | 1.24 | 30% | $57.17 | +52% |  |
| 194 | BBVA | Banco Bilbao Vizcaya Argen | $24.53 | 2.07 | 8% | $37.16 | +52% |  |
| 195 | ICE | Intercontinental Exchange  | $124.49 | 6.87 | 17% | $188.01 | +51% |  |
| 196 | GMED | Globus Medical, Inc. | $84.65 | 4.28 | 19% | $127.75 | +51% |  |
| 197 | BRX | Brixmor Property Group Inc | $32.09 | 1.43 | 22% | $48.43 | +51% |  |
| 198 | BEN | Franklin Resources, Inc. | $32.65 | 1.31 | 25% | $48.92 | +50% |  |
| 199 | AGNC | AGNC Investment Corp. | $10.62 | 1.28 | 0% | $15.9 | +50% |  |
| 200 | PCG | Pacific Gas & Electric Co. | $17.08 | 1.29 | 10% | $25.55 | +50% |  |
| 201 | PFG | Principal Financial Group  | $105.44 | 6.97 | 13% | $157.3 | +49% |  |
| 202 | SEIC | SEI Investments Company | $87.93 | 5.86 | 12% | $131.02 | +49% |  |
| 203 | HBAN | Huntington Bancshares Inco | $17.9 | 1.3 | 11% | $26.66 | +49% |  |
| 204 | YUMC | Yum China Holdings, Inc. | $40.18 | 2.61 | 13% | $59.72 | +49% |  |
| 205 | GL | Globe Life Inc. | $176.4 | 14.45 | 8% | $260.75 | +48% |  |
| 206 | HCA | HCA Healthcare, Inc. | $386.94 | 29.02 | 10% | $570.18 | +47% |  |
| 207 | BR | Broadridge Financial Solut | $136.26 | 9.35 | 12% | $200.91 | +47% |  |
| 208 | WMG | Warner Music Group Corp. | $26.29 | 0.84 | 30% | $38.73 | +47% |  |
| 209 | HPQ | HP Inc. | $22.92 | 2.7 | 0% | $33.53 | +46% |  |
| 210 | WCC | WESCO International, Inc. | $357.53 | 14.05 | 24% | $522.74 | +46% |  |
| 211 | TRU | TransUnion | $67.0 | 3.61 | 17% | $97.41 | +45% |  |
| 212 | HTHT | H World Group Limited | $41.39 | 2.33 | 16% | $60.12 | +45% |  |
| 213 | GEV | GE Vernova Inc. | $1085.47 | 34.19 | 30% | $1576.46 | +45% |  |
| 214 | TRV | The Travelers Companies, I | $318.29 | 33.52 | 2% | $460.49 | +45% |  |
| 215 | EXPE | Expedia Group, Inc. | $250.95 | 11.32 | 21% | $360.72 | +44% |  |
| 216 | JPM | JP Morgan Chase & Co. | $335.12 | 20.88 | 13% | $481.13 | +44% |  |
| 217 | GIS | General Mills, Inc. | $35.4 | 4.09 | 0% | $50.79 | +44% |  |
| 218 | VZ | Verizon Communications Inc | $46.07 | 4.1 | 5% | $65.67 | +42% |  |
| 219 | TRGP | Targa Resources, Inc. | $273.45 | 9.79 | 26% | $388.1 | +42% |  |
| 220 | BEKE | KE Holdings Inc | $14.3 | 0.44 | 30% | $20.29 | +42% |  |
| 221 | DELL | Dell Technologies Inc. | $409.45 | 12.57 | 30% | $579.59 | +42% |  |
| 222 | EXEL | Exelixis, Inc. | $53.23 | 3.02 | 15% | $75.3 | +42% |  |
| 223 | ZTS | Zoetis Inc. | $77.82 | 6.1 | 8% | $109.16 | +40% |  |
| 224 | HSY | The Hershey Company | $176.68 | 5.37 | 30% | $247.6 | +40% |  |
| 225 | BXP | BXP, Inc. | $65.67 | 1.99 | 30% | $91.76 | +40% |  |
| 226 | FCX | Freeport-McMoRan, Inc. | $62.8 | 1.89 | 30% | $87.15 | +39% |  |
| 227 | NTES | NetEase, Inc. | $114.82 | 7.79 | 10% | $158.51 | +38% |  |
| 228 | WSE | Wise Group plc | $11.06 | 0.49 | 20% | $15.17 | +37% |  |
| 229 | LULU | lululemon athletica inc. | $112.06 | 12.35 | 0% | $153.37 | +37% |  |
| 230 | EPD | Enterprise Products Partne | $36.84 | 2.7 | 8% | $49.86 | +35% |  |
| 231 | MET | MetLife, Inc. | $84.63 | 5.17 | 12% | $114.26 | +35% |  |
| 232 | FNF | Fidelity National Financia | $46.11 | 2.81 | 12% | $62.05 | +35% |  |
| 233 | NXPI | NXP Semiconductors N.V. | $298.64 | 10.45 | 25% | $401.61 | +34% |  |
| 234 | MPLX | MPLX LP | $56.07 | 4.62 | 6% | $75.41 | +34% |  |
| 235 | GS | Goldman Sachs Group, Inc.  | $1065.09 | 54.75 | 16% | $1426.2 | +34% |  |
| 236 | MS | Morgan Stanley | $221.04 | 11.03 | 17% | $295.85 | +34% |  |
| 237 | AFL | AFLAC Incorporated | $118.23 | 8.75 | 8% | $158.19 | +34% |  |
| 238 | TIMB | TIM S.A. | $21.92 | 1.72 | 6% | $29.28 | +34% |  |
| 239 | HSBC | HSBC Holdings, plc. | $95.06 | 6.05 | 11% | $126.83 | +33% |  |
| 240 | LUV | Southwest Airlines Company | $52.09 | 1.5 | 30% | $69.16 | +33% |  |
| 241 | INFY | Infosys Limited | $10.57 | 0.8 | 7% | $14.01 | +32% |  |
| 242 | GSK | GSK plc | $51.89 | 3.75 | 8% | $68.58 | +32% |  |
| 243 | CRM | Salesforce, Inc. | $150.19 | 8.64 | 13% | $196.38 | +31% |  |
| 244 | PLD | Prologis, Inc. | $140.53 | 3.98 | 30% | $183.51 | +31% |  |
| 245 | MRK | Merck & Company, Inc. | $125.45 | 3.55 | 30% | $163.69 | +30% |  |
| 246 | CHKP | Check Point Software Techn | $122.84 | 9.72 | 6% | $160.02 | +30% |  |
| 247 | UI | Ubiquiti Inc. | $541.1 | 15.53 | 30% | $702.4 | +30% |  |
| 248 | RCL | Royal Caribbean Cruises Lt | $322.65 | 16.39 | 16% | $418.37 | +30% |  |
| 249 | AIZ | Assurant, Inc. | $260.77 | 19.51 | 7% | $336.18 | +29% |  |
| 250 | PODD | Insulet Corporation | $153.82 | 4.28 | 30% | $197.35 | +28% |  |
| 251 | BALL | Ball Corporation | $61.37 | 3.43 | 13% | $78.65 | +28% |  |
| 252 | BBY | Best Buy Co., Inc. | $76.89 | 5.4 | 8% | $98.4 | +28% |  |
| 253 | NMR | Nomura Holdings Inc | $8.79 | 0.74 | 4% | $11.23 | +28% |  |
| 254 | ORCL | Oracle Corporation | $152.46 | 5.82 | 22% | $194.54 | +28% |  |
| 255 | FICO | Fair Isaac Corporation | $1143.48 | 31.56 | 30% | $1455.19 | +27% |  |
| 256 | LVS | Las Vegas Sands Corp. | $46.28 | 2.71 | 12% | $58.55 | +26% |  |
| 257 | DIS | Walt Disney Company (The) | $98.05 | 6.25 | 10% | $123.81 | +26% |  |
| 258 | AON | Aon plc | $315.95 | 18.23 | 12% | $398.97 | +26% |  |
| 259 | HII | Huntington Ingalls Industr | $279.09 | 15.38 | 13% | $352.36 | +26% |  |
| 260 | FTI | TechnipFMC plc | $67.03 | 2.61 | 21% | $84.59 | +26% |  |
| 261 | NGG | National Grid Transco, PLC | $83.42 | 4.32 | 14% | $105.12 | +26% |  |
| 262 | EMBJ | Embraer S.A. | $62.8 | 1.71 | 30% | $78.85 | +26% |  |
| 263 | ALSN | Allison Transmission Holdi | $124.52 | 6.43 | 14% | $155.57 | +25% |  |
| 264 | WRB | W.R. Berkley Corporation | $69.29 | 4.72 | 8% | $85.85 | +24% |  |
| 265 | AMT | American Tower Corporation | $168.72 | 6.19 | 22% | $208.87 | +24% |  |
| 266 | DXCM | DexCom, Inc. | $68.65 | 2.33 | 24% | $85.0 | +24% |  |
| 267 | TSM | Taiwan Semiconductor Manuf | $434.99 | 11.61 | 30% | $535.32 | +23% |  |
| 268 | IBN | ICICI Bank Limited | $29.14 | 1.57 | 13% | $35.86 | +23% |  |
| 269 | MFC | Manulife Financial Corpora | $40.18 | 2.44 | 10% | $49.47 | +23% |  |
| 270 | SPOT | Spotify Technology S.A. | $441.21 | 14.65 | 24% | $537.88 | +22% |  |
| 271 | SPG | Simon Property Group, Inc. | $225.49 | 14.39 | 9% | $274.83 | +22% |  |
| 272 | ZM | Zoom Communications, Inc. | $82.88 | 6.79 | 4% | $100.83 | +22% |  |
| 273 | BUD | Anheuser-Busch Inbev SA Sp | $84.08 | 3.61 | 18% | $102.17 | +22% |  |
| 274 | FITB | Fifth Third Bancorp | $56.41 | 2.97 | 13% | $68.41 | +21% |  |
| 275 | ULTA | Ulta Beauty, Inc. | $485.52 | 26.7 | 12% | $589.05 | +21% |  |
| 276 | TXT | Textron Inc. | $89.06 | 5.24 | 11% | $107.69 | +21% |  |
| 277 | STT | State Street Corporation | $169.51 | 9.85 | 11% | $204.82 | +21% |  |
| 278 | VALE | VALE S.A. | $15.12 | 0.66 | 17% | $18.22 | +20% |  |
| 279 | EC | Ecopetrol S.A. | $14.45 | 1.4 | 0% | $17.39 | +20% |  |
| 280 | BKNG | Booking Holdings Inc. Comm | $177.05 | 7.58 | 18% | $212.54 | +20% |  |
| 281 | FOXA | Fox Corporation | $48.86 | 3.8 | 4% | $58.64 | +20% |  |
| 282 | SOFI | SoFi Technologies, Inc. | $17.3 | 0.45 | 30% | $20.75 | +20% |  |
| 283 | TOST | Toast, Inc. | $25.77 | 0.67 | 30% | $30.89 | +20% |  |
| 284 | TW | Tradeweb Markets Inc. | $91.5 | 4.05 | 17% | $109.42 | +20% |  |
| 285 | APP | Applovin Corporation | $445.93 | 11.5 | 30% | $530.25 | +19% |  |
| 286 | ABEV | Ambev S.A. | $3.14 | 0.19 | 10% | $3.73 | +19% |  |
| 287 | MCK | McKesson Corporation | $763.81 | 38.34 | 14% | $905.93 | +19% |  |
| 288 | EHC | Encompass Health Corporati | $99.72 | 5.84 | 10% | $118.13 | +18% |  |
| 289 | CNA | CNA Financial Corporation | $46.94 | 4.47 | 0% | $55.51 | +18% |  |
| 290 | ONON | On Holding AG | $36.58 | 0.93 | 30% | $42.88 | +17% |  |
| 291 | ARGX | argenx SE | $888.65 | 22.48 | 30% | $1036.52 | +17% |  |
| 292 | DECK | Deckers Outdoor Corporatio | $102.59 | 7.02 | 6% | $119.5 | +16% |  |
| 293 | BNT | Brookfield Wealth Solution | $42.97 | 2.74 | 8% | $50.0 | +16% |  |
| 294 | AXP | American Express Company | $342.46 | 16.03 | 15% | $397.79 | +16% |  |
| 295 | PCAR | PACCAR Inc. | $121.68 | 4.7 | 19% | $141.4 | +16% |  |
| 296 | VIK | Viking Holdings Ltd | $102.9 | 2.69 | 29% | $119.52 | +16% |  |
| 297 | ADSK | Autodesk, Inc. | $189.73 | 6.85 | 21% | $220.18 | +16% |  |
| 298 | NOC | Northrop Grumman Corporati | $499.33 | 31.91 | 8% | $578.49 | +16% |  |
| 299 | CART | Maplebear Inc. | $46.8 | 1.8 | 19% | $54.22 | +16% |  |
| 300 | LNG | Cheniere Energy, Inc. | $235.1 | 5.9 | 30% | $272.04 | +16% |  |
| 301 | GIL | Gildan Activewear, Inc. | $53.48 | 1.71 | 24% | $61.78 | +16% |  |
| 302 | CDW | CDW Corporation | $128.02 | 8.21 | 8% | $147.74 | +15% |  |
| 303 | PAC | Grupo Aeroportuario Del Pa | $252.21 | 11.3 | 16% | $290.95 | +15% |  |
| 304 | LLY | Eli Lilly and Company | $1127.69 | 28.19 | 30% | $1299.81 | +15% |  |
| 305 | BTI | British American Tobacco   | $62.48 | 4.61 | 5% | $71.87 | +15% |  |
| 306 | TROW | T. Rowe Price Group, Inc. | $106.34 | 9.32 | 1% | $122.25 | +15% |  |
| 307 | FUTU | Futu Holdings Limited | $98.12 | 9.05 | 0% | $112.39 | +14% |  |
| 308 | META | Meta Platforms, Inc. | $542.87 | 27.52 | 13% | $619.7 | +14% |  |
| 309 | TS | Tenaris S.A. | $57.36 | 3.8 | 7% | $65.48 | +14% |  |
| 310 | WDC | Western Digital Corporatio | $675.39 | 16.68 | 30% | $769.09 | +14% |  |
| 311 | OKE | ONEOK, Inc. | $89.52 | 5.61 | 8% | $101.75 | +14% |  |
| 312 | OTIS | Otis Worldwide Corporation | $73.63 | 3.76 | 12% | $83.66 | +14% |  |
| 313 | RY | Royal Bank Of Canada | $203.73 | 10.82 | 12% | $231.15 | +14% |  |
| 314 | DG | Dollar General Corporation | $117.56 | 7.07 | 9% | $133.49 | +14% |  |
| 315 | PGR | Progressive Corporation (T | $215.54 | 19.66 | 0% | $244.15 | +13% |  |
| 316 | CACI | CACI International, Inc. | $443.26 | 24.2 | 11% | $501.41 | +13% |  |
| 317 | RYAAY | Ryanair Holdings plc | $64.17 | 4.65 | 5% | $72.51 | +13% |  |
| 318 | IESC | IES Holdings, Inc. | $766.54 | 18.78 | 30% | $865.92 | +13% |  |
| 319 | BSBR | Banco Santander Brasil SA | $5.16 | 0.32 | 8% | $5.83 | +13% |  |
| 320 | PRU | Prudential Financial, Inc. | $107.03 | 9.71 | 0% | $120.58 | +13% |  |
| 321 | MKL | Markel Group Inc. | $1883.38 | 138.24 | 4% | $2118.96 | +12% |  |
| 322 | EFX | Equifax, Inc. | $151.93 | 5.68 | 19% | $170.89 | +12% |  |
| 323 | ARCC | Ares Capital Corporation | $17.99 | 1.63 | 0% | $20.24 | +12% |  |
| 324 | KKR | KKR & Co. Inc. | $92.65 | 2.94 | 23% | $103.77 | +12% |  |
| 325 | BMRN | BioMarin Pharmaceutical In | $57.35 | 1.39 | 30% | $64.09 | +12% |  |
| 326 | BSX | Boston Scientific Corporat | $44.2 | 2.39 | 11% | $49.16 | +11% |  |
| 327 | KMI | Kinder Morgan, Inc. | $33.01 | 1.49 | 14% | $36.27 | +10% |  |
| 328 | NVO | Novo Nordisk A/S | $47.64 | 4.17 | 0% | $52.12 | +9% |  |
| 329 | SAP | SAP  SE | $148.06 | 7.11 | 13% | $160.89 | +9% |  |
| 330 | ES | Eversource Energy (D/B/A) | $72.08 | 4.67 | 6% | $78.09 | +8% |  |
| 331 | GEHC | GE HealthCare Technologies | $64.94 | 4.17 | 6% | $69.99 | +8% |  |
| 332 | UNM | Unum Group | $88.92 | 4.62 | 11% | $95.77 | +8% |  |
| 333 | ATO | Atmos Energy Corporation | $173.67 | 8.13 | 13% | $186.02 | +7% |  |
| 334 | RMD | ResMed Inc. | $198.6 | 10.37 | 10% | $212.16 | +7% |  |
| 335 | FOX | Fox Corporation | $44.39 | 3.8 | 0% | $47.19 | +6% |  |
| 336 | DLTR | Dollar Tree, Inc. | $118.21 | 6.23 | 10% | $125.39 | +6% |  |
| 337 | PAA | Plains All American Pipeli | $21.62 | 1.11 | 11% | $22.92 | +6% |  |
| 338 | HPE | Hewlett Packard Enterprise | $46.72 | 1.07 | 30% | $49.34 | +6% |  |
| 339 | CNQ | Canadian Natural Resources | $39.6 | 3.36 | 0% | $41.73 | +5% |  |
| 340 | RELX | RELX PLC PLC | $30.92 | 1.48 | 12% | $32.56 | +5% |  |
| 341 | CLS | Celestica, Inc. | $361.4 | 8.24 | 30% | $379.94 | +5% |  |
| 342 | DVN | Devon Energy Corporation | $42.6 | 3.59 | 0% | $44.58 | +5% |  |
| 343 | TD | Toronto Dominion Bank (The | $120.49 | 6.0 | 11% | $125.67 | +4% |  |
| 344 | HLN | Haleon plc | $9.27 | 0.49 | 10% | $9.61 | +4% |  |
| 345 | TPR | Tapestry, Inc. | $146.0 | 3.28 | 30% | $151.24 | +4% |  |
| 346 | JCI | Johnson Controls Internati | $145.49 | 3.27 | 30% | $150.6 | +4% |  |
| 347 | R | Ryder System, Inc. | $267.92 | 12.03 | 13% | $277.32 | +4% |  |
| 348 | UMC | United Microelectronics Co | $27.73 | 0.62 | 30% | $28.59 | +3% |  |
| 349 | MO | Altria Group, Inc. | $73.21 | 4.79 | 5% | $75.27 | +3% |  |
| 350 | AMZN | Amazon.com, Inc. | $227.01 | 7.17 | 21% | $233.15 | +3% |  |
| 351 | SE | Sea Limited | $89.01 | 2.54 | 24% | $91.43 | +3% |  |
| 352 | CME | CME Group Inc. | $225.0 | 11.72 | 10% | $230.17 | +2% |  |
| 353 | LPLA | LPL Financial Holdings Inc | $277.33 | 11.12 | 16% | $283.6 | +2% |  |
| 354 | WIT | Wipro Limited | $2.19 | 0.13 | 7% | $2.23 | +2% |  |
| 355 | MAS | Masco Corporation | $79.72 | 4.04 | 10% | $81.35 | +2% |  |
| 356 | CSX | CSX Corporation | $47.44 | 1.63 | 19% | $48.35 | +2% |  |
| 357 | RDDT | Reddit, Inc. | $158.02 | 3.49 | 30% | $160.92 | +2% |  |
| 358 | ADP | Automatic Data Processing, | $216.31 | 10.73 | 10% | $219.52 | +2% |  |
| 359 | REGN | Regeneron Pharmaceuticals, | $620.14 | 40.93 | 4% | $629.49 | +2% |  |
| 360 | CBRE | CBRE Group Inc | $134.58 | 4.37 | 20% | $136.39 | +1% |  |
| 361 | AEG | Aegon Ltd. New York Regist | $8.36 | 0.68 | 0% | $8.44 | +1% |  |
| 362 | TOL | Toll Brothers, Inc. | $162.08 | 13.16 | 0% | $163.43 | +1% |  |
| 363 | PEG | Public Service Enterprise  | $82.63 | 4.52 | 8% | $82.78 | +0% |  |
| 364 | WY | Weyerhaeuser Company | $25.76 | 0.56 | 30% | $25.82 | +0% |  |
| 365 | GPN | Global Payments Inc. | $68.16 | 2.72 | 15% | $68.06 | -0% |  |
| 366 | SGI | Somnigroup International I | $78.59 | 2.5 | 20% | $78.29 | -0% |  |
| 367 | BLK | BlackRock, Inc. | $971.92 | 39.75 | 14% | $963.44 | -1% |  |
| 368 | HDB | HDFC Bank Limited | $25.37 | 1.41 | 8% | $25.14 | -1% |  |
| 369 | NDAQ | Nasdaq, Inc. | $77.65 | 3.32 | 13% | $76.91 | -1% |  |
| 370 | PNR | Pentair plc. | $76.0 | 3.98 | 9% | $75.04 | -1% |  |
| 371 | SNN | Smith & Nephew SNATS, Inc. | $30.22 | 1.43 | 11% | $29.79 | -1% |  |
| 372 | AZN | AstraZeneca PLC | $185.68 | 6.65 | 17% | $182.53 | -2% |  |
| 373 | PAG | Penske Automotive Group, I | $183.84 | 13.83 | 1% | $180.33 | -2% |  |
| 374 | DY | Dycom Industries, Inc. | $493.61 | 10.46 | 30% | $482.3 | -2% |  |
| 375 | ALLE | Allegion plc | $137.0 | 7.32 | 8% | $132.83 | -3% |  |
| 376 | CCL | Carnival Corporation Ltd. | $28.46 | 2.22 | 0% | $27.57 | -3% |  |
| 377 | COR | Cencora, Inc. | $286.95 | 13.06 | 11% | $277.88 | -3% |  |
| 378 | SSNC | SS&C Technologies Holdings | $63.02 | 3.22 | 9% | $60.74 | -4% |  |
| 379 | CCEP | Coca-Cola Europacific Part | $99.6 | 4.85 | 10% | $94.95 | -5% |  |
| 380 | ROP | Roper Technologies, Inc. | $332.42 | 16.02 | 10% | $316.05 | -5% |  |
| 381 | NWSA | News Corporation | $25.03 | 0.79 | 19% | $23.78 | -5% |  |
| 382 | PHM | PulteGroup, Inc. | $135.81 | 10.34 | 0% | $128.41 | -6% |  |
| 383 | FN | Fabrinet | $567.79 | 11.64 | 30% | $536.71 | -6% |  |
| 384 | AMRZ | Amrize Ltd | $55.88 | 2.09 | 15% | $52.74 | -6% |  |
| 385 | ED | Consolidated Edison, Inc. | $110.76 | 5.93 | 7% | $104.5 | -6% |  |
| 386 | AMKR | Amkor Technology, Inc. | $85.62 | 1.74 | 30% | $80.23 | -6% |  |
| 387 | VMI | Valmont Industries, Inc. | $583.55 | 17.97 | 20% | $546.55 | -6% |  |
| 388 | TGT | Target Corporation | $139.57 | 7.56 | 7% | $130.57 | -6% |  |
| 389 | TRMB | Trimble Inc. | $50.24 | 1.91 | 15% | $46.92 | -7% |  |
| 390 | ROST | Ross Stores, Inc. | $215.13 | 7.16 | 18% | $200.42 | -7% |  |
| 391 | PAYX | Paychex, Inc. | $96.72 | 4.89 | 8% | $90.01 | -7% |  |
| 392 | PHG | Koninklijke Philips N.V. N | $27.29 | 1.14 | 12% | $25.4 | -7% |  |
| 393 | STZ | Constellation Brands, Inc. | $144.45 | 9.61 | 2% | $134.5 | -7% |  |
| 394 | DRI | Darden Restaurants, Inc. | $212.76 | 10.45 | 9% | $198.12 | -7% |  |
| 395 | TSCO | Tractor Supply Company | $30.75 | 2.03 | 2% | $28.56 | -7% |  |
| 396 | SPGI | S&P Global Inc. | $395.14 | 15.81 | 13% | $366.72 | -7% |  |
| 397 | AM | Antero Midstream Corporati | $22.69 | 0.86 | 14% | $21.04 | -7% |  |
| 398 | WDS | Woodside Energy Group Limi | $19.06 | 1.42 | 0% | $17.63 | -8% |  |
| 399 | CRH | CRH PLC | $113.05 | 5.39 | 9% | $103.84 | -8% |  |
| 400 | SCI | Service Corporation Intern | $72.68 | 3.79 | 7% | $66.66 | -8% |  |
| 401 | MA | Mastercard Incorporated | $488.92 | 17.26 | 16% | $447.67 | -8% |  |
| 402 | MGA | Magna International, Inc. | $65.35 | 2.37 | 15% | $59.86 | -8% |  |
| 403 | CLX | Clorox Company (The) | $95.27 | 6.15 | 3% | $87.26 | -8% |  |
| 404 | JBL | Jabil Inc. | $374.64 | 7.42 | 30% | $342.13 | -9% |  |
| 405 | AA | Alcoa Corporation | $53.08 | 3.9 | 0% | $48.43 | -9% |  |
| 406 | BMY | Bristol-Myers Squibb Compa | $55.39 | 3.57 | 3% | $50.43 | -9% |  |
| 407 | EVRG | Evergy, Inc. | $86.66 | 3.76 | 11% | $78.79 | -9% |  |
| 408 | NYT | New York Times Company (Th | $68.57 | 2.33 | 16% | $62.07 | -10% |  |
| 409 | TRI | Thomson Reuters Corp | $81.01 | 3.48 | 11% | $73.25 | -10% |  |
| 410 | RIO | Rio Tinto Plc | $95.11 | 6.09 | 3% | $85.86 | -10% |  |
| 411 | DLR | Digital Realty Trust, Inc. | $192.44 | 3.77 | 30% | $173.83 | -10% |  |
| 412 | EXPD | Expeditors International o | $161.67 | 6.19 | 14% | $145.94 | -10% |  |
| 413 | SNY | Sanofi | $41.8 | 2.25 | 6% | $37.71 | -10% |  |
| 414 | IQV | IQVIA Holdings, Inc. | $186.43 | 8.05 | 11% | $166.94 | -10% |  |
| 415 | AS | Amer Sports, Inc. | $34.12 | 0.8 | 25% | $30.51 | -11% |  |
| 416 | PR | Permian Resources Corporat | $18.86 | 0.89 | 9% | $16.79 | -11% |  |
| 417 | DUK | Duke Energy Corporation (H | $127.11 | 6.5 | 7% | $112.84 | -11% |  |
| 418 | ABNB | Airbnb, Inc. | $141.88 | 4.04 | 20% | $125.94 | -11% |  |
| 419 | KVUE | Kenvue Inc. | $18.96 | 0.84 | 10% | $16.84 | -11% |  |
| 420 | FERG | Ferguson Enterprises Inc. | $240.76 | 10.16 | 11% | $213.09 | -12% |  |
| 421 | CQP | Cheniere Energy Partners,  | $60.05 | 4.28 | 0% | $53.15 | -12% |  |
| 422 | AEE | Ameren Corporation | $114.53 | 5.55 | 8% | $101.08 | -12% |  |
| 423 | GD | General Dynamics Corporati | $344.7 | 15.89 | 9% | $304.03 | -12% |  |
| 424 | COIN | Coinbase Global, Inc. | $142.52 | 2.72 | 30% | $125.42 | -12% |  |
| 425 | L | Loews Corporation | $110.9 | 7.86 | 0% | $97.61 | -12% |  |
| 426 | JBHT | J.B. Hunt Transport Servic | $274.68 | 6.43 | 25% | $240.58 | -12% |  |
| 427 | ARMK | Aramark | $54.78 | 1.34 | 24% | $47.83 | -13% |  |
| 428 | PPG | PPG Industries, Inc. | $122.4 | 6.98 | 4% | $106.48 | -13% |  |
| 429 | DCI | Donaldson Company, Inc. | $89.11 | 3.71 | 11% | $77.53 | -13% |  |
| 430 | CCK | Crown Holdings, Inc. | $110.01 | 6.29 | 4% | $95.45 | -13% |  |
| 431 | TXN | Texas Instruments Incorpor | $311.81 | 5.86 | 30% | $270.2 | -13% |  |
| 432 | BG | Bunge Limited | $111.55 | 3.8 | 15% | $96.7 | -13% |  |
| 433 | WPC | W. P. Carey Inc. REIT | $73.35 | 2.34 | 17% | $63.63 | -13% |  |
| 434 | YUM | Yum! Brands, Inc. | $151.14 | 6.2 | 11% | $130.74 | -14% |  |
| 435 | ERIC | Ericsson | $11.06 | 0.77 | 0% | $9.56 | -14% |  |
| 436 | AVY | Avery Dennison Corporation | $164.61 | 8.87 | 5% | $142.0 | -14% |  |
| 437 | FTAI | FTAI Aviation Ltd. | $268.4 | 5.02 | 30% | $231.47 | -14% |  |
| 438 | CG | The Carlyle Group Inc. | $41.9 | 1.46 | 15% | $36.06 | -14% |  |
| 439 | VLTO | Veralto Corp | $87.99 | 3.88 | 10% | $75.68 | -14% |  |
| 440 | NEE | NextEra Energy, Inc. | $87.7 | 3.94 | 9% | $75.35 | -14% |  |
| 441 | SANM | Sanmina Corporation | $253.56 | 4.72 | 30% | $217.63 | -14% |  |
| 442 | WYNN | Wynn Resorts, Limited | $99.38 | 3.49 | 14% | $85.18 | -14% |  |
| 443 | AZO | AutoZone, Inc. | $3059.04 | 145.3 | 8% | $2614.63 | -14% |  |
| 444 | V | Visa Inc. | $330.52 | 11.47 | 15% | $281.43 | -15% |  |
| 445 | NTAP | NetApp, Inc. | $154.59 | 6.35 | 11% | $131.63 | -15% |  |
| 446 | DGX | Quest Diagnostics Incorpor | $206.24 | 9.05 | 9% | $175.55 | -15% |  |
| 447 | KDP | Keurig Dr Pepper Inc. | $32.52 | 1.35 | 10% | $27.53 | -15% |  |
| 448 | TKR | Timken Company (The) | $144.01 | 4.41 | 17% | $122.03 | -15% |  |
| 449 | AEP | American Electric Power Co | $137.0 | 6.75 | 7% | $115.93 | -15% |  |
| 450 | QSR | Restaurant Brands Internat | $73.23 | 3.11 | 10% | $61.95 | -15% |  |
| 451 | CAT | Caterpillar, Inc. | $1057.01 | 20.08 | 29% | $893.56 | -16% |  |
| 452 | MRSH | Marsh | $162.23 | 8.0 | 7% | $137.08 | -16% |  |
| 453 | SN | SharkNinja, Inc. | $142.85 | 4.96 | 14% | $120.69 | -16% |  |
| 454 | EXC | Exelon Corporation | $46.75 | 2.73 | 3% | $39.47 | -16% |  |
| 455 | LEN | Lennar Corporation | $93.86 | 6.38 | 0% | $79.23 | -16% |  |
| 456 | TMUS | T-Mobile US, Inc. | $181.57 | 9.41 | 6% | $152.58 | -16% |  |
| 457 | CMS | CMS Energy Corporation | $77.1 | 3.62 | 8% | $64.78 | -16% |  |
| 458 | NWS | News Corporation | $28.34 | 0.79 | 19% | $23.78 | -16% |  |
| 459 | DKS | Dick's Sporting Goods Inc | $237.29 | 10.27 | 9% | $198.95 | -16% |  |
| 460 | UNP | Union Pacific Corporation | $267.73 | 12.15 | 8% | $223.76 | -16% |  |
| 461 | USFD | US Foods Holding Corp. | $96.22 | 2.97 | 17% | $80.48 | -16% |  |
| 462 | MDT | Medtronic plc. | $80.52 | 3.73 | 8% | $67.25 | -16% |  |
| 463 | GRMN | Garmin Ltd. | $235.41 | 8.97 | 12% | $195.61 | -17% |  |
| 464 | AAPL | Apple Inc. | $275.15 | 8.25 | 17% | $228.0 | -17% |  |
| 465 | LH | Labcorp Holdings Inc. | $266.34 | 11.29 | 10% | $220.31 | -17% |  |
| 466 | CHRW | C.H. Robinson Worldwide, I | $180.34 | 4.94 | 19% | $149.0 | -17% |  |
| 467 | SAIA | Saia, Inc. | $433.69 | 9.54 | 25% | $358.09 | -17% |  |
| 468 | SLF | Sun Life Financial Inc. | $77.5 | 3.78 | 6% | $63.89 | -18% |  |
| 469 | BRO | Brown & Brown, Inc. | $60.83 | 3.07 | 6% | $49.99 | -18% |  |
| 470 | PNW | Pinnacle West Capital Corp | $107.28 | 5.36 | 6% | $87.95 | -18% |  |
| 471 | EBAY | eBay Inc. | $108.0 | 4.33 | 10% | $87.87 | -19% |  |
| 472 | AAL | American Airlines Group, I | $17.57 | 0.31 | 30% | $14.29 | -19% |  |
| 473 | MUFG | Mitsubishi UFJ Financial G | $20.02 | 1.31 | 0% | $16.27 | -19% |  |
| 474 | BURL | Burlington Stores, Inc. | $324.48 | 9.73 | 17% | $263.22 | -19% |  |
| 475 | TLK | PT Telekomunikasi Indonesi | $14.19 | 0.92 | 0% | $11.42 | -20% |  |
| 476 | TFII | TFI International Inc. | $145.79 | 3.59 | 21% | $117.32 | -20% |  |
| 477 | CSL | Carlisle Companies Incorpo | $388.4 | 17.13 | 8% | $311.84 | -20% |  |
| 478 | SMFG | Sumitomo Mitsui Financial  | $23.7 | 1.53 | 0% | $19.0 | -20% |  |
| 479 | IBM | International Business Mac | $258.27 | 11.31 | 8% | $206.75 | -20% |  |
| 480 | EME | EMCOR Group, Inc. | $862.66 | 29.76 | 13% | $688.48 | -20% |  |
| 481 | XYZ | Block, Inc. | $74.08 | 1.28 | 30% | $59.02 | -20% |  |
| 482 | IX | ORIX Corporation | $38.48 | 2.47 | 0% | $30.67 | -20% |  |
| 483 | AYI | Acuity Inc. | $359.39 | 15.06 | 9% | $286.31 | -20% |  |
| 484 | MCD | McDonald's Corporation | $264.54 | 12.14 | 7% | $210.46 | -20% |  |
| 485 | ET | Energy Transfer LP | $19.18 | 1.2 | 0% | $15.25 | -20% |  |
| 486 | PPL | PPL Corporation | $37.0 | 1.63 | 8% | $29.43 | -20% |  |
| 487 | WDAY | Workday, Inc. | $113.77 | 3.21 | 18% | $90.39 | -21% |  |
| 488 | FIX | Comfort Systems USA, Inc. | $2017.57 | 34.7 | 30% | $1599.97 | -21% |  |
| 489 | KEYS | Keysight Technologies Inc. | $360.06 | 6.19 | 30% | $285.41 | -21% |  |
| 490 | DHI | D.R. Horton, Inc. | $166.95 | 10.65 | 0% | $132.26 | -21% |  |
| 491 | BCH | Banco De Chile | $38.82 | 2.43 | 0% | $30.68 | -21% |  |
| 492 | ERIE | Erie Indemnity Company | $229.96 | 10.91 | 6% | $180.88 | -21% |  |
| 493 | MSCI | MSCI Inc. | $544.56 | 17.53 | 14% | $428.24 | -21% |  |
| 494 | AWK | American Water Works Compa | $130.0 | 5.64 | 8% | $102.1 | -22% |  |
| 495 | XEL | Xcel Energy Inc. | $81.75 | 3.47 | 8% | $63.93 | -22% |  |
| 496 | AVB | AvalonBay Communities, Inc | $186.13 | 8.08 | 8% | $145.53 | -22% |  |
| 497 | VEEV | Veeva Systems Inc. | $158.08 | 5.64 | 12% | $122.77 | -22% |  |
| 498 | NI | NiSource Inc | $47.81 | 2.01 | 8% | $37.03 | -22% |  |
| 499 | VRTX | Vertex Pharmaceuticals Inc | $480.18 | 16.85 | 12% | $371.25 | -23% |  |
| 500 | CP | Canadian Pacific Kansas Ci | $87.04 | 3.15 | 11% | $67.08 | -23% |  |

### 🔴 BEARISH — 500 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | D | Dominion Energy, Inc. | $69.51 | 3.39 | 5% | $53.58 | -23% |  |
| 2 | APH | Amphenol Corporation | $165.15 | 3.48 | 24% | $127.21 | -23% |  |
| 3 | RL | Ralph Lauren Corporation | $410.11 | 15.09 | 11% | $315.77 | -23% |  |
| 4 | PEP | Pepsico, Inc. | $139.52 | 6.38 | 6% | $107.23 | -23% |  |
| 5 | ITT | ITT Inc. | $200.08 | 5.66 | 17% | $153.51 | -23% |  |
| 6 | SNA | Snap-On Incorporated | $400.95 | 19.37 | 5% | $306.56 | -24% |  |
| 7 | ETR | Entergy Corporation | $115.38 | 3.92 | 12% | $87.88 | -24% |  |
| 8 | ELV | Elevance Health, Inc. | $387.32 | 23.59 | 0% | $292.95 | -24% |  |
| 9 | KO | Coca-Cola Company (The) | $80.42 | 3.18 | 9% | $60.51 | -25% |  |
| 10 | URI | United Rentals, Inc. | $1139.51 | 39.09 | 12% | $857.42 | -25% |  |
| 11 | WEC | WEC Energy Group, Inc. | $117.07 | 4.99 | 7% | $87.97 | -25% |  |
| 12 | IFF | International Flavors & Fr | $75.08 | 3.23 | 7% | $56.42 | -25% |  |
| 13 | UL | Unilever PLC | $60.54 | 2.95 | 4% | $45.38 | -25% |  |
| 14 | AJG | Arthur J. Gallagher & Co. | $217.86 | 6.19 | 16% | $162.85 | -25% |  |
| 15 | NVR | NVR, Inc. | $6814.44 | 409.55 | 0% | $5085.97 | -25% |  |
| 16 | CPRT | Copart, Inc. | $30.05 | 1.61 | 2% | $22.4 | -26% |  |
| 17 | BAM | Brookfield Asset Managemen | $44.66 | 1.56 | 11% | $33.22 | -26% |  |
| 18 | VMC | Vulcan Materials Company ( | $312.97 | 8.45 | 17% | $232.73 | -26% |  |
| 19 | STE | STERIS plc (Ireland) | $210.6 | 7.94 | 10% | $156.72 | -26% |  |
| 20 | ADI | Analog Devices, Inc. | $417.93 | 6.73 | 30% | $310.31 | -26% |  |
| 21 | ORLY | O'Reilly Automotive, Inc. | $86.9 | 3.07 | 11% | $64.47 | -26% |  |
| 22 | ONC | BeOne Medicines Ltd. | $275.34 | 4.43 | 30% | $204.26 | -26% |  |
| 23 | SUNB | Sunbelt Rentals Holdings,  | $75.18 | 3.15 | 7% | $55.61 | -26% |  |
| 24 | PM | Philip Morris Internationa | $178.93 | 7.1 | 8% | $132.15 | -26% |  |
| 25 | BIP | Brookfield Infrastructure  | $36.39 | 0.66 | 27% | $26.82 | -26% |  |
| 26 | AVGO | Broadcom Inc. | $378.91 | 6.02 | 30% | $277.57 | -27% |  |
| 27 | AMAT | Applied Materials, Inc. | $668.0 | 10.62 | 30% | $489.67 | -27% |  |
| 28 | LMT | Lockheed Martin Corporatio | $505.02 | 20.66 | 8% | $370.05 | -27% |  |
| 29 | CRS | Carpenter Technology Corpo | $599.24 | 9.53 | 30% | $439.42 | -27% |  |
| 30 | ZBRA | Zebra Technologies Corpora | $243.39 | 8.28 | 12% | $178.48 | -27% |  |
| 31 | PSX | Phillips 66 | $171.76 | 10.12 | 0% | $125.67 | -27% |  |
| 32 | VRSN | VeriSign, Inc. | $250.85 | 9.06 | 10% | $183.68 | -27% |  |
| 33 | ARES | Ares Management Corporatio | $112.47 | 2.17 | 25% | $82.14 | -27% |  |
| 34 | LECO | Lincoln Electric Holdings, | $273.72 | 9.69 | 11% | $199.68 | -27% |  |
| 35 | HWM | Howmet Aerospace Inc. | $273.14 | 4.32 | 30% | $199.19 | -27% |  |
| 36 | ITW | Illinois Tool Works Inc. | $270.6 | 10.77 | 8% | $197.16 | -27% |  |
| 37 | ADM | Archer-Daniels-Midland Com | $76.54 | 2.24 | 15% | $55.8 | -27% |  |
| 38 | LOW | Lowe's Companies, Inc. | $221.93 | 11.83 | 2% | $160.38 | -28% |  |
| 39 | OGE | OGE Energy Corp | $48.95 | 2.25 | 5% | $35.15 | -28% |  |
| 40 | UNH | UnitedHealth Group Incorpo | $415.53 | 13.3 | 12% | $297.24 | -28% |  |
| 41 | ROK | Rockwell Automation, Inc. | $479.39 | 9.64 | 23% | $342.96 | -28% |  |
| 42 | J | Jacobs Solutions Inc. | $124.39 | 3.4 | 16% | $88.76 | -29% |  |
| 43 | SIMO | Silicon Motion Technology  | $325.26 | 5.04 | 30% | $232.39 | -29% |  |
| 44 | BJ | BJ's Wholesale Club Holdin | $86.31 | 4.35 | 3% | $61.6 | -29% |  |
| 45 | GM | General Motors Company | $78.53 | 2.74 | 10% | $55.85 | -29% |  |
| 46 | WTRG | Essential Utilities, Inc. | $37.93 | 1.96 | 2% | $26.95 | -29% |  |
| 47 | TMO | Thermo Fisher Scientific I | $505.75 | 18.21 | 10% | $358.28 | -29% |  |
| 48 | FDX | FedEx Corporation | $329.44 | 18.75 | 0% | $232.85 | -29% |  |
| 49 | ZBH | Zimmer Biomet Holdings, In | $90.96 | 3.86 | 6% | $64.27 | -29% |  |
| 50 | MLM | Martin Marietta Materials, | $628.94 | 15.98 | 18% | $444.27 | -29% |  |
| 51 | LNT | Alliant Energy Corporation | $76.19 | 3.18 | 6% | $53.83 | -29% |  |
| 52 | ASX | ASE Technology Holding Co. | $41.85 | 0.64 | 30% | $29.51 | -30% |  |
| 53 | A | Agilent Technologies, Inc. | $135.51 | 4.99 | 9% | $95.52 | -30% |  |
| 54 | PINS | Pinterest, Inc. | $19.48 | 0.48 | 18% | $13.73 | -30% |  |
| 55 | UPS | United Parcel Service, Inc | $109.31 | 6.18 | 0% | $76.75 | -30% |  |
| 56 | WM | Waste Management, Inc. | $223.08 | 6.92 | 13% | $156.31 | -30% |  |
| 57 | HUBB | Hubbell Inc | $536.04 | 16.94 | 12% | $373.23 | -30% |  |
| 58 | IHG | Intercontinental Hotels Gr | $174.13 | 4.86 | 15% | $121.18 | -30% |  |
| 59 | AGX | Argan, Inc. | $753.07 | 11.37 | 30% | $524.26 | -30% |  |
| 60 | CMI | Cummins Inc. | $727.59 | 19.28 | 16% | $505.92 | -30% |  |
| 61 | DOC | Healthpeak Properties, Inc | $21.23 | 0.32 | 30% | $14.75 | -30% |  |
| 62 | XYL | Xylem Inc. | $117.0 | 4.02 | 10% | $81.06 | -31% |  |
| 63 | FE | FirstEnergy Corp. | $48.01 | 1.84 | 8% | $33.26 | -31% |  |
| 64 | CPT | Camden Property Trust | $113.59 | 3.58 | 12% | $78.7 | -31% |  |
| 65 | GWW | W.W. Grainger, Inc. | $1374.78 | 37.26 | 15% | $949.03 | -31% |  |
| 66 | COP | ConocoPhillips | $106.41 | 5.9 | 0% | $73.27 | -31% |  |
| 67 | LOGI | Logitech International S.A | $100.85 | 4.8 | 3% | $69.44 | -31% |  |
| 68 | CNP | CenterPoint Energy, Inc (H | $44.22 | 1.63 | 8% | $30.41 | -31% |  |
| 69 | PFE | Pfizer, Inc. | $23.67 | 1.31 | 0% | $16.27 | -31% |  |
| 70 | WMB | Williams Companies, Inc. ( | $77.53 | 2.28 | 13% | $53.19 | -31% |  |
| 71 | MDLZ | Mondelez International, In | $61.2 | 2.02 | 11% | $42.0 | -31% |  |
| 72 | RPRX | Royalty Pharma plc | $54.69 | 1.9 | 10% | $37.48 | -32% |  |
| 73 | KRYS | Krystal Biotech, Inc. | $359.93 | 7.49 | 22% | $246.58 | -32% |  |
| 74 | RPM | RPM International Inc. | $111.7 | 5.19 | 3% | $76.25 | -32% |  |
| 75 | ASML | ASML Holding N.V. - New Yo | $1841.18 | 29.46 | 28% | $1256.55 | -32% |  |
| 76 | SO | Southern Company (The) | $95.91 | 3.91 | 6% | $65.41 | -32% |  |
| 77 | SONY | Sony Group Corporation | $19.32 | 1.06 | 0% | $13.16 | -32% |  |
| 78 | MCO | Moody's Corporation | $438.85 | 13.96 | 11% | $297.03 | -32% |  |
| 79 | TJX | TJX Companies, Inc. (The) | $155.19 | 5.14 | 10% | $104.68 | -32% |  |
| 80 | WWD | Woodward, Inc. | $436.44 | 8.34 | 23% | $291.58 | -33% |  |
| 81 | OXY | Occidental Petroleum Corpo | $51.21 | 0.74 | 30% | $34.12 | -33% |  |
| 82 | FLEX | Flex Ltd. | $161.28 | 2.32 | 30% | $106.97 | -34% |  |
| 83 | SWK | Stanley Black & Decker, In | $92.31 | 2.44 | 15% | $61.24 | -34% |  |
| 84 | WTS | Watts Water Technologies,  | $375.09 | 10.92 | 13% | $248.75 | -34% |  |
| 85 | MEDP | Medpace Holdings, Inc. | $519.96 | 15.91 | 12% | $344.02 | -34% |  |
| 86 | AFRM | Affirm Holdings, Inc. | $76.85 | 1.1 | 30% | $50.72 | -34% |  |
| 87 | MTD | Mettler-Toledo Internation | $1243.42 | 42.52 | 9% | $819.17 | -34% |  |
| 88 | XPO | XPO, Inc. | $203.02 | 2.9 | 30% | $133.72 | -34% |  |
| 89 | TXRH | Texas Roadhouse, Inc. | $190.61 | 6.27 | 10% | $125.4 | -34% |  |
| 90 | PG | Procter & Gamble Company ( | $148.5 | 6.85 | 3% | $97.47 | -34% |  |
| 91 | DOV | Dover Corporation | $230.73 | 8.01 | 9% | $151.44 | -34% |  |
| 92 | KIM | Kimco Realty Corporation ( | $25.52 | 0.87 | 9% | $16.69 | -35% |  |
| 93 | SBAC | SBA Communications Corpora | $180.95 | 9.5 | 0% | $117.98 | -35% |  |
| 94 | ABT | Abbott Laboratories | $93.24 | 3.57 | 6% | $60.66 | -35% |  |
| 95 | DEO | Diageo plc | $82.61 | 4.33 | 0% | $53.77 | -35% |  |
| 96 | MTZ | MasTec, Inc. | $403.57 | 5.69 | 30% | $262.36 | -35% |  |
| 97 | VRSK | Verisk Analytics, Inc. | $177.04 | 6.57 | 7% | $114.81 | -35% |  |
| 98 | NXT | Nextpower Inc. | $113.18 | 3.84 | 9% | $73.0 | -36% |  |
| 99 | ALGN | Align Technology, Inc. | $175.71 | 5.96 | 9% | $113.36 | -36% |  |
| 100 | CNI | Canadian National Railway  | $120.36 | 5.34 | 3% | $77.55 | -36% |  |
| 101 | APD | Air Products and Chemicals | $279.93 | 9.49 | 9% | $179.59 | -36% |  |
| 102 | DTM | DT Midstream, Inc. | $149.75 | 4.51 | 11% | $96.04 | -36% |  |
| 103 | GGG | Graco Inc. | $75.94 | 3.06 | 5% | $48.68 | -36% |  |
| 104 | SYY | Sysco Corporation | $80.85 | 3.6 | 3% | $51.4 | -36% |  |
| 105 | FDXF | FedEx Freight Holding Comp | $158.53 | 4.55 | 12% | $100.61 | -36% |  |
| 106 | CX | Cemex, S.A.B. de C.V. Spon | $12.38 | 0.35 | 12% | $7.82 | -37% |  |
| 107 | E | ENI S.p.A. | $46.79 | 2.26 | 1% | $29.5 | -37% |  |
| 108 | ALNY | Alnylam Pharmaceuticals, I | $293.17 | 3.99 | 30% | $183.97 | -37% |  |
| 109 | AMGN | Amgen Inc. | $352.82 | 14.36 | 4% | $221.17 | -37% |  |
| 110 | TDY | Teledyne Technologies Inco | $627.19 | 19.76 | 10% | $393.05 | -37% |  |
| 111 | WSM | Williams-Sonoma, Inc. | $240.06 | 8.93 | 6% | $150.09 | -38% |  |
| 112 | IBKR | Interactive Brokers Group, | $92.16 | 2.33 | 15% | $57.52 | -38% |  |
| 113 | TT | Trane Technologies plc | $503.46 | 13.09 | 14% | $314.09 | -38% |  |
| 114 | DTE | DTE Energy Company | $152.81 | 6.08 | 5% | $95.36 | -38% |  |
| 115 | LII | Lennox International, Inc. | $570.73 | 22.49 | 5% | $356.11 | -38% |  |
| 116 | GMAB | Genmab A/S | $26.14 | 1.31 | 0% | $16.27 | -38% |  |
| 117 | ATI | ATI Inc. | $199.5 | 3.03 | 27% | $123.83 | -38% |  |
| 118 | JNJ | Johnson & Johnson | $244.88 | 8.62 | 7% | $151.62 | -38% |  |
| 119 | OHI | Omega Healthcare Investors | $47.62 | 2.07 | 3% | $29.48 | -38% |  |
| 120 | UTHR | United Therapeutics Corpor | $543.39 | 27.06 | 0% | $336.04 | -38% |  |
| 121 | WST | West Pharmaceutical Servic | $346.56 | 7.49 | 18% | $213.79 | -38% |  |
| 122 | LHX | L3Harris Technologies, Inc | $288.52 | 9.2 | 9% | $176.43 | -39% |  |
| 123 | QCOM | QUALCOMM Incorporated | $204.9 | 9.3 | 2% | $125.09 | -39% |  |
| 124 | WAB | Westinghouse Air Brake Tec | $282.45 | 7.06 | 14% | $172.47 | -39% |  |
| 125 | ANET | Arista Networks, Inc. | $165.45 | 2.91 | 23% | $100.91 | -39% |  |
| 126 | TKO | TKO Group Holdings, Inc. | $203.8 | 2.69 | 30% | $124.03 | -39% |  |
| 127 | KMB | Kimberly-Clark Corporation | $108.1 | 5.17 | 0% | $65.79 | -39% |  |
| 128 | LRCX | Lam Research Corporation | $401.82 | 5.3 | 30% | $244.38 | -39% |  |
| 129 | TYL | Tyler Technologies, Inc. | $281.09 | 7.25 | 14% | $170.18 | -40% |  |
| 130 | SRE | DBA Sempra | $93.43 | 2.94 | 9% | $56.25 | -40% |  |
| 131 | MSI | Motorola Solutions, Inc. | $397.01 | 12.39 | 9% | $238.15 | -40% |  |
| 132 | EMR | Emerson Electric Company | $145.34 | 4.32 | 10% | $87.11 | -40% |  |
| 133 | HBANP | Huntington Bancshares Inco | $16.15 | 0.778 | 0% | $9.66 | -40% |  |
| 134 | CAH | Cardinal Health, Inc. | $234.75 | 6.55 | 11% | $139.61 | -40% |  |
| 135 | SLB | SLB Limited | $47.42 | 2.27 | 0% | $28.19 | -41% |  |
| 136 | HEI | Heico Corporation | $342.45 | 5.62 | 24% | $203.04 | -41% |  |
| 137 | NVT | nVent Electric plc | $171.91 | 2.94 | 23% | $101.54 | -41% |  |
| 138 | AEIS | Advanced Energy Industries | $375.15 | 4.8 | 30% | $221.32 | -41% |  |
| 139 | CGNX | Cognex Corporation | $66.54 | 0.85 | 30% | $39.19 | -41% |  |
| 140 | SYK | Stryker Corporation | $316.11 | 8.63 | 12% | $185.61 | -41% |  |
| 141 | STRL | Sterling Infrastructure, I | $881.92 | 11.2 | 30% | $516.42 | -41% |  |
| 142 | CTAS | Cintas Corporation | $169.09 | 4.73 | 11% | $98.71 | -42% |  |
| 143 | BX | Blackstone Inc. | $114.18 | 3.9 | 7% | $66.61 | -42% |  |
| 144 | RSG | Republic Services, Inc. | $213.5 | 6.96 | 8% | $124.08 | -42% |  |
| 145 | CCI | Crown Castle Inc. | $79.53 | 2.37 | 9% | $45.95 | -42% |  |
| 146 | SNDK | Sandisk Corporation | $2335.0 | 29.19 | 30% | $1345.91 | -42% |  |
| 147 | FRT | Federal Realty Investment  | $124.55 | 5.77 | 0% | $71.65 | -42% |  |
| 148 | SLMBP | SLM Corporation - Floating | $74.79 | 2.145 | 10% | $42.9 | -43% |  |
| 149 | LIN | Linde plc | $522.28 | 15.09 | 10% | $299.2 | -43% |  |
| 150 | ESLT | Elbit Systems Ltd. | $732.71 | 12.38 | 22% | $419.62 | -43% |  |
| 151 | MAR | Marriott International | $378.91 | 9.55 | 13% | $216.67 | -43% |  |
| 152 | NDSN | Nordson Corporation | $304.64 | 9.36 | 8% | $174.22 | -43% |  |
| 153 | FAST | Fastenal Company | $46.92 | 1.13 | 14% | $26.78 | -43% |  |
| 154 | LAMR | Lamar Advertising Company | $154.36 | 5.42 | 6% | $88.05 | -43% |  |
| 155 | RTX | RTX Corporation | $186.59 | 5.34 | 10% | $106.22 | -43% |  |
| 156 | CVNA | Carvana Co. | $66.2 | 1.73 | 12% | $37.69 | -43% |  |
| 157 | ILMN | Illumina, Inc. | $177.65 | 5.51 | 8% | $100.77 | -43% |  |
| 158 | WMT | Walmart Inc. | $115.78 | 2.84 | 13% | $65.12 | -44% |  |
| 159 | VRT | Vertiv Holdings, LLC | $325.57 | 3.97 | 30% | $183.05 | -44% |  |
| 160 | MMM | 3M Company | $167.97 | 5.19 | 8% | $94.35 | -44% |  |
| 161 | BWA | BorgWarner Inc. | $69.47 | 1.72 | 13% | $38.97 | -44% |  |
| 162 | NVS | Novartis AG | $155.12 | 6.98 | 0% | $86.68 | -44% |  |
| 163 | IDXX | IDEXX Laboratories, Inc. | $554.94 | 13.6 | 13% | $310.21 | -44% |  |
| 164 | ALC | Alcon Inc. | $68.13 | 1.67 | 13% | $38.11 | -44% |  |
| 165 | CSCO | Cisco Systems, Inc. | $118.97 | 3.0 | 12% | $66.42 | -44% |  |
| 166 | O | Realty Income Corporation | $62.04 | 1.22 | 18% | $34.51 | -44% |  |
| 167 | FTS | Fortis Inc. | $57.76 | 2.39 | 2% | $32.1 | -44% |  |
| 168 | IEX | IDEX Corporation | $228.07 | 6.75 | 9% | $126.92 | -44% |  |
| 169 | NTNX | Nutanix, Inc. | $46.94 | 0.95 | 17% | $26.09 | -44% |  |
| 170 | EGP | EastGroup Properties, Inc. | $204.69 | 5.51 | 11% | $113.65 | -44% |  |
| 171 | HD | Home Depot, Inc. (The) | $345.0 | 14.08 | 2% | $191.26 | -45% |  |
| 172 | ECL | Ecolab Inc. | $281.2 | 7.4 | 11% | $155.9 | -45% |  |
| 173 | PKG | Packaging Corporation of A | $241.09 | 8.22 | 6% | $133.67 | -45% |  |
| 174 | ISRG | Intuitive Surgical, Inc. | $399.69 | 8.23 | 17% | $221.03 | -45% |  |
| 175 | PEN | Penumbra, Inc. | $317.4 | 4.35 | 27% | $175.47 | -45% |  |
| 176 | DRS | Leonardo DRS, Inc. | $44.36 | 1.07 | 13% | $24.54 | -45% |  |
| 177 | BN | Brookfield Corporation | $43.0 | 0.51 | 30% | $23.52 | -45% |  |
| 178 | SHW | Sherwin-Williams Company ( | $339.08 | 10.41 | 8% | $185.59 | -45% |  |
| 179 | MNST | Monster Beverage Corporati | $95.83 | 2.07 | 15% | $52.02 | -46% |  |
| 180 | GE | GE Aerospace | $371.36 | 8.06 | 15% | $200.36 | -46% |  |
| 181 | AME | AMETEK, Inc. | $240.95 | 6.63 | 10% | $129.91 | -46% |  |
| 182 | ROL | Rollins, Inc. | $42.8 | 1.09 | 11% | $23.0 | -46% |  |
| 183 | XOM | Exxon Mobil Corporation | $137.55 | 5.94 | 0% | $73.77 | -46% |  |
| 184 | EMA | Emera Incorporated | $53.26 | 2.3 | 0% | $28.56 | -46% |  |
| 185 | BA | Boeing Company (The) | $218.12 | 2.53 | 30% | $116.66 | -46% |  |
| 186 | MKSI | MKS Inc. | $410.31 | 4.76 | 30% | $219.48 | -46% |  |
| 187 | TPL | Texas Pacific Land Corpora | $391.04 | 7.27 | 18% | $209.18 | -46% |  |
| 188 | RACE | Ferrari N.V. | $352.2 | 10.21 | 8% | $187.6 | -47% |  |
| 189 | GRAB | Grab Holdings Limited | $3.46 | 0.04 | 30% | $1.84 | -47% |  |
| 190 | ON | ON Semiconductor Corporati | $118.74 | 1.37 | 30% | $63.17 | -47% |  |
| 191 | CR | Crane Company | $223.59 | 5.46 | 12% | $118.59 | -47% |  |
| 192 | KR | Kroger Company (The) | $57.77 | 1.71 | 8% | $30.59 | -47% |  |
| 193 | RMBS | Rambus, Inc. | $123.69 | 2.1 | 20% | $65.33 | -47% |  |
| 194 | TER | Teradyne, Inc. | $471.96 | 5.38 | 30% | $248.07 | -47% |  |
| 195 | PBA | Pembina Pipeline Corp. | $47.14 | 1.87 | 1% | $24.74 | -48% |  |
| 196 | AMCR | Amcor plc | $42.86 | 1.24 | 8% | $22.46 | -48% |  |
| 197 | REG | Regency Centers Corporatio | $80.25 | 2.91 | 3% | $41.85 | -48% |  |
| 198 | PH | Parker-Hannifin Corporatio | $989.91 | 27.12 | 9% | $515.82 | -48% |  |
| 199 | NOW | ServiceNow, Inc. | $89.52 | 1.68 | 18% | $46.65 | -48% |  |
| 200 | CHD | Church & Dwight Company, I | $98.15 | 3.04 | 6% | $51.14 | -48% |  |
| 201 | PSA | Public Storage | $320.74 | 9.69 | 7% | $165.88 | -48% |  |
| 202 | BLD | TopBuild Corp. | $427.14 | 17.77 | 0% | $220.68 | -48% |  |
| 203 | TDG | Transdigm Group Incorporat | $1332.56 | 31.98 | 12% | $684.41 | -49% |  |
| 204 | BWXT | BWX Technologies, Inc. | $204.77 | 3.75 | 18% | $104.39 | -49% |  |
| 205 | SBUX | Starbucks Corporation | $103.16 | 1.31 | 26% | $52.55 | -49% |  |
| 206 | BTSG | BrightSpring Health Servic | $69.7 | 0.77 | 30% | $35.5 | -49% |  |
| 207 | CASY | Caseys General Stores, Inc | $784.71 | 19.16 | 11% | $398.42 | -49% |  |
| 208 | TRP | TC Energy Corporation | $70.19 | 2.39 | 4% | $35.56 | -49% |  |
| 209 | AIT | Applied Industrial Technol | $343.54 | 10.58 | 6% | $174.26 | -49% |  |
| 210 | DHR | Danaher Corporation | $193.21 | 5.16 | 9% | $97.6 | -50% |  |
| 211 | HRL | Hormel Foods Corporation | $26.02 | 0.85 | 4% | $13.15 | -50% |  |
| 212 | FWONA | Liberty Media Corporation  | $82.96 | 2.29 | 8% | $41.58 | -50% |  |
| 213 | CLH | Clean Harbors, Inc. | $299.39 | 7.39 | 10% | $149.49 | -50% |  |
| 214 | GNRC | Generac Holdlings Inc. | $295.16 | 3.19 | 30% | $147.09 | -50% |  |
| 215 | ETN | Eaton Corporation, PLC | $419.87 | 10.2 | 10% | $208.77 | -50% |  |
| 216 | CTVA | Corteva, Inc. | $81.62 | 1.85 | 12% | $40.58 | -50% |  |
| 217 | MICC | The Magnum Ice Cream Compa | $17.21 | 0.55 | 5% | $8.55 | -50% |  |
| 218 | ODFL | Old Dominion Freight Line, | $220.12 | 4.8 | 13% | $109.0 | -50% |  |
| 219 | AAON | AAON, Inc. | $133.26 | 1.43 | 30% | $65.94 | -50% |  |
| 220 | Q | Qnity Electronics, Inc. | $167.49 | 3.1 | 16% | $82.79 | -51% |  |
| 221 | WMS | Advanced Drainage Systems, | $155.26 | 5.45 | 2% | $76.69 | -51% |  |
| 222 | CVS | CVS Health Corporation | $104.66 | 2.28 | 13% | $51.64 | -51% |  |
| 223 | NVMI | Nova Ltd. | $534.24 | 7.96 | 22% | $263.14 | -51% |  |
| 224 | SPXC | SPX Technologies, Inc. | $244.56 | 5.23 | 13% | $120.03 | -51% |  |
| 225 | FTV | Fortive Corporation | $61.73 | 1.7 | 8% | $30.27 | -51% |  |
| 226 | HLT | Hilton Worldwide Holdings  | $340.55 | 6.54 | 15% | $165.78 | -51% |  |
| 227 | FER | Ferrovial N.V. | $70.2 | 1.42 | 14% | $34.15 | -51% |  |
| 228 | HON | Honeywell International In | $231.24 | 6.27 | 8% | $112.15 | -52% |  |
| 229 | FFIV | F5, Inc. | $386.01 | 12.16 | 4% | $186.48 | -52% |  |
| 230 | COST | Costco Wholesale Corporati | $942.24 | 19.88 | 13% | $452.85 | -52% |  |
| 231 | MRVL | Marvell Technology, Inc. | $281.26 | 2.9 | 30% | $133.72 | -52% |  |
| 232 | STX | Seagate Technology Holding | $1025.36 | 10.56 | 30% | $486.91 | -52% |  |
| 233 | TU | Telus Corporation | $11.08 | 0.42 | 0% | $5.24 | -53% |  |
| 234 | NSC | Norfolk Southern Corporati | $312.06 | 11.86 | 0% | $147.28 | -53% |  |
| 235 | BDX | Becton, Dickinson and Comp | $151.38 | 5.74 | 0% | $71.28 | -53% |  |
| 236 | HBANM | Huntington Bancshares Inco | $20.52 | 0.778 | 0% | $9.66 | -53% |  |
| 237 | TSN | Tyson Foods, Inc. | $57.8 | 1.27 | 11% | $27.05 | -53% |  |
| 238 | CCJ | Cameco Corporation | $103.58 | 1.05 | 30% | $48.41 | -53% |  |
| 239 | PWR | Quanta Services, Inc. | $718.59 | 7.26 | 30% | $334.75 | -53% |  |
| 240 | NBIS | Nebius Group N.V. | $256.63 | 2.59 | 30% | $119.42 | -54% |  |
| 241 | NKE | Nike, Inc. | $40.9 | 1.52 | 0% | $18.88 | -54% |  |
| 242 | EQR | Equity Residential | $67.17 | 2.5 | 0% | $31.05 | -54% |  |
| 243 | ROKU | Roku, Inc. | $134.73 | 1.35 | 30% | $62.25 | -54% |  |
| 244 | ULS | UL Solutions Inc. | $95.83 | 1.72 | 16% | $44.06 | -54% |  |
| 245 | AMH | American Homes 4 Rent | $33.29 | 1.23 | 0% | $15.27 | -54% |  |
| 246 | ENB | Enbridge Inc | $56.19 | 2.07 | 0% | $25.71 | -54% |  |
| 247 | WAT | Waters Corporation | $376.89 | 7.88 | 12% | $172.19 | -54% |  |
| 248 | CHT | Chunghwa Telecom Co., Ltd. | $44.79 | 1.58 | 1% | $20.46 | -54% |  |
| 249 | IMO | Imperial Oil Limited | $113.28 | 4.16 | 0% | $51.66 | -54% |  |
| 250 | ELS | Equity Lifestyle Propertie | $62.93 | 2.0 | 3% | $28.58 | -55% |  |
| 251 | ENTG | Entegris, Inc. | $176.28 | 1.73 | 30% | $79.77 | -55% |  |
| 252 | EW | Edwards Lifesciences Corpo | $89.72 | 1.85 | 12% | $40.45 | -55% |  |
| 253 | MPWR | Monolithic Power Systems,  | $1438.3 | 13.95 | 30% | $643.22 | -55% |  |
| 254 | CW | Curtiss-Wright Corporation | $767.73 | 13.67 | 15% | $341.0 | -56% |  |
| 255 | WSO | Watsco, Inc. | $412.19 | 12.2 | 4% | $182.12 | -56% |  |
| 256 | RDY | Dr. Reddy's Laboratories L | $15.25 | 0.54 | 0% | $6.71 | -56% |  |
| 257 | GFL | GFL Environmental Inc. Sub | $37.78 | 0.36 | 30% | $16.6 | -56% |  |
| 258 | CRDO | Credo Technology Group Hol | $268.03 | 2.52 | 30% | $116.19 | -57% |  |
| 259 | ESS | Essex Property Trust, Inc. | $285.57 | 8.88 | 2% | $122.77 | -57% |  |
| 260 | WELL | Welltower Inc. | $223.73 | 2.08 | 30% | $95.91 | -57% |  |
| 261 | WCN | Waste Connections, Inc. | $166.21 | 4.11 | 7% | $71.32 | -57% |  |
| 262 | SWKS | Skyworks Solutions, Inc. | $69.94 | 2.4 | 0% | $29.8 | -57% |  |
| 263 | GLW | Corning Incorporated | $228.01 | 2.07 | 30% | $95.45 | -58% |  |
| 264 | CMG | Chipotle Mexican Grill, In | $32.28 | 1.09 | 0% | $13.54 | -58% |  |
| 265 | FTNT | Fortinet, Inc. | $149.93 | 2.58 | 14% | $62.72 | -58% |  |
| 266 | VICR | Vicor Corporation | $331.59 | 2.99 | 30% | $137.87 | -58% |  |
| 267 | SOLS | Solstice Advanced Material | $86.91 | 1.18 | 20% | $36.15 | -58% |  |
| 268 | CVX | Chevron Corporation | $172.24 | 5.74 | 0% | $71.28 | -59% |  |
| 269 | CL | Colgate-Palmolive Company | $91.06 | 2.58 | 3% | $37.72 | -59% |  |
| 270 | GFS | GlobalFoundries Inc. | $86.12 | 1.69 | 11% | $35.62 | -59% |  |
| 271 | EQIX | Equinix, Inc. | $1087.61 | 14.47 | 20% | $447.14 | -59% |  |
| 272 | ASND | Ascendis Pharma A/S | $261.58 | 8.63 | 0% | $107.17 | -59% |  |
| 273 | RRX | Regal Rexnord Corporation | $227.18 | 4.29 | 12% | $92.22 | -59% |  |
| 274 | TTMI | TTM Technologies, Inc. | $210.57 | 1.83 | 30% | $84.38 | -60% |  |
| 275 | INVH | Invitation Homes Inc. | $29.91 | 0.95 | 0% | $11.8 | -61% |  |
| 276 | HONAV | Honeywell Aerospace Inc. C | $221.01 | 4.75 | 8% | $86.67 | -61% |  |
| 277 | SHOP | Shopify Inc. | $111.62 | 1.02 | 28% | $43.05 | -61% |  |
| 278 | EA | Electronic Arts Inc. | $204.73 | 3.5 | 13% | $78.85 | -62% |  |
| 279 | PLTR | Palantir Technologies Inc. | $107.27 | 0.89 | 30% | $41.04 | -62% |  |
| 280 | RBA | RB Global, Inc. | $115.5 | 2.15 | 11% | $44.17 | -62% |  |
| 281 | MDLN | Medline Inc. | $37.77 | 1.14 | 0% | $14.16 | -62% |  |
| 282 | EXR | Extra Space Storage Inc | $147.19 | 4.45 | 0% | $55.26 | -62% |  |
| 283 | TSEM | Tower Semiconductor Ltd. | $269.88 | 2.16 | 30% | $99.59 | -63% |  |
| 284 | MOD | Modine Manufacturing Compa | $283.67 | 2.27 | 30% | $104.67 | -63% |  |
| 285 | RBC | RBC Bearings Incorporated | $648.89 | 9.08 | 16% | $235.92 | -64% |  |
| 286 | CNH | CNH Industrial N.V. | $10.93 | 0.32 | 0% | $3.97 | -64% |  |
| 287 | CARR | Carrier Global Corporation | $76.0 | 1.5 | 8% | $27.48 | -64% |  |
| 288 | CRBG | Corebridge Financial Inc. | $28.14 | 0.4 | 15% | $10.01 | -64% |  |
| 289 | BROS | Dutch Bros Inc. | $66.6 | 0.64 | 24% | $23.35 | -65% |  |
| 290 | DE | Deere & Company | $630.76 | 17.66 | 0% | $219.31 | -65% |  |
| 291 | POWL | Powell Industries, Inc. | $309.2 | 5.14 | 11% | $107.03 | -65% |  |
| 292 | ESI | Element Solutions Inc. | $47.72 | 0.62 | 16% | $16.19 | -66% |  |
| 293 | SW | Smurfit WestRock plc | $46.84 | 0.72 | 12% | $15.76 | -66% |  |
| 294 | APTV | Aptiv PLC | $61.97 | 1.68 | 0% | $20.86 | -66% |  |
| 295 | COO | The Cooper Companies, Inc. | $70.64 | 1.18 | 10% | $23.76 | -66% |  |
| 296 | AHR | American Healthcare REIT,  | $50.92 | 0.59 | 18% | $17.13 | -66% |  |
| 297 | CDNS | Cadence Design Systems, In | $368.23 | 4.31 | 18% | $122.97 | -67% |  |
| 298 | NOK | Nokia Corporation Sponsore | $13.98 | 0.16 | 19% | $4.67 | -67% |  |
| 299 | MELI | MercadoLibre, Inc. | $1619.25 | 37.89 | 3% | $535.23 | -67% |  |
| 300 | DT | Dynatrace, Inc. | $40.28 | 0.54 | 14% | $13.23 | -67% |  |
| 301 | DD | DuPont de Nemours, Inc. | $137.8 | 1.14 | 26% | $44.96 | -67% |  |
| 302 | AKAM | Akamai Technologies, Inc. | $112.89 | 2.96 | 0% | $36.76 | -67% |  |
| 303 | P | Everpure, Inc. | $71.69 | 0.66 | 23% | $23.15 | -68% |  |
| 304 | FWONK | Liberty Media Corporation  | $90.45 | 2.29 | 0% | $28.44 | -69% |  |
| 305 | HOOD | Robinhood Markets, Inc. | $93.47 | 2.06 | 3% | $29.23 | -69% |  |
| 306 | HUM | Humana Inc. | $376.0 | 9.36 | 0% | $116.24 | -69% |  |
| 307 | IR | Ingersoll Rand Inc. | $81.7 | 1.48 | 6% | $25.18 | -69% |  |
| 308 | LITE | Lumentum Holdings Inc. | $861.97 | 5.69 | 30% | $262.36 | -70% |  |
| 309 | MAA | Mid-America Apartment Comm | $138.08 | 3.3 | 0% | $40.98 | -70% |  |
| 310 | OWL | Blue Owl Capital Inc. | $8.48 | 0.12 | 11% | $2.52 | -70% |  |
| 311 | APO | Apollo Global Management,  | $121.51 | 1.59 | 13% | $35.95 | -70% |  |
| 312 | KLAC | KLA Corporation | $258.8 | 3.52 | 12% | $76.35 | -70% |  |
| 313 | CIEN | Ciena Corporation | $484.69 | 3.01 | 30% | $138.79 | -71% |  |
| 314 | ONTO | Onto Innovation Inc. | $344.24 | 2.13 | 30% | $98.21 | -72% |  |
| 315 | MAIR | Madison Air Solutions Corp | $40.0 | 0.35 | 21% | $11.16 | -72% |  |
| 316 | MTSI | MACOM Technology Solutions | $390.19 | 2.34 | 30% | $107.89 | -72% |  |
| 317 | PFGC | Performance Food Group Com | $107.27 | 2.1 | 2% | $29.28 | -73% |  |
| 318 | RVTY | Revvity, Inc. | $113.53 | 2.08 | 4% | $30.96 | -73% |  |
| 319 | JHX | James Hardie Industries pl | $26.02 | 0.19 | 24% | $7.05 | -73% |  |
| 320 | FORM | FormFactor, Inc. | $148.75 | 0.86 | 30% | $39.65 | -73% |  |
| 321 | AMD | Advanced Micro Devices, In | $532.57 | 2.98 | 30% | $137.4 | -74% |  |
| 322 | AXON | Axon Enterprise, Inc. | $444.73 | 2.49 | 30% | $114.81 | -74% |  |
| 323 | OKTA | Okta, Inc. | $119.26 | 1.38 | 11% | $29.35 | -75% |  |
| 324 | DASH | DoorDash, Inc. | $176.91 | 2.11 | 10% | $42.62 | -76% |  |
| 325 | COHR | Coherent Corp. | $407.25 | 2.12 | 30% | $97.75 | -76% |  |
| 326 | SNPS | Synopsys, Inc. | $455.02 | 4.37 | 15% | $107.08 | -76% |  |
| 327 | SKM | SK Telecom Co., Ltd. | $33.55 | 0.59 | 0% | $7.33 | -78% |  |
| 328 | MOH | Molina Healthcare Inc | $216.04 | 3.74 | 0% | $46.44 | -78% |  |
| 329 | ENLT | Enlight Renewable Energy L | $88.41 | 0.41 | 30% | $18.9 | -79% |  |
| 330 | ABBV | AbbVie Inc. | $243.14 | 2.04 | 14% | $49.57 | -80% |  |
| 331 | COF | Capital One Financial Corp | $204.9 | 3.26 | 0% | $41.38 | -80% |  |
| 332 | IREN | IREN LIMITED | $47.74 | 0.77 | 0% | $9.56 | -80% |  |
| 333 | DOCN | DigitalOcean Holdings, Inc | $145.34 | 2.28 | 0% | $28.31 | -80% |  |
| 334 | MGM | MGM Resorts International | $47.2 | 0.73 | 0% | $9.07 | -81% |  |
| 335 | TPG | TPG Inc. | $40.02 | 0.23 | 22% | $7.6 | -81% |  |
| 336 | VTR | Ventas, Inc. | $87.43 | 0.55 | 19% | $16.01 | -82% |  |
| 337 | DKNG | DraftKings Inc. | $23.1 | 0.09 | 30% | $4.15 | -82% |  |
| 338 | ICLR | ICON plc | $160.96 | 2.27 | 0% | $28.19 | -82% |  |
| 339 | IRM | Iron Mountain Incorporated | $131.06 | 0.92 | 15% | $22.75 | -83% |  |
| 340 | TECH | Bio-Techne Corp | $70.7 | 0.7 | 7% | $12.16 | -83% |  |
| 341 | ALAB | Astera Labs, Inc. | $398.0 | 1.47 | 30% | $67.78 | -83% |  |
| 342 | IOT | Samsara Inc. | $28.98 | 0.1 | 26% | $4.01 | -86% |  |
| 343 | NRG | NRG Energy, Inc. | $147.11 | 0.91 | 12% | $20.08 | -86% |  |
| 344 | CBRS | Cerebras Systems Inc. | $168.52 | 0.46 | 30% | $21.21 | -87% |  |
| 345 | KNX | Knight-Swift Transportatio | $77.07 | 0.21 | 30% | $9.68 | -87% |  |
| 346 | CSGP | CoStar Group, Inc. | $28.64 | 0.07 | 30% | $3.23 | -89% |  |
| 347 | PSKY | Paramount Skydance Corpora | $9.43 | 0.03 | 23% | $1.05 | -89% |  |
| 348 | ARM | Arm Holdings plc | $347.71 | 0.83 | 30% | $38.27 | -89% |  |
| 349 | MCHP | Microchip Technology Incor | $94.12 | 0.22 | 30% | $10.14 | -89% |  |
| 350 | STM | STMicroelectronics N.V. | $74.88 | 0.16 | 30% | $7.38 | -90% |  |
| 351 | IONQ | IonQ, Inc. | $50.56 | 0.39 | 0% | $4.84 | -90% |  |
| 352 | TSLA | Tesla, Inc. | $375.12 | 1.09 | 21% | $35.68 | -90% |  |
| 353 | TWLO | Twilio Inc. | $190.88 | 0.67 | 17% | $18.09 | -90% |  |
| 354 | CAVA | CAVA Group, Inc. | $83.3 | 0.52 | 2% | $7.25 | -91% |  |
| 355 | PANW | Palo Alto Networks, Inc. | $293.09 | 1.14 | 11% | $23.89 | -92% |  |
| 356 | FANG | Diamondback Energy, Inc. | $182.55 | 0.99 | 0% | $12.29 | -93% |  |
| 357 | INIO | INNIO N.V. | $38.24 | 0.14 | 8% | $2.55 | -93% |  |
| 358 | GPC | Genuine Parts Company | $112.99 | 0.44 | 5% | $6.83 | -94% |  |
| 359 | DDOG | Datadog, Inc. | $220.94 | 0.4 | 18% | $11.42 | -95% |  |
| 360 | LSCC | Lattice Semiconductor Corp | $144.2 | 0.14 | 30% | $6.46 | -96% |  |
| 361 | JAZZ | Jazz Pharmaceuticals plc | $226.2 | 0.11 | 30% | $5.07 | -98% |  |
| 362 | ARXS | Arxis, Inc. | $44.24 | 0.02 | 24% | $0.72 | -98% |  |
| 363 | FPS | Forgent Power Solutions, I | $58.7 | 0.02 | 30% | $0.92 | -98% |  |
| 364 | SPCX | Space Exploration Technolo | $153.0 | -0.67 | — | — | no earnings | no_earnings |
| 365 | INTC | Intel Corporation | $132.87 | -0.6 | — | — | no earnings | no_earnings |
| 366 | GOOGM | Alphabet Inc. - Depositary | $48.95 | None | — | — | no earnings | no_earnings |
| 367 | GOOGN | Alphabet Inc. - Depositary | $48.86 | None | — | — | no earnings | no_earnings |
| 368 | CCZ | Comcast Holdings ZONES | $65.8 | None | — | — | no earnings | no_earnings |
| 369 | CRWD | CrowdStrike Holdings, Inc. | $678.65 | -0.14 | — | — | no earnings | no_earnings |
| 370 | TBB | AT&T Inc. 5.350% Global No | $20.47 | None | — | — | no earnings | no_earnings |
| 371 | BE | Bloom Energy Corporation | $309.18 | -0.03 | — | — | no earnings | no_earnings |
| 372 | NET | Cloudflare, Inc. | $226.65 | -0.25 | — | — | no earnings | no_earnings |
| 373 | SNOW | Snowflake Inc. | $227.06 | -3.52 | — | — | no earnings | no_earnings |
| 374 | BRKRP | Bruker Corporation - 6.375 | $449.45 | None | — | — | no earnings | no_earnings |
| 375 | WBD | Warner Bros. Discovery, In | $26.98 | -0.7 | — | — | no earnings | no_earnings |
| 376 | F | Ford Motor Company | $14.11 | -1.55 | — | — | no earnings | no_earnings |
| 377 | SOMN | Southern Company (The) 202 | $49.82 | None | — | — | no earnings | no_earnings |
| 378 | CRWV | CoreWeave, Inc. | $98.76 | -2.72 | — | — | no earnings | no_earnings |
| 379 | HBANL | Huntington Bancshares Inco | $25.18 | None | — | — | no earnings | no_earnings |
| 380 | RKLB | Rocket Lab Corporation | $80.69 | -0.32 | — | — | no earnings | no_earnings |
| 381 | BMNP | BitMine Immersion Technolo | $81.41 | None | — | — | no earnings | no_earnings |
| 382 | BTSGU | BrightSpring Health Servic | $230.13 | None | — | — | no earnings | no_earnings |
| 383 | TTWO | Take-Two Interactive Softw | $238.72 | -1.62 | — | — | no earnings | no_earnings |
| 384 | MCHPP | Microchip Technology Incor | $79.05 | None | — | — | no earnings | no_earnings |
| 385 | RKT | Rocket Companies, Inc. | $14.78 | -0.03 | — | — | no earnings | no_earnings |
| 386 | LYV | Live Nation Entertainment, | $175.11 | -1.77 | — | — | no earnings | no_earnings |
| 387 | HBANZ | Huntington Bancshares Inco | $19.9 | None | — | — | no earnings | no_earnings |
| 388 | HMC | Honda Motor Company, Ltd. | $26.14 | -1.97 | — | — | no earnings | no_earnings |
| 389 | RVMD | Revolution Medicines, Inc. | $178.17 | -7.11 | — | — | no earnings | no_earnings |
| 390 | NTRA | Natera, Inc. | $260.74 | -1.62 | — | — | no earnings | no_earnings |
| 391 | PPLC | PPL Corporation Corporate | $49.35 | None | — | — | no earnings | no_earnings |
| 392 | BIDU | Baidu, Inc. | $103.99 | -0.16 | — | — | no earnings | no_earnings |
| 393 | RBLX | Roblox Corporation | $46.39 | -1.57 | — | — | no earnings | no_earnings |
| 394 | SMCIP | Super Micro Computer, Inc. | $54.76 | None | — | — | no earnings | no_earnings |
| 395 | VOD | Vodafone Group Plc | $13.86 | -0.14 | — | — | no earnings | no_earnings |
| 396 | CNC | Centene Corporation | $64.77 | -13.05 | — | — | no earnings | no_earnings |
| 397 | STRF | Strategy Inc - 10.00% Seri | $88.33 | None | — | — | no earnings | no_earnings |
| 398 | CPNG | Coupang, Inc. | $17.06 | -0.1 | — | — | no earnings | no_earnings |
| 399 | MSTR | Strategy Inc | $85.33 | -36.99 | — | — | no earnings | no_earnings |
| 400 | EL | Estee Lauder Companies, In | $81.5 | -0.7 | — | — | no earnings | no_earnings |
| 401 | AGNCN | AGNC Investment Corp. - De | $25.66 | -1.86 | — | — | no earnings | no_earnings |
| 402 | AGNCO | AGNC Investment Corp. - De | $25.45 | -1.86 | — | — | no earnings | no_earnings |
| 403 | AGNCZ | AGNC Investment Corp. - De | $25.43 | None | — | — | no earnings | no_earnings |
| 404 | AGNCP | AGNC Investment Corp. - De | $25.04 | -1.86 | — | — | no earnings | no_earnings |
| 405 | AGNCM | AGNC Investment Corp. - De | $24.98 | -1.86 | — | — | no earnings | no_earnings |
| 406 | AGNCL | AGNC Investment Corp. - De | $24.93 | None | — | — | no earnings | no_earnings |
| 407 | ECHO |  | $97.19 | None | — | — | no earnings | no_earnings |
| 408 | KHC | The Kraft Heinz Company | $23.47 | -4.86 | — | — | no earnings | no_earnings |
| 409 | STRC | Strategy Inc - Variable Ra | $75.69 | None | — | — | no earnings | no_earnings |
| 410 | ASTS | AST SpaceMobile, Inc. | $65.62 | -1.8 | — | — | no earnings | no_earnings |
| 411 | FISV | Fiserv, Inc. | $47.53 | None | — | — | no earnings | no_earnings |
| 412 | SYM | Symbotic Inc. | $40.77 | -0.08 | — | — | no earnings | no_earnings |
| 413 | ROIV | Roivant Sciences Ltd. | $34.02 | -0.54 | — | — | no earnings | no_earnings |
| 414 | BEP | Brookfield Renewable Partn | $35.23 | -0.3 | — | — | no earnings | no_earnings |
| 415 | MRNA | Moderna, Inc. | $59.75 | -8.14 | — | — | no earnings | no_earnings |
| 416 | MDB | MongoDB, Inc. | $294.1 | -0.38 | — | — | no earnings | no_earnings |
| 417 | BNH | Brookfield Finance Inc. 4. | $15.23 | None | — | — | no earnings | no_earnings |
| 418 | INSM | Insmed Incorporated | $104.47 | -5.76 | — | — | no earnings | no_earnings |
| 419 | BNTX | BioNTech SE | $90.0 | -5.77 | — | — | no earnings | no_earnings |
| 420 | SOJC | Southern Company (The) Ser | $20.53 | None | — | — | no earnings | no_earnings |
| 421 | BNJ | Brookfield Finance Inc. 4. | $14.93 | None | — | — | no earnings | no_earnings |
| 422 | SOJD | Southern Company (The) Ser | $19.28 | None | — | — | no earnings | no_earnings |
| 423 | DOW | Dow Inc. | $29.31 | -4.0 | — | — | no earnings | no_earnings |
| 424 | OMC | Omnicom Group Inc. | $73.43 | -0.37 | — | — | no earnings | no_earnings |
| 425 | IP | International Paper Compan | $39.02 | -5.19 | — | — | no earnings | no_earnings |
| 426 | ZS | Zscaler, Inc. | $123.8 | -0.48 | — | — | no earnings | no_earnings |
| 427 | TLN | Talen Energy Corporation | $416.8 | -0.5 | — | — | no earnings | no_earnings |
| 428 | AQNB | Algonquin Power & Utilitie | $25.54 | None | — | — | no earnings | no_earnings |
| 429 | GH | Guardant Health, Inc. | $142.94 | -3.4 | — | — | no earnings | no_earnings |
| 430 | TEAM | Atlassian Corporation | $74.68 | -0.82 | — | — | no earnings | no_earnings |
| 431 | RIVN | Rivian Automotive, Inc. | $14.86 | -2.92 | — | — | no earnings | no_earnings |
| 432 | VTRS | Viatris Inc. | $16.07 | -0.3 | — | — | no earnings | no_earnings |
| 433 | QNT | Quantinuum Inc. | $71.68 | -1.76 | — | — | no earnings | no_earnings |
| 434 | BDRX | Biodexa Pharmaceuticals pl | $2.5 | -3.3 | — | — | no earnings | no_earnings |
| 435 | H | Hyatt Hotels Corporation | $197.01 | -0.33 | — | — | no earnings | no_earnings |
| 436 | BPYPM | Brookfield Property Partne | $15.9 | None | — | — | no earnings | no_earnings |
| 437 | SOJE | Southern Company (The) Ser | $16.87 | None | — | — | no earnings | no_earnings |
| 438 | DUKB | Duke Energy Corporation 5. | $23.4 | None | — | — | no earnings | no_earnings |
| 439 | STRK | Strategy Inc - 8.00% Serie | $51.72 | None | — | — | no earnings | no_earnings |
| 440 | APG | APi Group Corporation | $41.68 | -0.64 | — | — | no earnings | no_earnings |
| 441 | LYB | LyondellBasell Industries  | $55.84 | -2.12 | — | — | no earnings | no_earnings |
| 442 | YPF | YPF Sociedad Anonima | $45.76 | -1.04 | — | — | no earnings | no_earnings |
| 443 | SITM | SiTime Corporation | $675.7 | -0.88 | — | — | no earnings | no_earnings |
| 444 | STRD | Strategy Inc - 10.00% Seri | $50.0 | None | — | — | no earnings | no_earnings |
| 445 | CRCL | Circle Internet Group, Inc | $68.81 | -0.23 | — | — | no earnings | no_earnings |
| 446 | FLUT | Flutter Entertainment plc | $96.19 | -2.1 | — | — | no earnings | no_earnings |
| 447 | ALB | Albemarle Corporation | $141.05 | -3.41 | — | — | no earnings | no_earnings |
| 448 | STLA | Stellantis N.V. | $5.74 | -8.51 | — | — | no earnings | no_earnings |
| 449 | VNOM | Viper Energy, Inc. | $43.55 | -0.57 | — | — | no earnings | no_earnings |
| 450 | SMTC | Semtech Corporation | $162.27 | -0.41 | — | — | no earnings | no_earnings |
| 451 | RBRK | Rubrik, Inc. | $71.02 | -1.46 | — | — | no earnings | no_earnings |
| 452 | SUI | Sun Communities, Inc. | $118.58 | -0.49 | — | — | no earnings | no_earnings |
| 453 | KKRS | KKR Group Finance Co. IX L | $16.24 | None | — | — | no earnings | no_earnings |
| 454 | APOS | Apollo Global Management,  | $25.36 | None | — | — | no earnings | no_earnings |
| 455 | BEPC | Brookfield Renewable Corpo | $37.62 | -25.07 | — | — | no earnings | no_earnings |
| 456 | VLYPN | Valley National Bancorp -  | $25.45 | None | — | — | no earnings | no_earnings |
| 457 | BBIO | BridgeBio Pharma, Inc. | $69.69 | -3.74 | — | — | no earnings | no_earnings |
| 458 | KLAR | Klarna Group plc | $19.13 | -0.52 | — | — | no earnings | no_earnings |
| 459 | SREA | DBA Sempra 5.750% Junior S | $20.95 | None | — | — | no earnings | no_earnings |
| 460 | HUT | Hut 8 Corp. | $117.68 | -2.83 | — | — | no earnings | no_earnings |
| 461 | QXO | QXO, Inc. | $18.0 | -0.95 | — | — | no earnings | no_earnings |
| 462 | IONS | Ionis Pharmaceuticals, Inc | $78.34 | -2.01 | — | — | no earnings | no_earnings |
| 463 | WULF | TeraWulf Inc. | $26.06 | -2.51 | — | — | no earnings | no_earnings |
| 464 | LI | Li Auto Inc. | $11.83 | -0.27 | — | — | no earnings | no_earnings |
| 465 | W | Wayfair Inc. | $93.52 | -2.35 | — | — | no earnings | no_earnings |
| 466 | EQH | Equitable Holdings, Inc. | $43.84 | -2.85 | — | — | no earnings | no_earnings |
| 467 | AUR | Aurora Innovation, Inc. | $6.24 | -0.43 | — | — | no earnings | no_earnings |
| 468 | AXSM | Axsome Therapeutics, Inc. | $237.33 | -3.73 | — | — | no earnings | no_earnings |
| 469 | ELAN | Elanco Animal Health Incor | $24.37 | -0.5 | — | — | no earnings | no_earnings |
| 470 | LFUS | Littelfuse, Inc. | $477.22 | -1.67 | — | — | no earnings | no_earnings |
| 471 | HAS | Hasbro, Inc. | $84.88 | -1.61 | — | — | no earnings | no_earnings |
| 472 | SJM | The J.M. Smucker Company | $112.5 | -1.31 | — | — | no earnings | no_earnings |
| 473 | NIO | NIO Inc. | $4.73 | -0.55 | — | — | no earnings | no_earnings |
| 474 | PS | Pershing Square Inc. | $29.62 | -0.94 | — | — | no earnings | no_earnings |
| 475 | MDGL | Madrigal Pharmaceuticals,  | $513.79 | -13.51 | — | — | no earnings | no_earnings |
| 476 | VIAV | Viavi Solutions Inc. | $50.44 | -0.25 | — | — | no earnings | no_earnings |
| 477 | APLD | Applied Digital Corporatio | $40.95 | -0.38 | — | — | no earnings | no_earnings |
| 478 | U | Unity Software Inc. | $26.71 | -1.57 | — | — | no earnings | no_earnings |
| 479 | XPEV | XPeng Inc. | $12.19 | -0.35 | — | — | no earnings | no_earnings |
| 480 | IVZ | Invesco Ltd | $25.87 | -1.47 | — | — | no earnings | no_earnings |
| 481 | BIPJ | Brookfield Infrastructure  | $24.81 | None | — | — | no earnings | no_earnings |
| 482 | ALGM | Allegro MicroSystems, Inc. | $60.16 | -0.08 | — | — | no earnings | no_earnings |
| 483 | ARWR | Arrowhead Pharmaceuticals, | $79.27 | -2.27 | — | — | no earnings | no_earnings |
| 484 | BAX | Baxter International Inc. | $21.55 | -1.91 | — | — | no earnings | no_earnings |
| 485 | AAOI | Applied Optoelectronics, I | $138.54 | -0.65 | — | — | no earnings | no_earnings |
| 486 | GLXY | Galaxy Digital Inc. | $28.26 | -0.24 | — | — | no earnings | no_earnings |
| 487 | SMMT | Summit Therapeutics Inc. | $14.18 | -1.59 | — | — | no earnings | no_earnings |
| 488 | OC | Owens Corning Inc | $136.26 | -4.74 | — | — | no earnings | no_earnings |
| 489 | CIFR | Cipher Digital Inc. | $25.68 | -2.32 | — | — | no earnings | no_earnings |
| 490 | RIOT | Riot Platforms, Inc. | $27.76 | -2.49 | — | — | no earnings | no_earnings |
| 491 | GSAT | Globalstar, Inc. | $79.95 | -0.15 | — | — | no earnings | no_earnings |
| 492 | CRL | Charles River Laboratories | $212.71 | -3.7 | — | — | no earnings | no_earnings |
| 493 | CYTK | Cytokinetics, Incorporated | $80.8 | -6.85 | — | — | no earnings | no_earnings |
| 494 | APGE | Apogee Therapeutics, Inc. | $132.68 | -4.33 | — | — | no earnings | no_earnings |
| 495 | GTLS | Chart Industries, Inc. | $208.84 | -1.02 | — | — | no earnings | no_earnings |
| 496 | MP | MP Materials Corp. | $55.62 | -0.4 | — | — | no earnings | no_earnings |
| 497 | TEM | Tempus AI, Inc. | $54.87 | -1.72 | — | — | no earnings | no_earnings |
| 498 | WLK | Westlake Corporation | $76.54 | -12.7 | — | — | no earnings | no_earnings |
| 499 | NUVL | Nuvalent, Inc. | $123.53 | -6.07 | — | — | no earnings | no_earnings |
| 500 | LINE | Lineage, Inc. | $42.61 | -0.62 | — | — | no earnings | no_earnings |

---
## Global (top ~1000 companies worldwide by market cap)
Valued 992 holdings · **496 most undervalued (BULLISH)** vs **496 most overvalued (BEARISH)** · 0 near-median (neutral, excluded).

### 🟢 BULLISH — 496 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | SBER.ME | SBERBANK OF RUSSIA | $133.3 | 50.4 | 17% | $1348.93 | +912% |  |
| 2 | GMKN.ME | MMC NORILSK NICKEL | $16720.0 | 2619.9 | 30% | $120800.31 | +622% |  |
| 3 | ONGC.NS | OIL AND NATURAL GAS CORP. | $233.15 | 32.94 | 30% | $1518.82 | +551% |  |
| 4 | 9984.T | SOFTBANK GROUP CORP | $6226.0 | 872.67 | 30% | $40237.72 | +546% |  |
| 5 | BABWF | International Consolidated | $5.85 | 0.82 | 30% | $37.81 | +546% |  |
| 6 | VOW3.DE | VOLKSWAGEN AG              | $74.5 | 12.21 | 26% | $475.08 | +538% |  |
| 7 | 6902.T | DENSO CORP | $1875.0 | 257.87 | 30% | $11890.06 | +534% |  |
| 8 | PRX.AS | PROSUS | $37.01 | 5.08 | 30% | $234.23 | +533% |  |
| 9 | NPSNY | Naspers Ltd. | $9.9 | 1.35 | 30% | $61.11 | +517% |  |
| 10 | 8725.T | MS&AD INS GP HLDGS | $4241.0 | 528.95 | 30% | $24389.22 | +475% |  |
| 11 | GAZP.ME | GAZPROM PJSC | $198.0 | 88.51 | 0% | $1099.15 | +455% |  |
| 12 | GFI | Gold Fields Limited | $32.82 | 3.94 | 30% | $181.67 | +454% |  |
| 13 | EQT | EQT Corporation | $51.65 | 5.27 | 30% | $242.99 | +370% |  |
| 14 | REP.MC | REPSOL,  S.A. | $21.2 | 2.14 | 30% | $98.67 | +365% |  |
| 15 | B | Barrick Mining Corporation | $36.75 | 3.65 | 30% | $168.3 | +358% |  |
| 16 | KGC | Kinross Gold Corporation | $24.04 | 2.35 | 30% | $108.36 | +351% |  |
| 17 | 601688.SS | HUATAI SECURITIES CO LTD | $20.41 | 1.86 | 30% | $85.76 | +320% |  |
| 18 | 601899.SS | ZIJIN MINING GROUP CO.LTD | $25.1 | 2.27 | 30% | $104.67 | +317% |  |
| 19 | 601336.SS | NEW CHINA LIFE INSURANCE C | $59.6 | 11.82 | 10% | $237.48 | +298% |  |
| 20 | 000776.SZ | GF SECURITIES CO LTD | $22.35 | 1.93 | 30% | $88.99 | +298% |  |
| 21 | TTE | TotalEnergies SE | $78.28 | 6.74 | 30% | $310.77 | +297% |  |
| 22 | AU | AngloGold Ashanti PLC | $79.34 | 6.81 | 30% | $314.0 | +296% |  |
| 23 | TM | Toyota Motor Corporation | $166.5 | 18.27 | 23% | $643.96 | +287% |  |
| 24 | UAL | United Airlines Holdings,  | $134.6 | 11.19 | 30% | $515.96 | +283% |  |
| 25 | NVTK.ME | NOVATEK PJSC | $993.0 | 144.24 | 16% | $3769.13 | +280% |  |
| 26 | NEM | Newmont Corporation | $95.35 | 7.71 | 30% | $355.5 | +273% |  |
| 27 | 8053.T | SUMITOMO CORP | $6201.0 | 498.37 | 30% | $22979.22 | +271% |  |
| 28 | 600030.SS | CITIC SECURITIES CO LTD | $27.74 | 2.2 | 30% | $101.44 | +266% |  |
| 29 | VG | Venture Global, Inc. | $10.83 | 0.96 | 27% | $38.92 | +259% |  |
| 30 | LKOH.ME | OIL CO LUKOIL PJSC | $3911.0 | 1129.04 | 0% | $14020.9 | +258% |  |
| 31 | EOG | EOG Resources, Inc. | $133.59 | 10.17 | 30% | $468.93 | +251% |  |
| 32 | 8309.T | SUMITOMO MITSUI TRUST GP I | $5972.0 | 451.41 | 30% | $20813.95 | +248% |  |
| 33 | EMAAR.AE | EMAAR PROPERTIES | $12.2 | 2.14 | 10% | $42.47 | +248% |  |
| 34 | NTR | Nutrien Ltd. | $60.96 | 4.91 | 28% | $209.67 | +244% |  |
| 35 | JSWSTEEL.NS | JSW STEEL LIMITED | $1231.3 | 91.22 | 30% | $4206.04 | +242% |  |
| 36 | SHEL | Shell PLC | $77.33 | 6.42 | 27% | $259.28 | +235% |  |
| 37 | 3993.HK | CMOC | $15.22 | 1.1 | 30% | $50.72 | +233% |  |
| 38 | CVE | Cenovus Energy Inc | $24.68 | 1.77 | 30% | $81.61 | +231% |  |
| 39 | ROSN.ME | ROSNEFT OIL CO | $351.2 | 92.95 | 0% | $1154.29 | +229% |  |
| 40 | 600999.SS | CHINA MERCHANTS SECURITIES | $20.48 | 1.46 | 30% | $67.32 | +229% |  |
| 41 | 8002.T | MARUBENI CORP | $4692.0 | 329.86 | 30% | $15209.43 | +224% |  |
| 42 | LYG | Lloyds Banking Group Plc | $5.75 | 0.4 | 30% | $18.44 | +221% |  |
| 43 | 600919.SS | BANK OF JIANGSU | $11.09 | 1.81 | 9% | $35.22 | +218% |  |
| 44 | 2259.HK | ZIJIN GOLD INTL | $93.75 | 6.43 | 30% | $296.48 | +216% |  |
| 45 | 9433.T | KDDI CORPORATION | $2681.0 | 183.59 | 30% | $8465.11 | +216% |  |
| 46 | BABA | Alibaba Group Holding Limi | $95.07 | 6.48 | 30% | $298.78 | +214% |  |
| 47 | 002142.SZ | BANK OF NINGBO CO. LTD. | $31.13 | 4.41 | 12% | $97.77 | +214% |  |
| 48 | AEM | Agnico Eagle Mines Limited | $156.18 | 10.62 | 30% | $489.67 | +214% |  |
| 49 | EQNR | Equinor ASA | $31.56 | 2.21 | 29% | $98.8 | +213% |  |
| 50 | SU | Suncor Energy  Inc. | $54.36 | 3.7 | 30% | $169.95 | +213% |  |
| 51 | 0267.HK | CITIC | $11.78 | 2.32 | 5% | $36.4 | +209% |  |
| 52 | BPAC3.SA | BTGP BANCO  ON      N2 | $22.73 | 1.51 | 30% | $69.62 | +206% |  |
| 53 | 000001.SZ | PING AN BANK CO LTD | $10.23 | 2.12 | 3% | $31.06 | +204% |  |
| 54 | MFG | Mizuho Financial Group, In | $9.59 | 0.62 | 30% | $28.59 | +198% |  |
| 55 | SYF | Synchrony Financial | $78.52 | 9.66 | 14% | $227.35 | +190% |  |
| 56 | FSLR | First Solar, Inc. | $248.64 | 15.49 | 30% | $714.22 | +187% |  |
| 57 | 6669.TW | WIWYNN CORPORATION | $4280.0 | 265.43 | 30% | $12238.65 | +186% |  |
| 58 | GMBXF | Grupo Mexico S.A.B. de C.V | $11.51 | 0.71 | 30% | $32.74 | +184% |  |
| 59 | CMCSA | Comcast Corporation | $22.69 | 5.1 | 0% | $63.33 | +179% |  |
| 60 | MPC | Marathon Petroleum Corpora | $253.56 | 15.19 | 30% | $700.39 | +176% |  |
| 61 | 2887.TW | TS FINANCIAL HOLDING CO LT | $31.9 | 1.91 | 30% | $88.07 | +176% |  |
| 62 | CFG | Citizens Financial Group,  | $70.66 | 4.22 | 30% | $194.58 | +175% |  |
| 63 | GILD | Gilead Sciences, Inc. | $123.84 | 7.36 | 30% | $339.36 | +174% |  |
| 64 | 1398.HK | ICBC | $6.62 | 1.17 | 4% | $17.93 | +171% |  |
| 65 | MT | Arcelor Mittal NY Registry | $61.82 | 3.82 | 29% | $167.24 | +170% |  |
| 66 | 2328.HK | PICC P&C | $14.36 | 2.1 | 8% | $38.8 | +170% |  |
| 67 | DB | Deutsche Bank AG | $34.38 | 3.6 | 16% | $92.69 | +170% |  |
| 68 | BCS | Barclays PLC | $27.3 | 2.29 | 20% | $71.27 | +161% |  |
| 69 | T | AT&T Inc. | $22.42 | 3.04 | 9% | $58.41 | +160% |  |
| 70 | C | Citigroup, Inc. | $144.98 | 8.09 | 30% | $373.02 | +157% |  |
| 71 | UBER | Uber Technologies, Inc. | $72.25 | 4.03 | 30% | $185.82 | +157% |  |
| 72 | SHG | Shinhan Financial Group Co | $61.99 | 6.66 | 14% | $159.24 | +157% |  |
| 73 | 601668.SS | CHINA CONSTRUCTION ENGINEE | $4.4 | 0.91 | 0% | $11.3 | +157% |  |
| 74 | LICI.NS | LIFE INSURA CORP OF INDIA | $423.25 | 45.43 | 14% | $1079.13 | +155% |  |
| 75 | 7974.T | NINTENDO CO LTD | $6589.0 | 364.21 | 30% | $16793.27 | +155% |  |
| 76 | BBD | Banco Bradesco Sa | $3.35 | 0.4 | 11% | $8.54 | +155% |  |
| 77 | 600900.SS | CHINA YANGTZE POWER CO | $26.65 | 1.47 | 30% | $67.78 | +154% |  |
| 78 | 600028.SS | CHINA PETROLEUM & CHEMICAL | $4.52 | 0.27 | 28% | $11.43 | +153% |  |
| 79 | VLO | Valero Energy Corporation | $255.06 | 13.7 | 30% | $631.69 | +148% |  |
| 80 | 002714.SZ | MUYUAN FOODS GROUP CO LTD | $33.56 | 1.8 | 30% | $83.0 | +147% |  |
| 81 | NWG | NatWest Group plc | $17.35 | 1.84 | 13% | $42.8 | +147% |  |
| 82 | 600188.SS | YANKUANG ENERGY GROUP COMP | $17.98 | 0.96 | 30% | $44.26 | +146% |  |
| 83 | 601995.SS | CHINA INTL CAPITAL CORPORA | $35.56 | 1.88 | 30% | $86.68 | +144% |  |
| 84 | ALL | Allstate Corporation (The) | $231.6 | 45.21 | 0% | $561.44 | +142% |  |
| 85 | 0883.HK | CNOOC | $20.86 | 2.97 | 6% | $50.53 | +142% |  |
| 86 | ITSA3.SA | ITAUSA      ON  EJ  N1 | $13.3 | 1.52 | 11% | $32.09 | +141% |  |
| 87 | NU | Nu Holdings Ltd. | $12.46 | 0.65 | 30% | $29.97 | +140% |  |
| 88 | 9992.HK | POP MART | $158.5 | 11.06 | 23% | $380.43 | +140% |  |
| 89 | 601601.SS | CHINA PACIFIC INSURANCE (G | $28.43 | 5.48 | 0% | $68.05 | +139% |  |
| 90 | 601166.SS | INDUSTRIAL BANK CO LTD | $16.77 | 3.2 | 0% | $39.74 | +137% |  |
| 91 | BMW.DE | BAYERISCHE MOTOREN WERKE A | $59.02 | 11.19 | 0% | $138.96 | +135% |  |
| 92 | PBR | Petroleo Brasileiro S.A. P | $16.52 | 3.13 | 0% | $38.87 | +135% |  |
| 93 | ACGL | Arch Capital Group Ltd. | $94.33 | 13.0 | 7% | $221.71 | +135% |  |
| 94 | 601818.SS | CHINA EVERBRIGHT BANK CO L | $2.97 | 0.56 | 0% | $6.95 | +134% |  |
| 95 | FNLPF | Fresnillo Plc | $37.37 | 1.88 | 30% | $86.68 | +132% |  |
| 96 | PLZL.ME | POLYUS PJSC | $8376.0 | 1048.52 | 8% | $19220.81 | +130% |  |
| 97 | KEY | KeyCorp | $23.41 | 1.63 | 22% | $53.71 | +129% |  |
| 98 | BNP.PA | BNP PARIBAS ACT.A | $101.4 | 10.6 | 12% | $231.99 | +129% |  |
| 99 | DAL | Delta Air Lines, Inc. | $92.11 | 6.85 | 20% | $209.87 | +128% |  |
| 100 | 600150.SS | CHINA CSSC HOLDINGS LIMITE | $33.4 | 1.65 | 30% | $76.08 | +128% |  |
| 101 | KB | KB Financial Group Inc | $99.99 | 10.42 | 12% | $226.83 | +127% |  |
| 102 | SCHW | Charles Schwab Corporation | $89.44 | 5.03 | 26% | $202.1 | +126% |  |
| 103 | 002415.SZ | HANGZHOU HIKVISION DIGITAL | $33.32 | 1.63 | 30% | $75.16 | +126% |  |
| 104 | VICI | VICI Properties Inc. | $26.53 | 2.92 | 10% | $59.85 | +126% |  |
| 105 | COALINDIA.NS | COAL INDIA LTD | $435.65 | 50.46 | 9% | $976.15 | +124% |  |
| 106 | PUK | Prudential Public Limited  | $26.65 | 3.07 | 9% | $59.69 | +124% |  |
| 107 | 3968.HK | CM BANK | $44.7 | 6.59 | 4% | $99.42 | +122% |  |
| 108 | GLE.PA | SOCIETE GENERALE | $76.51 | 7.04 | 14% | $169.07 | +121% |  |
| 109 | 7182.T | JAPAN POST BANK CO LTD | $3069.0 | 147.01 | 30% | $6778.45 | +121% |  |
| 110 | HIG | The Hartford Insurance Gro | $130.37 | 14.21 | 10% | $287.44 | +120% |  |
| 111 | 8058.T | MITSUBISHI CORP | $4403.0 | 209.88 | 30% | $9677.3 | +120% |  |
| 112 | UCG.MI | UNICREDIT | $77.12 | 7.27 | 13% | $169.08 | +119% |  |
| 113 | EBO.F | Erste Group Bank AG        | $115.6 | 8.57 | 18% | $246.59 | +113% |  |
| 114 | 2222.SR | Saudi Arabian Oil Co. | $26.14 | 1.54 | 24% | $55.44 | +112% |  |
| 115 | 300750.SZ | CONTEMPORARY AMPEREX TECHN | $381.0 | 17.52 | 30% | $807.83 | +112% |  |
| 116 | TLX.DE | Talanx AG                  | $107.5 | 10.26 | 12% | $227.26 | +111% |  |
| 117 | TEL | TE Connectivity plc | $200.07 | 9.78 | 28% | $422.55 | +111% |  |
| 118 | TATASTEEL.NS | TATA STEEL LIMITED | $188.6 | 8.64 | 30% | $398.38 | +111% |  |
| 119 | SAF.PA | SAFRAN | $337.2 | 17.19 | 27% | $711.69 | +111% |  |
| 120 | CBOE | Cboe Global Markets, Inc. | $244.98 | 11.71 | 29% | $516.47 | +111% |  |
| 121 | FMG.AX | FORTESCUE FPO [FMG] | $19.07 | 1.76 | 13% | $40.14 | +110% |  |
| 122 | ITUB | Itau Unibanco Banco Holdin | $8.03 | 0.79 | 11% | $16.83 | +110% |  |
| 123 | 601998.SS | CHINA CITIC BANK CORPORATI | $7.13 | 1.2 | 0% | $14.9 | +109% |  |
| 124 | PKN.WA | PKNORLEN | $122.52 | 5.55 | 30% | $255.9 | +109% |  |
| 125 | TECK | Teck Resources Ltd | $59.0 | 2.66 | 30% | $122.65 | +108% |  |
| 126 | 1109.HK | CHINA RES LAND | $30.16 | 4.11 | 4% | $62.37 | +107% |  |
| 127 | BHP | BHP Group Limited | $81.16 | 4.03 | 27% | $167.11 | +106% |  |
| 128 | 601288.SS | AGRICULTURAL BANK OF CHINA | $6.19 | 0.79 | 5% | $12.7 | +105% |  |
| 129 | 000858.SZ | WULIANGYE YIBIN CO. LTD. | $73.17 | 3.25 | 30% | $149.85 | +105% |  |
| 130 | ADBE | Adobe Inc. | $193.41 | 17.48 | 13% | $395.36 | +104% |  |
| 131 | TCOM | Trip.com Group Limited | $40.49 | 6.66 | 0% | $82.71 | +104% |  |
| 132 | 601066.SS | CHINA SECURITIES CO.  LTD. | $30.25 | 1.33 | 30% | $61.32 | +103% |  |
| 133 | JD | JD.com, Inc. | $25.19 | 1.36 | 25% | $51.03 | +103% |  |
| 134 | UBS | UBS Group AG Registered | $49.94 | 2.79 | 24% | $100.72 | +102% |  |
| 135 | NFLX | Netflix, Inc. | $70.9 | 3.1 | 30% | $142.94 | +102% |  |
| 136 | 600000.SS | SHANGHAI PUDONG DEVELOPMEN | $8.76 | 1.42 | 0% | $17.63 | +101% |  |
| 137 | PTT-R.BK | PTT_PTT | $35.0 | 3.25 | 12% | $70.18 | +100% |  |
| 138 | 601328.SS | BANK OF COMMUNICATIONS CO  | $6.51 | 1.04 | 0% | $12.92 | +98% |  |
| 139 | AMP | Ameriprise Financial, Inc. | $453.29 | 40.12 | 12% | $897.82 | +98% |  |
| 140 | NTRS | Northern Trust Corporation | $175.97 | 9.56 | 24% | $348.18 | +98% |  |
| 141 | INVE-B.ST | Investor AB ser. B | $392.1 | 62.21 | 0% | $772.55 | +97% |  |
| 142 | SAN | Banco Santander, S.A. Spon | $13.38 | 1.01 | 16% | $26.26 | +96% |  |
| 143 | QNBTR.IS | QNB BANK | $207.3 | 8.74 | 30% | $402.99 | +94% |  |
| 144 | 6701.T | NEC CORP | $3795.0 | 202.88 | 24% | $7356.35 | +94% |  |
| 145 | BAC | Bank of America Corporatio | $58.19 | 4.03 | 18% | $112.37 | +93% |  |
| 146 | 000651.SZ | GREE ELECTRICAL APP INC OF | $37.02 | 5.22 | 2% | $71.22 | +92% |  |
| 147 | MUV2.DE | MUENCHENER RUECKVERS.-GES. | $474.3 | 52.23 | 7% | $910.57 | +92% |  |
| 148 | 600309.SS | WANHUA CHEMICAL GROUP CO L | $71.79 | 4.2 | 21% | $137.53 | +92% |  |
| 149 | 601318.SS | PING AN INSURANCE(GROUP)CO | $47.23 | 7.25 | 0% | $90.03 | +91% |  |
| 150 | CM | Canadian Imperial Bank of  | $114.37 | 7.09 | 19% | $213.93 | +87% |  |
| 151 | NUE | Nucor Corporation | $248.89 | 10.08 | 30% | $464.78 | +87% |  |
| 152 | ABN.AS | ABN AMRO BANK N.V. | $36.48 | 2.54 | 16% | $67.43 | +85% |  |
| 153 | HAL | Halliburton Company | $34.67 | 1.81 | 23% | $63.95 | +84% |  |
| 154 | 601658.SS | POSTAL SAVINGS BANK OF CHI | $4.92 | 0.73 | 0% | $9.07 | +84% |  |
| 155 | TFC | Truist Financial Corporati | $50.67 | 4.04 | 13% | $93.34 | +84% |  |
| 156 | 1180.SR | The Saudi National Bank | $39.98 | 4.11 | 8% | $73.48 | +84% |  |
| 157 | TEVA | Teva Pharmaceutical Indust | $33.62 | 1.34 | 30% | $61.79 | +84% |  |
| 158 | 601919.SS | COSCO SHIPPING HOLDINGS | $13.39 | 1.98 | 0% | $24.59 | +84% |  |
| 159 | ING | ING Group, N.V. | $31.02 | 2.49 | 13% | $56.82 | +83% |  |
| 160 | AMX | America Movil, S.A.B. de C | $26.3 | 1.65 | 19% | $48.18 | +83% |  |
| 161 | 5802.T | SUMITOMO ELECTRIC INDUSTRI | $11935.0 | 473.69 | 30% | $21841.25 | +83% |  |
| 162 | 2317.TW | HON HAI PRECISION INDUSTRY | $248.5 | 13.39 | 22% | $452.92 | +82% |  |
| 163 | 300059.SZ | EAST MONEY INFORMATION CO  | $20.07 | 0.83 | 29% | $36.48 | +82% |  |
| 164 | 601628.SS | CHINA LIFE INSURANCE CO LT | $35.04 | 5.12 | 0% | $63.58 | +82% |  |
| 165 | EMIRATESNBD.AE | EMIRATES NBD BANK | $30.44 | 3.74 | 4% | $55.16 | +81% |  |
| 166 | Z74.SI | Singtel | $4.43 | 0.34 | 14% | $8.0 | +80% |  |
| 167 | AXISBANK.BO | AXIS BANK LTD. | $1376.55 | 84.52 | 19% | $2479.57 | +80% |  |
| 168 | 601319.SS | THE PEOPLE S INSURANCE COM | $6.91 | 1.0 | 0% | $12.42 | +80% |  |
| 169 | RF | Regions Financial Corporat | $29.98 | 2.41 | 12% | $53.07 | +77% |  |
| 170 | GOOG | Alphabet Inc. | $342.19 | 13.11 | 30% | $604.49 | +77% |  |
| 171 | EOAN.DE | E.ON SE                    | $18.13 | 1.31 | 14% | $31.99 | +76% |  |
| 172 | 2914.T | JAPAN TOBACCO INC | $6072.0 | 281.34 | 25% | $10704.95 | +76% |  |
| 173 | ISP.MI | INTESA SANPAOLO | $5.91 | 0.54 | 9% | $10.38 | +76% |  |
| 174 | CINF | Cincinnati Financial Corpo | $177.73 | 17.5 | 8% | $312.14 | +76% |  |
| 175 | AIG | American International Gro | $74.85 | 5.68 | 13% | $131.23 | +75% |  |
| 176 | BKR | Baker Hughes Company | $56.94 | 3.13 | 21% | $99.66 | +75% |  |
| 177 | 4578.T | OTSUKA HLDGS CO LTD | $10895.0 | 685.09 | 18% | $19054.76 | +75% |  |
| 178 | U11.SI | UOB | $39.8 | 2.75 | 15% | $69.51 | +75% |  |
| 179 | ACN | Accenture plc | $125.82 | 12.52 | 7% | $219.7 | +75% |  |
| 180 | WFC | Wells Fargo & Company | $84.74 | 6.47 | 13% | $147.64 | +74% |  |
| 181 | BIIB | Biogen Inc. | $201.96 | 9.29 | 25% | $348.85 | +73% |  |
| 182 | STLD | Steel Dynamics, Inc. | $251.0 | 9.34 | 30% | $430.66 | +72% |  |
| 183 | BAP | Credicorp Ltd. | $380.41 | 26.17 | 15% | $652.82 | +72% |  |
| 184 | EXPGF | Experian plc | $33.42 | 1.63 | 23% | $57.22 | +71% |  |
| 185 | HNR1.DE | HANNOVER RUECK SE NA O.N. | $237.0 | 23.8 | 6% | $405.13 | +71% |  |
| 186 | 2359.HK | WUXI APPTEC | $145.4 | 7.98 | 20% | $246.69 | +70% |  |
| 187 | 6178.T | JAPAN POST HLDGS CO LTD | $2161.0 | 129.04 | 18% | $3650.56 | +69% |  |
| 188 | VWS.CO | Vestas Wind Systems A/S | $173.35 | 6.35 | 30% | $292.79 | +69% |  |
| 189 | PNC | PNC Financial Services Gro | $245.28 | 17.22 | 14% | $413.91 | +69% |  |
| 190 | MSFT | Microsoft Corporation | $352.83 | 16.79 | 23% | $594.44 | +68% |  |
| 191 | MU | Micron Technology, Inc. | $1213.56 | 44.29 | 30% | $2042.16 | +68% |  |
| 192 | 6201.T | TOYOTA INDUSTRIES CORP | $20450.0 | 744.38 | 30% | $34322.43 | +68% |  |
| 193 | CI | The Cigna Group | $281.87 | 23.59 | 10% | $472.66 | +68% |  |
| 194 | JBS | JBS N.V. | $12.03 | 1.62 | 0% | $20.12 | +67% |  |
| 195 | CB | Chubb Limited | $330.82 | 28.29 | 9% | $548.02 | +66% |  |
| 196 | FMX | Fomento Economico Mexicano | $125.37 | 4.5 | 30% | $207.49 | +66% |  |
| 197 | 601939.SS | CHINA CONSTRUCTION BANK | $9.78 | 1.3 | 0% | $16.14 | +65% |  |
| 198 | VST | Vistra Corp. | $167.77 | 5.97 | 30% | $275.27 | +64% |  |
| 199 | BK | The Bank of New York Mello | $137.16 | 8.06 | 18% | $223.99 | +63% |  |
| 200 | FFH.TO | FAIRFAX FINANCIAL HOLDINGS | $2340.67 | 287.43 | 1% | $3809.43 | +63% |  |
| 201 | ACA.PA | CREDIT AGRICOLE | $17.59 | 2.13 | 2% | $28.59 | +63% |  |
| 202 | A5G.IR | AIB GROUP PLC | $10.4 | 0.93 | 8% | $16.89 | +62% |  |
| 203 | USB | U.S. Bancorp | $61.21 | 4.77 | 11% | $99.14 | +62% |  |
| 204 | MTB | M&T Bank Corporation | $236.77 | 17.81 | 12% | $382.7 | +62% |  |
| 205 | WPM | Wheaton Precious Metals Co | $113.08 | 3.96 | 30% | $182.59 | +62% |  |
| 206 | QNBK.QA | QATAR NATIONAL BANK | $17.5 | 1.75 | 5% | $28.26 | +62% |  |
| 207 | PDD | PDD Holdings Inc. | $73.3 | 9.5 | 0% | $117.98 | +61% |  |
| 208 | ZURN.SW | ZURICH INSURANCE N | $586.2 | 38.2 | 15% | $942.6 | +61% |  |
| 209 | 2382.TW | QUANTA COMPUTER | $362.0 | 18.91 | 20% | $581.66 | +61% |  |
| 210 | BNS | Bank Nova Scotia Halifax P | $86.46 | 5.1 | 17% | $138.5 | +60% |  |
| 211 | 601988.SS | BANK OF CHINA LTD | $5.76 | 0.74 | 0% | $9.19 | +60% |  |
| 212 | GFNORTEO.MX | GRUPO FINANCIERO BANORTE | $185.85 | 21.61 | 2% | $296.44 | +60% |  |
| 213 | RJF | Raymond James Financial, I | $150.52 | 10.6 | 13% | $239.65 | +59% |  |
| 214 | BMPS.MI | BANCA MONTE PASCHI SIENA | $10.78 | 1.38 | 0% | $17.14 | +59% |  |
| 215 | 5108.T | BRIDGESTONE CORP | $3462.0 | 119.19 | 30% | $5495.7 | +59% |  |
| 216 | 6273.T | SMC CORP | $71630.0 | 2640.07 | 28% | $113533.01 | +58% |  |
| 217 | INTU | Intuit Inc. | $255.07 | 16.4 | 15% | $403.44 | +58% |  |
| 218 | CEG | Constellation Energy Corpo | $268.69 | 11.5 | 24% | $424.1 | +58% |  |
| 219 | 0762.HK | CHINA UNICOM | $6.34 | 0.78 | 1% | $9.99 | +58% |  |
| 220 | BMO | Bank Of Montreal | $174.8 | 9.16 | 19% | $274.2 | +57% |  |
| 221 | PYPL | PayPal Holdings, Inc. | $42.38 | 5.33 | 0% | $66.19 | +56% |  |
| 222 | SCCO | Southern Copper Corporatio | $174.73 | 5.91 | 30% | $272.5 | +56% |  |
| 223 | FNV | Franco-Nevada Corporation | $210.0 | 7.1 | 30% | $327.37 | +56% |  |
| 224 | 0857.HK | PETROCHINA | $8.78 | 1.0 | 2% | $13.64 | +55% |  |
| 225 | NVDA | NVIDIA Corporation | $195.74 | 6.54 | 30% | $301.55 | +54% |  |
| 226 | EIX | Edison International | $74.75 | 9.2 | 0% | $114.25 | +53% |  |
| 227 | 0992.HK | LENOVO GROUP | $23.44 | 1.09 | 21% | $35.68 | +52% |  |
| 228 | BP | BP p.l.c. | $37.72 | 1.24 | 30% | $57.17 | +52% |  |
| 229 | BBVA | Banco Bilbao Vizcaya Argen | $24.53 | 2.07 | 8% | $37.16 | +52% |  |
| 230 | ICE | Intercontinental Exchange  | $124.49 | 6.87 | 17% | $188.01 | +51% |  |
| 231 | PRY.MI | PRYSMIAN | $143.7 | 4.69 | 30% | $216.25 | +50% |  |
| 232 | TCEHY | Tencent Holding Ltd. | $53.41 | 3.56 | 13% | $80.31 | +50% |  |
| 233 | ADS.DE | adidas AG                  | $178.0 | 7.72 | 23% | $267.39 | +50% |  |
| 234 | PCG | Pacific Gas & Electric Co. | $17.08 | 1.29 | 10% | $25.55 | +50% |  |
| 235 | HBAN | Huntington Bancshares Inco | $17.9 | 1.3 | 11% | $26.66 | +49% |  |
| 236 | 2338.HK | WEICHAI POWER | $35.96 | 1.51 | 23% | $53.24 | +48% |  |
| 237 | DTE.DE | DEUTSCHE TELEKOM AG        | $26.04 | 1.81 | 11% | $38.48 | +48% |  |
| 238 | LDO.MI | LEONARDO | $45.16 | 2.24 | 19% | $66.63 | +48% |  |
| 239 | HCA | HCA Healthcare, Inc. | $386.94 | 29.02 | 10% | $570.18 | +47% |  |
| 240 | 000333.SZ | MIDEA GROUP CO LTD | $78.55 | 5.82 | 10% | $115.24 | +47% |  |
| 241 | GEV | GE Vernova Inc. | $1085.47 | 34.19 | 30% | $1576.46 | +45% |  |
| 242 | CBK.F | Commerzbank AG             | $37.5 | 2.17 | 15% | $54.44 | +45% |  |
| 243 | CS.PA | AXA | $43.05 | 3.42 | 8% | $62.46 | +45% |  |
| 244 | 6098.T | RECRUIT HOLDINGS CO LTD | $11040.0 | 347.32 | 30% | $16014.49 | +45% |  |
| 245 | MBG.DE | Mercedes-Benz Group AG     | $43.58 | 5.09 | 0% | $63.21 | +45% |  |
| 246 | TRV | The Travelers Companies, I | $318.29 | 33.52 | 2% | $460.49 | +45% |  |
| 247 | EXPE | Expedia Group, Inc. | $250.95 | 11.32 | 21% | $360.72 | +44% |  |
| 248 | JPM | JP Morgan Chase & Co. | $335.12 | 20.88 | 13% | $481.13 | +44% |  |
| 249 | 1299.HK | AIA | $70.8 | 4.63 | 12% | $101.56 | +43% |  |
| 250 | SREN.SW | SWISS RE N | $127.3 | 12.59 | 3% | $182.57 | +43% |  |
| 251 | 2881.TW | FUBON FINANCIAL HLDG CO LT | $134.0 | 8.36 | 13% | $191.62 | +43% |  |
| 252 | VZ | Verizon Communications Inc | $46.07 | 4.1 | 5% | $65.67 | +42% |  |
| 253 | BAMI.MI | BANCO BPM | $15.02 | 1.38 | 4% | $21.33 | +42% |  |
| 254 | TRGP | Targa Resources, Inc. | $273.45 | 9.79 | 26% | $388.1 | +42% |  |
| 255 | DELL | Dell Technologies Inc. | $409.45 | 12.57 | 30% | $579.59 | +42% |  |
| 256 | ZTS | Zoetis Inc. | $77.82 | 6.1 | 8% | $109.16 | +40% |  |
| 257 | HSY | The Hershey Company | $176.68 | 5.37 | 30% | $247.6 | +40% |  |
| 258 | ALV.DE | Allianz SE                 | $407.2 | 30.98 | 8% | $567.64 | +39% |  |
| 259 | 6971.T | KYOCERA CORP | $3411.0 | 102.83 | 30% | $4741.36 | +39% |  |
| 260 | FCX | Freeport-McMoRan, Inc. | $62.8 | 1.89 | 30% | $87.15 | +39% |  |
| 261 | SAMPO.HE | Sampo Plc A | $9.02 | 0.61 | 10% | $12.5 | +38% |  |
| 262 | NTES | NetEase, Inc. | $114.82 | 7.79 | 10% | $158.51 | +38% |  |
| 263 | OTP.BD | OTP | $45870.0 | 4408.52 | 3% | $62334.87 | +36% |  |
| 264 | 1120.SR | Al Rajhi Bank | $66.35 | 4.02 | 12% | $89.96 | +36% |  |
| 265 | EPD | Enterprise Products Partne | $36.84 | 2.7 | 8% | $49.86 | +35% |  |
| 266 | 7011.T | MITSUBISHI HEAVY INDUSTRIE | $3567.0 | 104.56 | 30% | $4821.13 | +35% |  |
| 267 | MET | MetLife, Inc. | $84.63 | 5.17 | 12% | $114.26 | +35% |  |
| 268 | 0941.HK | CHINA MOBILE | $77.4 | 7.28 | 3% | $104.15 | +35% |  |
| 269 | 601138.SS | FOXCONN INDUSTRIAL INTERNE | $70.22 | 2.05 | 30% | $94.52 | +35% |  |
| 270 | NXPI | NXP Semiconductors N.V. | $298.64 | 10.45 | 25% | $401.61 | +34% |  |
| 271 | MPLX | MPLX LP | $56.07 | 4.62 | 6% | $75.41 | +34% |  |
| 272 | GS | Goldman Sachs Group, Inc.  | $1065.09 | 54.75 | 16% | $1426.2 | +34% |  |
| 273 | MS | Morgan Stanley | $221.04 | 11.03 | 17% | $295.85 | +34% |  |
| 274 | AFL | AFLAC Incorporated | $118.23 | 8.75 | 8% | $158.19 | +34% |  |
| 275 | HSBC | HSBC Holdings, plc. | $95.06 | 6.05 | 11% | $126.83 | +33% |  |
| 276 | LUV | Southwest Airlines Company | $52.09 | 1.5 | 30% | $69.16 | +33% |  |
| 277 | 6762.T | TDK CORP | $3575.0 | 102.78 | 30% | $4739.06 | +33% |  |
| 278 | INFY | Infosys Limited | $10.57 | 0.8 | 7% | $14.01 | +32% |  |
| 279 | GSK | GSK plc | $51.89 | 3.75 | 8% | $68.58 | +32% |  |
| 280 | POWERGRID.NS | POWER GRID CORP. LTD. | $284.5 | 20.1 | 8% | $375.67 | +32% |  |
| 281 | CRM | Salesforce, Inc. | $150.19 | 8.64 | 13% | $196.38 | +31% |  |
| 282 | PLD | Prologis, Inc. | $140.53 | 3.98 | 30% | $183.51 | +31% |  |
| 283 | MRK | Merck & Company, Inc. | $125.45 | 3.55 | 30% | $163.69 | +30% |  |
| 284 | 2882.TW | CATHAY FINANCIAL HLDG CO | $106.0 | 7.06 | 9% | $137.55 | +30% |  |
| 285 | UI | Ubiquiti Inc. | $541.1 | 15.53 | 30% | $702.4 | +30% |  |
| 286 | RCL | Royal Caribbean Cruises Lt | $322.65 | 16.39 | 16% | $418.37 | +30% |  |
| 287 | ICTEF | International Container Te | $14.75 | 0.54 | 23% | $19.11 | +30% |  |
| 288 | 2885.TW | YUANTA FINANCIAL HOLDING C | $66.3 | 2.74 | 20% | $85.7 | +29% |  |
| 289 | CABK.MC | CAIXABANK, S.A. | $12.3 | 0.81 | 10% | $15.8 | +28% |  |
| 290 | KOTAKBANK.NS | KOTAK MAHINDRA BANK LTD | $409.75 | 19.39 | 17% | $525.9 | +28% |  |
| 291 | HEI.DE | Heidelberg Materials AG    | $183.75 | 11.18 | 11% | $235.22 | +28% |  |
| 292 | NMR | Nomura Holdings Inc | $8.79 | 0.74 | 4% | $11.23 | +28% |  |
| 293 | FRE.DE | Fresenius SE & Co. KGaA    | $39.76 | 2.68 | 9% | $50.79 | +28% |  |
| 294 | ORCL | Oracle Corporation | $152.46 | 5.82 | 22% | $194.54 | +28% |  |
| 295 | AM.PA | DASSAULT AVIATION | $285.6 | 12.52 | 18% | $363.91 | +27% |  |
| 296 | FICO | Fair Isaac Corporation | $1143.48 | 31.56 | 30% | $1455.19 | +27% |  |
| 297 | 600690.SS | HAIER SMART HOME CO LTD | $19.72 | 2.01 | 0% | $24.96 | +27% |  |
| 298 | LVS | Las Vegas Sands Corp. | $46.28 | 2.71 | 12% | $58.55 | +26% |  |
| 299 | DIS | Walt Disney Company (The) | $98.05 | 6.25 | 10% | $123.81 | +26% |  |
| 300 | AON | Aon plc | $315.95 | 18.23 | 12% | $398.97 | +26% |  |
| 301 | FTI | TechnipFMC plc | $67.03 | 2.61 | 21% | $84.59 | +26% |  |
| 302 | NGG | National Grid Transco, PLC | $83.42 | 4.32 | 14% | $105.12 | +26% |  |
| 303 | 0016.HK | SHK PPT | $114.2 | 7.59 | 9% | $143.76 | +26% |  |
| 304 | UCB.VI | UCB | $255.8 | 8.04 | 26% | $320.88 | +25% |  |
| 305 | SHRIRAMFIN.NS | SHRIRAM FINANCE LIMITED | $1030.8 | 53.24 | 14% | $1288.43 | +25% |  |
| 306 | 2388.HK | BOC HONG KONG | $45.56 | 3.79 | 4% | $56.91 | +25% |  |
| 307 | SGO.PA | SAINT GOBAIN | $80.32 | 5.78 | 7% | $100.2 | +25% |  |
| 308 | G.MI | GENERALI | $42.54 | 2.69 | 10% | $52.73 | +24% |  |
| 309 | WRB | W.R. Berkley Corporation | $69.29 | 4.72 | 8% | $85.85 | +24% |  |
| 310 | AMT | American Tower Corporation | $168.72 | 6.19 | 22% | $208.87 | +24% |  |
| 311 | DXCM | DexCom, Inc. | $68.65 | 2.33 | 24% | $85.0 | +24% |  |
| 312 | TSM | Taiwan Semiconductor Manuf | $434.99 | 11.61 | 30% | $535.32 | +23% |  |
| 313 | IBN | ICICI Bank Limited | $29.14 | 1.57 | 13% | $35.86 | +23% |  |
| 314 | MFC | Manulife Financial Corpora | $40.18 | 2.44 | 10% | $49.47 | +23% |  |
| 315 | SPOT | Spotify Technology S.A. | $441.21 | 14.65 | 24% | $537.88 | +22% |  |
| 316 | SPG | Simon Property Group, Inc. | $225.49 | 14.39 | 9% | $274.83 | +22% |  |
| 317 | NA.TO | NATIONAL BANK OF CANADA | $223.81 | 11.3 | 14% | $272.57 | +22% |  |
| 318 | BUD | Anheuser-Busch Inbev SA Sp | $84.08 | 3.61 | 18% | $102.17 | +22% |  |
| 319 | QBE.AX | QBE INSUR. FPO [QBE] | $24.84 | 2.05 | 4% | $30.16 | +21% |  |
| 320 | FITB | Fifth Third Bancorp | $56.41 | 2.97 | 13% | $68.41 | +21% |  |
| 321 | STT | State Street Corporation | $169.51 | 9.85 | 11% | $204.82 | +21% |  |
| 322 | VALE | VALE S.A. | $15.12 | 0.66 | 17% | $18.22 | +20% |  |
| 323 | EC | Ecopetrol S.A. | $14.45 | 1.4 | 0% | $17.39 | +20% |  |
| 324 | BKNG | Booking Holdings Inc. Comm | $177.05 | 7.58 | 18% | $212.54 | +20% |  |
| 325 | 0728.HK | CHINA TELECOM | $4.35 | 0.42 | 0% | $5.22 | +20% |  |
| 326 | NDA-FI.HE | Nordea Bank Abp | $16.23 | 1.36 | 3% | $19.33 | +19% |  |
| 327 | APP | Applovin Corporation | $445.93 | 11.5 | 30% | $530.25 | +19% |  |
| 328 | ABEV | Ambev S.A. | $3.14 | 0.19 | 10% | $3.73 | +19% |  |
| 329 | MCK | McKesson Corporation | $763.81 | 38.34 | 14% | $905.93 | +19% |  |
| 330 | RWE.DE | RWE AG                     | $55.1 | 3.26 | 10% | $65.05 | +18% |  |
| 331 | DNB.OL | DNB BANK ASA | $293.4 | 27.86 | 0% | $345.98 | +18% |  |
| 332 | BBCA.JK | Bank Central Asia Tbk | $6175.0 | 471.16 | 4% | $7239.31 | +17% |  |
| 333 | ARGX | argenx SE | $888.65 | 22.48 | 30% | $1036.52 | +17% |  |
| 334 | ADVANC.BK | ADVANC_ADVANCED INFO SERVI | $352.0 | 17.09 | 14% | $410.25 | +16% |  |
| 335 | AXP | American Express Company | $342.46 | 16.03 | 15% | $397.79 | +16% |  |
| 336 | PCAR | PACCAR Inc. | $121.68 | 4.7 | 19% | $141.4 | +16% |  |
| 337 | VIK | Viking Holdings Ltd | $102.9 | 2.69 | 29% | $119.52 | +16% |  |
| 338 | ADSK | Autodesk, Inc. | $189.73 | 6.85 | 21% | $220.18 | +16% |  |
| 339 | NOC | Northrop Grumman Corporati | $499.33 | 31.91 | 8% | $578.49 | +16% |  |
| 340 | LNG | Cheniere Energy, Inc. | $235.1 | 5.9 | 30% | $272.04 | +16% |  |
| 341 | LLY | Eli Lilly and Company | $1127.69 | 28.19 | 30% | $1299.81 | +15% |  |
| 342 | PKO.WA | PKOBP | $102.62 | 8.59 | 2% | $118.36 | +15% |  |
| 343 | POW.TO | POWER CORPORATION OF CANAD | $85.9 | 4.16 | 14% | $98.9 | +15% |  |
| 344 | BTI | British American Tobacco   | $62.48 | 4.61 | 5% | $71.87 | +15% |  |
| 345 | TCS.NS | TATA CONSULTANCY SERV LT | $2095.9 | 135.95 | 7% | $2410.25 | +15% |  |
| 346 | DG.PA | VINCI | $130.55 | 8.66 | 7% | $149.43 | +14% |  |
| 347 | DHL.DE | DEUTSCHE POST AG           | $52.34 | 3.09 | 9% | $59.94 | +14% |  |
| 348 | PST.MI | POSTE ITALIANE | $28.16 | 1.88 | 7% | $32.23 | +14% |  |
| 349 | META | Meta Platforms, Inc. | $542.87 | 27.52 | 13% | $619.7 | +14% |  |
| 350 | TS | Tenaris S.A. | $57.36 | 3.8 | 7% | $65.48 | +14% |  |
| 351 | WDC | Western Digital Corporatio | $675.39 | 16.68 | 30% | $769.09 | +14% |  |
| 352 | OKE | ONEOK, Inc. | $89.52 | 5.61 | 8% | $101.75 | +14% |  |
| 353 | OTIS | Otis Worldwide Corporation | $73.63 | 3.76 | 12% | $83.66 | +14% |  |
| 354 | RY | Royal Bank Of Canada | $203.73 | 10.82 | 12% | $231.15 | +14% |  |
| 355 | DG | Dollar General Corporation | $117.56 | 7.07 | 9% | $133.49 | +14% |  |
| 356 | PGR | Progressive Corporation (T | $215.54 | 19.66 | 0% | $244.15 | +13% |  |
| 357 | RYAAY | Ryanair Holdings plc | $64.17 | 4.65 | 5% | $72.51 | +13% |  |
| 358 | BSBR | Banco Santander Brasil SA | $5.16 | 0.32 | 8% | $5.83 | +13% |  |
| 359 | PRU | Prudential Financial, Inc. | $107.03 | 9.71 | 0% | $120.58 | +13% |  |
| 360 | 0001.HK | CKH HOLDINGS | $67.25 | 3.09 | 15% | $75.75 | +13% |  |
| 361 | RHM.F | RHEINMETALL AG             | $931.8 | 22.7 | 30% | $1046.67 | +12% |  |
| 362 | KKR | KKR & Co. Inc. | $92.65 | 2.94 | 23% | $103.77 | +12% |  |
| 363 | DEWA.AE | DUBAI ELECTRICITY | $2.75 | 0.17 | 8% | $3.07 | +12% |  |
| 364 | BAJFINANCE.NS | BAJAJ FINANCE LIMITED | $981.4 | 30.49 | 24% | $1095.33 | +12% |  |
| 365 | ADANIENT.NS | ADANI ENTERPRISES LIMITED | $3040.3 | 73.52 | 30% | $3389.92 | +12% |  |
| 366 | 2802.T | AJINOMOTO CO INC | $5721.0 | 138.38 | 30% | $6380.53 | +12% |  |
| 367 | ULTRACEMCO.NS | ULTRATECH CEMENT LIMITED | $11455.0 | 276.88 | 30% | $12766.59 | +11% |  |
| 368 | BSX | Boston Scientific Corporat | $44.2 | 2.39 | 11% | $49.16 | +11% |  |
| 369 | 2408.TW | NANYA TECHNOLOGY CORPORATI | $449.0 | 10.83 | 30% | $499.36 | +11% |  |
| 370 | GWO.TO | GREAT-WEST LIFECO INC | $88.7 | 4.65 | 11% | $97.92 | +10% |  |
| 371 | KMI | Kinder Morgan, Inc. | $33.01 | 1.49 | 14% | $36.27 | +10% |  |
| 372 | SHB-A.ST | Svenska Handelsbanken ser. | $141.3 | 12.14 | 1% | $155.34 | +10% |  |
| 373 | AD.AS | KONINKLIJKE AHOLD DELHAIZE | $35.51 | 2.52 | 4% | $38.91 | +10% |  |
| 374 | NVO | Novo Nordisk A/S | $47.64 | 4.17 | 0% | $52.12 | +9% |  |
| 375 | SEB-A.ST | Skandinaviska Enskilda Ban | $190.0 | 15.37 | 2% | $206.84 | +9% |  |
| 376 | 002475.SZ | LUXSHARE PRECISION INDUSTR | $68.0 | 2.33 | 21% | $74.0 | +9% |  |
| 377 | M&M.NS | MAHINDRA & MAHINDRA LTD | $3185.3 | 152.11 | 13% | $3466.46 | +9% |  |
| 378 | SAP | SAP  SE | $148.06 | 7.11 | 13% | $160.89 | +9% |  |
| 379 | 9432.T | NTT INC | $144.3 | 12.61 | 0% | $156.6 | +8% |  |
| 380 | HCLTECH.NS | HCL TECHNOLOGIES LTD | $1100.5 | 61.31 | 9% | $1193.12 | +8% |  |
| 381 | SBIN.NS | STATE BANK OF INDIA | $1045.2 | 91.16 | 0% | $1132.06 | +8% |  |
| 382 | ES | Eversource Energy (D/B/A) | $72.08 | 4.67 | 6% | $78.09 | +8% |  |
| 383 | 601898.SS | CHINA COAL ENERGY COMPANY | $12.51 | 1.09 | 0% | $13.54 | +8% |  |
| 384 | GEHC | GE HealthCare Technologies | $64.94 | 4.17 | 6% | $69.99 | +8% |  |
| 385 | ELE.MC | ENDESA,S.A. | $39.65 | 2.25 | 9% | $42.66 | +8% |  |
| 386 | DANS.VI | DANSKE BANK AS | $46.45 | 3.75 | 1% | $49.92 | +8% |  |
| 387 | NTPC.NS | NTPC LTD | $352.5 | 30.45 | 0% | $378.14 | +7% |  |
| 388 | ATO | Atmos Energy Corporation | $173.67 | 8.13 | 13% | $186.02 | +7% |  |
| 389 | RMD | ResMed Inc. | $198.6 | 10.37 | 10% | $212.16 | +7% |  |
| 390 | BHARTIARTL.NS | BHARTI AIRTEL LIMITED | $1849.9 | 44.42 | 29% | $1965.24 | +6% |  |
| 391 | HPE | Hewlett Packard Enterprise | $46.72 | 1.07 | 30% | $49.34 | +6% |  |
| 392 | AMS.MC | AMADEUS IT GROUP, S.A. | $51.14 | 3.05 | 7% | $54.0 | +6% |  |
| 393 | O39.SI | OCBC Bank | $24.86 | 1.65 | 5% | $26.2 | +5% |  |
| 394 | CNQ | Canadian Natural Resources | $39.6 | 3.36 | 0% | $41.73 | +5% |  |
| 395 | RELX | RELX PLC PLC | $30.92 | 1.48 | 12% | $32.56 | +5% |  |
| 396 | CLS | Celestica, Inc. | $361.4 | 8.24 | 30% | $379.94 | +5% |  |
| 397 | ADYEN.AS | ADYEN | $809.6 | 33.62 | 15% | $850.03 | +5% |  |
| 398 | DVN | Devon Energy Corporation | $42.6 | 3.59 | 0% | $44.58 | +5% |  |
| 399 | TD | Toronto Dominion Bank (The | $120.49 | 6.0 | 11% | $125.67 | +4% |  |
| 400 | 4901.T | FUJIFILM HOLDINGS CORPORAT | $3436.0 | 229.35 | 5% | $3583.43 | +4% |  |
| 401 | 002594.SZ | BYD COMPANY LIMITED | $78.2 | 1.95 | 27% | $81.4 | +4% |  |
| 402 | DB1.DE | DEUTSCHE BOERSE AG         | $238.2 | 11.21 | 12% | $247.53 | +4% |  |
| 403 | 4519.T | CHUGAI PHARMACEUTICAL CO | $7434.0 | 263.69 | 19% | $7716.38 | +4% |  |
| 404 | HLN | Haleon plc | $9.27 | 0.49 | 10% | $9.61 | +4% |  |
| 405 | TPR | Tapestry, Inc. | $146.0 | 3.28 | 30% | $151.24 | +4% |  |
| 406 | JCI | Johnson Controls Internati | $145.49 | 3.27 | 30% | $150.6 | +4% |  |
| 407 | UMC | United Microelectronics Co | $27.73 | 0.62 | 30% | $28.59 | +3% |  |
| 408 | MO | Altria Group, Inc. | $73.21 | 4.79 | 5% | $75.27 | +3% |  |
| 409 | AMZN | Amazon.com, Inc. | $227.01 | 7.17 | 21% | $233.15 | +3% |  |
| 410 | SE | Sea Limited | $89.01 | 2.54 | 24% | $91.43 | +3% |  |
| 411 | CME | CME Group Inc. | $225.0 | 11.72 | 10% | $230.17 | +2% |  |
| 412 | 2891.TW | CTBC FINANCIAL HOLDINGS CO | $70.3 | 4.06 | 7% | $71.88 | +2% |  |
| 413 | CSX | CSX Corporation | $47.44 | 1.63 | 19% | $48.35 | +2% |  |
| 414 | RDDT | Reddit, Inc. | $158.02 | 3.49 | 30% | $160.92 | +2% |  |
| 415 | AENA.MC | AENA, S.M.E., S.A. | $27.3 | 1.44 | 9% | $27.77 | +2% |  |
| 416 | BRK-B | Berkshire Hathaway Inc. Ne | $487.81 | 33.61 | 4% | $495.48 | +2% |  |
| 417 | ADP | Automatic Data Processing, | $216.31 | 10.73 | 10% | $219.52 | +2% |  |
| 418 | REGN | Regeneron Pharmaceuticals, | $620.14 | 40.93 | 4% | $629.49 | +2% |  |
| 419 | CBRE | CBRE Group Inc | $134.58 | 4.37 | 20% | $136.39 | +1% |  |
| 420 | IFC.TO | INTACT FINANCIAL CORPORATI | $288.76 | 18.77 | 5% | $292.15 | +1% |  |
| 421 | VHM.VN | VINHOMES JOINT STOCK COMPA | $162000.0 | 5571.4 | 19% | $163242.5 | +1% |  |
| 422 | XIACF | Xiaomi Corp. | $2.85 | 0.23 | 0% | $2.86 | +0% |  |
| 423 | MLYBY | Malayan Banking Berhad | $5.2 | 0.42 | 0% | $5.22 | +0% |  |
| 424 | PEG | Public Service Enterprise  | $82.63 | 4.52 | 8% | $82.78 | +0% |  |
| 425 | 0669.HK | TECHTRONIC IND | $127.2 | 5.12 | 15% | $127.39 | +0% |  |
| 426 | BLK | BlackRock, Inc. | $971.92 | 39.75 | 14% | $963.44 | -1% |  |
| 427 | HDB | HDFC Bank Limited | $25.37 | 1.41 | 8% | $25.14 | -1% |  |
| 428 | NDAQ | Nasdaq, Inc. | $77.65 | 3.32 | 13% | $76.91 | -1% |  |
| 429 | NTGY.MC | NATURGY ENERGY GROUP, S.A. | $28.0 | 2.22 | 0% | $27.57 | -2% |  |
| 430 | AZN | AstraZeneca PLC | $185.68 | 6.65 | 17% | $182.53 | -2% |  |
| 431 | KBCSF | KBC Group SA | $127.05 | 9.9 | 0% | $124.18 | -2% |  |
| 432 | SWED-A.ST | Swedbank AB ser A | $358.9 | 28.23 | 0% | $350.57 | -2% |  |
| 433 | HEN3.DE | Henkel AG & Co. KGaA       | $73.26 | 4.92 | 3% | $71.38 | -3% |  |
| 434 | CCL | Carnival Corporation Ltd. | $28.46 | 2.22 | 0% | $27.57 | -3% |  |
| 435 | COR | Cencora, Inc. | $286.95 | 13.06 | 11% | $277.88 | -3% |  |
| 436 | CSL.AX | CSL FPO [CSL] | $114.87 | 8.95 | 0% | $111.14 | -3% |  |
| 437 | BPE.MI | BPER BANCA | $13.34 | 1.04 | 0% | $12.92 | -3% |  |
| 438 | ASM.AS | ASM International N.V. | $960.8 | 20.12 | 30% | $927.71 | -3% |  |
| 439 | ATD.TO | ALIMENTATION COUCHE-TARD I | $93.57 | 4.79 | 8% | $89.46 | -4% |  |
| 440 | 300274.SZ | SUNGROW POWER SUPPLY CO LT | $151.05 | 5.79 | 15% | $144.12 | -5% |  |
| 441 | CCEP | Coca-Cola Europacific Part | $99.6 | 4.85 | 10% | $94.95 | -5% |  |
| 442 | ROP | Roper Technologies, Inc. | $332.42 | 16.02 | 10% | $316.05 | -5% |  |
| 443 | BAS.DE | BASF SE                    | $47.98 | 1.7 | 17% | $45.5 | -5% |  |
| 444 | 0066.HK | MTR CORPORATION | $30.94 | 2.36 | 0% | $29.31 | -5% |  |
| 445 | BAJAJFINSV.NS | BAJAJ FINSERV LTD. | $1766.9 | 61.06 | 17% | $1671.01 | -5% |  |
| 446 | PHM | PulteGroup, Inc. | $135.81 | 10.34 | 0% | $128.41 | -6% |  |
| 447 | AMRZ | Amrize Ltd | $55.88 | 2.09 | 15% | $52.74 | -6% |  |
| 448 | ED | Consolidated Edison, Inc. | $110.76 | 5.93 | 7% | $104.5 | -6% |  |
| 449 | ADANIPOWER.NS | ADANI POWER LTD | $229.1 | 6.63 | 21% | $215.68 | -6% |  |
| 450 | SLHN.SW | SWISS LIFE HOLDING AG N | $883.4 | 43.51 | 9% | $829.45 | -6% |  |
| 451 | BAJAJ-AUTO.NS | BAJAJ AUTO LIMITED | $9850.0 | 384.86 | 14% | $9242.67 | -6% |  |
| 452 | TGT | Target Corporation | $139.57 | 7.56 | 7% | $130.57 | -6% |  |
| 453 | ROST | Ross Stores, Inc. | $215.13 | 7.16 | 18% | $200.42 | -7% |  |
| 454 | PAYX | Paychex, Inc. | $96.72 | 4.89 | 8% | $90.01 | -7% |  |
| 455 | PHG | Koninklijke Philips N.V. N | $27.29 | 1.14 | 12% | $25.4 | -7% |  |
| 456 | STZ | Constellation Brands, Inc. | $144.45 | 9.61 | 2% | $134.5 | -7% |  |
| 457 | SPGI | S&P Global Inc. | $395.14 | 15.81 | 13% | $366.72 | -7% |  |
| 458 | 8766.T | TOKIO MARINE HOLDINGS INC | $6903.0 | 515.81 | 0% | $6405.55 | -7% |  |
| 459 | HO.PA | THALES | $214.0 | 8.12 | 14% | $197.84 | -8% |  |
| 460 | WDS | Woodside Energy Group Limi | $19.06 | 1.42 | 0% | $17.63 | -8% |  |
| 461 | CRH | CRH PLC | $113.05 | 5.39 | 9% | $103.84 | -8% |  |
| 462 | WBC.AX | WESTPAC FPO [WBC] | $35.14 | 2.03 | 5% | $32.24 | -8% |  |
| 463 | MA | Mastercard Incorporated | $488.92 | 17.26 | 16% | $447.67 | -8% |  |
| 464 | 6861.T | KEYENCE CORP | $77100.0 | 1833.67 | 25% | $70611.5 | -8% |  |
| 465 | JBL | Jabil Inc. | $374.64 | 7.42 | 30% | $342.13 | -9% |  |
| 466 | BMY | Bristol-Myers Squibb Compa | $55.39 | 3.57 | 3% | $50.43 | -9% |  |
| 467 | 2345.TW | ACCTON TECHNOLOGY CORP | $2380.0 | 46.89 | 30% | $2162.04 | -9% |  |
| 468 | ASSA-B.ST | ASSA ABLOY AB ser. B | $339.9 | 14.19 | 12% | $308.76 | -9% |  |
| 469 | 7010.SR | Saudi Telecom Co. | $43.88 | 2.99 | 1% | $39.8 | -9% |  |
| 470 | ASELS.IS | ASELSAN | $362.5 | 7.13 | 30% | $328.76 | -9% |  |
| 471 | 003816.SZ | CGN POWER CO LTD | $3.94 | 0.19 | 9% | $3.57 | -10% |  |
| 472 | TRI | Thomson Reuters Corp | $81.01 | 3.48 | 11% | $73.25 | -10% |  |
| 473 | RIO | Rio Tinto Plc | $95.11 | 6.09 | 3% | $85.86 | -10% |  |
| 474 | DLR | Digital Realty Trust, Inc. | $192.44 | 3.77 | 30% | $173.83 | -10% |  |
| 475 | SNY | Sanofi | $41.8 | 2.25 | 6% | $37.71 | -10% |  |
| 476 | IQV | IQVIA Holdings, Inc. | $186.43 | 8.05 | 11% | $166.94 | -10% |  |
| 477 | J36.SI | JMH USD | $62.76 | 3.77 | 4% | $56.1 | -11% |  |
| 478 | D05.SI | DBS | $65.43 | 3.83 | 4% | $58.19 | -11% |  |
| 479 | DUK | Duke Energy Corporation (H | $127.11 | 6.5 | 7% | $112.84 | -11% |  |
| 480 | ABNB | Airbnb, Inc. | $141.88 | 4.04 | 20% | $125.94 | -11% |  |
| 481 | KVUE | Kenvue Inc. | $18.96 | 0.84 | 10% | $16.84 | -11% |  |
| 482 | FERG | Ferguson Enterprises Inc. | $240.76 | 10.16 | 11% | $213.09 | -12% |  |
| 483 | CQP | Cheniere Energy Partners,  | $60.05 | 4.28 | 0% | $53.15 | -12% |  |
| 484 | AEE | Ameren Corporation | $114.53 | 5.55 | 8% | $101.08 | -12% |  |
| 485 | GD | General Dynamics Corporati | $344.7 | 15.89 | 9% | $304.03 | -12% |  |
| 486 | COIN | Coinbase Global, Inc. | $142.52 | 2.72 | 30% | $125.42 | -12% |  |
| 487 | ACS.MC | ACS,ACTIVIDADES DE CONSTRU | $126.9 | 3.81 | 19% | $111.49 | -12% |  |
| 488 | DSY.PA | DASSAULT SYSTEMES | $17.51 | 0.92 | 6% | $15.37 | -12% |  |
| 489 | 300124.SZ | SHENZHEN INOVANCE TECHNOLO | $63.28 | 1.73 | 21% | $55.49 | -12% |  |
| 490 | JBHT | J.B. Hunt Transport Servic | $274.68 | 6.43 | 25% | $240.58 | -12% |  |
| 491 | LT.NS | LARSEN & TOUBRO LTD. | $4202.1 | 116.79 | 20% | $3678.63 | -12% |  |
| 492 | 9633.HK | NONGFU SPRING | $42.54 | 1.63 | 13% | $37.13 | -13% |  |
| 493 | 8750.T | DAIICHI LIFE GROUP INC | $1726.5 | 121.26 | 0% | $1505.86 | -13% |  |
| 494 | PPG | PPG Industries, Inc. | $122.4 | 6.98 | 4% | $106.48 | -13% |  |
| 495 | TXN | Texas Instruments Incorpor | $311.81 | 5.86 | 30% | $270.2 | -13% |  |
| 496 | 8001.T | ITOCHU CORP | $1833.5 | 128.07 | 0% | $1590.43 | -13% |  |

### 🔴 BEARISH — 496 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | YUM | Yum! Brands, Inc. | $151.14 | 6.2 | 11% | $130.74 | -14% |  |
| 2 | ERIC | Ericsson | $11.06 | 0.77 | 0% | $9.56 | -14% |  |
| 3 | FTAI | FTAI Aviation Ltd. | $268.4 | 5.02 | 30% | $231.47 | -14% |  |
| 4 | NEE | NextEra Energy, Inc. | $87.7 | 3.94 | 9% | $75.35 | -14% |  |
| 5 | AZO | AutoZone, Inc. | $3059.04 | 145.3 | 8% | $2614.63 | -14% |  |
| 6 | V | Visa Inc. | $330.52 | 11.47 | 15% | $281.43 | -15% |  |
| 7 | NTAP | NetApp, Inc. | $154.59 | 6.35 | 11% | $131.63 | -15% |  |
| 8 | 9983.T | FAST RETAILING CO LTD | $84070.0 | 1559.55 | 30% | $71357.45 | -15% |  |
| 9 | 8801.T | MITSUI FUDOSAN | $1480.0 | 101.04 | 0% | $1254.76 | -15% |  |
| 10 | KDP | Keurig Dr Pepper Inc. | $32.52 | 1.35 | 10% | $27.53 | -15% |  |
| 11 | VIE.PA | VEOLIA ENVIRON. | $36.08 | 1.7 | 8% | $30.58 | -15% |  |
| 12 | AEP | American Electric Power Co | $137.0 | 6.75 | 7% | $115.93 | -15% |  |
| 13 | QSR | Restaurant Brands Internat | $73.23 | 3.11 | 10% | $61.95 | -15% |  |
| 14 | CAT | Caterpillar, Inc. | $1057.01 | 20.08 | 29% | $893.56 | -16% |  |
| 15 | MRSH | Marsh | $162.23 | 8.0 | 7% | $137.08 | -16% |  |
| 16 | EXC | Exelon Corporation | $46.75 | 2.73 | 3% | $39.47 | -16% |  |
| 17 | SAAB-B.ST | SAAB AB ser. B | $482.0 | 11.99 | 22% | $406.9 | -16% |  |
| 18 | CTRA | Coterra Energy Inc. | $32.56 | 2.17 | 0% | $27.41 | -16% |  |
| 19 | TMUS | T-Mobile US, Inc. | $181.57 | 9.41 | 6% | $152.58 | -16% |  |
| 20 | CPG.L | COMPASS GROUP PLC ORD 11 1 | $31.84 | 1.19 | 13% | $26.71 | -16% |  |
| 21 | UNP | Union Pacific Corporation | $267.73 | 12.15 | 8% | $223.76 | -16% |  |
| 22 | MDT | Medtronic plc. | $80.52 | 3.73 | 8% | $67.25 | -16% |  |
| 23 | GRMN | Garmin Ltd. | $235.41 | 8.97 | 12% | $195.61 | -17% |  |
| 24 | CSU.TO | CONSTELLATION SOFTWARE INC | $2764.23 | 49.76 | 30% | $2294.37 | -17% |  |
| 25 | KNEBV.HE | KONE Corporation | $49.77 | 1.89 | 12% | $41.31 | -17% |  |
| 26 | AAPL | Apple Inc. | $275.15 | 8.25 | 17% | $228.0 | -17% |  |
| 27 | 000725.SZ | BOE TECHNOLOGY GROUP | $7.79 | 0.17 | 25% | $6.44 | -17% |  |
| 28 | SLF | Sun Life Financial Inc. | $77.5 | 3.78 | 6% | $63.89 | -18% |  |
| 29 | HEIA.AS | HEINEKEN | $73.52 | 3.38 | 8% | $60.26 | -18% |  |
| 30 | RO.SW | ROCHE I | $336.4 | 16.05 | 7% | $275.01 | -18% |  |
| 31 | SIKA.SW | SIKA N | $166.3 | 6.5 | 11% | $135.9 | -18% |  |
| 32 | EBAY | eBay Inc. | $108.0 | 4.33 | 10% | $87.87 | -19% |  |
| 33 | MUFG | Mitsubishi UFJ Financial G | $20.02 | 1.31 | 0% | $16.27 | -19% |  |
| 34 | 601088.SS | CHINA SHENHUA ENERGY COMPA | $39.57 | 2.59 | 0% | $32.16 | -19% |  |
| 35 | 6301.T | KOMATSU | $6329.0 | 413.75 | 0% | $5138.12 | -19% |  |
| 36 | RELIANCE.NS | RELIANCE INDUSTRIES LTD | $1316.5 | 59.71 | 7% | $1058.6 | -20% |  |
| 37 | SMFG | Sumitomo Mitsui Financial  | $23.7 | 1.53 | 0% | $19.0 | -20% |  |
| 38 | IBM | International Business Mac | $258.27 | 11.31 | 8% | $206.75 | -20% |  |
| 39 | 8031.T | MITSUI & CO | $4508.0 | 290.77 | 0% | $3610.91 | -20% |  |
| 40 | NAB.AX | NAT. BANK FPO [NAB] | $37.51 | 2.0 | 4% | $29.99 | -20% |  |
| 41 | EME | EMCOR Group, Inc. | $862.66 | 29.76 | 13% | $688.48 | -20% |  |
| 42 | XYZ | Block, Inc. | $74.08 | 1.28 | 30% | $59.02 | -20% |  |
| 43 | IX | ORIX Corporation | $38.48 | 2.47 | 0% | $30.67 | -20% |  |
| 44 | MCD | McDonald's Corporation | $264.54 | 12.14 | 7% | $210.46 | -20% |  |
| 45 | ET | Energy Transfer LP | $19.18 | 1.2 | 0% | $15.25 | -20% |  |
| 46 | PPL | PPL Corporation | $37.0 | 1.63 | 8% | $29.43 | -20% |  |
| 47 | LR.PA | LEGRAND | $145.15 | 4.86 | 14% | $115.19 | -21% |  |
| 48 | WDAY | Workday, Inc. | $113.77 | 3.21 | 18% | $90.39 | -21% |  |
| 49 | FIX | Comfort Systems USA, Inc. | $2017.57 | 34.7 | 30% | $1599.97 | -21% |  |
| 50 | KEYS | Keysight Technologies Inc. | $360.06 | 6.19 | 30% | $285.41 | -21% |  |
| 51 | DHI | D.R. Horton, Inc. | $166.95 | 10.65 | 0% | $132.26 | -21% |  |
| 52 | 8035.T | TOKYO ELECTRON | $72920.0 | 1250.64 | 30% | $57665.44 | -21% |  |
| 53 | 9434.T | SOFTBANK CORP. | $204.7 | 11.26 | 3% | $161.56 | -21% |  |
| 54 | ABBN.SW | ABB LTD N | $84.88 | 2.16 | 20% | $66.75 | -21% |  |
| 55 | ANZ.AX | ANZ GROUP FPO [ANZ] | $35.04 | 1.97 | 2% | $27.53 | -21% |  |
| 56 | MSCI | MSCI Inc. | $544.56 | 17.53 | 14% | $428.24 | -21% |  |
| 57 | AWK | American Water Works Compa | $130.0 | 5.64 | 8% | $102.1 | -22% |  |
| 58 | 300476.SZ | VICTORY GIANT TECHNOLOGY ( | $319.55 | 5.43 | 30% | $250.37 | -22% |  |
| 59 | XEL | Xcel Energy Inc. | $81.75 | 3.47 | 8% | $63.93 | -22% |  |
| 60 | AVB | AvalonBay Communities, Inc | $186.13 | 8.08 | 8% | $145.53 | -22% |  |
| 61 | VEEV | Veeva Systems Inc. | $158.08 | 5.64 | 12% | $122.77 | -22% |  |
| 62 | 8630.T | SOMPO HOLDINGS INC | $6126.0 | 250.92 | 9% | $4747.88 | -22% |  |
| 63 | 3382.T | SEVEN & I HOLDINGS CO LTD | $1903.5 | 118.83 | 0% | $1475.68 | -22% |  |
| 64 | VRTX | Vertex Pharmaceuticals Inc | $480.18 | 16.85 | 12% | $371.25 | -23% |  |
| 65 | LONN.SW | LONZA N | $531.4 | 13.0 | 20% | $409.98 | -23% |  |
| 66 | MARUTI.NS | MARUTI SUZUKI INDIA LTD. | $13753.0 | 467.33 | 13% | $10621.8 | -23% |  |
| 67 | CP | Canadian Pacific Kansas Ci | $87.04 | 3.15 | 11% | $67.08 | -23% |  |
| 68 | D | Dominion Energy, Inc. | $69.51 | 3.39 | 5% | $53.58 | -23% |  |
| 69 | APH | Amphenol Corporation | $165.15 | 3.48 | 24% | $127.21 | -23% |  |
| 70 | RL | Ralph Lauren Corporation | $410.11 | 15.09 | 11% | $315.77 | -23% |  |
| 71 | PEP | Pepsico, Inc. | $139.52 | 6.38 | 6% | $107.23 | -23% |  |
| 72 | 600519.SS | KWEICHOW MOUTAI | $1168.63 | 66.06 | 2% | $896.9 | -23% |  |
| 73 | HOT.F | HOCHTIEF AG                | $499.6 | 10.7 | 24% | $382.06 | -24% |  |
| 74 | ETR | Entergy Corporation | $115.38 | 3.92 | 12% | $87.88 | -24% |  |
| 75 | ELV | Elevance Health, Inc. | $387.32 | 23.59 | 0% | $292.95 | -24% |  |
| 76 | KO | Coca-Cola Company (The) | $80.42 | 3.18 | 9% | $60.51 | -25% |  |
| 77 | URI | United Rentals, Inc. | $1139.51 | 39.09 | 12% | $857.42 | -25% |  |
| 78 | WEC | WEC Energy Group, Inc. | $117.07 | 4.99 | 7% | $87.97 | -25% |  |
| 79 | UL | Unilever PLC | $60.54 | 2.95 | 4% | $45.38 | -25% |  |
| 80 | ENR.F | Siemens Energy AG          | $157.02 | 2.55 | 30% | $117.58 | -25% |  |
| 81 | AJG | Arthur J. Gallagher & Co. | $217.86 | 6.19 | 16% | $162.85 | -25% |  |
| 82 | 0388.HK | HKEX | $362.2 | 14.88 | 8% | $270.13 | -25% |  |
| 83 | CPRT | Copart, Inc. | $30.05 | 1.61 | 2% | $22.4 | -26% |  |
| 84 | BAM | Brookfield Asset Managemen | $44.66 | 1.56 | 11% | $33.22 | -26% |  |
| 85 | VMC | Vulcan Materials Company ( | $312.97 | 8.45 | 17% | $232.73 | -26% |  |
| 86 | ADI | Analog Devices, Inc. | $417.93 | 6.73 | 30% | $310.31 | -26% |  |
| 87 | ORLY | O'Reilly Automotive, Inc. | $86.9 | 3.07 | 11% | $64.47 | -26% |  |
| 88 | ONC | BeOne Medicines Ltd. | $275.34 | 4.43 | 30% | $204.26 | -26% |  |
| 89 | 600111.SS | CHINA NTHN RARE EARTH (GP) | $47.26 | 0.76 | 30% | $35.04 | -26% |  |
| 90 | PM | Philip Morris Internationa | $178.93 | 7.1 | 8% | $132.15 | -26% |  |
| 91 | CEZ.PR | CEZ | $1207.0 | 53.77 | 6% | $889.38 | -26% |  |
| 92 | BIP | Brookfield Infrastructure  | $36.39 | 0.66 | 27% | $26.82 | -26% |  |
| 93 | AVGO | Broadcom Inc. | $378.91 | 6.02 | 30% | $277.57 | -27% |  |
| 94 | AMAT | Applied Materials, Inc. | $668.0 | 10.62 | 30% | $489.67 | -27% |  |
| 95 | LMT | Lockheed Martin Corporatio | $505.02 | 20.66 | 8% | $370.05 | -27% |  |
| 96 | CRS | Carpenter Technology Corpo | $599.24 | 9.53 | 30% | $439.42 | -27% |  |
| 97 | ENGI.PA | ENGIE | $27.32 | 1.51 | 1% | $19.99 | -27% |  |
| 98 | PSX | Phillips 66 | $171.76 | 10.12 | 0% | $125.67 | -27% |  |
| 99 | 8015.T | TOYOTA TSUSHO CORP | $5958.0 | 351.0 | 0% | $4358.87 | -27% |  |
| 100 | 6857.T | ADVANTEST CORP | $32440.0 | 513.37 | 30% | $23670.85 | -27% |  |
| 101 | ARES | Ares Management Corporatio | $112.47 | 2.17 | 25% | $82.14 | -27% |  |
| 102 | HWM | Howmet Aerospace Inc. | $273.14 | 4.32 | 30% | $199.19 | -27% |  |
| 103 | ITW | Illinois Tool Works Inc. | $270.6 | 10.77 | 8% | $197.16 | -27% |  |
| 104 | WMMVF | Wal-Mart De Mexico S.A.B.  | $2.92 | 0.16 | 1% | $2.13 | -27% |  |
| 105 | ADM | Archer-Daniels-Midland Com | $76.54 | 2.24 | 15% | $55.8 | -27% |  |
| 106 | LOW | Lowe's Companies, Inc. | $221.93 | 11.83 | 2% | $160.38 | -28% |  |
| 107 | SU.PA | SCHNEIDER ELECTRIC SE | $277.75 | 7.97 | 15% | $199.59 | -28% |  |
| 108 | 2360.TW | CHROMA ATE INC | $2035.0 | 31.68 | 30% | $1460.73 | -28% |  |
| 109 | UNH | UnitedHealth Group Incorpo | $415.53 | 13.3 | 12% | $297.24 | -28% |  |
| 110 | ROK | Rockwell Automation, Inc. | $479.39 | 9.64 | 23% | $342.96 | -28% |  |
| 111 | SUNPHARMA.NS | SUN PHARMACEUTICAL IND L | $1861.5 | 47.87 | 18% | $1330.87 | -28% |  |
| 112 | HM-B.ST | Hennes & Mauritz AB, H & M | $166.0 | 7.66 | 4% | $118.77 | -28% |  |
| 113 | 5803.T | FUJIKURA | $6131.0 | 94.61 | 30% | $4362.35 | -29% |  |
| 114 | GM | General Motors Company | $78.53 | 2.74 | 10% | $55.85 | -29% |  |
| 115 | TMO | Thermo Fisher Scientific I | $505.75 | 18.21 | 10% | $358.28 | -29% |  |
| 116 | FDX | FedEx Corporation | $329.44 | 18.75 | 0% | $232.85 | -29% |  |
| 117 | L.TO | LOBLAW CO | $66.09 | 2.21 | 11% | $46.73 | -29% |  |
| 118 | ITC.NS | ITC LTD | $290.0 | 16.5 | 0% | $204.9 | -29% |  |
| 119 | MLM | Martin Marietta Materials, | $628.94 | 15.98 | 18% | $444.27 | -29% |  |
| 120 | CFR.SW | RICHEMONT N | $187.15 | 5.42 | 14% | $131.89 | -30% |  |
| 121 | ASX | ASE Technology Holding Co. | $41.85 | 0.64 | 30% | $29.51 | -30% |  |
| 122 | A | Agilent Technologies, Inc. | $135.51 | 4.99 | 9% | $95.52 | -30% |  |
| 123 | UPS | United Parcel Service, Inc | $109.31 | 6.18 | 0% | $76.75 | -30% |  |
| 124 | WM | Waste Management, Inc. | $223.08 | 6.92 | 13% | $156.31 | -30% |  |
| 125 | ITX.MC | INDUSTRIA DE DISE...O TEXT | $55.86 | 2.02 | 9% | $38.86 | -30% |  |
| 126 | HUBB | Hubbell Inc | $536.04 | 16.94 | 12% | $373.23 | -30% |  |
| 127 | IHG | Intercontinental Hotels Gr | $174.13 | 4.86 | 15% | $121.18 | -30% |  |
| 128 | HBAN.SW | HELVETIA BALOISE HOLDING N | $208.4 | 10.32 | 2% | $145.0 | -30% |  |
| 129 | CMI | Cummins Inc. | $727.59 | 19.28 | 16% | $505.92 | -30% |  |
| 130 | XYL | Xylem Inc. | $117.0 | 4.02 | 10% | $81.06 | -31% |  |
| 131 | FE | FirstEnergy Corp. | $48.01 | 1.84 | 8% | $33.26 | -31% |  |
| 132 | GWW | W.W. Grainger, Inc. | $1374.78 | 37.26 | 15% | $949.03 | -31% |  |
| 133 | COP | ConocoPhillips | $106.41 | 5.9 | 0% | $73.27 | -31% |  |
| 134 | CDI.PA | CHRISTIAN DIOR | $453.2 | 25.09 | 0% | $311.58 | -31% |  |
| 135 | TLS.AX | TELSTRA FPO [TLS] | $5.15 | 0.2 | 7% | $3.54 | -31% |  |
| 136 | CNP | CenterPoint Energy, Inc (H | $44.22 | 1.63 | 8% | $30.41 | -31% |  |
| 137 | 4568.T | DAIICHI SANKYO COMPANY LIM | $2535.5 | 140.39 | 0% | $1743.42 | -31% |  |
| 138 | PFE | Pfizer, Inc. | $23.67 | 1.31 | 0% | $16.27 | -31% |  |
| 139 | WMB | Williams Companies, Inc. ( | $77.53 | 2.28 | 13% | $53.19 | -31% |  |
| 140 | MDLZ | Mondelez International, In | $61.2 | 2.02 | 11% | $42.0 | -31% |  |
| 141 | RPRX | Royalty Pharma plc | $54.69 | 1.9 | 10% | $37.48 | -32% |  |
| 142 | ASML | ASML Holding N.V. - New Yo | $1841.18 | 29.46 | 28% | $1256.55 | -32% |  |
| 143 | SO | Southern Company (The) | $95.91 | 3.91 | 6% | $65.41 | -32% |  |
| 144 | SONY | Sony Group Corporation | $19.32 | 1.06 | 0% | $13.16 | -32% |  |
| 145 | MCO | Moody's Corporation | $438.85 | 13.96 | 11% | $297.03 | -32% |  |
| 146 | TJX | TJX Companies, Inc. (The) | $155.19 | 5.14 | 10% | $104.68 | -32% |  |
| 147 | SHL.DE | Siemens Healthineers AG    | $34.2 | 1.86 | 0% | $23.1 | -32% |  |
| 148 | EPI-A.ST | Epiroc AB ser. A | $255.6 | 7.04 | 14% | $172.05 | -33% |  |
| 149 | 8308.T | RESONA HOLDINGS | $2102.0 | 113.78 | 0% | $1412.97 | -33% |  |
| 150 | 601211.SS | GUOTAI HAITONG SECURITIES  | $17.4 | 0.94 | 0% | $11.67 | -33% |  |
| 151 | 6702.T | FUJITSU | $3199.0 | 172.74 | 0% | $2145.16 | -33% |  |
| 152 | WWD | Woodward, Inc. | $436.44 | 8.34 | 23% | $291.58 | -33% |  |
| 153 | SCMN.SW | SWISSCOM N | $640.0 | 23.83 | 8% | $427.03 | -33% |  |
| 154 | OXY | Occidental Petroleum Corpo | $51.21 | 0.74 | 30% | $34.12 | -33% |  |
| 155 | FLEX | Flex Ltd. | $161.28 | 2.32 | 30% | $106.97 | -34% |  |
| 156 | AFRM | Affirm Holdings, Inc. | $76.85 | 1.1 | 30% | $50.72 | -34% |  |
| 157 | MTD | Mettler-Toledo Internation | $1243.42 | 42.52 | 9% | $819.17 | -34% |  |
| 158 | PG | Procter & Gamble Company ( | $148.5 | 6.85 | 3% | $97.47 | -34% |  |
| 159 | DOV | Dover Corporation | $230.73 | 8.01 | 9% | $151.44 | -34% |  |
| 160 | UMG.AS | UNIVERSAL MUSIC GROUP | $18.14 | 0.83 | 3% | $11.87 | -35% |  |
| 161 | GULF.BK | GULF_GULF DEVELOPMENT | $59.75 | 1.68 | 13% | $39.05 | -35% |  |
| 162 | ABT | Abbott Laboratories | $93.24 | 3.57 | 6% | $60.66 | -35% |  |
| 163 | DEO | Diageo plc | $82.61 | 4.33 | 0% | $53.77 | -35% |  |
| 164 | AI.PA | AIR LIQUIDE | $171.24 | 5.52 | 10% | $111.36 | -35% |  |
| 165 | MTZ | MasTec, Inc. | $403.57 | 5.69 | 30% | $262.36 | -35% |  |
| 166 | ADANIPORTS.NS | ADANI PORT & SEZ LTD | $1795.0 | 58.19 | 10% | $1160.1 | -35% |  |
| 167 | CNI | Canadian National Railway  | $120.36 | 5.34 | 3% | $77.55 | -36% |  |
| 168 | APD | Air Products and Chemicals | $279.93 | 9.49 | 9% | $179.59 | -36% |  |
| 169 | MQG.AX | MACQ GROUP FPO [MQG] | $249.36 | 9.71 | 6% | $159.85 | -36% |  |
| 170 | SYY | Sysco Corporation | $80.85 | 3.6 | 3% | $51.4 | -36% |  |
| 171 | E | ENI S.p.A. | $46.79 | 2.26 | 1% | $29.5 | -37% |  |
| 172 | ALL.AX | ARISTOCRAT FPO [ALL] | $58.69 | 2.38 | 5% | $36.96 | -37% |  |
| 173 | ALNY | Alnylam Pharmaceuticals, I | $293.17 | 3.99 | 30% | $183.97 | -37% |  |
| 174 | AMGN | Amgen Inc. | $352.82 | 14.36 | 4% | $221.17 | -37% |  |
| 175 | TDY | Teledyne Technologies Inco | $627.19 | 19.76 | 10% | $393.05 | -37% |  |
| 176 | WSM | Williams-Sonoma, Inc. | $240.06 | 8.93 | 6% | $150.09 | -38% |  |
| 177 | IBKR | Interactive Brokers Group, | $92.16 | 2.33 | 15% | $57.52 | -38% |  |
| 178 | TT | Trane Technologies plc | $503.46 | 13.09 | 14% | $314.09 | -38% |  |
| 179 | SCHN.SW | SCHINDLER N | $259.0 | 9.53 | 6% | $161.61 | -38% |  |
| 180 | DTE | DTE Energy Company | $152.81 | 6.08 | 5% | $95.36 | -38% |  |
| 181 | IBE.MC | ACCIONES IBERDROLA | $21.72 | 0.8 | 6% | $13.53 | -38% |  |
| 182 | 0019.HK | SWIRE PACIFIC A | $82.95 | 2.11 | 14% | $51.55 | -38% |  |
| 183 | ATI | ATI Inc. | $199.5 | 3.03 | 27% | $123.83 | -38% |  |
| 184 | KNIN.SW | KUEHNE+NAGEL INT N | $194.05 | 7.02 | 7% | $120.34 | -38% |  |
| 185 | JNJ | Johnson & Johnson | $244.88 | 8.62 | 7% | $151.62 | -38% |  |
| 186 | DTG.F | Daimler Truck Holding AG   | $41.41 | 1.57 | 6% | $25.58 | -38% |  |
| 187 | VOLV-A.ST | Volvo, AB ser. A | $325.8 | 16.18 | 0% | $200.93 | -38% |  |
| 188 | WST | West Pharmaceutical Servic | $346.56 | 7.49 | 18% | $213.79 | -38% |  |
| 189 | LHX | L3Harris Technologies, Inc | $288.52 | 9.2 | 9% | $176.43 | -39% |  |
| 190 | QCOM | QUALCOMM Incorporated | $204.9 | 9.3 | 2% | $125.09 | -39% |  |
| 191 | WAB | Westinghouse Air Brake Tec | $282.45 | 7.06 | 14% | $172.47 | -39% |  |
| 192 | ANET | Arista Networks, Inc. | $165.45 | 2.91 | 23% | $100.91 | -39% |  |
| 193 | TKO | TKO Group Holdings, Inc. | $203.8 | 2.69 | 30% | $124.03 | -39% |  |
| 194 | KMB | Kimberly-Clark Corporation | $108.1 | 5.17 | 0% | $65.79 | -39% |  |
| 195 | LRCX | Lam Research Corporation | $401.82 | 5.3 | 30% | $244.38 | -39% |  |
| 196 | MC.PA | LVMH | $489.55 | 21.85 | 2% | $296.51 | -39% |  |
| 197 | SRE | DBA Sempra | $93.43 | 2.94 | 9% | $56.25 | -40% |  |
| 198 | 603288.SS | FOSHAN HAITIAN FLAVOURING  | $32.98 | 1.25 | 5% | $19.81 | -40% |  |
| 199 | MSI | Motorola Solutions, Inc. | $397.01 | 12.39 | 9% | $238.15 | -40% |  |
| 200 | EMR | Emerson Electric Company | $145.34 | 4.32 | 10% | $87.11 | -40% |  |
| 201 | 600176.SS | CHINA JUSHI CO LTD | $74.12 | 0.96 | 30% | $44.26 | -40% |  |
| 202 | CAH | Cardinal Health, Inc. | $234.75 | 6.55 | 11% | $139.61 | -40% |  |
| 203 | SLB | SLB Limited | $47.42 | 2.27 | 0% | $28.19 | -41% |  |
| 204 | CBA.AX | CWLTH BANK FPO [CBA] | $162.02 | 6.21 | 4% | $96.1 | -41% |  |
| 205 | HEI | Heico Corporation | $342.45 | 5.62 | 24% | $203.04 | -41% |  |
| 206 | 300502.SZ | EOPTOLINK TECHNOLOGY INC L | $566.0 | 7.26 | 30% | $334.75 | -41% |  |
| 207 | NVT | nVent Electric plc | $171.91 | 2.94 | 23% | $101.54 | -41% |  |
| 208 | 2308.TW | DELTA ELECTRONIC | $1810.0 | 23.17 | 30% | $1068.34 | -41% |  |
| 209 | SYK | Stryker Corporation | $316.11 | 8.63 | 12% | $185.61 | -41% |  |
| 210 | SAND.ST | Sandvik AB | $389.6 | 11.82 | 9% | $228.66 | -41% |  |
| 211 | DOL.TO | DOLLARAMA INC | $191.95 | 4.86 | 13% | $112.68 | -41% |  |
| 212 | STRL | Sterling Infrastructure, I | $881.92 | 11.2 | 30% | $516.42 | -41% |  |
| 213 | CTAS | Cintas Corporation | $169.09 | 4.73 | 11% | $98.71 | -42% |  |
| 214 | BX | Blackstone Inc. | $114.18 | 3.9 | 7% | $66.61 | -42% |  |
| 215 | RSG | Republic Services, Inc. | $213.5 | 6.96 | 8% | $124.08 | -42% |  |
| 216 | 600276.SS | JIANGSU HENGRUI PHARMACEUT | $48.67 | 1.22 | 13% | $28.29 | -42% |  |
| 217 | LISP.SW | LINDT PS | $9560.0 | 313.31 | 7% | $5557.25 | -42% |  |
| 218 | H.TO | HYDRO ONE LIMITED | $58.42 | 2.28 | 4% | $33.91 | -42% |  |
| 219 | CCI | Crown Castle Inc. | $79.53 | 2.37 | 9% | $45.95 | -42% |  |
| 220 | 2327.TW | YAGEO CORP | $1015.0 | 12.71 | 30% | $586.04 | -42% |  |
| 221 | SNDK | Sandisk Corporation | $2335.0 | 29.19 | 30% | $1345.91 | -42% |  |
| 222 | WES.AX | WESFARMER FPO [WES] | $90.74 | 2.7 | 9% | $52.3 | -42% |  |
| 223 | ENEL.MI | ENEL | $10.07 | 0.38 | 4% | $5.79 | -42% |  |
| 224 | LIN | Linde plc | $522.28 | 15.09 | 10% | $299.2 | -43% |  |
| 225 | ESLT | Elbit Systems Ltd. | $732.71 | 12.38 | 22% | $419.62 | -43% |  |
| 226 | MAR | Marriott International | $378.91 | 9.55 | 13% | $216.67 | -43% |  |
| 227 | FAST | Fastenal Company | $46.92 | 1.13 | 14% | $26.78 | -43% |  |
| 228 | 6920.T | LASERTEC CORP | $50000.0 | 967.88 | 19% | $28562.58 | -43% |  |
| 229 | RTX | RTX Corporation | $186.59 | 5.34 | 10% | $106.22 | -43% |  |
| 230 | CVNA | Carvana Co. | $66.2 | 1.73 | 12% | $37.69 | -43% |  |
| 231 | ILMN | Illumina, Inc. | $177.65 | 5.51 | 8% | $100.77 | -43% |  |
| 232 | 5016.T | JX ADVANCED METALS CORPORA | $4553.0 | 112.89 | 13% | $2571.53 | -44% |  |
| 233 | WMT | Walmart Inc. | $115.78 | 2.84 | 13% | $65.12 | -44% |  |
| 234 | VRT | Vertiv Holdings, LLC | $325.57 | 3.97 | 30% | $183.05 | -44% |  |
| 235 | MMM | 3M Company | $167.97 | 5.19 | 8% | $94.35 | -44% |  |
| 236 | WN.TO | WESTON GEORGE | $104.01 | 2.7 | 12% | $58.46 | -44% |  |
| 237 | NVS | Novartis AG | $155.12 | 6.98 | 0% | $86.68 | -44% |  |
| 238 | IDXX | IDEXX Laboratories, Inc. | $554.94 | 13.6 | 13% | $310.21 | -44% |  |
| 239 | ALC | Alcon Inc. | $68.13 | 1.67 | 13% | $38.11 | -44% |  |
| 240 | CSCO | Cisco Systems, Inc. | $118.97 | 3.0 | 12% | $66.42 | -44% |  |
| 241 | HAL.NS | HINDUSTAN AERONAUTICS LTD | $4364.0 | 136.3 | 8% | $2433.38 | -44% |  |
| 242 | O | Realty Income Corporation | $62.04 | 1.22 | 18% | $34.51 | -44% |  |
| 243 | FTS | Fortis Inc. | $57.76 | 2.39 | 2% | $32.1 | -44% |  |
| 244 | 601985.SS | CHINA NATIONAL NUCLEAR POW | $8.93 | 0.4 | 0% | $4.97 | -44% |  |
| 245 | HD | Home Depot, Inc. (The) | $345.0 | 14.08 | 2% | $191.26 | -45% |  |
| 246 | ECL | Ecolab Inc. | $281.2 | 7.4 | 11% | $155.9 | -45% |  |
| 247 | ISRG | Intuitive Surgical, Inc. | $399.69 | 8.23 | 17% | $221.03 | -45% |  |
| 248 | BN.PA | DANONE | $72.36 | 2.82 | 3% | $40.03 | -45% |  |
| 249 | 600487.SS | HENGTONG OPTIC-ELECTRIC CO | $110.81 | 1.33 | 30% | $61.32 | -45% |  |
| 250 | MAERSK-B.CO | A.P. Møller - Mærsk B A/S | $15980.0 | 710.36 | 0% | $8821.55 | -45% |  |
| 251 | 1211.SR | Saudi Arabian Mining Co. | $60.1 | 2.28 | 3% | $33.14 | -45% |  |
| 252 | 300433.SZ | LENS TECHNOLOGY CO LTD | $55.59 | 0.67 | 30% | $30.6 | -45% |  |
| 253 | 8802.T | MITSUBISHI ESTATE CO | $4101.0 | 181.67 | 0% | $2256.06 | -45% |  |
| 254 | 6981.T | MURATA MANUFACTURING CO | $10770.0 | 127.71 | 30% | $5888.55 | -45% |  |
| 255 | BN | Brookfield Corporation | $43.0 | 0.51 | 30% | $23.52 | -45% |  |
| 256 | SHW | Sherwin-Williams Company ( | $339.08 | 10.41 | 8% | $185.59 | -45% |  |
| 257 | 002050.SZ | ZHEJIANG SANHUA INTELLIGEN | $41.5 | 1.01 | 13% | $22.7 | -45% |  |
| 258 | GALD.SW | GALDERMA GROUP N | $176.8 | 2.09 | 30% | $96.37 | -46% |  |
| 259 | 6367.T | DAIKIN INDUSTRIES | $24050.0 | 939.69 | 2% | $13074.63 | -46% |  |
| 260 | MNST | Monster Beverage Corporati | $95.83 | 2.07 | 15% | $52.02 | -46% |  |
| 261 | GE | GE Aerospace | $371.36 | 8.06 | 15% | $200.36 | -46% |  |
| 262 | AME | AMETEK, Inc. | $240.95 | 6.63 | 10% | $129.91 | -46% |  |
| 263 | GIVN.SW | GIVAUDAN N | $3381.0 | 115.33 | 5% | $1821.83 | -46% |  |
| 264 | SDZ.SW | SANDOZ GROUP N | $72.02 | 1.69 | 13% | $38.8 | -46% |  |
| 265 | EL.PA | ESSILORLUXOTTICA | $166.35 | 4.98 | 8% | $89.45 | -46% |  |
| 266 | XOM | Exxon Mobil Corporation | $137.55 | 5.94 | 0% | $73.77 | -46% |  |
| 267 | BA | Boeing Company (The) | $218.12 | 2.53 | 30% | $116.66 | -46% |  |
| 268 | MKSI | MKS Inc. | $410.31 | 4.76 | 30% | $219.48 | -46% |  |
| 269 | TPL | Texas Pacific Land Corpora | $391.04 | 7.27 | 18% | $209.18 | -46% |  |
| 270 | BEL.NS | BHARAT ELECTRONICS LTD | $408.5 | 8.31 | 16% | $218.25 | -47% |  |
| 271 | RACE | Ferrari N.V. | $352.2 | 10.21 | 8% | $187.6 | -47% |  |
| 272 | ON | ON Semiconductor Corporati | $118.74 | 1.37 | 30% | $63.17 | -47% |  |
| 273 | 6954.T | FANUC CORPORATION | $7026.0 | 178.78 | 11% | $3741.11 | -47% |  |
| 274 | KR | Kroger Company (The) | $57.77 | 1.71 | 8% | $30.59 | -47% |  |
| 275 | NESN.SW | NESTLE N | $82.71 | 3.51 | 0% | $43.59 | -47% |  |
| 276 | TER | Teradyne, Inc. | $471.96 | 5.38 | 30% | $248.07 | -47% |  |
| 277 | PBA | Pembina Pipeline Corp. | $47.14 | 1.87 | 1% | $24.74 | -48% |  |
| 278 | OR.PA | L'OREAL | $387.9 | 11.44 | 7% | $202.91 | -48% |  |
| 279 | PH | Parker-Hannifin Corporatio | $989.91 | 27.12 | 9% | $515.82 | -48% |  |
| 280 | NOW | ServiceNow, Inc. | $89.52 | 1.68 | 18% | $46.65 | -48% |  |
| 281 | 7741.T | HOYA CORP | $25575.0 | 744.42 | 8% | $13271.71 | -48% |  |
| 282 | PSA | Public Storage | $320.74 | 9.69 | 7% | $165.88 | -48% |  |
| 283 | GMG.AX | GOOD GROUP STAPLED [GMG] | $32.01 | 0.84 | 10% | $16.56 | -48% |  |
| 284 | AIR.PA | AIRBUS SE | $191.44 | 6.32 | 5% | $98.65 | -48% |  |
| 285 | TDG | Transdigm Group Incorporat | $1332.56 | 31.98 | 12% | $684.41 | -49% |  |
| 286 | SBUX | Starbucks Corporation | $103.16 | 1.31 | 26% | $52.55 | -49% |  |
| 287 | CASY | Caseys General Stores, Inc | $784.71 | 19.16 | 11% | $398.42 | -49% |  |
| 288 | TRP | TC Energy Corporation | $70.19 | 2.39 | 4% | $35.56 | -49% |  |
| 289 | MRK.DE | MERCK KGAA                 | $143.3 | 5.84 | 0% | $72.52 | -49% |  |
| 290 | DHR | Danaher Corporation | $193.21 | 5.16 | 9% | $97.6 | -50% |  |
| 291 | 285A.T | KIOXIA HOLDINGS CORPORATIO | $92180.0 | 1007.35 | 30% | $46447.65 | -50% |  |
| 292 | ATCO-B.ST | Atlas Copco AB ser. B | $167.9 | 5.36 | 5% | $84.49 | -50% |  |
| 293 | ETN | Eaton Corporation, PLC | $419.87 | 10.2 | 10% | $208.77 | -50% |  |
| 294 | CTVA | Corteva, Inc. | $81.62 | 1.85 | 12% | $40.58 | -50% |  |
| 295 | ODFL | Old Dominion Freight Line, | $220.12 | 4.8 | 13% | $109.0 | -50% |  |
| 296 | Q | Qnity Electronics, Inc. | $167.49 | 3.1 | 16% | $82.79 | -51% |  |
| 297 | CVS | CVS Health Corporation | $104.66 | 2.28 | 13% | $51.64 | -51% |  |
| 298 | 300308.SZ | ZHONGJI INNOLIGHT CO LTD | $1253.89 | 13.37 | 30% | $616.47 | -51% |  |
| 299 | 6501.T | HITACHI | $4478.0 | 176.7 | 0% | $2194.34 | -51% |  |
| 300 | HLT | Hilton Worldwide Holdings  | $340.55 | 6.54 | 15% | $165.78 | -51% |  |
| 301 | VACN.SW | VAT GROUP N | $677.8 | 7.15 | 30% | $329.68 | -51% |  |
| 302 | HON | Honeywell International In | $231.24 | 6.27 | 8% | $112.15 | -52% |  |
| 303 | COST | Costco Wholesale Corporati | $942.24 | 19.88 | 13% | $452.85 | -52% |  |
| 304 | IFX.DE | INFINEON TECHNOLOGIES AG   | $78.9 | 0.82 | 30% | $37.81 | -52% |  |
| 305 | MRVL | Marvell Technology, Inc. | $281.26 | 2.9 | 30% | $133.72 | -52% |  |
| 306 | STX | Seagate Technology Holding | $1025.36 | 10.56 | 30% | $486.91 | -52% |  |
| 307 | EQT.ST | EQT AB | $261.4 | 6.84 | 8% | $124.0 | -53% |  |
| 308 | NSC | Norfolk Southern Corporati | $312.06 | 11.86 | 0% | $147.28 | -53% |  |
| 309 | BDX | Becton, Dickinson and Comp | $151.38 | 5.74 | 0% | $71.28 | -53% |  |
| 310 | AOT.BK | AOT_AIRPORTS OF THAILAND | $62.25 | 1.27 | 13% | $29.19 | -53% |  |
| 311 | CCJ | Cameco Corporation | $103.58 | 1.05 | 30% | $48.41 | -53% |  |
| 312 | PWR | Quanta Services, Inc. | $718.59 | 7.26 | 30% | $334.75 | -53% |  |
| 313 | NBIS | Nebius Group N.V. | $256.63 | 2.59 | 30% | $119.42 | -54% |  |
| 314 | NKE | Nike, Inc. | $40.9 | 1.52 | 0% | $18.88 | -54% |  |
| 315 | EQR | Equity Residential | $67.17 | 2.5 | 0% | $31.05 | -54% |  |
| 316 | 4063.T | SHIN-ETSU CHEMICAL CO | $6835.0 | 252.39 | 0% | $3134.29 | -54% |  |
| 317 | ENB | Enbridge Inc | $56.19 | 2.07 | 0% | $25.71 | -54% |  |
| 318 | WAT | Waters Corporation | $376.89 | 7.88 | 12% | $172.19 | -54% |  |
| 319 | CHT | Chunghwa Telecom Co., Ltd. | $44.79 | 1.58 | 1% | $20.46 | -54% |  |
| 320 | IMO | Imperial Oil Limited | $113.28 | 4.16 | 0% | $51.66 | -54% |  |
| 321 | ENTG | Entegris, Inc. | $176.28 | 1.73 | 30% | $79.77 | -55% |  |
| 322 | 000063.SZ | ZTE CORPORATION | $35.67 | 0.92 | 7% | $16.13 | -55% |  |
| 323 | EW | Edwards Lifesciences Corpo | $89.72 | 1.85 | 12% | $40.45 | -55% |  |
| 324 | TITAN.NS | TITAN COMPANY LIMITED | $4290.0 | 57.07 | 22% | $1933.59 | -55% |  |
| 325 | HINDUNILVR.NS | HINDUSTAN UNILEVER LTD. | $2177.0 | 45.22 | 12% | $977.79 | -55% |  |
| 326 | TCL.AX | TRANSURBAN STAPLED [TCL] | $15.39 | 0.15 | 30% | $6.92 | -55% |  |
| 327 | MPWR | Monolithic Power Systems,  | $1438.3 | 13.95 | 30% | $643.22 | -55% |  |
| 328 | SIE.DE | SIEMENS AG                 | $269.45 | 9.67 | 0% | $120.09 | -55% |  |
| 329 | CW | Curtiss-Wright Corporation | $767.73 | 13.67 | 15% | $341.0 | -56% |  |
| 330 | 002371.SZ | NAURA TECHNOLOGY GROUP CO  | $813.37 | 7.74 | 30% | $356.88 | -56% |  |
| 331 | 300408.SZ | CHAOZHOU THREE-CIRCLE (GRO | $160.05 | 1.51 | 30% | $69.62 | -56% |  |
| 332 | CRDO | Credo Technology Group Hol | $268.03 | 2.52 | 30% | $116.19 | -57% |  |
| 333 | WELL | Welltower Inc. | $223.73 | 2.08 | 30% | $95.91 | -57% |  |
| 334 | WCN | Waste Connections, Inc. | $166.21 | 4.11 | 7% | $71.32 | -57% |  |
| 335 | 600183.SS | SHENGYI TECHNOLOGY CO LTD | $178.5 | 1.63 | 30% | $75.16 | -58% |  |
| 336 | 6503.T | MITSUBISHI ELECTRIC CORP | $5858.0 | 198.14 | 0% | $2460.59 | -58% |  |
| 337 | NZYM.VI | NOVOZYMES AS | $54.38 | 1.28 | 8% | $22.82 | -58% |  |
| 338 | GLW | Corning Incorporated | $228.01 | 2.07 | 30% | $95.45 | -58% |  |
| 339 | CMG | Chipotle Mexican Grill, In | $32.28 | 1.09 | 0% | $13.54 | -58% |  |
| 340 | FTNT | Fortinet, Inc. | $149.93 | 2.58 | 14% | $62.72 | -58% |  |
| 341 | CVX | Chevron Corporation | $172.24 | 5.74 | 0% | $71.28 | -59% |  |
| 342 | CL | Colgate-Palmolive Company | $91.06 | 2.58 | 3% | $37.72 | -59% |  |
| 343 | GFS | GlobalFoundries Inc. | $86.12 | 1.69 | 11% | $35.62 | -59% |  |
| 344 | EQIX | Equinix, Inc. | $1087.61 | 14.47 | 20% | $447.14 | -59% |  |
| 345 | 4062.T | IBIDEN CO LTD | $24000.0 | 213.6 | 30% | $9848.83 | -59% |  |
| 346 | 0981.HK | SMIC | $80.0 | 0.71 | 30% | $32.74 | -59% |  |
| 347 | ASIANPAINT.NS | ASIAN PAINTS LIMITED | $2640.0 | 45.23 | 14% | $1078.63 | -59% |  |
| 348 | WEGE3.SA | WEG         ON      NM | $46.5 | 1.5 | 0% | $18.75 | -60% |  |
| 349 | FER.MC | FERROVIAL N.V. | $60.86 | 1.24 | 10% | $24.23 | -60% |  |
| 350 | RMS.PA | HERMES INTL | $1604.0 | 43.08 | 3% | $623.82 | -61% |  |
| 351 | SHOP | Shopify Inc. | $111.62 | 1.02 | 28% | $43.05 | -61% |  |
| 352 | EA | Electronic Arts Inc. | $204.73 | 3.5 | 13% | $78.85 | -62% |  |
| 353 | PLTR | Palantir Technologies Inc. | $107.27 | 0.89 | 30% | $41.04 | -62% |  |
| 354 | MDLN | Medline Inc. | $37.77 | 1.14 | 0% | $14.16 | -62% |  |
| 355 | EXR | Extra Space Storage Inc | $147.19 | 4.45 | 0% | $55.26 | -62% |  |
| 356 | S63.SI | ST Engineering | $10.41 | 0.15 | 16% | $3.85 | -63% |  |
| 357 | TSEM | Tower Semiconductor Ltd. | $269.88 | 2.16 | 30% | $99.59 | -63% |  |
| 358 | P911.DE | Dr. Ing. h.c. F. Porsche A | $42.74 | 0.34 | 30% | $15.68 | -63% |  |
| 359 | CARR | Carrier Global Corporation | $76.0 | 1.5 | 8% | $27.48 | -64% |  |
| 360 | DE | Deere & Company | $630.76 | 17.66 | 0% | $219.31 | -65% |  |
| 361 | DELTA.BK | DELTA_DELTA ELECTRONICS | $304.0 | 2.28 | 30% | $105.13 | -65% |  |
| 362 | NESTLEIND.NS | NESTLE INDIA LIMITED | $1409.8 | 18.09 | 16% | $479.41 | -66% |  |
| 363 | SW | Smurfit WestRock plc | $46.84 | 0.72 | 12% | $15.76 | -66% |  |
| 364 | CDNS | Cadence Design Systems, In | $368.23 | 4.31 | 18% | $122.97 | -67% |  |
| 365 | NOK | Nokia Corporation Sponsore | $13.98 | 0.16 | 19% | $4.67 | -67% |  |
| 366 | 6146.T | DISCO CORPORATION | $78510.0 | 1246.57 | 11% | $26203.15 | -67% |  |
| 367 | MELI | MercadoLibre, Inc. | $1619.25 | 37.89 | 3% | $535.23 | -67% |  |
| 368 | 688012.SS | ADVANCED MICRO-FABRICATION | $413.0 | 2.91 | 30% | $134.18 | -68% |  |
| 369 | DMART.NS | AVENUE SUPERMARTS LIMITED | $4299.2 | 45.52 | 20% | $1387.96 | -68% |  |
| 370 | HOOD | Robinhood Markets, Inc. | $93.47 | 2.06 | 3% | $29.23 | -69% |  |
| 371 | BESI.AS | BE Semiconductor Industrie | $283.6 | 1.91 | 30% | $88.07 | -69% |  |
| 372 | HUM | Humana Inc. | $376.0 | 9.36 | 0% | $116.24 | -69% |  |
| 373 | IR | Ingersoll Rand Inc. | $81.7 | 1.48 | 6% | $25.18 | -69% |  |
| 374 | LITE | Lumentum Holdings Inc. | $861.97 | 5.69 | 30% | $262.36 | -70% |  |
| 375 | APO | Apollo Global Management,  | $121.51 | 1.59 | 13% | $35.95 | -70% |  |
| 376 | KLAC | KLA Corporation | $258.8 | 3.52 | 12% | $76.35 | -70% |  |
| 377 | ADANIGREEN.NS | ADANI GREEN ENERGY LTD | $1525.9 | 9.61 | 30% | $443.11 | -71% |  |
| 378 | 300394.SZ | SUZHOU TFC OPTICAL COMMUN  | $318.0 | 1.98 | 30% | $91.3 | -71% |  |
| 379 | CIEN | Ciena Corporation | $484.69 | 3.01 | 30% | $138.79 | -71% |  |
| 380 | MTSI | MACOM Technology Solutions | $390.19 | 2.34 | 30% | $107.89 | -72% |  |
| 381 | WOW.AX | WOOLWORTHS FPO [WOW] | $40.24 | 0.49 | 12% | $10.61 | -74% |  |
| 382 | AMD | Advanced Micro Devices, In | $532.57 | 2.98 | 30% | $137.4 | -74% |  |
| 383 | AXON | Axon Enterprise, Inc. | $444.73 | 2.49 | 30% | $114.81 | -74% |  |
| 384 | 603986.SS | GIGA DEVICE SEMICONDUCTOR  | $770.0 | 4.26 | 30% | $196.42 | -74% |  |
| 385 | KOG.OL | KONGSBERG GRUPPEN | $276.8 | 5.45 | 0% | $67.68 | -76% |  |
| 386 | DSV.VI | DSV AS | $208.1 | 4.07 | 0% | $50.54 | -76% |  |
| 387 | DASH | DoorDash, Inc. | $176.91 | 2.11 | 10% | $42.62 | -76% |  |
| 388 | COHR | Coherent Corp. | $407.25 | 2.12 | 30% | $97.75 | -76% |  |
| 389 | SNPS | Synopsys, Inc. | $455.02 | 4.37 | 15% | $107.08 | -76% |  |
| 390 | HOLN.SW | HOLCIM N | $74.98 | 0.7 | 15% | $17.51 | -77% |  |
| 391 | 6752.T | PANASONIC HOLDINGS CORP | $4540.0 | 81.14 | 0% | $1007.63 | -78% |  |
| 392 | 2454.TW | MEDIATEK INC | $3880.0 | 65.94 | 0% | $838.3 | -78% |  |
| 393 | 3037.TW | UNIMICRON TECHNOLOGY | $975.0 | 4.39 | 30% | $202.42 | -79% |  |
| 394 | ABBV | AbbVie Inc. | $243.14 | 2.04 | 14% | $49.57 | -80% |  |
| 395 | TPRO.MI | TECHNOPROBE | $33.92 | 0.15 | 30% | $6.92 | -80% |  |
| 396 | COF | Capital One Financial Corp | $204.9 | 3.26 | 0% | $41.38 | -80% |  |
| 397 | ORA.PA | ORANGE | $17.12 | 0.12 | 17% | $3.23 | -81% |  |
| 398 | VTR | Ventas, Inc. | $87.43 | 0.55 | 19% | $16.01 | -82% |  |
| 399 | 1303.TW | NAN YA PLASTIC | $148.0 | 0.57 | 30% | $26.28 | -82% |  |
| 400 | IRM | Iron Mountain Incorporated | $131.06 | 0.92 | 15% | $22.75 | -83% |  |
| 401 | ALAB | Astera Labs, Inc. | $398.0 | 1.47 | 30% | $67.78 | -83% |  |
| 402 | 2082.SR | ACWA POWER Co. | $198.5 | 2.34 | 2% | $31.96 | -84% |  |
| 403 | 688256.SS | CAMBRICON TECHNOLOGIES COR | $1458.0 | 4.36 | 30% | $201.03 | -86% |  |
| 404 | NRG | NRG Energy, Inc. | $147.11 | 0.91 | 12% | $20.08 | -86% |  |
| 405 | EBK.DE | ENBW ENERGIE BAD.-WUE. ON | $68.0 | 0.7 | 0% | $8.69 | -87% |  |
| 406 | CBRS | Cerebras Systems Inc. | $168.52 | 0.46 | 30% | $21.21 | -87% |  |
| 407 | ARM | Arm Holdings plc | $347.71 | 0.83 | 30% | $38.27 | -89% |  |
| 408 | MCHP | Microchip Technology Incor | $94.12 | 0.22 | 30% | $10.14 | -89% |  |
| 409 | STM | STMicroelectronics N.V. | $74.88 | 0.16 | 30% | $7.38 | -90% |  |
| 410 | TSLA | Tesla, Inc. | $375.12 | 1.09 | 21% | $35.68 | -90% |  |
| 411 | TWLO | Twilio Inc. | $190.88 | 0.67 | 17% | $18.09 | -90% |  |
| 412 | VIC.VN | VINGROUP JSC | $228000.0 | 1417.5 | 4% | $21150.51 | -91% |  |
| 413 | PANW | Palo Alto Networks, Inc. | $293.09 | 1.14 | 11% | $23.89 | -92% |  |
| 414 | GLCNF | Glencore Plc | $6.85 | 0.03 | 8% | $0.55 | -92% |  |
| 415 | ETERNAL.NS | ETERNAL LIMITED | $255.0 | 0.38 | 30% | $17.52 | -93% |  |
| 416 | FANG | Diamondback Energy, Inc. | $182.55 | 0.99 | 0% | $12.29 | -93% |  |
| 417 | INIO | INNIO N.V. | $38.24 | 0.14 | 8% | $2.55 | -93% |  |
| 418 | 1347.HK | HUA HONG GRACE | $189.5 | 0.25 | 30% | $11.53 | -94% |  |
| 419 | DDOG | Datadog, Inc. | $220.94 | 0.4 | 18% | $11.42 | -95% |  |
| 420 | III.L | 3I GROUP PLC ORD 73 19/22P | $2510.0 | 5.38 | 0% | $66.81 | -97% |  |
| 421 | STAN.L | STANDARD CHARTERED PLC ORD | $2029.5 | 1.57 | 21% | $51.14 | -98% |  |
| 422 | MTN.JO | MTN Group Ltd | $22910.0 | 11.01 | 30% | $507.66 | -98% |  |
| 423 | SBK.JO | Standard Bank Group Ltd | $31863.0 | 29.87 | 10% | $611.1 | -98% |  |
| 424 | FSR.JO | Firstrand Ltd | $9649.0 | 7.86 | 10% | $157.2 | -98% |  |
| 425 | RR.L | ROLLS-ROYCE HOLDINGS PLC O | $1405.8 | 0.69 | 17% | $18.52 | -99% |  |
| 426 | ANTO.L | ANTOFAGASTA PLC ORD 5P | $3722.0 | 1.02 | 30% | $47.03 | -99% |  |
| 427 | RKT.L | RECKITT BENCKISER GROUP PL | $4896.0 | 4.89 | 1% | $64.59 | -99% |  |
| 428 | SSE.L | SSE PLC ORD 50P | $2396.0 | 1.05 | 19% | $31.5 | -99% |  |
| 429 | LUMI.TA | BK LEUMI LE ISRAEL | $6595.0 | 6.84 | 0% | $84.94 | -99% |  |
| 430 | POLI.TA | BANK HAPOALIM B.M. | $6810.0 | 7.21 | 0% | $89.54 | -99% |  |
| 431 | IMB.L | IMPERIAL BRANDS PLC ORD 10 | $2788.0 | 2.13 | 7% | $37.26 | -99% |  |
| 432 | TSCO.L | TESCO PLC ORD 6 1/3P | $461.0 | 0.27 | 9% | $5.09 | -99% |  |
| 433 | BT-A.L | BT GROUP PLC ORD 5P | $191.15 | 0.11 | 7% | $1.91 | -99% |  |
| 434 | CPI.JO | Capitec Bank Hldgs Ltd | $467284.0 | 145.51 | 19% | $4348.51 | -99% |  |
| 435 | AV.L | AVIVA PLC ORD 32 17/19P | $643.0 | 0.26 | 12% | $5.63 | -99% |  |
| 436 | BA.L | BAE SYSTEMS PLC ORD 2.5P | $1765.5 | 0.68 | 10% | $13.86 | -99% |  |
| 437 | LSEG.L | LONDON STOCK EXCHANGE GROU | $7840.0 | 2.37 | 14% | $55.71 | -99% |  |
| 438 | KFH.KW | Kuwait Finance House | $772.0 | 0.03 | 10% | $0.6 | -100% |  |
| 439 | SPCX | Space Exploration Technolo | $153.0 | -0.67 | — | — | no earnings | no_earnings |
| 440 | 005930.KS | SamsungElec | $339500.0 | None | — | — | no earnings | no_earnings |
| 441 | 000660.KS | SK hynix | $2673000.0 | None | — | — | no earnings | no_earnings |
| 442 | INTC | Intel Corporation | $132.87 | -0.6 | — | — | no earnings | no_earnings |
| 443 | CRWD | CrowdStrike Holdings, Inc. | $678.65 | -0.14 | — | — | no earnings | no_earnings |
| 444 | 402340.KS | SKSQUARE | $1720000.0 | None | — | — | no earnings | no_earnings |
| 445 | BE | Bloom Energy Corporation | $309.18 | -0.03 | — | — | no earnings | no_earnings |
| 446 | 005380.KS | HyundaiMtr | $480500.0 | None | — | — | no earnings | no_earnings |
| 447 | NET | Cloudflare, Inc. | $226.65 | -0.25 | — | — | no earnings | no_earnings |
| 448 | SNOW | Snowflake Inc. | $227.06 | -3.52 | — | — | no earnings | no_earnings |
| 449 | WBD | Warner Bros. Discovery, In | $26.98 | -0.7 | — | — | no earnings | no_earnings |
| 450 | F | Ford Motor Company | $14.11 | -1.55 | — | — | no earnings | no_earnings |
| 451 | 6723.T | RENESAS ELECTRONICS CORP | $4800.0 | -28.58 | — | — | no earnings | no_earnings |
| 452 | CRWV | CoreWeave, Inc. | $98.76 | -2.72 | — | — | no earnings | no_earnings |
| 453 | BAYN.DE | Bayer AG                   | $47.08 | -2.19 | — | — | no earnings | no_earnings |
| 454 | 028260.KS | SAMSUNG C&T | $494500.0 | None | — | — | no earnings | no_earnings |
| 455 | AAL.L | ANGLO AMERICAN PLC ORD USD | $3645.0 | -0.8 | — | — | no earnings | no_earnings |
| 456 | 3690.HK | MEITUAN-W | $64.25 | -4.53 | — | — | no earnings | no_earnings |
| 457 | 032830.KS | SAMSUNG LIFE | $432500.0 | None | — | — | no earnings | no_earnings |
| 458 | 373220.KS | LG Energy Solution | $331500.0 | None | — | — | no earnings | no_earnings |
| 459 | RKLB | Rocket Lab Corporation | $80.69 | -0.32 | — | — | no earnings | no_earnings |
| 460 | TAK | Takeda Pharmaceutical Comp | $15.65 | -0.3 | — | — | no earnings | no_earnings |
| 461 | 688795.SS | MOORE THREADS TECH CO LTD | $672.77 | -2.1 | — | — | no earnings | no_earnings |
| 462 | TTWO | Take-Two Interactive Softw | $238.72 | -1.62 | — | — | no earnings | no_earnings |
| 463 | 2010.SR | Saudi Basic Industries Cor | $53.1 | -0.19 | — | — | no earnings | no_earnings |
| 464 | RKT | Rocket Companies, Inc. | $14.78 | -0.03 | — | — | no earnings | no_earnings |
| 465 | GBTC | Grayscale Bitcoin Trust (B | $45.9 | None | — | — | no earnings | no_earnings |
| 466 | LYV | Live Nation Entertainment, | $175.11 | -1.77 | — | — | no earnings | no_earnings |
| 467 | 207940.KS | SAMSUNG BIOLOGICS | $1343000.0 | None | — | — | no earnings | no_earnings |
| 468 | 329180.KS | HD HYUNDAI HEAVY INDUSTRIE | $564000.0 | None | — | — | no earnings | no_earnings |
| 469 | 009155.KS | SamsungElecMech(1P) | $777000.0 | None | — | — | no earnings | no_earnings |
| 470 | RVMD | Revolution Medicines, Inc. | $178.17 | -7.11 | — | — | no earnings | no_earnings |
| 471 | KER.PA | KERING | $266.4 | -0.24 | — | — | no earnings | no_earnings |
| 472 | NTRA | Natera, Inc. | $260.74 | -1.62 | — | — | no earnings | no_earnings |
| 473 | BIDU | Baidu, Inc. | $103.99 | -0.16 | — | — | no earnings | no_earnings |
| 474 | 000270.KS | KIA CORP. | $135300.0 | None | — | — | no earnings | no_earnings |
| 475 | HMC | Honda Motor Company, Ltd. | $26.14 | -1.97 | — | — | no earnings | no_earnings |
| 476 | 012450.KS | HANWHA AEROSPACE | $1011000.0 | None | — | — | no earnings | no_earnings |
| 477 | 034020.KS | Doosan Enerbility | $81100.0 | None | — | — | no earnings | no_earnings |
| 478 | RBLX | Roblox Corporation | $46.39 | -1.57 | — | — | no earnings | no_earnings |
| 479 | 688783.SS | XI'AN ESWIN MATERIAL TECHN | $53.86 | -0.21 | — | — | no earnings | no_earnings |
| 480 | CNC | Centene Corporation | $64.77 | -13.05 | — | — | no earnings | no_earnings |
| 481 | VOD | Vodafone Group Plc | $13.86 | -0.14 | — | — | no earnings | no_earnings |
| 482 | CPNG | Coupang, Inc. | $17.06 | -0.1 | — | — | no earnings | no_earnings |
| 483 | MSTR | Strategy Inc | $85.33 | -36.99 | — | — | no earnings | no_earnings |
| 484 | SATS | EchoStar Corporation | $103.92 | -50.21 | — | — | no earnings | no_earnings |
| 485 | ORSTED.CO | ORSTED A/S | $146.35 | -2.4 | — | — | no earnings | no_earnings |
| 486 | EL | Estee Lauder Companies, In | $81.5 | -0.7 | — | — | no earnings | no_earnings |
| 487 | 034730.KS | SK | $815000.0 | None | — | — | no earnings | no_earnings |
| 488 | 012330.KS | Mobis | $486500.0 | None | — | — | no earnings | no_earnings |
| 489 | KHC | The Kraft Heinz Company | $23.47 | -4.86 | — | — | no earnings | no_earnings |
| 490 | ML.PA | MICHELIN | $33.62 | None | — | — | no earnings | no_earnings |
| 491 | 688521.SS | VERISILICON MICROELECTRONI | $336.0 | -1.25 | — | — | no earnings | no_earnings |
| 492 | ASTS | AST SpaceMobile, Inc. | $65.62 | -1.8 | — | — | no earnings | no_earnings |
| 493 | FISV | Fiserv, Inc. | $47.53 | None | — | — | no earnings | no_earnings |
| 494 | 068270.KS | Celltrion | $165900.0 | None | — | — | no earnings | no_earnings |
| 495 | SYM | Symbotic Inc. | $40.77 | -0.08 | — | — | no earnings | no_earnings |
| 496 | ROIV | Roivant Sciences Ltd. | $34.02 | -0.54 | — | — | no earnings | no_earnings |

