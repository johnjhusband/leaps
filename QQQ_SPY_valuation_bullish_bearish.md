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
| 1 | CHTR | Charter Communications, In | $132.12 | 36.95 | 9% | $702.78 | +432% |  |
| 2 | CMCSA | Comcast Corporation | $23.82 | 5.1 | 0% | $63.33 | +166% |  |
| 3 | GILD | Gilead Sciences, Inc. | $129.16 | 7.35 | 30% | $338.9 | +162% |  |
| 4 | NFLX | Netflix, Inc. | $82.18 | 3.1 | 30% | $142.94 | +74% |  |
| 5 | CEG | Constellation Energy Corpo | $254.83 | 11.52 | 25% | $439.04 | +72% |  |
| 6 | GOOG | Alphabet Inc. | $365.76 | 13.09 | 30% | $603.56 | +65% |  |
| 7 | GOOGL | Alphabet Inc. | $368.53 | 13.12 | 30% | $604.95 | +64% |  |
| 8 | PYPL | PayPal Holdings, Inc. | $41.29 | 5.33 | 0% | $66.19 | +60% |  |
| 9 | BKR | Baker Hughes Company | $62.59 | 3.13 | 21% | $99.66 | +59% |  |
| 10 | CTSH | Cognizant Technology Solut | $53.21 | 4.61 | 8% | $83.03 | +56% |  |
| 11 | WDC | Western Digital Corporatio | $511.72 | 16.73 | 30% | $771.4 | +51% |  |
| 12 | ADBE | Adobe Inc. | $251.44 | 17.15 | 12% | $377.52 | +50% |  |
| 13 | NVDA | NVIDIA Corporation | $205.1 | 6.52 | 30% | $300.63 | +47% |  |
| 14 | MSFT | Microsoft Corporation | $416.67 | 16.79 | 23% | $595.89 | +43% |  |
| 15 | PDD | PDD Holdings Inc. | $85.07 | 9.53 | 0% | $118.35 | +39% |  |
| 16 | INTU | Intuit Inc. | $296.76 | 16.38 | 15% | $403.83 | +36% |  |
| 17 | NXPI | NXP Semiconductors N.V. | $295.96 | 10.45 | 25% | $395.08 | +34% |  |
| 18 | BKNG | Booking Holdings Inc. Comm | $165.84 | 7.58 | 18% | $212.54 | +28% |  |
| 19 | PCAR | PACCAR Inc. | $116.68 | 4.7 | 19% | $140.4 | +20% |  |
| 20 | DXCM | DexCom, Inc. | $72.86 | 2.33 | 24% | $85.03 | +17% |  |
| 21 | MU | Micron Technology, Inc. | $864.01 | 21.17 | 30% | $976.12 | +13% |  |
| 22 | AMAT | Applied Materials, Inc. | $453.01 | 10.65 | 30% | $491.06 | +8% |  |
| 23 | GEHC | GE HealthCare Technologies | $64.67 | 4.17 | 6% | $69.79 | +8% |  |
| 24 | META | Meta Platforms, Inc. | $593.0 | 27.52 | 12% | $609.86 | +3% |  |
| 25 | AMZN | Amazon.com, Inc. | $246.03 | 7.77 | 21% | $249.76 | +2% |  |
| 26 | CCEP | Coca-Cola Europacific Part | $94.74 | 4.94 | 9% | $96.09 | +1% |  |
| 27 | CSX | CSX Corporation | $46.99 | 1.63 | 19% | $47.66 | +1% |  |
| 28 | REGN | Regeneron Pharmaceuticals, | $635.45 | 40.99 | 4% | $630.41 | -1% |  |
| 29 | ADSK | Autodesk, Inc. | $229.96 | 6.85 | 21% | $220.09 | -4% |  |
| 30 | ROP | Roper Technologies, Inc. | $332.18 | 16.01 | 10% | $316.0 | -5% |  |
| 31 | APP | Applovin Corporation | $557.2 | 11.48 | 30% | $529.33 | -5% |  |
| 32 | ADP | Automatic Data Processing, | $231.95 | 10.72 | 10% | $219.32 | -5% |  |
| 33 | TXN | Texas Instruments Incorpor | $285.06 | 5.84 | 30% | $269.28 | -6% |  |
| 34 | ABNB | Airbnb, Inc. | $133.54 | 4.05 | 20% | $124.32 | -7% |  |
| 35 | KDP | Keurig Dr Pepper Inc. | $30.53 | 1.35 | 10% | $27.57 | -10% |  |
| 36 | AEP | American Electric Power Co | $129.14 | 6.75 | 7% | $115.93 | -10% |  |
| 37 | ROST | Ross Stores, Inc. | $230.37 | 7.16 | 18% | $200.08 | -13% |  |
| 38 | SNDK | Sandisk Corporation | $1559.32 | 29.32 | 30% | $1351.91 | -13% |  |
| 39 | PAYX | Paychex, Inc. | $100.53 | 4.53 | 9% | $86.95 | -14% |  |
| 40 | EXC | Exelon Corporation | $45.75 | 2.73 | 3% | $39.47 | -14% |  |
| 41 | TMUS | T-Mobile US, Inc. | $178.1 | 9.4 | 6% | $152.64 | -14% |  |
| 42 | TRI | Thomson Reuters Corp | $86.04 | 3.48 | 11% | $73.55 | -14% |  |
| 43 | VRTX | Vertex Pharmaceuticals Inc | $446.83 | 16.85 | 12% | $371.25 | -17% |  |
| 44 | XEL | Xcel Energy Inc. | $79.04 | 3.47 | 8% | $63.93 | -19% |  |
| 45 | LRCX | Lam Research Corporation | $303.28 | 5.28 | 30% | $243.45 | -20% |  |
| 46 | ADI | Analog Devices, Inc. | $401.39 | 6.7 | 30% | $308.93 | -23% |  |
| 47 | ASML | ASML Holding N.V. - New Yo | $1641.74 | 30.04 | 27% | $1250.55 | -24% |  |
| 48 | PEP | Pepsico, Inc. | $141.92 | 6.37 | 6% | $107.67 | -24% |  |
| 49 | AAPL | Apple Inc. | $307.34 | 8.27 | 17% | $227.78 | -26% |  |
| 50 | CPRT | Copart, Inc. | $30.96 | 1.61 | 2% | $22.4 | -28% |  |

### 🔴 BEARISH — 50 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | ORLY | O'Reilly Automotive, Inc. | $90.33 | 3.07 | 11% | $64.47 | -29% |  |
| 2 | MDLZ | Mondelez International, In | $62.04 | 2.02 | 11% | $42.0 | -32% |  |
| 3 | AMGN | Amgen Inc. | $349.58 | 14.37 | 4% | $221.32 | -37% |  |
| 4 | WDAY | Workday, Inc. | $144.28 | 3.2 | 18% | $90.11 | -38% |  |
| 5 | VRSK | Verisk Analytics, Inc. | $181.73 | 6.56 | 7% | $113.41 | -38% |  |
| 6 | ALNY | Alnylam Pharmaceuticals, I | $303.05 | 3.97 | 30% | $183.05 | -40% |  |
| 7 | LIN | Linde plc | $507.9 | 15.08 | 10% | $299.0 | -41% |  |
| 8 | MNST | Monster Beverage Corporati | $89.55 | 2.07 | 15% | $51.7 | -42% |  |
| 9 | FAST | Fastenal Company | $46.79 | 1.13 | 14% | $26.78 | -43% |  |
| 10 | STX | Seagate Technology Holding | $847.47 | 10.51 | 30% | $484.6 | -43% |  |
| 11 | IDXX | IDEXX Laboratories, Inc. | $562.16 | 13.6 | 13% | $310.21 | -45% |  |
| 12 | SBUX | Starbucks Corporation | $95.29 | 1.31 | 26% | $52.55 | -45% |  |
| 13 | MAR | Marriott International | $392.51 | 9.54 | 13% | $215.68 | -45% |  |
| 14 | CTAS | Cintas Corporation | $179.85 | 4.75 | 11% | $98.59 | -45% |  |
| 15 | WMT | Walmart Inc. | $118.88 | 2.84 | 13% | $65.07 | -45% |  |
| 16 | CSCO | Cisco Systems, Inc. | $121.64 | 3.0 | 12% | $66.42 | -45% |  |
| 17 | QCOM | QUALCOMM Incorporated | $215.94 | 9.31 | 0% | $115.62 | -46% |  |
| 18 | HON | Honeywell International In | $213.97 | 6.27 | 8% | $112.36 | -48% |  |
| 19 | ISRG | Intuitive Surgical, Inc. | $422.06 | 8.23 | 17% | $220.65 | -48% |  |
| 20 | MRVL | Marvell Technology, Inc. | $263.47 | 2.9 | 30% | $133.72 | -49% |  |
| 21 | FER | Ferrovial N.V. | $66.81 | 1.35 | 14% | $32.46 | -51% |  |
| 22 | COST | Costco Wholesale Corporati | $971.87 | 19.92 | 13% | $452.96 | -53% |  |
| 23 | FTNT | Fortinet, Inc. | $144.68 | 2.58 | 14% | $62.72 | -57% |  |
| 24 | MPWR | Monolithic Power Systems,  | $1481.05 | 13.92 | 30% | $641.83 | -57% |  |
| 25 | ODFL | Old Dominion Freight Line, | $242.57 | 4.78 | 12% | $102.34 | -58% |  |
| 26 | KLAC | KLA Corporation | $1929.2 | 35.3 | 12% | $765.69 | -60% |  |
| 27 | SHOP | Shopify Inc. | $109.54 | 1.02 | 28% | $43.02 | -61% |  |
| 28 | EA | Electronic Arts Inc. | $203.0 | 3.51 | 13% | $79.07 | -61% |  |
| 29 | MELI | MercadoLibre, Inc. | $1607.8 | 37.94 | 4% | $586.58 | -64% |  |
| 30 | CDNS | Cadence Design Systems, In | $376.19 | 4.29 | 18% | $121.88 | -68% |  |
| 31 | LITE | Lumentum Holdings Inc. | $863.66 | 5.7 | 30% | $262.82 | -70% |  |
| 32 | PLTR | Palantir Technologies Inc. | $135.53 | 0.89 | 30% | $41.04 | -70% |  |
| 33 | AMD | Advanced Micro Devices, In | $466.38 | 2.98 | 30% | $137.4 | -70% |  |
| 34 | DASH | DoorDash, Inc. | $156.8 | 2.12 | 10% | $42.83 | -73% |  |
| 35 | AXON | Axon Enterprise, Inc. | $486.12 | 2.48 | 30% | $114.35 | -76% |  |
| 36 | SNPS | Synopsys, Inc. | $464.85 | 4.37 | 15% | $107.08 | -77% |  |
| 37 | ARM | Arm Holdings plc | $342.93 | 0.86 | 30% | $39.65 | -88% |  |
| 38 | MCHP | Microchip Technology Incor | $88.34 | 0.22 | 30% | $10.14 | -88% |  |
| 39 | TSLA | Tesla, Inc. | $391.0 | 1.09 | 22% | $36.88 | -91% |  |
| 40 | PANW | Palo Alto Networks, Inc. | $272.05 | 1.14 | 11% | $23.75 | -91% |  |
| 41 | FANG | Diamondback Energy, Inc. | $192.62 | 0.98 | 0% | $12.17 | -94% |  |
| 42 | DDOG | Datadog, Inc. | $234.11 | 0.4 | 18% | $11.41 | -95% |  |
| 43 | CRWD | CrowdStrike Holdings, Inc. | $671.02 | -0.13 | — | — | no earnings | no_earnings |
| 44 | INSM | Insmed Incorporated | $94.22 | -5.76 | — | — | no earnings | no_earnings |
| 45 | INTC | Intel Corporation | $99.17 | -0.6 | — | — | no earnings | no_earnings |
| 46 | KHC | The Kraft Heinz Company | $22.58 | -4.86 | — | — | no earnings | no_earnings |
| 47 | MSTR | Strategy Inc | $120.44 | -36.99 | — | — | no earnings | no_earnings |
| 48 | TTWO | Take-Two Interactive Softw | $214.39 | -1.63 | — | — | no earnings | no_earnings |
| 49 | WBD | Warner Bros. Discovery, In | $26.24 | -0.7 | — | — | no earnings | no_earnings |
| 50 | ZS | Zscaler, Inc. | $130.78 | -0.48 | — | — | no earnings | no_earnings |

<details><summary>Neutral / near-median (1) — excluded from the split</summary>

| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | AVGO | Broadcom Inc. | $385.73 | 6.02 | 30% | $277.57 | -28% |  |

</details>

---
## SPY (S&P 500)
Valued 503 holdings · **250 most undervalued (BULLISH)** vs **250 most overvalued (BEARISH)** · 3 near-median (neutral, excluded).

### 🟢 BULLISH — 250 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | CI | The Cigna Group | $289.48 | 113.71 | 10% | $2282.48 | +688% |  |
| 2 | EXE | Expand Energy Corporation | $92.07 | 13.44 | 27% | $553.81 | +502% |  |
| 3 | APA | APA Corporation | $36.57 | 4.29 | 30% | $197.81 | +441% |  |
| 4 | CHTR | Charter Communications, In | $132.12 | 36.95 | 9% | $702.78 | +432% |  |
| 5 | UAL | United Airlines Holdings,  | $105.73 | 11.18 | 30% | $515.5 | +388% |  |
| 6 | EQT | EQT Corporation | $53.75 | 5.27 | 30% | $242.99 | +352% |  |
| 7 | CF | CF Industries Holdings, In | $113.49 | 11.1 | 30% | $511.81 | +351% |  |
| 8 | EG | Everest Group, Ltd. | $334.41 | 49.12 | 17% | $1324.85 | +296% |  |
| 9 | AES | The AES Corporation | $14.67 | 1.92 | 18% | $55.15 | +276% |  |
| 10 | NEM | Newmont Corporation | $99.71 | 7.71 | 30% | $355.5 | +256% |  |
| 11 | EOG | EOG Resources, Inc. | $137.78 | 10.17 | 30% | $468.93 | +240% |  |
| 12 | SYF | Synchrony Financial | $70.84 | 9.66 | 13% | $222.2 | +214% |  |
| 13 | UHS | Universal Health Services, | $145.17 | 23.95 | 8% | $444.34 | +206% |  |
| 14 | CFG | Citizens Financial Group,  | $63.98 | 4.22 | 30% | $194.58 | +204% |  |
| 15 | C | Citigroup, Inc. | $132.47 | 8.09 | 30% | $373.02 | +182% |  |
| 16 | DAL | Delta Air Lines, Inc. | $79.42 | 6.85 | 20% | $213.98 | +169% |  |
| 17 | MPC | Marathon Petroleum Corpora | $262.01 | 15.2 | 30% | $700.85 | +168% |  |
| 18 | CMCSA | Comcast Corporation | $23.82 | 5.1 | 0% | $63.33 | +166% |  |
| 19 | UBER | Uber Technologies, Inc. | $70.71 | 4.03 | 30% | $185.82 | +163% |  |
| 20 | GILD | Gilead Sciences, Inc. | $129.16 | 7.35 | 30% | $338.9 | +162% |  |
| 21 | T | AT&T Inc. | $22.75 | 3.04 | 9% | $58.62 | +158% |  |
| 22 | FSLR | First Solar, Inc. | $279.01 | 15.49 | 30% | $714.22 | +156% |  |
| 23 | ALL | Allstate Corporation (The) | $221.01 | 45.2 | 0% | $561.31 | +154% |  |
| 24 | DVA | DaVita Inc. | $192.16 | 10.38 | 30% | $478.61 | +149% |  |
| 25 | KEY | KeyCorp | $21.76 | 1.63 | 22% | $54.02 | +148% |  |
| 26 | VLO | Valero Energy Corporation | $255.82 | 13.69 | 30% | $631.23 | +147% |  |
| 27 | ACGL | Arch Capital Group Ltd. | $91.19 | 13.0 | 7% | $224.11 | +146% |  |
| 28 | FIS | Fidelity National Informat | $40.95 | 5.16 | 9% | $99.23 | +142% |  |
| 29 | MKC | McCormick & Company, Incor | $47.24 | 6.1 | 8% | $110.28 | +133% |  |
| 30 | SCHW | Charles Schwab Corporation | $88.84 | 5.03 | 26% | $201.23 | +126% |  |
| 31 | HIG | The Hartford Insurance Gro | $132.14 | 14.21 | 10% | $284.72 | +116% |  |
| 32 | VICI | VICI Properties Inc. | $27.86 | 2.92 | 10% | $59.85 | +115% |  |
| 33 | HST | Host Hotels & Resorts, Inc | $24.62 | 1.47 | 23% | $51.77 | +110% |  |
| 34 | BAC | Bank of America Corporatio | $53.83 | 4.03 | 17% | $110.71 | +106% |  |
| 35 | NTRS | Northern Trust Corporation | $170.47 | 9.55 | 24% | $345.16 | +102% |  |
| 36 | TEL | TE Connectivity plc | $212.65 | 9.78 | 28% | $421.73 | +98% |  |
| 37 | AMP | Ameriprise Financial, Inc. | $454.66 | 40.15 | 12% | $894.9 | +97% |  |
| 38 | INCY | Incyte Corporation | $102.38 | 7.08 | 18% | $200.38 | +96% |  |
| 39 | TFC | Truist Financial Corporati | $49.2 | 4.04 | 13% | $94.08 | +91% |  |
| 40 | CINF | Cincinnati Financial Corpo | $165.29 | 17.49 | 8% | $311.96 | +89% |  |
| 41 | RF | Regions Financial Corporat | $28.54 | 2.41 | 12% | $53.22 | +86% |  |
| 42 | VST | Vistra Corp. | $148.76 | 5.98 | 30% | $275.73 | +85% |  |
| 43 | GDDY | GoDaddy Inc. | $84.38 | 6.31 | 15% | $156.04 | +85% |  |
| 44 | CPAY | Corpay, Inc. | $347.45 | 16.71 | 25% | $638.87 | +84% |  |
| 45 | CBOE | Cboe Global Markets, Inc. | $281.91 | 11.7 | 29% | $516.03 | +83% |  |
| 46 | NUE | Nucor Corporation | $254.39 | 10.07 | 30% | $464.32 | +82% |  |
| 47 | PNC | PNC Financial Services Gro | $228.37 | 17.22 | 14% | $413.37 | +81% |  |
| 48 | SMCI | Super Micro Computer, Inc. | $41.64 | 1.9 | 26% | $74.9 | +80% |  |
| 49 | WFC | Wells Fargo & Company | $81.94 | 6.47 | 13% | $146.86 | +79% |  |
| 50 | SOLV | Solventum Corporation | $81.01 | 8.17 | 7% | $144.04 | +78% |  |
| 51 | USB | U.S. Bancorp | $55.69 | 4.77 | 11% | $98.52 | +77% |  |
| 52 | BIIB | Biogen Inc. | $195.34 | 9.3 | 24% | $343.52 | +76% |  |
| 53 | AIG | American International Gro | $75.49 | 5.68 | 13% | $131.46 | +74% |  |
| 54 | NFLX | Netflix, Inc. | $82.18 | 3.1 | 30% | $142.94 | +74% |  |
| 55 | UDR | UDR, Inc. | $39.2 | 1.47 | 30% | $67.78 | +73% |  |
| 56 | CEG | Constellation Energy Corpo | $254.83 | 11.52 | 25% | $439.04 | +72% |  |
| 57 | MTB | M&T Bank Corporation | $222.44 | 17.82 | 12% | $381.2 | +71% |  |
| 58 | GEV | GE Vernova Inc. | $933.61 | 34.26 | 30% | $1579.69 | +69% |  |
| 59 | CB | Chubb Limited | $326.27 | 28.25 | 9% | $547.25 | +68% |  |
| 60 | LUV | Southwest Airlines Company | $41.54 | 1.5 | 30% | $69.16 | +66% |  |
| 61 | GOOG | Alphabet Inc. | $365.76 | 13.09 | 30% | $603.56 | +65% |  |
| 62 | GOOGL | Alphabet Inc. | $368.53 | 13.12 | 30% | $604.95 | +64% |  |
| 63 | GL | Globe Life Inc. | $159.18 | 14.45 | 8% | $259.78 | +63% |  |
| 64 | HAL | Halliburton Company | $39.18 | 1.81 | 23% | $63.93 | +63% |  |
| 65 | HBAN | Huntington Bancshares Inco | $16.52 | 1.3 | 11% | $26.69 | +62% |  |
| 66 | PYPL | PayPal Holdings, Inc. | $41.29 | 5.33 | 0% | $66.19 | +60% |  |
| 67 | STLD | Steel Dynamics, Inc. | $268.5 | 9.32 | 30% | $429.73 | +60% |  |
| 68 | BKR | Baker Hughes Company | $62.59 | 3.13 | 21% | $99.66 | +59% |  |
| 69 | RJF | Raymond James Financial, I | $151.45 | 10.59 | 13% | $239.42 | +58% |  |
| 70 | EXPE | Expedia Group, Inc. | $228.88 | 11.33 | 21% | $361.04 | +58% |  |
| 71 | BNY | The Bank of New York Mello | $142.39 | 8.06 | 17% | $222.09 | +56% |  |
| 72 | CTSH | Cognizant Technology Solut | $53.21 | 4.61 | 8% | $83.03 | +56% |  |
| 73 | EIX | Edison International | $73.33 | 9.2 | 0% | $114.25 | +56% |  |
| 74 | WTW | Willis Towers Watson Publi | $263.54 | 17.02 | 14% | $410.18 | +56% |  |
| 75 | HCA | HCA Healthcare, Inc. | $372.13 | 29.03 | 10% | $576.13 | +55% |  |
| 76 | JPM | JP Morgan Chase & Co. | $312.37 | 20.9 | 13% | $479.68 | +54% |  |
| 77 | GIS | General Mills, Inc. | $33.15 | 4.09 | 0% | $50.79 | +53% |  |
| 78 | CCL | Carnival Corporation Ltd. | $27.41 | 2.27 | 8% | $41.35 | +51% |  |
| 79 | WDC | Western Digital Corporatio | $511.72 | 16.73 | 30% | $771.4 | +51% |  |
| 80 | TRV | The Travelers Companies, I | $303.25 | 33.51 | 2% | $456.53 | +50% |  |
| 81 | BEN | Franklin Resources, Inc. | $31.33 | 1.31 | 24% | $47.1 | +50% |  |
| 82 | ADBE | Adobe Inc. | $251.44 | 17.15 | 12% | $377.52 | +50% |  |
| 83 | RCL | Royal Caribbean Cruises Lt | $280.0 | 16.38 | 16% | $418.47 | +50% |  |
| 84 | PCG | Pacific Gas & Electric Co. | $17.11 | 1.29 | 10% | $25.55 | +49% |  |
| 85 | PFG | Principal Financial Group  | $105.22 | 6.97 | 13% | $156.95 | +49% |  |
| 86 | BALL | Ball Corporation | $52.92 | 3.43 | 13% | $78.65 | +49% |  |
| 87 | TRGP | Targa Resources, Inc. | $264.09 | 9.8 | 26% | $389.57 | +48% |  |
| 88 | BXP | BXP, Inc. | $62.33 | 1.99 | 30% | $91.76 | +47% |  |
| 89 | VZ | Verizon Communications Inc | $45.37 | 4.1 | 6% | $66.8 | +47% |  |
| 90 | DELL | Dell Technologies Inc. | $394.39 | 12.54 | 30% | $578.2 | +47% |  |
| 91 | NVDA | NVIDIA Corporation | $205.1 | 6.52 | 30% | $300.63 | +47% |  |
| 92 | MSFT | Microsoft Corporation | $416.67 | 16.79 | 23% | $595.89 | +43% |  |
| 93 | GEN | Gen Digital Inc. | $26.28 | 1.57 | 14% | $36.74 | +40% |  |
| 94 | FCX | Freeport-McMoRan, Inc. | $63.37 | 1.89 | 30% | $87.15 | +38% |  |
| 95 | BBY | Best Buy Co., Inc. | $71.54 | 5.4 | 8% | $98.3 | +37% |  |
| 96 | ZTS | Zoetis Inc. | $79.44 | 6.1 | 8% | $109.16 | +37% |  |
| 97 | INTU | Intuit Inc. | $296.76 | 16.38 | 15% | $403.83 | +36% |  |
| 98 | MS | Morgan Stanley | $211.93 | 11.04 | 16% | $288.45 | +36% |  |
| 99 | MRK | Merck & Company, Inc. | $120.79 | 3.55 | 30% | $163.69 | +36% |  |
| 100 | PTC | PTC Inc. | $137.0 | 10.41 | 8% | $185.51 | +35% |  |
| 101 | IT | Gartner, Inc. | $164.02 | 10.12 | 12% | $221.58 | +35% |  |
| 102 | AFL | AFLAC Incorporated | $118.24 | 8.75 | 8% | $159.51 | +35% |  |
| 103 | LULU | lululemon athletica inc. | $114.23 | 12.35 | 0% | $153.37 | +34% |  |
| 104 | MET | MetLife, Inc. | $84.49 | 5.17 | 12% | $113.5 | +34% |  |
| 105 | HSY | The Hershey Company | $184.58 | 5.37 | 30% | $247.6 | +34% |  |
| 106 | GS | Goldman Sachs Group, Inc.  | $1038.68 | 54.74 | 15% | $1386.42 | +34% |  |
| 107 | NXPI | NXP Semiconductors N.V. | $295.96 | 10.45 | 25% | $395.08 | +34% |  |
| 108 | ICE | Intercontinental Exchange  | $141.5 | 6.88 | 17% | $188.28 | +33% |  |
| 109 | BR | Broadridge Financial Solut | $151.34 | 9.35 | 12% | $200.73 | +33% |  |
| 110 | HPQ | HP Inc. | $25.58 | 2.7 | 0% | $33.53 | +31% |  |
| 111 | FITB | Fifth Third Bancorp | $52.01 | 2.97 | 13% | $68.01 | +31% |  |
| 112 | SPG | Simon Property Group, Inc. | $210.31 | 14.39 | 9% | $274.83 | +31% |  |
| 113 | AIZ | Assurant, Inc. | $257.35 | 19.51 | 7% | $336.18 | +31% |  |
| 114 | PODD | Insulet Corporation | $153.22 | 4.28 | 30% | $197.35 | +29% |  |
| 115 | BKNG | Booking Holdings Inc. Comm | $165.84 | 7.58 | 18% | $212.54 | +28% |  |
| 116 | DG | Dollar General Corporation | $103.7 | 7.07 | 9% | $132.87 | +28% |  |
| 117 | FICO | Fair Isaac Corporation | $1137.33 | 31.5 | 30% | $1452.43 | +28% |  |
| 118 | AXP | American Express Company | $310.66 | 16.03 | 14% | $391.77 | +26% |  |
| 119 | STT | State Street Corporation | $161.75 | 9.85 | 11% | $203.35 | +26% |  |
| 120 | ULTA | Ulta Beauty, Inc. | $467.07 | 26.67 | 12% | $586.82 | +26% |  |
| 121 | LDOS | Leidos Holdings, Inc. | $124.43 | 10.92 | 3% | $156.07 | +25% |  |
| 122 | WRB | W.R. Berkley Corporation | $68.57 | 4.72 | 8% | $85.97 | +25% |  |
| 123 | DIS | Walt Disney Company (The) | $99.71 | 6.25 | 10% | $123.59 | +24% |  |
| 124 | AON | Aon plc | $328.53 | 18.23 | 12% | $400.04 | +22% |  |
| 125 | ACN | Accenture plc | $178.25 | 12.19 | 7% | $214.71 | +20% |  |
| 126 | PCAR | PACCAR Inc. | $116.68 | 4.7 | 19% | $140.4 | +20% |  |
| 127 | HII | Huntington Ingalls Industr | $293.04 | 15.38 | 13% | $352.36 | +20% |  |
| 128 | PGR | Progressive Corporation (T | $204.02 | 19.67 | 0% | $244.27 | +20% |  |
| 129 | FDX | FedEx Corporation | $331.0 | 18.73 | 11% | $393.71 | +19% |  |
| 130 | OTIS | Otis Worldwide Corporation | $70.34 | 3.76 | 12% | $83.17 | +18% |  |
| 131 | TXT | Textron Inc. | $91.08 | 5.24 | 11% | $107.69 | +18% |  |
| 132 | MAS | Masco Corporation | $69.41 | 4.04 | 10% | $81.09 | +17% |  |
| 133 | MCK | McKesson Corporation | $775.66 | 38.4 | 14% | $905.75 | +17% |  |
| 134 | DXCM | DexCom, Inc. | $72.86 | 2.33 | 24% | $85.03 | +17% |  |
| 135 | LVS | Las Vegas Sands Corp. | $50.25 | 2.71 | 12% | $58.55 | +16% |  |
| 136 | PRU | Prudential Financial, Inc. | $104.62 | 9.71 | 0% | $120.58 | +15% |  |
| 137 | DLTR | Dollar Tree, Inc. | $108.8 | 6.23 | 10% | $124.88 | +15% |  |
| 138 | LLY | Eli Lilly and Company | $1131.42 | 28.17 | 30% | $1298.88 | +15% |  |
| 139 | OKE | ONEOK, Inc. | $88.25 | 5.61 | 8% | $101.23 | +15% |  |
| 140 | TROW | T. Rowe Price Group, Inc. | $105.99 | 9.32 | 1% | $121.16 | +14% |  |
| 141 | MU | Micron Technology, Inc. | $864.01 | 21.17 | 30% | $976.12 | +13% |  |
| 142 | ES | Eversource Energy (D/B/A) | $70.6 | 4.67 | 6% | $78.71 | +12% |  |
| 143 | KKR | KKR & Co. Inc. | $93.4 | 2.94 | 23% | $103.77 | +11% |  |
| 144 | CDW | CDW Corporation | $133.04 | 8.21 | 8% | $147.74 | +11% |  |
| 145 | KMI | Kinder Morgan, Inc. | $31.68 | 1.49 | 14% | $35.11 | +11% |  |
| 146 | DECK | Deckers Outdoor Corporatio | $108.13 | 7.02 | 6% | $119.5 | +10% |  |
| 147 | JKHY | Jack Henry & Associates, I | $130.11 | 7.16 | 10% | $141.52 | +9% |  |
| 148 | PHM | PulteGroup, Inc. | $118.4 | 10.34 | 0% | $128.41 | +8% |  |
| 149 | AMAT | Applied Materials, Inc. | $453.01 | 10.65 | 30% | $491.06 | +8% |  |
| 150 | RMD | ResMed Inc. | $196.04 | 10.37 | 10% | $212.16 | +8% |  |
| 151 | GEHC | GE HealthCare Technologies | $64.67 | 4.17 | 6% | $69.79 | +8% |  |
| 152 | TPR | Tapestry, Inc. | $140.1 | 3.28 | 30% | $151.24 | +8% |  |
| 153 | ATO | Atmos Energy Corporation | $170.24 | 8.12 | 13% | $183.25 | +8% |  |
| 154 | CRM | Salesforce, Inc. | $185.66 | 8.63 | 13% | $197.46 | +6% |  |
| 155 | TGT | Target Corporation | $122.57 | 7.57 | 7% | $130.26 | +6% |  |
| 156 | NOC | Northrop Grumman Corporati | $544.4 | 31.9 | 8% | $578.31 | +6% |  |
| 157 | DPZ | Domino's Pizza Inc | $313.99 | 17.36 | 9% | $333.23 | +6% |  |
| 158 | AMT | American Tower Corporation | $194.12 | 6.19 | 22% | $205.22 | +6% |  |
| 159 | WY | Weyerhaeuser Company | $24.48 | 0.56 | 30% | $25.82 | +6% |  |
| 160 | CPB | The Campbell's Company | $21.68 | 1.84 | 0% | $22.85 | +5% |  |
| 161 | CBRE | CBRE Group Inc | $130.93 | 4.39 | 20% | $137.36 | +5% |  |
| 162 | JCI | Johnson Controls Internati | $143.65 | 3.28 | 30% | $150.13 | +4% |  |
| 163 | PEG | Public Service Enterprise  | $79.48 | 4.52 | 8% | $82.7 | +4% |  |
| 164 | MO | Altria Group, Inc. | $72.19 | 4.79 | 5% | $75.09 | +4% |  |
| 165 | GPN | Global Payments Inc. | $66.32 | 2.72 | 15% | $68.31 | +3% |  |
| 166 | META | Meta Platforms, Inc. | $593.0 | 27.52 | 12% | $609.86 | +3% |  |
| 167 | PNR | Pentair plc. | $73.15 | 3.98 | 9% | $75.11 | +3% |  |
| 168 | BSX | Boston Scientific Corporat | $48.55 | 2.39 | 11% | $49.43 | +2% |  |
| 169 | AMZN | Amazon.com, Inc. | $246.03 | 7.77 | 21% | $249.76 | +2% |  |
| 170 | BRK-B | Berkshire Hathaway Inc. Ne | $488.13 | 33.58 | 4% | $495.04 | +1% |  |
| 171 | CSX | CSX Corporation | $46.99 | 1.63 | 19% | $47.66 | +1% |  |
| 172 | ALLE | Allegion plc | $130.16 | 7.31 | 8% | $131.72 | +1% |  |
| 173 | COR | Cencora, Inc. | $275.04 | 13.04 | 11% | $277.82 | +1% |  |
| 174 | DVN | Devon Energy Corporation | $44.28 | 3.59 | 0% | $44.58 | +1% |  |
| 175 | HPE | Hewlett Packard Enterprise | $49.2 | 1.07 | 30% | $49.34 | +0% |  |
| 176 | EFX | Equifax, Inc. | $172.13 | 5.68 | 19% | $171.39 | -0% |  |
| 177 | REGN | Regeneron Pharmaceuticals, | $635.45 | 40.99 | 4% | $630.41 | -1% |  |
| 178 | TSCO | Tractor Supply Company | $29.78 | 2.03 | 3% | $29.45 | -1% |  |
| 179 | CRH | CRH PLC | $105.06 | 5.39 | 9% | $103.77 | -1% |  |
| 180 | ED | Consolidated Edison, Inc. | $106.26 | 5.93 | 7% | $104.45 | -2% |  |
| 181 | CAT | Caterpillar, Inc. | $904.28 | 20.08 | 28% | $875.03 | -3% |  |
| 182 | STZ | Constellation Brands, Inc. | $140.91 | 9.61 | 3% | $136.25 | -3% |  |
| 183 | BLK | BlackRock, Inc. | $995.6 | 39.72 | 14% | $956.83 | -4% |  |
| 184 | ADSK | Autodesk, Inc. | $229.96 | 6.85 | 21% | $220.09 | -4% |  |
| 185 | LEN | Lennar Corporation | $90.49 | 6.95 | 0% | $86.31 | -5% |  |
| 186 | KVUE | Kenvue Inc. | $17.71 | 0.84 | 10% | $16.84 | -5% |  |
| 187 | ROP | Roper Technologies, Inc. | $332.18 | 16.01 | 10% | $316.0 | -5% |  |
| 188 | APP | Applovin Corporation | $557.2 | 11.48 | 30% | $529.33 | -5% |  |
| 189 | ADP | Automatic Data Processing, | $231.95 | 10.72 | 10% | $219.32 | -5% |  |
| 190 | TXN | Texas Instruments Incorpor | $285.06 | 5.84 | 30% | $269.28 | -6% |  |
| 191 | EVRG | Evergy, Inc. | $83.27 | 3.76 | 11% | $78.47 | -6% |  |
| 192 | PPG | PPG Industries, Inc. | $113.8 | 6.98 | 4% | $106.48 | -6% |  |
| 193 | ABNB | Airbnb, Inc. | $133.54 | 4.05 | 20% | $124.32 | -7% |  |
| 194 | AEE | Ameren Corporation | $109.27 | 5.56 | 8% | $101.69 | -7% |  |
| 195 | DLR | Digital Realty Trust, Inc. | $186.79 | 3.77 | 30% | $173.83 | -7% |  |
| 196 | FDS | FactSet Research Systems I | $255.62 | 15.54 | 4% | $237.97 | -7% |  |
| 197 | CLX | Clorox Company (The) | $94.14 | 6.15 | 3% | $87.26 | -7% |  |
| 198 | ORCL | Oracle Corporation | $213.68 | 5.58 | 23% | $195.96 | -8% |  |
| 199 | APH | Amphenol Corporation | $138.81 | 3.48 | 24% | $127.21 | -8% |  |
| 200 | AVY | Avery Dennison Corporation | $155.18 | 8.88 | 5% | $142.16 | -8% |  |
| 201 | MA | Mastercard Incorporated | $491.08 | 17.29 | 16% | $448.65 | -9% |  |
| 202 | DHI | D.R. Horton, Inc. | $145.6 | 10.64 | 0% | $132.13 | -9% |  |
| 203 | DUK | Duke Energy Corporation (H | $124.22 | 6.5 | 7% | $112.79 | -9% |  |
| 204 | IQV | IQVIA Holdings, Inc. | $183.45 | 8.05 | 11% | $166.41 | -9% |  |
| 205 | L | Loews Corporation | $107.57 | 7.86 | 0% | $97.61 | -9% |  |
| 206 | KDP | Keurig Dr Pepper Inc. | $30.53 | 1.35 | 10% | $27.57 | -10% |  |
| 207 | EXPD | Expeditors International o | $160.44 | 6.19 | 14% | $144.47 | -10% |  |
| 208 | CMS | CMS Energy Corporation | $72.04 | 3.62 | 8% | $64.78 | -10% |  |
| 209 | AEP | American Electric Power Co | $129.14 | 6.75 | 7% | $115.93 | -10% |  |
| 210 | YUM | Yum! Brands, Inc. | $150.87 | 6.2 | 12% | $134.84 | -11% |  |
| 211 | CME | CME Group Inc. | $257.4 | 11.71 | 10% | $229.66 | -11% |  |
| 212 | FDXF |  | $167.84 | 4.55 | 22% | $149.73 | -11% |  |
| 213 | NEE | NextEra Energy, Inc. | $85.84 | 3.94 | 9% | $76.43 | -11% |  |
| 214 | BMY | Bristol-Myers Squibb Compa | $57.27 | 3.57 | 3% | $50.43 | -12% |  |
| 215 | GD | General Dynamics Corporati | $346.44 | 15.9 | 9% | $304.92 | -12% |  |
| 216 | VLTO | Veralto Corp | $86.05 | 3.88 | 10% | $75.68 | -12% |  |
| 217 | DGX | Quest Diagnostics Incorpor | $200.29 | 9.05 | 9% | $175.55 | -12% |  |
| 218 | FOXA | Fox Corporation | $66.89 | 3.8 | 4% | $58.33 | -13% |  |
| 219 | NDAQ | Nasdaq, Inc. | $87.28 | 3.32 | 13% | $76.13 | -13% |  |
| 220 | NWSA | News Corporation | $27.26 | 0.79 | 19% | $23.78 | -13% |  |
| 221 | ROST | Ross Stores, Inc. | $230.37 | 7.16 | 18% | $200.08 | -13% |  |
| 222 | FIX | Comfort Systems USA, Inc. | $1843.94 | 34.67 | 30% | $1598.59 | -13% |  |
| 223 | KEYS | Keysight Technologies Inc. | $329.83 | 6.2 | 30% | $285.87 | -13% |  |
| 224 | SNDK | Sandisk Corporation | $1559.32 | 29.32 | 30% | $1351.91 | -13% |  |
| 225 | TRMB | Trimble Inc. | $54.19 | 1.91 | 15% | $46.92 | -13% |  |
| 226 | XYZ | Block, Inc. | $68.15 | 1.28 | 30% | $59.02 | -13% |  |
| 227 | PAYX | Paychex, Inc. | $100.53 | 4.53 | 9% | $86.95 | -14% |  |
| 228 | EXC | Exelon Corporation | $45.75 | 2.73 | 3% | $39.47 | -14% |  |
| 229 | V | Visa Inc. | $323.57 | 11.45 | 14% | $278.49 | -14% |  |
| 230 | RL | Ralph Lauren Corporation | $366.55 | 15.1 | 11% | $314.7 | -14% |  |
| 231 | SPGI | S&P Global Inc. | $424.44 | 15.79 | 13% | $364.33 | -14% |  |
| 232 | TMUS | T-Mobile US, Inc. | $178.1 | 9.4 | 6% | $152.64 | -14% |  |
| 233 | PNW | Pinnacle West Capital Corp | $103.06 | 5.36 | 6% | $87.97 | -15% |  |
| 234 | POOL | Pool Corporation | $185.52 | 10.87 | 3% | $158.4 | -15% |  |
| 235 | JBL | Jabil Inc. | $353.24 | 7.42 | 27% | $301.45 | -15% |  |
| 236 | BRO | Brown & Brown, Inc. | $58.86 | 3.07 | 6% | $49.87 | -15% |  |
| 237 | JBHT | J.B. Hunt Transport Servic | $284.95 | 6.44 | 25% | $240.96 | -15% |  |
| 238 | EME | EMCOR Group, Inc. | $817.44 | 29.75 | 13% | $688.25 | -16% |  |
| 239 | AZO | AutoZone, Inc. | $3116.43 | 145.54 | 8% | $2618.95 | -16% |  |
| 240 | DRI | Darden Restaurants, Inc. | $198.12 | 9.49 | 7% | $165.99 | -16% |  |
| 241 | LH | Labcorp Holdings Inc. | $265.15 | 11.3 | 10% | $221.41 | -16% |  |
| 242 | MDT | Medtronic plc. | $81.67 | 3.73 | 8% | $68.09 | -17% |  |
| 243 | NCLH | Norwegian Cruise Line Hold | $18.75 | 1.24 | 0% | $15.58 | -17% |  |
| 244 | VRTX | Vertex Pharmaceuticals Inc | $446.83 | 16.85 | 12% | $371.25 | -17% |  |
| 245 | MRSH | Marsh | $165.44 | 8.01 | 7% | $137.25 | -17% |  |
| 246 | GRMN | Garmin Ltd. | $236.57 | 8.97 | 12% | $195.61 | -17% |  |
| 247 | CASY | Caseys General Stores, Inc | $761.91 | 17.44 | 24% | $626.52 | -18% |  |
| 248 | NVR | NVR, Inc. | $6182.55 | 409.28 | 0% | $5082.61 | -18% |  |
| 249 | PPL | PPL Corporation | $35.74 | 1.63 | 8% | $29.37 | -18% |  |
| 250 | AWK | American Water Works Compa | $124.47 | 5.64 | 8% | $102.1 | -18% |  |

### 🔴 BEARISH — 250 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | UNP | Union Pacific Corporation | $272.32 | 12.15 | 8% | $221.19 | -19% |  |
| 2 | XEL | Xcel Energy Inc. | $79.04 | 3.47 | 8% | $63.93 | -19% |  |
| 3 | SNA | Snap-On Incorporated | $379.77 | 19.37 | 5% | $306.56 | -19% |  |
| 4 | CHRW | C.H. Robinson Worldwide, I | $184.09 | 4.93 | 19% | $148.32 | -19% |  |
| 5 | VMC | Vulcan Materials Company ( | $281.38 | 8.44 | 17% | $226.38 | -20% |  |
| 6 | EBAY | eBay Inc. | $109.35 | 4.33 | 10% | $87.87 | -20% |  |
| 7 | LRCX | Lam Research Corporation | $303.28 | 5.28 | 30% | $243.45 | -20% |  |
| 8 | D | Dominion Energy, Inc. | $66.9 | 3.39 | 5% | $53.58 | -20% |  |
| 9 | ERIE | Erie Indemnity Company | $227.22 | 10.92 | 6% | $181.05 | -20% |  |
| 10 | MLM | Martin Marietta Materials, | $575.83 | 15.95 | 18% | $458.35 | -20% |  |
| 11 | NI | NiSource Inc | $46.61 | 2.01 | 8% | $37.1 | -20% |  |
| 12 | HWM | Howmet Aerospace Inc. | $251.9 | 4.31 | 30% | $198.73 | -21% |  |
| 13 | ETR | Entergy Corporation | $110.74 | 3.92 | 12% | $87.3 | -21% |  |
| 14 | FOX | Fox Corporation | $59.88 | 3.8 | 0% | $47.19 | -21% |  |
| 15 | NTAP | NetApp, Inc. | $167.04 | 6.35 | 11% | $131.63 | -21% |  |
| 16 | PLD | Prologis, Inc. | $144.54 | 3.97 | 18% | $113.8 | -21% |  |
| 17 | BF-B | Brown Forman Inc | $26.16 | 1.53 | 2% | $20.5 | -22% |  |
| 18 | URI | United Rentals, Inc. | $1067.77 | 39.08 | 12% | $836.74 | -22% |  |
| 19 | ITW | Illinois Tool Works Inc. | $252.72 | 10.77 | 8% | $197.16 | -22% |  |
| 20 | WEC | WEC Energy Group, Inc. | $112.95 | 4.99 | 7% | $88.06 | -22% |  |
| 21 | SWK | Stanley Black & Decker, In | $78.48 | 2.44 | 15% | $61.03 | -22% |  |
| 22 | ZBRA | Zebra Technologies Corpora | $232.11 | 8.29 | 12% | $178.93 | -23% |  |
| 23 | ADI | Analog Devices, Inc. | $401.39 | 6.7 | 30% | $308.93 | -23% |  |
| 24 | IFF | International Flavors & Fr | $73.01 | 3.23 | 7% | $56.1 | -23% |  |
| 25 | AVB | AvalonBay Communities, Inc | $189.72 | 8.06 | 8% | $145.17 | -24% |  |
| 26 | BG | Bunge Limited | $126.46 | 3.79 | 15% | $96.45 | -24% |  |
| 27 | HSIC | Henry Schein, Inc. | $77.45 | 3.31 | 8% | $59.12 | -24% |  |
| 28 | ROK | Rockwell Automation, Inc. | $446.71 | 9.65 | 23% | $340.82 | -24% |  |
| 29 | NWS | News Corporation | $31.19 | 0.79 | 19% | $23.78 | -24% |  |
| 30 | KO | Coca-Cola Company (The) | $79.48 | 3.18 | 9% | $60.4 | -24% |  |
| 31 | LOW | Lowe's Companies, Inc. | $210.74 | 11.82 | 2% | $160.24 | -24% |  |
| 32 | PEP | Pepsico, Inc. | $141.92 | 6.37 | 6% | $107.67 | -24% |  |
| 33 | TMO | Thermo Fisher Scientific I | $472.8 | 18.2 | 10% | $358.57 | -24% |  |
| 34 | AJG | Arthur J. Gallagher & Co. | $216.14 | 6.18 | 16% | $162.59 | -25% |  |
| 35 | CMI | Cummins Inc. | $651.22 | 19.28 | 15% | $490.01 | -25% |  |
| 36 | MCD | McDonald's Corporation | $279.84 | 12.12 | 7% | $210.12 | -25% |  |
| 37 | PM | Philip Morris Internationa | $178.29 | 7.1 | 9% | $133.93 | -25% |  |
| 38 | DOC | Healthpeak Properties, Inc | $19.79 | 0.32 | 30% | $14.75 | -25% |  |
| 39 | UNH | UnitedHealth Group Incorpo | $399.47 | 13.26 | 12% | $296.34 | -26% |  |
| 40 | ZBH | Zimmer Biomet Holdings, In | $87.33 | 3.86 | 6% | $64.82 | -26% |  |
| 41 | AAPL | Apple Inc. | $307.34 | 8.27 | 17% | $227.78 | -26% |  |
| 42 | LNT | Alliant Energy Corporation | $72.87 | 3.18 | 6% | $53.83 | -26% |  |
| 43 | WMB | Williams Companies, Inc. ( | $71.96 | 2.28 | 13% | $53.19 | -26% |  |
| 44 | STE | STERIS plc (Ireland) | $212.35 | 7.92 | 10% | $156.61 | -26% |  |
| 45 | XYL | Xylem Inc. | $109.94 | 4.02 | 10% | $81.06 | -26% |  |
| 46 | J | Jacobs Solutions Inc. | $122.55 | 3.39 | 16% | $89.53 | -27% |  |
| 47 | GWW | W.W. Grainger, Inc. | $1300.01 | 37.18 | 15% | $946.99 | -27% |  |
| 48 | IBM | International Business Mac | $284.84 | 11.31 | 8% | $206.66 | -27% |  |
| 49 | CPRT | Copart, Inc. | $30.96 | 1.61 | 2% | $22.4 | -28% |  |
| 50 | WSM | Williams-Sonoma, Inc. | $204.98 | 8.92 | 6% | $148.03 | -28% |  |
| 51 | AVGO | Broadcom Inc. | $385.73 | 6.02 | 30% | $277.57 | -28% |  |
| 52 | FE | FirstEnergy Corp. | $46.42 | 1.84 | 8% | $33.26 | -28% |  |
| 53 | ORLY | O'Reilly Automotive, Inc. | $90.33 | 3.07 | 11% | $64.47 | -29% |  |
| 54 | CNP | CenterPoint Energy, Inc (H | $42.69 | 1.63 | 8% | $30.35 | -29% |  |
| 55 | HUBB | Hubbell Inc | $476.82 | 16.93 | 10% | $339.06 | -29% |  |
| 56 | MTD | Mettler-Toledo Internation | $1154.33 | 42.59 | 9% | $820.52 | -29% |  |
| 57 | VEEV | Veeva Systems Inc. | $172.61 | 5.64 | 12% | $122.72 | -29% |  |
| 58 | KIM | Kimco Realty Corporation ( | $24.23 | 0.87 | 10% | $17.21 | -29% |  |
| 59 | WM | Waste Management, Inc. | $220.4 | 6.92 | 13% | $156.31 | -29% |  |
| 60 | SO | Southern Company (The) | $92.6 | 3.91 | 6% | $65.56 | -29% |  |
| 61 | UPS | United Parcel Service, Inc | $108.54 | 6.18 | 0% | $76.75 | -29% |  |
| 62 | DOV | Dover Corporation | $214.76 | 8.01 | 9% | $151.44 | -30% |  |
| 63 | ELV | Elevance Health, Inc. | $415.53 | 23.6 | 0% | $293.07 | -30% |  |
| 64 | LII | Lennox International, Inc. | $508.43 | 22.52 | 5% | $357.44 | -30% |  |
| 65 | A | Agilent Technologies, Inc. | $135.44 | 4.98 | 9% | $94.98 | -30% |  |
| 66 | LMT | Lockheed Martin Corporatio | $523.76 | 20.64 | 7% | $367.12 | -30% |  |
| 67 | CPT | Camden Property Trust | $112.6 | 3.58 | 12% | $78.7 | -30% |  |
| 68 | TER | Teradyne, Inc. | $357.93 | 5.4 | 30% | $248.99 | -30% |  |
| 69 | MSCI | MSCI Inc. | $615.46 | 17.54 | 14% | $427.74 | -30% |  |
| 70 | TT | Trane Technologies plc | $456.84 | 13.11 | 14% | $314.71 | -31% |  |
| 71 | PSX | Phillips 66 | $183.08 | 10.12 | 0% | $125.67 | -31% |  |
| 72 | TTD | The Trade Desk, Inc. | $19.95 | 0.88 | 4% | $13.63 | -32% |  |
| 73 | WST | West Pharmaceutical Servic | $314.5 | 7.49 | 18% | $213.7 | -32% |  |
| 74 | MDLZ | Mondelez International, In | $62.04 | 2.02 | 11% | $42.0 | -32% |  |
| 75 | ALGN | Align Technology, Inc. | $167.74 | 5.95 | 9% | $113.17 | -32% |  |
| 76 | IBKR | Interactive Brokers Group, | $84.4 | 2.33 | 14% | $56.92 | -33% |  |
| 77 | SYY | Sysco Corporation | $76.29 | 3.6 | 3% | $51.4 | -33% |  |
| 78 | CAH | Cardinal Health, Inc. | $205.71 | 6.54 | 11% | $138.28 | -33% |  |
| 79 | ABT | Abbott Laboratories | $91.07 | 3.57 | 6% | $60.66 | -33% |  |
| 80 | KMB | Kimberly-Clark Corporation | $99.04 | 5.17 | 0% | $65.86 | -34% |  |
| 81 | WAB | Westinghouse Air Brake Tec | $260.4 | 7.08 | 14% | $172.96 | -34% |  |
| 82 | PG | Procter & Gamble Company ( | $146.54 | 6.84 | 3% | $97.14 | -34% |  |
| 83 | MCO | Moody's Corporation | $451.35 | 13.95 | 11% | $296.68 | -34% |  |
| 84 | JNJ | Johnson & Johnson | $232.77 | 8.64 | 7% | $152.4 | -34% |  |
| 85 | DTE | DTE Energy Company | $145.77 | 6.08 | 5% | $95.4 | -35% |  |
| 86 | TDY | Teledyne Technologies Inco | $602.27 | 19.75 | 10% | $392.85 | -35% |  |
| 87 | ANET | Arista Networks, Inc. | $154.27 | 2.92 | 23% | $100.44 | -35% |  |
| 88 | TJX | TJX Companies, Inc. (The) | $160.71 | 5.14 | 10% | $104.68 | -35% |  |
| 89 | ARES | Ares Management Corporatio | $125.65 | 2.17 | 25% | $81.58 | -35% |  |
| 90 | GM | General Motors Company | $82.11 | 2.74 | 9% | $53.01 | -35% |  |
| 91 | APD | Air Products and Chemicals | $282.35 | 9.49 | 9% | $179.55 | -36% |  |
| 92 | AMGN | Amgen Inc. | $349.58 | 14.37 | 4% | $221.32 | -37% |  |
| 93 | EMR | Emerson Electric Company | $138.12 | 4.32 | 10% | $86.4 | -37% |  |
| 94 | COP | ConocoPhillips | $117.14 | 5.9 | 0% | $73.27 | -38% |  |
| 95 | PFE | Pfizer, Inc. | $26.04 | 1.31 | 0% | $16.27 | -38% |  |
| 96 | WDAY | Workday, Inc. | $144.28 | 3.2 | 18% | $90.11 | -38% |  |
| 97 | VRSK | Verisk Analytics, Inc. | $181.73 | 6.56 | 7% | $113.41 | -38% |  |
| 98 | VRSN | VeriSign, Inc. | $294.92 | 9.05 | 10% | $183.15 | -38% |  |
| 99 | HD | Home Depot, Inc. (The) | $310.78 | 14.08 | 2% | $191.73 | -38% |  |
| 100 | NDSN | Nordson Corporation | $282.73 | 9.36 | 8% | $174.22 | -38% |  |
| 101 | SRE | DBA Sempra | $91.42 | 2.94 | 9% | $56.3 | -38% |  |
| 102 | MMM | 3M Company | $153.76 | 5.2 | 8% | $94.44 | -39% |  |
| 103 | ECL | Ecolab Inc. | $257.97 | 7.38 | 11% | $157.23 | -39% |  |
| 104 | TKO | TKO Group Holdings, Inc. | $203.49 | 2.69 | 30% | $124.03 | -39% |  |
| 105 | GE | GE Aerospace | $328.0 | 8.04 | 15% | $199.86 | -39% |  |
| 106 | SYK | Stryker Corporation | $305.66 | 8.65 | 12% | $186.29 | -39% |  |
| 107 | VRT | Vertiv Holdings, LLC | $300.51 | 3.97 | 30% | $183.05 | -39% |  |
| 108 | SHW | Sherwin-Williams Company ( | $305.3 | 10.41 | 8% | $185.59 | -39% |  |
| 109 | COO | The Cooper Companies, Inc. | $67.34 | 2.01 | 10% | $40.5 | -40% |  |
| 110 | PKG | Packaging Corporation of A | $222.82 | 8.22 | 6% | $133.67 | -40% |  |
| 111 | OXY | Occidental Petroleum Corpo | $56.93 | 0.74 | 30% | $34.12 | -40% |  |
| 112 | AMCR | Amcor plc | $38.13 | 1.25 | 8% | $22.64 | -41% |  |
| 113 | RSG | Republic Services, Inc. | $210.04 | 6.97 | 8% | $124.26 | -41% |  |
| 114 | IEX | IDEX Corporation | $215.35 | 6.76 | 9% | $127.1 | -41% |  |
| 115 | LIN | Linde plc | $507.9 | 15.08 | 10% | $299.0 | -41% |  |
| 116 | PH | Parker-Hannifin Corporatio | $882.34 | 27.09 | 9% | $517.14 | -41% |  |
| 117 | FRT | Federal Realty Investment  | $122.56 | 5.77 | 0% | $71.65 | -42% |  |
| 118 | RTX | RTX Corporation | $180.99 | 5.32 | 10% | $105.82 | -42% |  |
| 119 | Q | Qnity Electronics, Inc. | $142.05 | 3.1 | 16% | $82.69 | -42% |  |
| 120 | MSI | Motorola Solutions, Inc. | $410.34 | 12.39 | 9% | $238.15 | -42% |  |
| 121 | BX | Blackstone Inc. | $115.35 | 3.9 | 7% | $66.61 | -42% |  |
| 122 | MNST | Monster Beverage Corporati | $89.55 | 2.07 | 15% | $51.7 | -42% |  |
| 123 | AME | AMETEK, Inc. | $226.55 | 6.62 | 10% | $129.71 | -43% |  |
| 124 | LHX | L3Harris Technologies, Inc | $307.83 | 9.2 | 9% | $176.51 | -43% |  |
| 125 | FAST | Fastenal Company | $46.79 | 1.13 | 14% | $26.78 | -43% |  |
| 126 | STX | Seagate Technology Holding | $847.47 | 10.51 | 30% | $484.6 | -43% |  |
| 127 | ADM | Archer-Daniels-Midland Com | $80.92 | 2.24 | 11% | $46.12 | -43% |  |
| 128 | SBAC | SBA Communications Corpora | $208.02 | 9.51 | 0% | $118.1 | -43% |  |
| 129 | CVNA | Carvana Co. | $66.51 | 1.73 | 12% | $37.69 | -43% |  |
| 130 | HRL | Hormel Foods Corporation | $23.62 | 0.85 | 5% | $13.4 | -43% |  |
| 131 | O | Realty Income Corporation | $60.84 | 1.22 | 18% | $34.51 | -43% |  |
| 132 | GNRC | Generac Holdlings Inc. | $261.54 | 3.19 | 30% | $147.09 | -44% |  |
| 133 | TDG | Transdigm Group Incorporat | $1238.74 | 32.08 | 12% | $686.55 | -45% |  |
| 134 | IDXX | IDEXX Laboratories, Inc. | $562.16 | 13.6 | 13% | $310.21 | -45% |  |
| 135 | SBUX | Starbucks Corporation | $95.29 | 1.31 | 26% | $52.55 | -45% |  |
| 136 | MAR | Marriott International | $392.51 | 9.54 | 13% | $215.68 | -45% |  |
| 137 | CTAS | Cintas Corporation | $179.85 | 4.75 | 11% | $98.59 | -45% |  |
| 138 | REG | Regency Centers Corporatio | $77.72 | 2.91 | 3% | $42.53 | -45% |  |
| 139 | WMT | Walmart Inc. | $118.88 | 2.84 | 13% | $65.07 | -45% |  |
| 140 | CSCO | Cisco Systems, Inc. | $121.64 | 3.0 | 12% | $66.42 | -45% |  |
| 141 | GLW | Corning Incorporated | $177.58 | 2.08 | 30% | $95.91 | -46% |  |
| 142 | BA | Boeing Company (The) | $215.45 | 2.52 | 30% | $116.19 | -46% |  |
| 143 | TPL | Texas Pacific Land Corpora | $389.79 | 7.29 | 18% | $209.76 | -46% |  |
| 144 | CVS | CVS Health Corporation | $95.93 | 2.28 | 13% | $51.39 | -46% |  |
| 145 | ON | ON Semiconductor Corporati | $117.26 | 1.36 | 30% | $62.71 | -46% |  |
| 146 | QCOM | QUALCOMM Incorporated | $215.94 | 9.31 | 0% | $115.62 | -46% |  |
| 147 | ETN | Eaton Corporation, PLC | $395.94 | 10.22 | 10% | $209.28 | -47% |  |
| 148 | HON | Honeywell International In | $213.97 | 6.27 | 8% | $112.36 | -48% |  |
| 149 | CHD | Church & Dwight Company, I | $96.74 | 3.04 | 6% | $50.64 | -48% |  |
| 150 | CTVA | Corteva, Inc. | $77.03 | 1.85 | 12% | $40.31 | -48% |  |
| 151 | ISRG | Intuitive Surgical, Inc. | $422.06 | 8.23 | 17% | $220.65 | -48% |  |
| 152 | DHR | Danaher Corporation | $184.3 | 5.16 | 8% | $94.98 | -48% |  |
| 153 | SLB | SLB Limited | $54.87 | 2.27 | 0% | $28.19 | -49% |  |
| 154 | TYL | Tyler Technologies, Inc. | $312.07 | 7.24 | 12% | $156.62 | -50% |  |
| 155 | FTV | Fortive Corporation | $61.28 | 1.7 | 8% | $30.27 | -51% |  |
| 156 | PSA | Public Storage | $309.68 | 9.69 | 5% | $153.0 | -51% |  |
| 157 | XOM | Exxon Mobil Corporation | $149.92 | 5.94 | 0% | $73.77 | -51% |  |
| 158 | ROL | Rollins, Inc. | $47.1 | 1.09 | 11% | $23.06 | -51% |  |
| 159 | HLT | Hilton Worldwide Holdings  | $343.1 | 6.55 | 16% | $167.12 | -51% |  |
| 160 | CCI | Crown Castle Inc. | $94.49 | 2.37 | 9% | $45.95 | -51% |  |
| 161 | PWR | Quanta Services, Inc. | $695.11 | 7.3 | 30% | $336.59 | -52% |  |
| 162 | FFIV | F5, Inc. | $393.35 | 12.19 | 4% | $186.94 | -52% |  |
| 163 | BDX | Becton, Dickinson and Comp | $151.16 | 5.73 | 0% | $71.16 | -53% |  |
| 164 | EW | Edwards Lifesciences Corpo | $85.96 | 1.85 | 12% | $40.45 | -53% |  |
| 165 | NSC | Norfolk Southern Corporati | $313.45 | 11.88 | 0% | $147.53 | -53% |  |
| 166 | WAT | Waters Corporation | $365.36 | 7.86 | 12% | $172.1 | -53% |  |
| 167 | TSN | Tyson Foods, Inc. | $58.73 | 1.27 | 12% | $27.44 | -53% |  |
| 168 | COST | Costco Wholesale Corporati | $971.87 | 19.92 | 13% | $452.96 | -53% |  |
| 169 | CMG | Chipotle Mexican Grill, In | $29.34 | 1.09 | 0% | $13.54 | -54% |  |
| 170 | WELL | Welltower Inc. | $206.93 | 2.07 | 30% | $95.45 | -54% |  |
| 171 | EQR | Equity Residential | $68.19 | 2.5 | 0% | $31.05 | -54% |  |
| 172 | KR | Kroger Company (The) | $63.57 | 1.54 | 8% | $28.14 | -56% |  |
| 173 | BLDR | Builders FirstSource, Inc. | $73.64 | 2.62 | 0% | $32.54 | -56% |  |
| 174 | NKE | Nike, Inc. | $42.98 | 1.52 | 0% | $18.88 | -56% |  |
| 175 | FTNT | Fortinet, Inc. | $144.68 | 2.58 | 14% | $62.72 | -57% |  |
| 176 | MPWR | Monolithic Power Systems,  | $1481.05 | 13.92 | 30% | $641.83 | -57% |  |
| 177 | CL | Colgate-Palmolive Company | $88.58 | 2.58 | 3% | $37.67 | -58% |  |
| 178 | ODFL | Old Dominion Freight Line, | $242.57 | 4.78 | 12% | $102.34 | -58% |  |
| 179 | NOW | ServiceNow, Inc. | $112.45 | 1.68 | 18% | $46.65 | -58% |  |
| 180 | EQIX | Equinix, Inc. | $1080.95 | 14.48 | 20% | $447.45 | -59% |  |
| 181 | ESS | Essex Property Trust, Inc. | $285.43 | 8.88 | 1% | $116.82 | -59% |  |
| 182 | CARR | Carrier Global Corporation | $67.16 | 1.5 | 8% | $27.26 | -59% |  |
| 183 | SWKS | Skyworks Solutions, Inc. | $73.57 | 2.4 | 0% | $29.8 | -60% |  |
| 184 | KLAC | KLA Corporation | $1929.2 | 35.3 | 12% | $765.69 | -60% |  |
| 185 | INVH | Invitation Homes Inc. | $30.04 | 0.95 | 0% | $11.8 | -61% |  |
| 186 | EA | Electronic Arts Inc. | $203.0 | 3.51 | 13% | $79.07 | -61% |  |
| 187 | CVX | Chevron Corporation | $187.31 | 5.73 | 0% | $71.16 | -62% |  |
| 188 | EXR | Extra Space Storage Inc | $145.31 | 4.45 | 0% | $55.26 | -62% |  |
| 189 | DE | Deere & Company | $583.44 | 17.68 | 0% | $219.56 | -62% |  |
| 190 | HOOD | Robinhood Markets, Inc. | $82.47 | 2.06 | 3% | $29.23 | -65% |  |
| 191 | SW | Smurfit WestRock plc | $41.28 | 0.72 | 10% | $14.57 | -65% |  |
| 192 | IR | Ingersoll Rand Inc. | $72.25 | 1.48 | 6% | $25.18 | -65% |  |
| 193 | HUM | Humana Inc. | $350.08 | 9.38 | 0% | $116.48 | -67% |  |
| 194 | CDNS | Cadence Design Systems, In | $376.19 | 4.29 | 18% | $121.88 | -68% |  |
| 195 | DD | DuPont de Nemours, Inc. | $46.85 | 0.38 | 26% | $14.92 | -68% |  |
| 196 | RVTY | Revvity, Inc. | $98.37 | 2.08 | 4% | $30.92 | -69% |  |
| 197 | APTV | Aptiv PLC | $68.6 | 1.68 | 0% | $20.86 | -70% |  |
| 198 | LITE | Lumentum Holdings Inc. | $863.66 | 5.7 | 30% | $262.82 | -70% |  |
| 199 | PLTR | Palantir Technologies Inc. | $135.53 | 0.89 | 30% | $41.04 | -70% |  |
| 200 | MAA | Mid-America Apartment Comm | $137.54 | 3.3 | 0% | $40.98 | -70% |  |
| 201 | AMD | Advanced Micro Devices, In | $466.38 | 2.98 | 30% | $137.4 | -70% |  |
| 202 | MOS | Mosaic Company (The) | $22.24 | 0.14 | 29% | $6.28 | -72% |  |
| 203 | APO | Apollo Global Management,  | $128.03 | 1.59 | 13% | $35.95 | -72% |  |
| 204 | CIEN | Ciena Corporation | $488.21 | 2.98 | 30% | $137.4 | -72% |  |
| 205 | DASH | DoorDash, Inc. | $156.8 | 2.12 | 10% | $42.83 | -73% |  |
| 206 | COHR | Coherent Corp. | $376.99 | 2.11 | 30% | $97.29 | -74% |  |
| 207 | AKAM | Akamai Technologies, Inc. | $149.32 | 2.96 | 0% | $36.76 | -75% |  |
| 208 | TECH | Bio-Techne Corp | $51.99 | 0.7 | 7% | $12.42 | -76% |  |
| 209 | AXON | Axon Enterprise, Inc. | $486.12 | 2.48 | 30% | $114.35 | -76% |  |
| 210 | SNPS | Synopsys, Inc. | $464.85 | 4.37 | 15% | $107.08 | -77% |  |
| 211 | COF | Capital One Financial Corp | $180.67 | 3.25 | 0% | $41.28 | -77% |  |
| 212 | ABBV | AbbVie Inc. | $227.23 | 2.05 | 14% | $48.93 | -78% |  |
| 213 | VTR | Ventas, Inc. | $82.02 | 0.55 | 19% | $16.01 | -80% |  |
| 214 | MGM | MGM Resorts International | $47.51 | 0.73 | 0% | $9.07 | -81% |  |
| 215 | IRM | Iron Mountain Incorporated | $124.66 | 0.92 | 15% | $22.75 | -82% |  |
| 216 | NRG | NRG Energy, Inc. | $129.2 | 0.9 | 12% | $19.86 | -85% |  |
| 217 | MCHP | Microchip Technology Incor | $88.34 | 0.22 | 30% | $10.14 | -88% |  |
| 218 | PSKY | Paramount Skydance Corpora | $10.22 | 0.03 | 23% | $1.05 | -90% |  |
| 219 | CSGP | CoStar Group, Inc. | $33.89 | 0.07 | 30% | $3.23 | -90% |  |
| 220 | TSLA | Tesla, Inc. | $391.0 | 1.09 | 22% | $36.88 | -91% |  |
| 221 | PANW | Palo Alto Networks, Inc. | $272.05 | 1.14 | 11% | $23.75 | -91% |  |
| 222 | GPC | Genuine Parts Company | $98.15 | 0.44 | 4% | $6.76 | -93% |  |
| 223 | FANG | Diamondback Energy, Inc. | $192.62 | 0.98 | 0% | $12.17 | -94% |  |
| 224 | DDOG | Datadog, Inc. | $234.11 | 0.4 | 18% | $11.41 | -95% |  |
| 225 | ALB | Albemarle Corporation | $155.44 | -3.42 | — | — | no earnings | no_earnings |
| 226 | ARE | Alexandria Real Estate Equ | $51.28 | -6.27 | — | — | no earnings | no_earnings |
| 227 | BAX | Baxter International Inc. | $19.38 | -1.91 | — | — | no earnings | no_earnings |
| 228 | CAG | ConAgra Brands, Inc. | $13.01 | -0.1 | — | — | no earnings | no_earnings |
| 229 | CNC | Centene Corporation | $62.33 | -13.05 | — | — | no earnings | no_earnings |
| 230 | CRL | Charles River Laboratories | $181.34 | -3.72 | — | — | no earnings | no_earnings |
| 231 | CRWD | CrowdStrike Holdings, Inc. | $671.02 | -0.13 | — | — | no earnings | no_earnings |
| 232 | DOW | Dow Inc. | $33.97 | -4.0 | — | — | no earnings | no_earnings |
| 233 | EL | Estee Lauder Companies, In | $83.49 | -0.7 | — | — | no earnings | no_earnings |
| 234 | F | Ford Motor Company | $14.9 | -1.55 | — | — | no earnings | no_earnings |
| 235 | FISV | Fiserv, Inc. | $54.43 | None | — | — | no earnings | no_earnings |
| 236 | HAS | Hasbro, Inc. | $84.18 | -1.61 | — | — | no earnings | no_earnings |
| 237 | INTC | Intel Corporation | $99.17 | -0.6 | — | — | no earnings | no_earnings |
| 238 | IP | International Paper Compan | $33.61 | -5.19 | — | — | no earnings | no_earnings |
| 239 | IVZ | Invesco Ltd | $27.35 | -1.47 | — | — | no earnings | no_earnings |
| 240 | KHC | The Kraft Heinz Company | $22.58 | -4.86 | — | — | no earnings | no_earnings |
| 241 | LYB | LyondellBasell Industries  | $64.5 | -2.12 | — | — | no earnings | no_earnings |
| 242 | LYV | Live Nation Entertainment, | $160.07 | -1.78 | — | — | no earnings | no_earnings |
| 243 | MRNA | Moderna, Inc. | $47.44 | -8.14 | — | — | no earnings | no_earnings |
| 244 | OMC | Omnicom Group Inc. | $75.31 | -0.37 | — | — | no earnings | no_earnings |
| 245 | SATS | EchoStar Corporation | $116.28 | -50.21 | — | — | no earnings | no_earnings |
| 246 | SJM | The J.M. Smucker Company | $103.54 | -11.79 | — | — | no earnings | no_earnings |
| 247 | TAP | Molson Coors Beverage Comp | $39.06 | -10.55 | — | — | no earnings | no_earnings |
| 248 | TTWO | Take-Two Interactive Softw | $214.39 | -1.63 | — | — | no earnings | no_earnings |
| 249 | VTRS | Viatris Inc. | $15.88 | -0.3 | — | — | no earnings | no_earnings |
| 250 | WBD | Warner Bros. Discovery, In | $26.24 | -0.7 | — | — | no earnings | no_earnings |

<details><summary>Neutral / near-median (3) — excluded from the split</summary>

| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | COIN | Coinbase Global, Inc. | $152.4 | 2.71 | 30% | $124.95 | -18% |  |
| 2 | WYNN | Wynn Resorts, Limited | $104.48 | 3.49 | 14% | $85.18 | -18% |  |
| 3 | AOS | A.O. Smith Corporation | $57.2 | 3.75 | 0% | $46.57 | -19% |  |

</details>

---
## Russell 1000 (top ~1000 US by market cap)
Valued 1000 holdings · **500 most undervalued (BULLISH)** vs **500 most overvalued (BEARISH)** · 0 near-median (neutral, excluded).

### 🟢 BULLISH — 500 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | CET | 11017 | $52.5 | 9.15 | 30% | $421.9 | +704% |  |
| 2 | CI | The Cigna Group | $289.48 | 113.71 | 10% | $2282.48 | +688% |  |
| 3 | EXE | Expand Energy Corporation | $92.07 | 13.44 | 27% | $553.81 | +502% |  |
| 4 | KEP | Korea Electric Power Corpo | $12.39 | 4.43 | 5% | $70.41 | +468% |  |
| 5 | LTM | LATAM Airlines Group S.A. | $48.32 | 5.78 | 30% | $266.51 | +452% |  |
| 6 | APA | APA Corporation | $36.57 | 4.29 | 30% | $197.81 | +441% |  |
| 7 | CHTR | Charter Communications, In | $132.12 | 36.95 | 9% | $702.78 | +432% |  |
| 8 | GFI | Gold Fields Limited | $36.62 | 3.94 | 30% | $181.67 | +396% |  |
| 9 | UAL | United Airlines Holdings,  | $105.73 | 11.18 | 30% | $515.5 | +388% |  |
| 10 | EQT | EQT Corporation | $53.75 | 5.27 | 30% | $242.99 | +352% |  |
| 11 | CF | CF Industries Holdings, In | $113.49 | 11.1 | 30% | $511.81 | +351% |  |
| 12 | ALLY | Ally Financial Inc. | $42.77 | 4.12 | 30% | $189.97 | +344% |  |
| 13 | DINO | HF Sinclair Corporation | $71.39 | 6.66 | 30% | $307.08 | +330% |  |
| 14 | B | Barrick Mining Corporation | $39.46 | 3.62 | 30% | $166.91 | +323% |  |
| 15 | KGC | Kinross Gold Corporation | $26.22 | 2.35 | 30% | $108.36 | +313% |  |
| 16 | AXIA | AXIA Energia | $9.8 | 0.87 | 30% | $40.11 | +309% |  |
| 17 | AR | Antero Resources Corporati | $35.56 | 3.09 | 30% | $142.48 | +301% |  |
| 18 | EG | Everest Group, Ltd. | $334.41 | 49.12 | 17% | $1324.85 | +296% |  |
| 19 | RCI | Rogers Communication, Inc. | $37.63 | 9.38 | 4% | $142.54 | +279% |  |
| 20 | AES | The AES Corporation | $14.67 | 1.92 | 18% | $55.15 | +276% |  |
| 21 | AU | AngloGold Ashanti PLC | $84.12 | 6.81 | 30% | $314.0 | +273% |  |
| 22 | TM | Toyota Motor Corporation | $177.16 | 18.46 | 23% | $650.66 | +267% |  |
| 23 | AER | AerCap Holdings N.V. | $136.94 | 22.79 | 12% | $496.33 | +262% |  |
| 24 | NEM | Newmont Corporation | $99.71 | 7.71 | 30% | $355.5 | +256% |  |
| 25 | LYG | Lloyds Banking Group Plc | $5.31 | 0.41 | 30% | $18.9 | +256% |  |
| 26 | TCOM | Trip.com Group Limited | $47.69 | 7.04 | 14% | $167.45 | +251% |  |
| 27 | TTE | TotalEnergies SE | $88.71 | 6.74 | 30% | $310.77 | +250% |  |
| 28 | CDE | Coeur Mining, Inc. | $16.37 | 1.24 | 30% | $57.17 | +249% |  |
| 29 | HMY | Harmony Gold Mining Compan | $15.71 | 1.57 | 23% | $54.22 | +245% |  |
| 30 | EOG | EOG Resources, Inc. | $137.78 | 10.17 | 30% | $468.93 | +240% |  |
| 31 | TIGO | Millicom International Cel | $82.66 | 7.36 | 25% | $280.83 | +240% |  |
| 32 | SF | Stifel Financial Corporati | $70.72 | 5.13 | 30% | $236.54 | +234% |  |
| 33 | AGI | Alamos Gold Inc. | $35.52 | 2.51 | 30% | $115.73 | +226% |  |
| 34 | NTR | Nutrien Ltd. | $67.2 | 4.91 | 29% | $218.58 | +225% |  |
| 35 | SYF | Synchrony Financial | $70.84 | 9.66 | 13% | $222.2 | +214% |  |
| 36 | RNR | RenaissanceRe Holdings Ltd | $288.48 | 59.34 | 4% | $904.78 | +214% |  |
| 37 | PAAS | Pan American Silver Corp. | $47.58 | 3.17 | 30% | $146.16 | +207% |  |
| 38 | MFG | Mizuho Financial Group, In | $9.52 | 0.63 | 30% | $29.05 | +205% |  |
| 39 | VG | Venture Global, Inc. | $12.8 | 0.96 | 27% | $38.92 | +204% |  |
| 40 | CFG | Citizens Financial Group,  | $63.98 | 4.22 | 30% | $194.58 | +204% |  |
| 41 | SHEL | Shell PLC | $85.4 | 6.42 | 27% | $259.28 | +204% |  |
| 42 | HBM | Hudbay Minerals Inc. | $25.66 | 1.67 | 30% | $77.0 | +200% |  |
| 43 | DB | Deutsche Bank AG | $31.51 | 3.67 | 16% | $94.49 | +200% |  |
| 44 | AEM | Agnico Eagle Mines Limited | $163.66 | 10.62 | 30% | $489.67 | +199% |  |
| 45 | CVE | Cenovus Energy Inc | $28.22 | 1.81 | 30% | $83.46 | +196% |  |
| 46 | ARW | Arrow Electronics, Inc. | $219.09 | 13.98 | 30% | $644.6 | +194% |  |
| 47 | BPYPN | Brookfield Property Partne | $13.63 | 2.196 | 8% | $40.07 | +194% |  |
| 48 | BCS | Barclays PLC | $24.27 | 2.33 | 20% | $71.04 | +193% |  |
| 49 | BPOP | Popular, Inc. | $153.07 | 13.52 | 21% | $442.91 | +189% |  |
| 50 | GME | GameStop Corporation | $21.8 | 1.34 | 30% | $61.79 | +183% |  |
| 51 | C | Citigroup, Inc. | $132.47 | 8.09 | 30% | $373.02 | +182% |  |
| 52 | SU | Suncor Energy  Inc. | $62.22 | 3.78 | 30% | $173.62 | +179% |  |
| 53 | NWG | NatWest Group plc | $15.79 | 1.87 | 13% | $43.61 | +176% |  |
| 54 | SUZ | Suzano S.A. | $8.18 | 1.81 | 0% | $22.48 | +175% |  |
| 55 | DAL | Delta Air Lines, Inc. | $79.42 | 6.85 | 20% | $213.98 | +169% |  |
| 56 | EQNR | Equinor ASA | $36.94 | 2.21 | 29% | $98.8 | +168% |  |
| 57 | MPC | Marathon Petroleum Corpora | $262.01 | 15.2 | 30% | $700.85 | +168% |  |
| 58 | BPYPO | Brookfield Property Partne | $15.0 | 2.196 | 8% | $40.07 | +167% |  |
| 59 | CMCSA | Comcast Corporation | $23.82 | 5.1 | 0% | $63.33 | +166% |  |
| 60 | MLI | Mueller Industries, Inc. | $132.8 | 7.64 | 30% | $352.27 | +165% |  |
| 61 | UBER | Uber Technologies, Inc. | $70.71 | 4.03 | 30% | $185.82 | +163% |  |
| 62 | GILD | Gilead Sciences, Inc. | $129.16 | 7.35 | 30% | $338.9 | +162% |  |
| 63 | WF | Woori Financial Group Inc. | $60.57 | 7.93 | 10% | $157.88 | +161% |  |
| 64 | BBD | Banco Bradesco Sa | $3.36 | 0.41 | 11% | $8.75 | +160% |  |
| 65 | BPYPP | Brookfield Property Partne | $15.43 | 2.196 | 8% | $40.07 | +160% |  |
| 66 | T | AT&T Inc. | $22.75 | 3.04 | 9% | $58.62 | +158% |  |
| 67 | FSLR | First Solar, Inc. | $279.01 | 15.49 | 30% | $714.22 | +156% |  |
| 68 | ALL | Allstate Corporation (The) | $221.01 | 45.2 | 0% | $561.31 | +154% |  |
| 69 | NU | Nu Holdings Ltd. | $11.97 | 0.65 | 30% | $29.97 | +150% |  |
| 70 | DVA | DaVita Inc. | $192.16 | 10.38 | 30% | $478.61 | +149% |  |
| 71 | KEY | KeyCorp | $21.76 | 1.63 | 22% | $54.02 | +148% |  |
| 72 | BCE | BCE, Inc. | $24.41 | 4.87 | 0% | $60.48 | +148% |  |
| 73 | BABA | Alibaba Group Holding Limi | $121.06 | 6.5 | 30% | $299.71 | +148% |  |
| 74 | OVV | Ovintiv Inc. (DE) | $56.7 | 3.04 | 30% | $140.17 | +147% |  |
| 75 | VLO | Valero Energy Corporation | $255.82 | 13.69 | 30% | $631.23 | +147% |  |
| 76 | MT | Arcelor Mittal NY Registry | $67.21 | 3.82 | 28% | $165.82 | +147% |  |
| 77 | ACGL | Arch Capital Group Ltd. | $91.19 | 13.0 | 7% | $224.11 | +146% |  |
| 78 | FIS | Fidelity National Informat | $40.95 | 5.16 | 9% | $99.23 | +142% |  |
| 79 | EVR | Evercore Inc. | $339.43 | 17.79 | 30% | $820.27 | +142% |  |
| 80 | RGA | Reinsurance Group of Ameri | $204.96 | 18.41 | 17% | $492.73 | +140% |  |
| 81 | SHG | Shinhan Financial Group Co | $67.17 | 6.68 | 14% | $159.72 | +138% |  |
| 82 | SBS | Companhia de saneamento Ba | $5.35 | 0.5 | 15% | $12.71 | +138% |  |
| 83 | FITBO | Fifth Third Bancorp - Depo | $18.36 | 3.483 | 0% | $43.25 | +136% |  |
| 84 | MKC | McCormick & Company, Incor | $47.24 | 6.1 | 8% | $110.28 | +133% |  |
| 85 | MUSA | Murphy USA Inc. | $546.51 | 28.75 | 28% | $1251.87 | +129% |  |
| 86 | ITUB | Itau Unibanco Banco Holdin | $7.54 | 0.81 | 11% | $17.26 | +129% |  |
| 87 | UBS | UBS Group AG Registered | $47.01 | 2.79 | 25% | $106.67 | +127% |  |
| 88 | SCHW | Charles Schwab Corporation | $88.84 | 5.03 | 26% | $201.23 | +126% |  |
| 89 | PBR | Petroleo Brasileiro S.A. P | $17.75 | 3.2 | 0% | $39.74 | +124% |  |
| 90 | SAN | Banco Santander, S.A. Spon | $12.15 | 1.03 | 16% | $26.78 | +120% |  |
| 91 | SUN | Sunoco LP | $66.25 | 3.92 | 24% | $143.17 | +116% |  |
| 92 | HIG | The Hartford Insurance Gro | $132.14 | 14.21 | 10% | $284.72 | +116% |  |
| 93 | FMS | Fresenius Medical Care AG | $22.03 | 1.9 | 15% | $47.46 | +115% |  |
| 94 | HL | Hecla Mining Company | $14.78 | 0.69 | 30% | $31.82 | +115% |  |
| 95 | VICI | VICI Properties Inc. | $27.86 | 2.92 | 10% | $59.85 | +115% |  |
| 96 | JLL | Jones Lang LaSalle Incorpo | $295.71 | 18.6 | 22% | $633.03 | +114% |  |
| 97 | KB | KB Financial Group Inc | $107.91 | 10.46 | 12% | $227.7 | +111% |  |
| 98 | HST | Host Hotels & Resorts, Inc | $24.62 | 1.47 | 23% | $51.77 | +110% |  |
| 99 | PAYP | PayPay Corporation - Ameri | $15.08 | 1.12 | 18% | $31.68 | +110% |  |
| 100 | NLY | Annaly Capital Management  | $21.22 | 3.1 | 3% | $44.46 | +110% |  |
| 101 | GLPI | Gaming and Leisure Propert | $47.17 | 3.17 | 20% | $98.75 | +109% |  |
| 102 | BAC | Bank of America Corporatio | $53.83 | 4.03 | 17% | $110.71 | +106% |  |
| 103 | UMBF | UMB Financial Corporation | $129.92 | 11.43 | 14% | $266.89 | +105% |  |
| 104 | EDU | New Oriental Education & T | $45.74 | 2.7 | 23% | $93.71 | +105% |  |
| 105 | VLYPO | Valley National Bancorp -  | $25.0 | 1.11 | 30% | $51.18 | +105% |  |
| 106 | VLYPP | Valley National Bancorp -  | $25.1 | 1.11 | 30% | $51.18 | +104% |  |
| 107 | TECK | Teck Resources Ltd | $61.67 | 2.71 | 30% | $124.95 | +103% |  |
| 108 | NTRS | Northern Trust Corporation | $170.47 | 9.55 | 24% | $345.16 | +102% |  |
| 109 | CM | Canadian Imperial Bank of  | $108.84 | 7.26 | 19% | $219.06 | +101% |  |
| 110 | KSPI | Joint Stock Company Kaspi. | $81.17 | 11.37 | 3% | $163.21 | +101% |  |
| 111 | JEF | Jefferies Financial Group  | $55.69 | 2.98 | 25% | $111.05 | +99% |  |
| 112 | THC | Tenet Healthcare Corporati | $162.06 | 19.24 | 6% | $321.56 | +98% |  |
| 113 | TEL | TE Connectivity plc | $212.65 | 9.78 | 28% | $421.73 | +98% |  |
| 114 | AMP | Ameriprise Financial, Inc. | $454.66 | 40.15 | 12% | $894.9 | +97% |  |
| 115 | INCY | Incyte Corporation | $102.38 | 7.08 | 18% | $200.38 | +96% |  |
| 116 | ING | ING Group, N.V. | $29.67 | 2.54 | 13% | $57.96 | +95% |  |
| 117 | FHN | First Horizon Corporation | $24.16 | 1.99 | 14% | $47.06 | +95% |  |
| 118 | BAP | Credicorp Ltd. | $322.5 | 26.09 | 14% | $627.39 | +94% |  |
| 119 | SNX | TD SYNNEX Corporation | $268.8 | 12.02 | 28% | $516.1 | +92% |  |
| 120 | FIVE | Five Below, Inc. | $190.47 | 7.92 | 30% | $365.18 | +92% |  |
| 121 | TFC | Truist Financial Corporati | $49.2 | 4.04 | 13% | $94.08 | +91% |  |
| 122 | FCNCA | First Citizens BancShares, | $2075.1 | 173.48 | 13% | $3963.98 | +91% |  |
| 123 | CINF | Cincinnati Financial Corpo | $165.29 | 17.49 | 8% | $311.96 | +89% |  |
| 124 | COKE | Coca-Cola Consolidated, In | $179.91 | 7.29 | 30% | $336.13 | +87% |  |
| 125 | RF | Regions Financial Corporat | $28.54 | 2.41 | 12% | $53.22 | +86% |  |
| 126 | VST | Vistra Corp. | $148.76 | 5.98 | 30% | $275.73 | +85% |  |
| 127 | GDDY | GoDaddy Inc. | $84.38 | 6.31 | 15% | $156.04 | +85% |  |
| 128 | RGLD | Royal Gold, Inc. | $206.07 | 8.26 | 30% | $380.86 | +85% |  |
| 129 | PNFP | Pinnacle Financial Partner | $96.31 | 7.19 | 15% | $177.88 | +85% |  |
| 130 | FITBP | Fifth Third Bancorp - Depo | $23.46 | 3.483 | 0% | $43.25 | +84% |  |
| 131 | JD | JD.com, Inc. | $28.88 | 1.37 | 26% | $53.2 | +84% |  |
| 132 | CPAY | Corpay, Inc. | $347.45 | 16.71 | 25% | $638.87 | +84% |  |
| 133 | NBIX | Neurocrine Biosciences, In | $163.88 | 6.51 | 30% | $300.17 | +83% |  |
| 134 | CBOE | Cboe Global Markets, Inc. | $281.91 | 11.7 | 29% | $516.03 | +83% |  |
| 135 | NUE | Nucor Corporation | $254.39 | 10.07 | 30% | $464.32 | +82% |  |
| 136 | WBS | Webster Financial Corporat | $72.27 | 6.1 | 12% | $131.61 | +82% |  |
| 137 | AFG | American Financial Group,  | $132.46 | 10.53 | 13% | $239.97 | +81% |  |
| 138 | PNC | PNC Financial Services Gro | $228.37 | 17.22 | 14% | $413.37 | +81% |  |
| 139 | TEVA | Teva Pharmaceutical Indust | $34.19 | 1.34 | 30% | $61.79 | +81% |  |
| 140 | SMCI | Super Micro Computer, Inc. | $41.64 | 1.9 | 26% | $74.9 | +80% |  |
| 141 | RS | Reliance, Inc. | $394.41 | 15.34 | 30% | $707.31 | +79% |  |
| 142 | WFC | Wells Fargo & Company | $81.94 | 6.47 | 13% | $146.86 | +79% |  |
| 143 | SOLV | Solventum Corporation | $81.01 | 8.17 | 7% | $144.04 | +78% |  |
| 144 | USB | U.S. Bancorp | $55.69 | 4.77 | 11% | $98.52 | +77% |  |
| 145 | BHP | BHP Group Limited | $82.72 | 4.03 | 24% | $145.66 | +76% |  |
| 146 | EWBC | East West Bancorp, Inc. | $125.94 | 10.01 | 12% | $221.73 | +76% |  |
| 147 | BIIB | Biogen Inc. | $195.34 | 9.3 | 24% | $343.52 | +76% |  |
| 148 | BBDO | Banco Bradesco Sa | $2.91 | 0.41 | 0% | $5.09 | +75% |  |
| 149 | SQM | Sociedad Quimica y Minera  | $75.43 | 2.86 | 30% | $131.87 | +75% |  |
| 150 | VIV | Telefonica Brasil S.A. | $12.81 | 0.78 | 18% | $22.35 | +74% |  |
| 151 | AIG | American International Gro | $75.49 | 5.68 | 13% | $131.46 | +74% |  |
| 152 | NFLX | Netflix, Inc. | $82.18 | 3.1 | 30% | $142.94 | +74% |  |
| 153 | BNS | Bank Nova Scotia Halifax P | $80.56 | 5.22 | 16% | $139.29 | +73% |  |
| 154 | UDR | UDR, Inc. | $39.2 | 1.47 | 30% | $67.78 | +73% |  |
| 155 | AMX | America Movil, S.A.B. de C | $24.84 | 1.67 | 16% | $42.89 | +73% |  |
| 156 | CEG | Constellation Energy Corpo | $254.83 | 11.52 | 25% | $439.04 | +72% |  |
| 157 | BSAC | Banco Santander - Chile | $30.02 | 2.4 | 12% | $51.59 | +72% |  |
| 158 | FMX | Fomento Economico Mexicano | $122.88 | 4.57 | 30% | $210.72 | +72% |  |
| 159 | MTB | M&T Bank Corporation | $222.44 | 17.82 | 12% | $381.2 | +71% |  |
| 160 | BMO | Bank Of Montreal | $164.37 | 9.37 | 19% | $280.49 | +71% |  |
| 161 | BBVA | Banco Bilbao Vizcaya Argen | $22.22 | 2.11 | 8% | $37.85 | +70% |  |
| 162 | BAH | Booz Allen Hamilton Holdin | $79.48 | 6.9 | 10% | $135.32 | +70% |  |
| 163 | GEV | GE Vernova Inc. | $933.61 | 34.26 | 30% | $1579.69 | +69% |  |
| 164 | FITBI | Fifth Third Bancorp - Depo | $25.73 | 3.483 | 0% | $43.25 | +68% |  |
| 165 | CB | Chubb Limited | $326.27 | 28.25 | 9% | $547.25 | +68% |  |
| 166 | WTFC | Wintrust Financial Corpora | $152.9 | 11.93 | 12% | $255.55 | +67% |  |
| 167 | LUV | Southwest Airlines Company | $41.54 | 1.5 | 30% | $69.16 | +66% |  |
| 168 | ONBPP | Old National Bancorp - Dep | $24.76 | 0.891 | 30% | $41.08 | +66% |  |
| 169 | GOOG | Alphabet Inc. | $365.76 | 13.09 | 30% | $603.56 | +65% |  |
| 170 | JBS | JBS N.V. | $12.24 | 1.62 | 0% | $20.12 | +64% |  |
| 171 | GOOGL | Alphabet Inc. | $368.53 | 13.12 | 30% | $604.95 | +64% |  |
| 172 | HAL | Halliburton Company | $39.18 | 1.81 | 23% | $63.93 | +63% |  |
| 173 | GL | Globe Life Inc. | $159.18 | 14.45 | 8% | $259.78 | +63% |  |
| 174 | HBAN | Huntington Bancshares Inco | $16.52 | 1.3 | 11% | $26.69 | +62% |  |
| 175 | ZTO | ZTO Express (Cayman) Inc. | $22.28 | 1.69 | 11% | $35.85 | +61% |  |
| 176 | BRX | Brixmor Property Group Inc | $30.98 | 1.43 | 23% | $49.73 | +60% |  |
| 177 | PYPL | PayPal Holdings, Inc. | $41.29 | 5.33 | 0% | $66.19 | +60% |  |
| 178 | STLD | Steel Dynamics, Inc. | $268.5 | 9.32 | 30% | $429.73 | +60% |  |
| 179 | GMED | Globus Medical, Inc. | $80.0 | 4.28 | 19% | $127.85 | +60% |  |
| 180 | BKR | Baker Hughes Company | $62.59 | 3.13 | 21% | $99.66 | +59% |  |
| 181 | RJF | Raymond James Financial, I | $151.45 | 10.59 | 13% | $239.42 | +58% |  |
| 182 | AGNC | AGNC Investment Corp. | $10.17 | 1.28 | 0% | $16.07 | +58% |  |
| 183 | EXPE | Expedia Group, Inc. | $228.88 | 11.33 | 21% | $361.04 | +58% |  |
| 184 | SCCO | Southern Copper Corporatio | $172.97 | 5.9 | 30% | $272.04 | +57% |  |
| 185 | WPM | Wheaton Precious Metals Co | $116.23 | 3.95 | 30% | $182.13 | +57% |  |
| 186 | BNY | The Bank of New York Mello | $142.39 | 8.06 | 17% | $222.09 | +56% |  |
| 187 | CTSH | Cognizant Technology Solut | $53.21 | 4.61 | 8% | $83.03 | +56% |  |
| 188 | EIX | Edison International | $73.33 | 9.2 | 0% | $114.25 | +56% |  |
| 189 | WTW | Willis Towers Watson Publi | $263.54 | 17.02 | 14% | $410.18 | +56% |  |
| 190 | GIB | CGI Inc. | $67.28 | 5.51 | 9% | $104.56 | +55% |  |
| 191 | HCA | HCA Healthcare, Inc. | $372.13 | 29.03 | 10% | $576.13 | +55% |  |
| 192 | JPM | JP Morgan Chase & Co. | $312.37 | 20.9 | 13% | $479.68 | +54% |  |
| 193 | GIS | General Mills, Inc. | $33.15 | 4.09 | 0% | $50.79 | +53% |  |
| 194 | CCL | Carnival Corporation Ltd. | $27.41 | 2.27 | 8% | $41.35 | +51% |  |
| 195 | WDC | Western Digital Corporatio | $511.72 | 16.73 | 30% | $771.4 | +51% |  |
| 196 | TRV | The Travelers Companies, I | $303.25 | 33.51 | 2% | $456.53 | +50% |  |
| 197 | BEN | Franklin Resources, Inc. | $31.33 | 1.31 | 24% | $47.1 | +50% |  |
| 198 | ADBE | Adobe Inc. | $251.44 | 17.15 | 12% | $377.52 | +50% |  |
| 199 | FNV | Franco-Nevada Corporation | $218.74 | 7.11 | 30% | $327.83 | +50% |  |
| 200 | PUK | Prudential Public Limited  | $25.49 | 3.07 | 0% | $38.12 | +50% |  |
| 201 | RCL | Royal Caribbean Cruises Lt | $280.0 | 16.38 | 16% | $418.47 | +50% |  |
| 202 | SFD | Smithfield Foods, Inc. | $26.87 | 2.57 | 5% | $40.17 | +50% |  |
| 203 | PCG | Pacific Gas & Electric Co. | $17.11 | 1.29 | 10% | $25.55 | +49% |  |
| 204 | PFG | Principal Financial Group  | $105.22 | 6.97 | 13% | $156.95 | +49% |  |
| 205 | EXEL | Exelixis, Inc. | $52.7 | 3.02 | 16% | $78.36 | +49% |  |
| 206 | BALL | Ball Corporation | $52.92 | 3.43 | 13% | $78.65 | +49% |  |
| 207 | TRGP | Targa Resources, Inc. | $264.09 | 9.8 | 26% | $389.57 | +48% |  |
| 208 | WCC | WESCO International, Inc. | $354.31 | 14.07 | 24% | $522.23 | +47% |  |
| 209 | TME | Tencent Music Entertainmen | $9.08 | 0.84 | 5% | $13.38 | +47% |  |
| 210 | VZ | Verizon Communications Inc | $45.37 | 4.1 | 6% | $66.8 | +47% |  |
| 211 | BXP | BXP, Inc. | $62.33 | 1.99 | 30% | $91.76 | +47% |  |
| 212 | NVDA | NVIDIA Corporation | $205.1 | 6.52 | 30% | $300.63 | +47% |  |
| 213 | DELL | Dell Technologies Inc. | $394.39 | 12.54 | 30% | $578.2 | +47% |  |
| 214 | SEIC | SEI Investments Company | $89.42 | 5.86 | 12% | $131.02 | +46% |  |
| 215 | UMC | United Microelectronics Co | $19.7 | 0.62 | 30% | $28.59 | +45% |  |
| 216 | MSFT | Microsoft Corporation | $416.67 | 16.79 | 23% | $595.89 | +43% |  |
| 217 | RYAAY | Ryanair Holdings plc | $56.98 | 4.74 | 7% | $81.14 | +42% |  |
| 218 | GEN | Gen Digital Inc. | $26.28 | 1.57 | 14% | $36.74 | +40% |  |
| 219 | HSBC | HSBC Holdings, plc. | $90.8 | 6.05 | 11% | $126.83 | +40% |  |
| 220 | PDD | PDD Holdings Inc. | $85.07 | 9.53 | 0% | $118.35 | +39% |  |
| 221 | EMBJ | Embraer S.A. | $56.68 | 1.71 | 30% | $78.85 | +39% |  |
| 222 | TIMB | TIM S.A. | $21.57 | 1.76 | 6% | $29.96 | +39% |  |
| 223 | PKX | POSCO Holdings Inc. | $61.59 | 1.85 | 30% | $85.3 | +38% |  |
| 224 | TRU | TransUnion | $70.66 | 3.61 | 17% | $97.41 | +38% |  |
| 225 | FCX | Freeport-McMoRan, Inc. | $63.37 | 1.89 | 30% | $87.15 | +38% |  |
| 226 | ZTS | Zoetis Inc. | $79.44 | 6.1 | 8% | $109.16 | +37% |  |
| 227 | BBY | Best Buy Co., Inc. | $71.54 | 5.4 | 8% | $98.3 | +37% |  |
| 228 | IBN | ICICI Bank Limited | $25.95 | 1.55 | 13% | $35.4 | +36% |  |
| 229 | NMR | Nomura Holdings Inc | $8.41 | 0.74 | 4% | $11.45 | +36% |  |
| 230 | MS | Morgan Stanley | $211.93 | 11.04 | 16% | $288.45 | +36% |  |
| 231 | INTU | Intuit Inc. | $296.76 | 16.38 | 15% | $403.83 | +36% |  |
| 232 | GSK | GSK plc | $51.52 | 3.82 | 8% | $69.86 | +36% |  |
| 233 | MRK | Merck & Company, Inc. | $120.79 | 3.55 | 30% | $163.69 | +36% |  |
| 234 | PTC | PTC Inc. | $137.0 | 10.41 | 8% | $185.51 | +35% |  |
| 235 | IT | Gartner, Inc. | $164.02 | 10.12 | 12% | $221.58 | +35% |  |
| 236 | AFL | AFLAC Incorporated | $118.24 | 8.75 | 8% | $159.51 | +35% |  |
| 237 | ALSN | Allison Transmission Holdi | $115.75 | 6.44 | 14% | $155.82 | +35% |  |
| 238 | MET | MetLife, Inc. | $84.49 | 5.17 | 12% | $113.5 | +34% |  |
| 239 | LULU | lululemon athletica inc. | $114.23 | 12.35 | 0% | $153.37 | +34% |  |
| 240 | HSY | The Hershey Company | $184.58 | 5.37 | 30% | $247.6 | +34% |  |
| 241 | YUMC | Yum China Holdings, Inc. | $42.88 | 2.51 | 13% | $57.43 | +34% |  |
| 242 | GS | Goldman Sachs Group, Inc.  | $1038.68 | 54.74 | 15% | $1386.42 | +34% |  |
| 243 | NXPI | NXP Semiconductors N.V. | $295.96 | 10.45 | 25% | $395.08 | +34% |  |
| 244 | MPLX | MPLX LP | $56.48 | 4.62 | 6% | $75.41 | +34% |  |
| 245 | NTES | NetEase, Inc. | $119.48 | 7.82 | 10% | $159.12 | +33% |  |
| 246 | BP | BP p.l.c. | $42.97 | 1.24 | 30% | $57.17 | +33% |  |
| 247 | ICE | Intercontinental Exchange  | $141.5 | 6.88 | 17% | $188.28 | +33% |  |
| 248 | HTHT | H World Group Limited | $45.0 | 2.34 | 16% | $59.86 | +33% |  |
| 249 | BR | Broadridge Financial Solut | $151.34 | 9.35 | 12% | $200.73 | +33% |  |
| 250 | MFC | Manulife Financial Corpora | $38.71 | 2.5 | 10% | $51.24 | +32% |  |
| 251 | EPD | Enterprise Products Partne | $37.81 | 2.7 | 8% | $50.02 | +32% |  |
| 252 | FNF | Fidelity National Financia | $47.4 | 2.81 | 12% | $62.63 | +32% |  |
| 253 | FCFS | FirstCash Holdings, Inc. | $225.44 | 7.98 | 25% | $297.86 | +32% |  |
| 254 | ABEV | Ambev S.A. | $3.12 | 0.2 | 11% | $4.11 | +32% |  |
| 255 | VIK | Viking Holdings Ltd | $89.94 | 2.69 | 29% | $118.46 | +32% |  |
| 256 | HPQ | HP Inc. | $25.58 | 2.7 | 0% | $33.53 | +31% |  |
| 257 | CART | Maplebear Inc. | $41.26 | 1.8 | 19% | $54.02 | +31% |  |
| 258 | NGG | National Grid Transco, PLC | $81.86 | 4.4 | 14% | $107.07 | +31% |  |
| 259 | FITB | Fifth Third Bancorp | $52.01 | 2.97 | 13% | $68.01 | +31% |  |
| 260 | SPG | Simon Property Group, Inc. | $210.31 | 14.39 | 9% | $274.83 | +31% |  |
| 261 | AIZ | Assurant, Inc. | $257.35 | 19.51 | 7% | $336.18 | +31% |  |
| 262 | BUD | Anheuser-Busch Inbev SA Sp | $78.5 | 3.61 | 18% | $102.17 | +30% |  |
| 263 | TSM | Taiwan Semiconductor Manuf | $415.17 | 11.67 | 30% | $538.09 | +30% |  |
| 264 | SOFI | SoFi Technologies, Inc. | $16.03 | 0.45 | 30% | $20.75 | +29% |  |
| 265 | WMG | Warner Music Group Corp. | $29.93 | 0.84 | 30% | $38.73 | +29% |  |
| 266 | PODD | Insulet Corporation | $153.22 | 4.28 | 30% | $197.35 | +29% |  |
| 267 | PAC | Grupo Aeroportuario Del Pa | $228.8 | 11.44 | 16% | $294.55 | +29% |  |
| 268 | BKNG | Booking Holdings Inc. Comm | $165.84 | 7.58 | 18% | $212.54 | +28% |  |
| 269 | DG | Dollar General Corporation | $103.7 | 7.07 | 9% | $132.87 | +28% |  |
| 270 | FICO | Fair Isaac Corporation | $1137.33 | 31.5 | 30% | $1452.43 | +28% |  |
| 271 | CNA | CNA Financial Corporation | $43.66 | 4.47 | 0% | $55.51 | +27% |  |
| 272 | BEKE | KE Holdings Inc | $16.08 | 0.44 | 30% | $20.29 | +26% |  |
| 273 | AXP | American Express Company | $310.66 | 16.03 | 14% | $391.77 | +26% |  |
| 274 | STT | State Street Corporation | $161.75 | 9.85 | 11% | $203.35 | +26% |  |
| 275 | ULTA | Ulta Beauty, Inc. | $467.07 | 26.67 | 12% | $586.82 | +26% |  |
| 276 | WRB | W.R. Berkley Corporation | $68.57 | 4.72 | 8% | $85.97 | +25% |  |
| 277 | LDOS | Leidos Holdings, Inc. | $124.43 | 10.92 | 3% | $156.07 | +25% |  |
| 278 | TOST | Toast, Inc. | $24.64 | 0.67 | 30% | $30.89 | +25% |  |
| 279 | BTI | British American Tobacco   | $59.72 | 4.69 | 5% | $74.67 | +25% |  |
| 280 | FTI | TechnipFMC plc | $66.82 | 2.61 | 21% | $83.51 | +25% |  |
| 281 | DIS | Walt Disney Company (The) | $99.71 | 6.25 | 10% | $123.59 | +24% |  |
| 282 | UI | Ubiquiti Inc. | $567.33 | 15.54 | 30% | $702.86 | +24% |  |
| 283 | AMKR | Amkor Technology, Inc. | $64.95 | 1.74 | 30% | $80.23 | +24% |  |
| 284 | NVO | Novo Nordisk A/S | $42.96 | 4.26 | 0% | $52.9 | +23% |  |
| 285 | WES | Western Midstream Partners | $44.37 | 3.04 | 8% | $54.55 | +23% |  |
| 286 | RY | Royal Bank Of Canada | $194.04 | 11.06 | 12% | $236.8 | +22% |  |
| 287 | FUTU | Futu Holdings Limited | $92.33 | 9.06 | 0% | $112.51 | +22% |  |
| 288 | AON | Aon plc | $328.53 | 18.23 | 12% | $400.04 | +22% |  |
| 289 | ALV | Autoliv, Inc. | $127.56 | 9.29 | 6% | $154.02 | +21% |  |
| 290 | ACN | Accenture plc | $178.25 | 12.19 | 7% | $214.71 | +20% |  |
| 291 | PCAR | PACCAR Inc. | $116.68 | 4.7 | 19% | $140.4 | +20% |  |
| 292 | HII | Huntington Ingalls Industr | $293.04 | 15.38 | 13% | $352.36 | +20% |  |
| 293 | IESC | IES Holdings, Inc. | $720.72 | 18.74 | 30% | $864.08 | +20% |  |
| 294 | PGR | Progressive Corporation (T | $204.02 | 19.67 | 0% | $244.27 | +20% |  |
| 295 | FDX | FedEx Corporation | $331.0 | 18.73 | 11% | $393.71 | +19% |  |
| 296 | TOL | Toll Brothers, Inc. | $137.91 | 13.16 | 0% | $163.43 | +18% |  |
| 297 | OTIS | Otis Worldwide Corporation | $70.34 | 3.76 | 12% | $83.17 | +18% |  |
| 298 | TXT | Textron Inc. | $91.08 | 5.24 | 11% | $107.69 | +18% |  |
| 299 | ONON | On Holding AG | $37.08 | 0.95 | 30% | $43.8 | +18% |  |
| 300 | CHKP | Check Point Software Techn | $135.82 | 9.72 | 6% | $160.02 | +18% |  |
| 301 | MCK | McKesson Corporation | $775.66 | 38.4 | 14% | $905.75 | +17% |  |
| 302 | MAS | Masco Corporation | $69.41 | 4.04 | 10% | $81.09 | +17% |  |
| 303 | ARGX | argenx SE | $891.32 | 22.55 | 30% | $1039.75 | +17% |  |
| 304 | DXCM | DexCom, Inc. | $72.86 | 2.33 | 24% | $85.03 | +17% |  |
| 305 | LVS | Las Vegas Sands Corp. | $50.25 | 2.71 | 12% | $58.55 | +16% |  |
| 306 | MKL | Markel Group Inc. | $1818.67 | 138.22 | 4% | $2118.65 | +16% |  |
| 307 | PRU | Prudential Financial, Inc. | $104.62 | 9.71 | 0% | $120.58 | +15% |  |
| 308 | SGI | Somnigroup International I | $68.01 | 2.5 | 20% | $78.34 | +15% |  |
| 309 | LLY | Eli Lilly and Company | $1131.42 | 28.17 | 30% | $1298.88 | +15% |  |
| 310 | DLTR | Dollar Tree, Inc. | $108.8 | 6.23 | 10% | $124.88 | +15% |  |
| 311 | OKE | ONEOK, Inc. | $88.25 | 5.61 | 8% | $101.23 | +15% |  |
| 312 | TROW | T. Rowe Price Group, Inc. | $105.99 | 9.32 | 1% | $121.16 | +14% |  |
| 313 | LNG | Cheniere Energy, Inc. | $238.82 | 5.9 | 30% | $272.04 | +14% |  |
| 314 | TD | Toronto Dominion Bank (The | $113.16 | 6.13 | 11% | $128.39 | +14% |  |
| 315 | EHC | Encompass Health Corporati | $104.01 | 5.83 | 10% | $117.93 | +13% |  |
| 316 | EC | Ecopetrol S.A. | $15.15 | 1.38 | 0% | $17.14 | +13% |  |
| 317 | MU | Micron Technology, Inc. | $864.01 | 21.17 | 30% | $976.12 | +13% |  |
| 318 | BMRN | BioMarin Pharmaceutical In | $56.77 | 1.39 | 30% | $64.09 | +13% |  |
| 319 | BNT | Brookfield Wealth Solution | $44.43 | 2.74 | 8% | $50.0 | +12% |  |
| 320 | ES | Eversource Energy (D/B/A) | $70.6 | 4.67 | 6% | $78.71 | +12% |  |
| 321 | UNM | Unum Group | $86.84 | 4.62 | 11% | $96.85 | +12% |  |
| 322 | BSBR | Banco Santander Brasil SA | $5.24 | 0.32 | 8% | $5.83 | +11% |  |
| 323 | KKR | KKR & Co. Inc. | $93.4 | 2.94 | 23% | $103.77 | +11% |  |
| 324 | CDW | CDW Corporation | $133.04 | 8.21 | 8% | $147.74 | +11% |  |
| 325 | KMI | Kinder Morgan, Inc. | $31.68 | 1.49 | 14% | $35.11 | +11% |  |
| 326 | DECK | Deckers Outdoor Corporatio | $108.13 | 7.02 | 6% | $119.5 | +10% |  |
| 327 | TAK | Takeda Pharmaceutical Comp | $15.6 | 0.37 | 30% | $17.06 | +9% |  |
| 328 | SPOT | Spotify Technology S.A. | $496.95 | 14.96 | 24% | $539.82 | +9% |  |
| 329 | PHM | PulteGroup, Inc. | $118.4 | 10.34 | 0% | $128.41 | +8% |  |
| 330 | AMAT | Applied Materials, Inc. | $453.01 | 10.65 | 30% | $491.06 | +8% |  |
| 331 | RMD | ResMed Inc. | $196.04 | 10.37 | 10% | $212.16 | +8% |  |
| 332 | GEHC | GE HealthCare Technologies | $64.67 | 4.17 | 6% | $69.79 | +8% |  |
| 333 | TPR | Tapestry, Inc. | $140.1 | 3.28 | 30% | $151.24 | +8% |  |
| 334 | HLN | Haleon plc | $9.12 | 0.5 | 10% | $9.82 | +8% |  |
| 335 | ARCC | Ares Capital Corporation | $18.79 | 1.63 | 0% | $20.24 | +8% |  |
| 336 | ATO | Atmos Energy Corporation | $170.24 | 8.12 | 13% | $183.25 | +8% |  |
| 337 | VALE | VALE S.A. | $15.23 | 0.66 | 15% | $16.38 | +8% |  |
| 338 | GIL | Gildan Activewear, Inc. | $57.61 | 1.71 | 24% | $61.78 | +7% |  |
| 339 | HDB | HDFC Bank Limited | $23.41 | 1.4 | 8% | $24.96 | +7% |  |
| 340 | TS | Tenaris S.A. | $61.44 | 3.8 | 7% | $65.48 | +7% |  |
| 341 | TW | Tradeweb Markets Inc. | $102.53 | 4.05 | 17% | $109.24 | +6% |  |
| 342 | CRM | Salesforce, Inc. | $185.66 | 8.63 | 13% | $197.46 | +6% |  |
| 343 | WIT | Wipro Limited | $2.1 | 0.13 | 7% | $2.23 | +6% |  |
| 344 | TGT | Target Corporation | $122.57 | 7.57 | 7% | $130.26 | +6% |  |
| 345 | NOC | Northrop Grumman Corporati | $544.4 | 31.9 | 8% | $578.31 | +6% |  |
| 346 | DPZ | Domino's Pizza Inc | $313.99 | 17.36 | 9% | $333.23 | +6% |  |
| 347 | AMT | American Tower Corporation | $194.12 | 6.19 | 22% | $205.22 | +6% |  |
| 348 | SE | Sea Limited | $86.56 | 2.54 | 24% | $91.43 | +6% |  |
| 349 | WY | Weyerhaeuser Company | $24.48 | 0.56 | 30% | $25.82 | +6% |  |
| 350 | AEG | Aegon Ltd. New York Regist | $8.24 | 0.7 | 0% | $8.69 | +6% |  |
| 351 | PAG | Penske Automotive Group, I | $171.02 | 13.84 | 1% | $180.46 | +6% |  |
| 352 | CNQ | Canadian Natural Resources | $45.7 | 3.88 | 0% | $48.18 | +5% |  |
| 353 | CBRE | CBRE Group Inc | $130.93 | 4.39 | 20% | $137.36 | +5% |  |
| 354 | JCI | Johnson Controls Internati | $143.65 | 3.28 | 30% | $150.13 | +4% |  |
| 355 | PEG | Public Service Enterprise  | $79.48 | 4.52 | 8% | $82.7 | +4% |  |
| 356 | MO | Altria Group, Inc. | $72.19 | 4.79 | 5% | $75.09 | +4% |  |
| 357 | DY | Dycom Industries, Inc. | $466.28 | 10.49 | 30% | $483.68 | +4% |  |
| 358 | R | Ryder System, Inc. | $265.22 | 12.04 | 13% | $274.62 | +4% |  |
| 359 | GPN | Global Payments Inc. | $66.32 | 2.72 | 15% | $68.31 | +3% |  |
| 360 | META | Meta Platforms, Inc. | $593.0 | 27.52 | 12% | $609.86 | +3% |  |
| 361 | SNN | Smith & Nephew SNATS, Inc. | $30.61 | 1.43 | 12% | $31.46 | +3% |  |
| 362 | PNR | Pentair plc. | $73.15 | 3.98 | 9% | $75.11 | +3% |  |
| 363 | VMI | Valmont Industries, Inc. | $533.8 | 17.99 | 20% | $547.16 | +2% |  |
| 364 | CLS | Celestica, Inc. | $371.71 | 8.25 | 30% | $380.4 | +2% |  |
| 365 | CCK | Crown Holdings, Inc. | $93.38 | 6.29 | 4% | $95.45 | +2% |  |
| 366 | INFY | Infosys Limited | $12.4 | 0.8 | 5% | $12.65 | +2% |  |
| 367 | BSX | Boston Scientific Corporat | $48.55 | 2.39 | 11% | $49.43 | +2% |  |
| 368 | AMZN | Amazon.com, Inc. | $246.03 | 7.77 | 21% | $249.76 | +2% |  |
| 369 | CSX | CSX Corporation | $46.99 | 1.63 | 19% | $47.66 | +1% |  |
| 370 | CCEP | Coca-Cola Europacific Part | $94.74 | 4.94 | 9% | $96.09 | +1% |  |
| 371 | PAA | Plains All American Pipeli | $22.6 | 1.11 | 11% | $22.92 | +1% |  |
| 372 | ALLE | Allegion plc | $130.16 | 7.31 | 8% | $131.72 | +1% |  |
| 373 | COR | Cencora, Inc. | $275.04 | 13.04 | 11% | $277.82 | +1% |  |
| 374 | DVN | Devon Energy Corporation | $44.28 | 3.59 | 0% | $44.58 | +1% |  |
| 375 | HPE | Hewlett Packard Enterprise | $49.2 | 1.07 | 30% | $49.34 | +0% |  |
| 376 | SN | SharkNinja, Inc. | $119.82 | 4.96 | 14% | $119.54 | -0% |  |
| 377 | EFX | Equifax, Inc. | $172.13 | 5.68 | 19% | $171.39 | -0% |  |
| 378 | REGN | Regeneron Pharmaceuticals, | $635.45 | 40.99 | 4% | $630.41 | -1% |  |
| 379 | ZM | Zoom Communications, Inc. | $101.62 | 6.79 | 4% | $100.83 | -1% |  |
| 380 | PHG | Koninklijke Philips N.V. N | $26.11 | 1.16 | 12% | $25.84 | -1% |  |
| 381 | TSCO | Tractor Supply Company | $29.78 | 2.03 | 3% | $29.45 | -1% |  |
| 382 | CRH | CRH PLC | $105.06 | 5.39 | 9% | $103.77 | -1% |  |
| 383 | FTAI | FTAI Aviation Ltd. | $234.05 | 5.01 | 30% | $231.0 | -1% |  |
| 384 | AMRZ | Amrize Ltd | $53.58 | 2.09 | 15% | $52.82 | -1% |  |
| 385 | AZN | AstraZeneca PLC | $185.95 | 6.64 | 17% | $183.04 | -2% |  |
| 386 | ED | Consolidated Edison, Inc. | $106.26 | 5.93 | 7% | $104.45 | -2% |  |
| 387 | LPLA | LPL Financial Holdings Inc | $288.49 | 11.11 | 16% | $283.34 | -2% |  |
| 388 | AM | Antero Midstream Corporati | $21.52 | 0.86 | 14% | $21.04 | -2% |  |
| 389 | RIO | Rio Tinto Plc | $100.69 | 6.08 | 5% | $98.21 | -2% |  |
| 390 | CAT | Caterpillar, Inc. | $904.28 | 20.08 | 28% | $875.03 | -3% |  |
| 391 | STZ | Constellation Brands, Inc. | $140.91 | 9.61 | 3% | $136.25 | -3% |  |
| 392 | BLK | BlackRock, Inc. | $995.6 | 39.72 | 14% | $956.83 | -4% |  |
| 393 | ADSK | Autodesk, Inc. | $229.96 | 6.85 | 21% | $220.09 | -4% |  |
| 394 | SCI | Service Corporation Intern | $69.68 | 3.79 | 7% | $66.66 | -4% |  |
| 395 | USFD | US Foods Holding Corp. | $84.61 | 2.97 | 17% | $80.9 | -4% |  |
| 396 | LEN | Lennar Corporation | $90.49 | 6.95 | 0% | $86.31 | -5% |  |
| 397 | KVUE | Kenvue Inc. | $17.71 | 0.84 | 10% | $16.84 | -5% |  |
| 398 | ROP | Roper Technologies, Inc. | $332.18 | 16.01 | 10% | $316.0 | -5% |  |
| 399 | APP | Applovin Corporation | $557.2 | 11.48 | 30% | $529.33 | -5% |  |
| 400 | RELX | RELX PLC PLC | $35.15 | 1.5 | 12% | $33.37 | -5% |  |
| 401 | ADP | Automatic Data Processing, | $231.95 | 10.72 | 10% | $219.32 | -5% |  |
| 402 | TXN | Texas Instruments Incorpor | $285.06 | 5.84 | 30% | $269.28 | -6% |  |
| 403 | EVRG | Evergy, Inc. | $83.27 | 3.76 | 11% | $78.47 | -6% |  |
| 404 | PPG | PPG Industries, Inc. | $113.8 | 6.98 | 4% | $106.48 | -6% |  |
| 405 | CACI | CACI International, Inc. | $531.41 | 24.23 | 11% | $496.84 | -6% |  |
| 406 | SAP | SAP  SE | $184.77 | 7.24 | 14% | $172.58 | -7% |  |
| 407 | ABNB | Airbnb, Inc. | $133.54 | 4.05 | 20% | $124.32 | -7% |  |
| 408 | DLR | Digital Realty Trust, Inc. | $186.79 | 3.77 | 30% | $173.83 | -7% |  |
| 409 | AEE | Ameren Corporation | $109.27 | 5.56 | 8% | $101.69 | -7% |  |
| 410 | RDDT | Reddit, Inc. | $173.45 | 3.5 | 30% | $161.38 | -7% |  |
| 411 | FERG | Ferguson Enterprises Inc. | $229.58 | 10.17 | 11% | $213.29 | -7% |  |
| 412 | CLX | Clorox Company (The) | $94.14 | 6.15 | 3% | $87.26 | -7% |  |
| 413 | DKS | Dick's Sporting Goods Inc | $214.83 | 10.27 | 9% | $198.95 | -7% |  |
| 414 | ORCL | Oracle Corporation | $213.68 | 5.58 | 23% | $195.96 | -8% |  |
| 415 | APH | Amphenol Corporation | $138.81 | 3.48 | 24% | $127.21 | -8% |  |
| 416 | AVY | Avery Dennison Corporation | $155.18 | 8.88 | 5% | $142.16 | -8% |  |
| 417 | PSO | Pearson, Plc | $15.56 | 0.68 | 11% | $14.24 | -8% |  |
| 418 | MA | Mastercard Incorporated | $491.08 | 17.29 | 16% | $448.65 | -9% |  |
| 419 | DUK | Duke Energy Corporation (H | $124.22 | 6.5 | 7% | $112.79 | -9% |  |
| 420 | DHI | D.R. Horton, Inc. | $145.6 | 10.64 | 0% | $132.13 | -9% |  |
| 421 | IQV | IQVIA Holdings, Inc. | $183.45 | 8.05 | 11% | $166.41 | -9% |  |
| 422 | L | Loews Corporation | $107.57 | 7.86 | 0% | $97.61 | -9% |  |
| 423 | MGA | Magna International, Inc. | $66.09 | 2.37 | 15% | $59.86 | -9% |  |
| 424 | CRS | Carpenter Technology Corpo | $483.6 | 9.48 | 30% | $437.11 | -10% |  |
| 425 | KDP | Keurig Dr Pepper Inc. | $30.53 | 1.35 | 10% | $27.57 | -10% |  |
| 426 | CSL | Carlisle Companies Incorpo | $345.98 | 17.13 | 8% | $312.57 | -10% |  |
| 427 | ENSG | The Ensign Group, Inc. | $170.3 | 6.13 | 15% | $153.38 | -10% |  |
| 428 | EXPD | Expeditors International o | $160.44 | 6.19 | 14% | $144.47 | -10% |  |
| 429 | CMS | CMS Energy Corporation | $72.04 | 3.62 | 8% | $64.78 | -10% |  |
| 430 | AEP | American Electric Power Co | $129.14 | 6.75 | 7% | $115.93 | -10% |  |
| 431 | ARMK | Aramark | $53.41 | 1.34 | 24% | $47.96 | -10% |  |
| 432 | AS | Amer Sports, Inc. | $34.1 | 0.8 | 25% | $30.51 | -10% |  |
| 433 | YUM | Yum! Brands, Inc. | $150.87 | 6.2 | 12% | $134.84 | -11% |  |
| 434 | CME | CME Group Inc. | $257.4 | 11.71 | 10% | $229.66 | -11% |  |
| 435 | FDXF |  | $167.84 | 4.55 | 22% | $149.73 | -11% |  |
| 436 | NEE | NextEra Energy, Inc. | $85.84 | 3.94 | 9% | $76.43 | -11% |  |
| 437 | PR | Permian Resources Corporat | $19.17 | 0.89 | 9% | $17.01 | -11% |  |
| 438 | BMY | Bristol-Myers Squibb Compa | $57.27 | 3.57 | 3% | $50.43 | -12% |  |
| 439 | ASX | ASE Technology Holding Co. | $34.03 | 0.65 | 30% | $29.97 | -12% |  |
| 440 | GD | General Dynamics Corporati | $346.44 | 15.9 | 9% | $304.92 | -12% |  |
| 441 | VLTO | Veralto Corp | $86.05 | 3.88 | 10% | $75.68 | -12% |  |
| 442 | DGX | Quest Diagnostics Incorpor | $200.29 | 9.05 | 9% | $175.55 | -12% |  |
| 443 | NDAQ | Nasdaq, Inc. | $87.28 | 3.32 | 13% | $76.13 | -13% |  |
| 444 | FOXA | Fox Corporation | $66.89 | 3.8 | 4% | $58.33 | -13% |  |
| 445 | NWSA | News Corporation | $27.26 | 0.79 | 19% | $23.78 | -13% |  |
| 446 | DCI | Donaldson Company, Inc. | $83.65 | 3.71 | 10% | $72.93 | -13% |  |
| 447 | SSNC | SS&C Technologies Holdings | $69.91 | 3.22 | 9% | $60.85 | -13% |  |
| 448 | ROST | Ross Stores, Inc. | $230.37 | 7.16 | 18% | $200.08 | -13% |  |
| 449 | SNDK | Sandisk Corporation | $1559.32 | 29.32 | 30% | $1351.91 | -13% |  |
| 450 | FIX | Comfort Systems USA, Inc. | $1843.94 | 34.67 | 30% | $1598.59 | -13% |  |
| 451 | KEYS | Keysight Technologies Inc. | $329.83 | 6.2 | 30% | $285.87 | -13% |  |
| 452 | XYZ | Block, Inc. | $68.15 | 1.28 | 30% | $59.02 | -13% |  |
| 453 | TRMB | Trimble Inc. | $54.19 | 1.91 | 15% | $46.92 | -13% |  |
| 454 | PAYX | Paychex, Inc. | $100.53 | 4.53 | 9% | $86.95 | -14% |  |
| 455 | BCH | Banco De Chile | $36.48 | 2.5 | 0% | $31.56 | -14% |  |
| 456 | EXC | Exelon Corporation | $45.75 | 2.73 | 3% | $39.47 | -14% |  |
| 457 | FN | Fabrinet | $621.25 | 11.62 | 30% | $535.78 | -14% |  |
| 458 | SANM | Sanmina Corporation | $252.08 | 4.71 | 30% | $217.17 | -14% |  |
| 459 | V | Visa Inc. | $323.57 | 11.45 | 14% | $278.49 | -14% |  |
| 460 | RL | Ralph Lauren Corporation | $366.55 | 15.1 | 11% | $314.7 | -14% |  |
| 461 | SPGI | S&P Global Inc. | $424.44 | 15.79 | 13% | $364.33 | -14% |  |
| 462 | TMUS | T-Mobile US, Inc. | $178.1 | 9.4 | 6% | $152.64 | -14% |  |
| 463 | SNY | Sanofi | $45.02 | 2.3 | 6% | $38.55 | -14% |  |
| 464 | TRI | Thomson Reuters Corp | $86.04 | 3.48 | 11% | $73.55 | -14% |  |
| 465 | WPC | W. P. Carey Inc. REIT | $74.49 | 2.34 | 17% | $63.63 | -15% |  |
| 466 | PNW | Pinnacle West Capital Corp | $103.06 | 5.36 | 6% | $87.97 | -15% |  |
| 467 | JBL | Jabil Inc. | $353.24 | 7.42 | 27% | $301.45 | -15% |  |
| 468 | QSR | Restaurant Brands Internat | $72.66 | 3.11 | 10% | $61.95 | -15% |  |
| 469 | CNM | Core & Main, Inc. | $51.97 | 2.31 | 9% | $44.34 | -15% |  |
| 470 | BRO | Brown & Brown, Inc. | $58.86 | 3.07 | 6% | $49.87 | -15% |  |
| 471 | JBHT | J.B. Hunt Transport Servic | $284.95 | 6.44 | 25% | $240.96 | -15% |  |
| 472 | EME | EMCOR Group, Inc. | $817.44 | 29.75 | 13% | $688.25 | -16% |  |
| 473 | AZO | AutoZone, Inc. | $3116.43 | 145.54 | 8% | $2618.95 | -16% |  |
| 474 | HLI | Houlihan Lokey, Inc. | $139.25 | 6.22 | 9% | $116.9 | -16% |  |
| 475 | DRI | Darden Restaurants, Inc. | $198.12 | 9.49 | 7% | $165.99 | -16% |  |
| 476 | SLF | Sun Life Financial Inc. | $73.72 | 3.86 | 5% | $61.68 | -16% |  |
| 477 | LH | Labcorp Holdings Inc. | $265.15 | 11.3 | 10% | $221.41 | -16% |  |
| 478 | MDT | Medtronic plc. | $81.67 | 3.73 | 8% | $68.09 | -17% |  |
| 479 | VRTX | Vertex Pharmaceuticals Inc | $446.83 | 16.85 | 12% | $371.25 | -17% |  |
| 480 | MUFG | Mitsubishi UFJ Financial G | $19.91 | 1.33 | 0% | $16.52 | -17% |  |
| 481 | MRSH | Marsh | $165.44 | 8.01 | 7% | $137.25 | -17% |  |
| 482 | CG | The Carlyle Group Inc. | $43.48 | 1.46 | 15% | $36.06 | -17% |  |
| 483 | GRMN | Garmin Ltd. | $236.57 | 8.97 | 12% | $195.61 | -17% |  |
| 484 | WDS | Woodside Energy Group Limi | $21.33 | 1.42 | 0% | $17.63 | -17% |  |
| 485 | SMFG | Sumitomo Mitsui Financial  | $23.16 | 1.54 | 0% | $19.12 | -17% |  |
| 486 | CQP | Cheniere Energy Partners,  | $64.47 | 4.28 | 0% | $53.15 | -18% |  |
| 487 | BURL | Burlington Stores, Inc. | $317.05 | 9.73 | 17% | $261.31 | -18% |  |
| 488 | CASY | Caseys General Stores, Inc | $761.91 | 17.44 | 24% | $626.52 | -18% |  |
| 489 | PPL | PPL Corporation | $35.74 | 1.63 | 8% | $29.37 | -18% |  |
| 490 | NVR | NVR, Inc. | $6182.55 | 409.28 | 0% | $5082.61 | -18% |  |
| 491 | IX | ORIX Corporation | $37.88 | 2.5 | 0% | $31.05 | -18% |  |
| 492 | COIN | Coinbase Global, Inc. | $152.4 | 2.71 | 30% | $124.95 | -18% |  |
| 493 | AWK | American Water Works Compa | $124.47 | 5.64 | 8% | $102.1 | -18% |  |
| 494 | UL | Unilever PLC | $56.72 | 3.01 | 4% | $46.3 | -18% |  |
| 495 | WWD | Woodward, Inc. | $357.74 | 8.34 | 23% | $291.58 | -18% |  |
| 496 | WYNN | Wynn Resorts, Limited | $104.48 | 3.49 | 14% | $85.18 | -18% |  |
| 497 | UNP | Union Pacific Corporation | $272.32 | 12.15 | 8% | $221.19 | -19% |  |
| 498 | XEL | Xcel Energy Inc. | $79.04 | 3.47 | 8% | $63.93 | -19% |  |
| 499 | SNA | Snap-On Incorporated | $379.77 | 19.37 | 5% | $306.56 | -19% |  |
| 500 | NYT | New York Times Company (Th | $76.88 | 2.33 | 16% | $62.07 | -19% |  |

### 🔴 BEARISH — 500 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | CHRW | C.H. Robinson Worldwide, I | $184.09 | 4.93 | 19% | $148.32 | -19% |  |
| 2 | VMC | Vulcan Materials Company ( | $281.38 | 8.44 | 17% | $226.38 | -20% |  |
| 3 | ITT | ITT Inc. | $191.45 | 5.67 | 17% | $154.05 | -20% |  |
| 4 | EBAY | eBay Inc. | $109.35 | 4.33 | 10% | $87.87 | -20% |  |
| 5 | LRCX | Lam Research Corporation | $303.28 | 5.28 | 30% | $243.45 | -20% |  |
| 6 | D | Dominion Energy, Inc. | $66.9 | 3.39 | 5% | $53.58 | -20% |  |
| 7 | AFRM | Affirm Holdings, Inc. | $63.61 | 1.1 | 30% | $50.72 | -20% |  |
| 8 | ERIE | Erie Indemnity Company | $227.22 | 10.92 | 6% | $181.05 | -20% |  |
| 9 | MLM | Martin Marietta Materials, | $575.83 | 15.95 | 18% | $458.35 | -20% |  |
| 10 | NI | NiSource Inc | $46.61 | 2.01 | 8% | $37.1 | -20% |  |
| 11 | WTS | Watts Water Technologies,  | $314.21 | 10.93 | 13% | $248.98 | -21% |  |
| 12 | ERIC | Ericsson | $12.56 | 0.8 | 0% | $9.93 | -21% |  |
| 13 | HWM | Howmet Aerospace Inc. | $251.9 | 4.31 | 30% | $198.73 | -21% |  |
| 14 | ETR | Entergy Corporation | $110.74 | 3.92 | 12% | $87.3 | -21% |  |
| 15 | NTAP | NetApp, Inc. | $167.04 | 6.35 | 11% | $131.63 | -21% |  |
| 16 | FOX | Fox Corporation | $59.88 | 3.8 | 0% | $47.19 | -21% |  |
| 17 | PLD | Prologis, Inc. | $144.54 | 3.97 | 18% | $113.8 | -21% |  |
| 18 | ET | Energy Transfer LP | $19.39 | 1.2 | 0% | $15.25 | -21% |  |
| 19 | URI | United Rentals, Inc. | $1067.77 | 39.08 | 12% | $836.74 | -22% |  |
| 20 | ITW | Illinois Tool Works Inc. | $252.72 | 10.77 | 8% | $197.16 | -22% |  |
| 21 | WEC | WEC Energy Group, Inc. | $112.95 | 4.99 | 7% | $88.06 | -22% |  |
| 22 | SWK | Stanley Black & Decker, In | $78.48 | 2.44 | 15% | $61.03 | -22% |  |
| 23 | ZBRA | Zebra Technologies Corpora | $232.11 | 8.29 | 12% | $178.93 | -23% |  |
| 24 | ADI | Analog Devices, Inc. | $401.39 | 6.7 | 30% | $308.93 | -23% |  |
| 25 | IFF | International Flavors & Fr | $73.01 | 3.23 | 7% | $56.1 | -23% |  |
| 26 | AVB | AvalonBay Communities, Inc | $189.72 | 8.06 | 8% | $145.17 | -24% |  |
| 27 | ROK | Rockwell Automation, Inc. | $446.71 | 9.65 | 23% | $340.82 | -24% |  |
| 28 | BG | Bunge Limited | $126.46 | 3.79 | 15% | $96.45 | -24% |  |
| 29 | LECO | Lincoln Electric Holdings, | $262.13 | 9.7 | 11% | $200.07 | -24% |  |
| 30 | ASML | ASML Holding N.V. - New Yo | $1641.74 | 30.04 | 27% | $1250.55 | -24% |  |
| 31 | NWS | News Corporation | $31.19 | 0.79 | 19% | $23.78 | -24% |  |
| 32 | KO | Coca-Cola Company (The) | $79.48 | 3.18 | 9% | $60.4 | -24% |  |
| 33 | LOW | Lowe's Companies, Inc. | $210.74 | 11.82 | 2% | $160.24 | -24% |  |
| 34 | CP | Canadian Pacific Kansas Ci | $89.93 | 3.23 | 11% | $68.35 | -24% |  |
| 35 | PEP | Pepsico, Inc. | $141.92 | 6.37 | 6% | $107.67 | -24% |  |
| 36 | TMO | Thermo Fisher Scientific I | $472.8 | 18.2 | 10% | $358.57 | -24% |  |
| 37 | ONC | BeOne Medicines Ltd. | $270.1 | 4.43 | 30% | $204.26 | -24% |  |
| 38 | MEDP | Medpace Holdings, Inc. | $454.25 | 15.89 | 12% | $342.82 | -24% |  |
| 39 | CMI | Cummins Inc. | $651.22 | 19.28 | 15% | $490.01 | -25% |  |
| 40 | AJG | Arthur J. Gallagher & Co. | $216.14 | 6.18 | 16% | $162.59 | -25% |  |
| 41 | PM | Philip Morris Internationa | $178.29 | 7.1 | 9% | $133.93 | -25% |  |
| 42 | MCD | McDonald's Corporation | $279.84 | 12.12 | 7% | $210.12 | -25% |  |
| 43 | AEIS | Advanced Energy Industries | $294.81 | 4.8 | 30% | $221.32 | -25% |  |
| 44 | IHG | Intercontinental Hotels Gr | $162.15 | 4.86 | 15% | $121.18 | -25% |  |
| 45 | DOC | Healthpeak Properties, Inc | $19.79 | 0.32 | 30% | $14.75 | -25% |  |
| 46 | UNH | UnitedHealth Group Incorpo | $399.47 | 13.26 | 12% | $296.34 | -26% |  |
| 47 | ZBH | Zimmer Biomet Holdings, In | $87.33 | 3.86 | 6% | $64.82 | -26% |  |
| 48 | AAPL | Apple Inc. | $307.34 | 8.27 | 17% | $227.78 | -26% |  |
| 49 | WMB | Williams Companies, Inc. ( | $71.96 | 2.28 | 13% | $53.19 | -26% |  |
| 50 | LNT | Alliant Energy Corporation | $72.87 | 3.18 | 6% | $53.83 | -26% |  |
| 51 | STE | STERIS plc (Ireland) | $212.35 | 7.92 | 10% | $156.61 | -26% |  |
| 52 | XYL | Xylem Inc. | $109.94 | 4.02 | 10% | $81.06 | -26% |  |
| 53 | TXRH | Texas Roadhouse, Inc. | $170.46 | 6.27 | 10% | $125.4 | -26% |  |
| 54 | OGE | OGE Energy Corp | $47.8 | 2.25 | 5% | $35.09 | -27% |  |
| 55 | J | Jacobs Solutions Inc. | $122.55 | 3.39 | 16% | $89.53 | -27% |  |
| 56 | MKSI | MKS Inc. | $301.65 | 4.77 | 30% | $219.94 | -27% |  |
| 57 | GWW | W.W. Grainger, Inc. | $1300.01 | 37.18 | 15% | $946.99 | -27% |  |
| 58 | TLK | PT Telekomunikasi Indonesi | $15.54 | 0.91 | 0% | $11.3 | -27% |  |
| 59 | IBM | International Business Mac | $284.84 | 11.31 | 8% | $206.66 | -27% |  |
| 60 | RPM | RPM International Inc. | $104.96 | 5.19 | 3% | $76.25 | -27% |  |
| 61 | MTZ | MasTec, Inc. | $363.89 | 5.71 | 30% | $263.28 | -28% |  |
| 62 | CPRT | Copart, Inc. | $30.96 | 1.61 | 2% | $22.4 | -28% |  |
| 63 | TFII | TFI International Inc. | $159.5 | 3.59 | 21% | $115.49 | -28% |  |
| 64 | SAIA | Saia, Inc. | $466.51 | 9.51 | 23% | $337.38 | -28% |  |
| 65 | WSM | Williams-Sonoma, Inc. | $204.98 | 8.92 | 6% | $148.03 | -28% |  |
| 66 | AVGO | Broadcom Inc. | $385.73 | 6.02 | 30% | $277.57 | -28% |  |
| 67 | BAM | Brookfield Asset Managemen | $46.18 | 1.56 | 11% | $33.22 | -28% |  |
| 68 | FE | FirstEnergy Corp. | $46.42 | 1.84 | 8% | $33.26 | -28% |  |
| 69 | ORLY | O'Reilly Automotive, Inc. | $90.33 | 3.07 | 11% | $64.47 | -29% |  |
| 70 | VEEV | Veeva Systems Inc. | $172.61 | 5.64 | 12% | $122.72 | -29% |  |
| 71 | CNP | CenterPoint Energy, Inc (H | $42.69 | 1.63 | 8% | $30.35 | -29% |  |
| 72 | HUBB | Hubbell Inc | $476.82 | 16.93 | 10% | $339.06 | -29% |  |
| 73 | MTD | Mettler-Toledo Internation | $1154.33 | 42.59 | 9% | $820.52 | -29% |  |
| 74 | KIM | Kimco Realty Corporation ( | $24.23 | 0.87 | 10% | $17.21 | -29% |  |
| 75 | WM | Waste Management, Inc. | $220.4 | 6.92 | 13% | $156.31 | -29% |  |
| 76 | SO | Southern Company (The) | $92.6 | 3.91 | 6% | $65.56 | -29% |  |
| 77 | UPS | United Parcel Service, Inc | $108.54 | 6.18 | 0% | $76.75 | -29% |  |
| 78 | ELV | Elevance Health, Inc. | $415.53 | 23.6 | 0% | $293.07 | -30% |  |
| 79 | DOV | Dover Corporation | $214.76 | 8.01 | 9% | $151.44 | -30% |  |
| 80 | FLEX | Flex Ltd. | $151.92 | 2.32 | 30% | $106.97 | -30% |  |
| 81 | WTRG | Essential Utilities, Inc. | $37.36 | 1.96 | 2% | $26.31 | -30% |  |
| 82 | LII | Lennox International, Inc. | $508.43 | 22.52 | 5% | $357.44 | -30% |  |
| 83 | LMT | Lockheed Martin Corporatio | $523.76 | 20.64 | 7% | $367.12 | -30% |  |
| 84 | A | Agilent Technologies, Inc. | $135.44 | 4.98 | 9% | $94.98 | -30% |  |
| 85 | CPT | Camden Property Trust | $112.6 | 3.58 | 12% | $78.7 | -30% |  |
| 86 | AGX | Argan, Inc. | $694.72 | 11.39 | 28% | $485.81 | -30% |  |
| 87 | ATI | ATI Inc. | $177.47 | 3.03 | 27% | $123.83 | -30% |  |
| 88 | TER | Teradyne, Inc. | $357.93 | 5.4 | 30% | $248.99 | -30% |  |
| 89 | MSCI | MSCI Inc. | $615.46 | 17.54 | 14% | $427.74 | -30% |  |
| 90 | BIP | Brookfield Infrastructure  | $38.8 | 0.66 | 27% | $26.82 | -31% |  |
| 91 | BJ | BJ's Wholesale Club Holdin | $89.21 | 4.35 | 3% | $61.69 | -31% |  |
| 92 | TT | Trane Technologies plc | $456.84 | 13.11 | 14% | $314.71 | -31% |  |
| 93 | PSX | Phillips 66 | $183.08 | 10.12 | 0% | $125.67 | -31% |  |
| 94 | WST | West Pharmaceutical Servic | $314.5 | 7.49 | 18% | $213.7 | -32% |  |
| 95 | MDLZ | Mondelez International, In | $62.04 | 2.02 | 11% | $42.0 | -32% |  |
| 96 | ALGN | Align Technology, Inc. | $167.74 | 5.95 | 9% | $113.17 | -32% |  |
| 97 | IBKR | Interactive Brokers Group, | $84.4 | 2.33 | 14% | $56.92 | -33% |  |
| 98 | SYY | Sysco Corporation | $76.29 | 3.6 | 3% | $51.4 | -33% |  |
| 99 | AA | Alcoa Corporation | $71.89 | 3.9 | 0% | $48.43 | -33% |  |
| 100 | DTM | DT Midstream, Inc. | $142.5 | 4.5 | 11% | $95.83 | -33% |  |
| 101 | OHI | Omega Healthcare Investors | $44.47 | 2.07 | 3% | $29.92 | -33% |  |
| 102 | CAH | Cardinal Health, Inc. | $205.71 | 6.54 | 11% | $138.28 | -33% |  |
| 103 | RPRX | Royalty Pharma plc | $55.87 | 1.9 | 10% | $37.48 | -33% |  |
| 104 | DEO | Diageo plc | $80.43 | 4.33 | 0% | $53.77 | -33% |  |
| 105 | ABT | Abbott Laboratories | $91.07 | 3.57 | 6% | $60.66 | -33% |  |
| 106 | KMB | Kimberly-Clark Corporation | $99.04 | 5.17 | 0% | $65.86 | -34% |  |
| 107 | WAB | Westinghouse Air Brake Tec | $260.4 | 7.08 | 14% | $172.96 | -34% |  |
| 108 | WSE | Wise Group plc | $11.19 | 0.5 | 4% | $7.42 | -34% |  |
| 109 | PG | Procter & Gamble Company ( | $146.54 | 6.84 | 3% | $97.14 | -34% |  |
| 110 | MCO | Moody's Corporation | $451.35 | 13.95 | 11% | $296.68 | -34% |  |
| 111 | JNJ | Johnson & Johnson | $232.77 | 8.64 | 7% | $152.4 | -34% |  |
| 112 | GGG | Graco Inc. | $74.34 | 3.06 | 5% | $48.68 | -34% |  |
| 113 | DTE | DTE Energy Company | $145.77 | 6.08 | 5% | $95.4 | -35% |  |
| 114 | TDY | Teledyne Technologies Inco | $602.27 | 19.75 | 10% | $392.85 | -35% |  |
| 115 | GMAB | Genmab A/S | $25.15 | 1.32 | 0% | $16.39 | -35% |  |
| 116 | ANET | Arista Networks, Inc. | $154.27 | 2.92 | 23% | $100.44 | -35% |  |
| 117 | TJX | TJX Companies, Inc. (The) | $160.71 | 5.14 | 10% | $104.68 | -35% |  |
| 118 | PINS | Pinterest, Inc. | $21.42 | 0.48 | 18% | $13.94 | -35% |  |
| 119 | CNI | Canadian National Railway  | $120.38 | 5.47 | 3% | $78.1 | -35% |  |
| 120 | ARES | Ares Management Corporatio | $125.65 | 2.17 | 25% | $81.58 | -35% |  |
| 121 | GM | General Motors Company | $82.11 | 2.74 | 9% | $53.01 | -35% |  |
| 122 | CGNX | Cognex Corporation | $60.82 | 0.85 | 30% | $39.19 | -36% |  |
| 123 | APD | Air Products and Chemicals | $282.35 | 9.49 | 9% | $179.55 | -36% |  |
| 124 | ENTG | Entegris, Inc. | $125.41 | 1.73 | 30% | $79.77 | -36% |  |
| 125 | AMGN | Amgen Inc. | $349.58 | 14.37 | 4% | $221.32 | -37% |  |
| 126 | BSY | Bentley Systems, Incorpora | $32.93 | 0.87 | 14% | $20.82 | -37% |  |
| 127 | CR | Crane Company | $188.86 | 5.46 | 12% | $118.75 | -37% |  |
| 128 | EMR | Emerson Electric Company | $138.12 | 4.32 | 10% | $86.4 | -37% |  |
| 129 | SUNB | Sunbelt Rentals Holdings,  | $79.36 | 3.26 | 4% | $49.72 | -37% |  |
| 130 | PFE | Pfizer, Inc. | $26.04 | 1.31 | 0% | $16.27 | -38% |  |
| 131 | COP | ConocoPhillips | $117.14 | 5.9 | 0% | $73.27 | -38% |  |
| 132 | WDAY | Workday, Inc. | $144.28 | 3.2 | 18% | $90.11 | -38% |  |
| 133 | VRSK | Verisk Analytics, Inc. | $181.73 | 6.56 | 7% | $113.41 | -38% |  |
| 134 | VRSN | VeriSign, Inc. | $294.92 | 9.05 | 10% | $183.15 | -38% |  |
| 135 | BTSG | BrightSpring Health Servic | $57.4 | 0.77 | 30% | $35.5 | -38% |  |
| 136 | HD | Home Depot, Inc. (The) | $310.78 | 14.08 | 2% | $191.73 | -38% |  |
| 137 | ILMN | Illumina, Inc. | $162.32 | 5.5 | 8% | $100.17 | -38% |  |
| 138 | SRE | DBA Sempra | $91.42 | 2.94 | 9% | $56.3 | -38% |  |
| 139 | NDSN | Nordson Corporation | $282.73 | 9.36 | 8% | $174.22 | -38% |  |
| 140 | LOGI | Logitech International S.A | $112.93 | 4.8 | 3% | $69.44 | -38% |  |
| 141 | MMM | 3M Company | $153.76 | 5.2 | 8% | $94.44 | -39% |  |
| 142 | XPO | XPO, Inc. | $218.94 | 2.91 | 30% | $134.18 | -39% |  |
| 143 | CX | Cemex, S.A.B. de C.V. Spon | $12.47 | 0.35 | 12% | $7.64 | -39% |  |
| 144 | HEI | Heico Corporation | $331.43 | 5.6 | 24% | $202.56 | -39% |  |
| 145 | UTHR | United Therapeutics Corpor | $549.87 | 27.05 | 0% | $335.92 | -39% |  |
| 146 | ECL | Ecolab Inc. | $257.97 | 7.38 | 11% | $157.23 | -39% |  |
| 147 | TKO | TKO Group Holdings, Inc. | $203.49 | 2.69 | 30% | $124.03 | -39% |  |
| 148 | GE | GE Aerospace | $328.0 | 8.04 | 15% | $199.86 | -39% |  |
| 149 | SYK | Stryker Corporation | $305.66 | 8.65 | 12% | $186.29 | -39% |  |
| 150 | VRT | Vertiv Holdings, LLC | $300.51 | 3.97 | 30% | $183.05 | -39% |  |
| 151 | SHW | Sherwin-Williams Company ( | $305.3 | 10.41 | 8% | $185.59 | -39% |  |
| 152 | SONY | Sony Group Corporation | $21.89 | 1.07 | 0% | $13.29 | -39% |  |
| 153 | ALNY | Alnylam Pharmaceuticals, I | $303.05 | 3.97 | 30% | $183.05 | -40% |  |
| 154 | COO | The Cooper Companies, Inc. | $67.34 | 2.01 | 10% | $40.5 | -40% |  |
| 155 | PKG | Packaging Corporation of A | $222.82 | 8.22 | 6% | $133.67 | -40% |  |
| 156 | OXY | Occidental Petroleum Corpo | $56.93 | 0.74 | 30% | $34.12 | -40% |  |
| 157 | FTS | Fortis Inc. | $55.9 | 2.44 | 2% | $33.41 | -40% |  |
| 158 | NVT | nVent Electric plc | $162.86 | 2.95 | 22% | $97.44 | -40% |  |
| 159 | AMCR | Amcor plc | $38.13 | 1.25 | 8% | $22.64 | -41% |  |
| 160 | MICC | The Magnum Ice Cream Compa | $17.07 | 0.56 | 8% | $10.14 | -41% |  |
| 161 | RSG | Republic Services, Inc. | $210.04 | 6.97 | 8% | $124.26 | -41% |  |
| 162 | HBANP | Huntington Bancshares Inco | $16.32 | 0.778 | 0% | $9.66 | -41% |  |
| 163 | IEX | IDEX Corporation | $215.35 | 6.76 | 9% | $127.1 | -41% |  |
| 164 | LIN | Linde plc | $507.9 | 15.08 | 10% | $299.0 | -41% |  |
| 165 | PH | Parker-Hannifin Corporatio | $882.34 | 27.09 | 9% | $517.14 | -41% |  |
| 166 | STRL | Sterling Infrastructure, I | $882.43 | 11.21 | 30% | $516.88 | -41% |  |
| 167 | RTX | RTX Corporation | $180.99 | 5.32 | 10% | $105.82 | -42% |  |
| 168 | FRT | Federal Realty Investment  | $122.56 | 5.77 | 0% | $71.65 | -42% |  |
| 169 | Q | Qnity Electronics, Inc. | $142.05 | 3.1 | 16% | $82.69 | -42% |  |
| 170 | LAMR | Lamar Advertising Company | $151.42 | 5.42 | 6% | $88.05 | -42% |  |
| 171 | NVS | Novartis AG | $149.16 | 6.98 | 0% | $86.68 | -42% |  |
| 172 | MSI | Motorola Solutions, Inc. | $410.34 | 12.39 | 9% | $238.15 | -42% |  |
| 173 | MNST | Monster Beverage Corporati | $89.55 | 2.07 | 15% | $51.7 | -42% |  |
| 174 | BX | Blackstone Inc. | $115.35 | 3.9 | 7% | $66.61 | -42% |  |
| 175 | SLMBP | SLM Corporation - Floating | $74.6 | 2.145 | 10% | $42.9 | -42% |  |
| 176 | LHX | L3Harris Technologies, Inc | $307.83 | 9.2 | 9% | $176.51 | -43% |  |
| 177 | AME | AMETEK, Inc. | $226.55 | 6.62 | 10% | $129.71 | -43% |  |
| 178 | STX | Seagate Technology Holding | $847.47 | 10.51 | 30% | $484.6 | -43% |  |
| 179 | FAST | Fastenal Company | $46.79 | 1.13 | 14% | $26.78 | -43% |  |
| 180 | ADM | Archer-Daniels-Midland Com | $80.92 | 2.24 | 11% | $46.12 | -43% |  |
| 181 | ALC | Alcon Inc. | $66.81 | 1.67 | 13% | $38.01 | -43% |  |
| 182 | SBAC | SBA Communications Corpora | $208.02 | 9.51 | 0% | $118.1 | -43% |  |
| 183 | CVNA | Carvana Co. | $66.51 | 1.73 | 12% | $37.69 | -43% |  |
| 184 | O | Realty Income Corporation | $60.84 | 1.22 | 18% | $34.51 | -43% |  |
| 185 | HRL | Hormel Foods Corporation | $23.62 | 0.85 | 5% | $13.4 | -43% |  |
| 186 | EMA | Emera Incorporated | $51.76 | 2.36 | 0% | $29.31 | -43% |  |
| 187 | PEN | Penumbra, Inc. | $320.53 | 4.33 | 28% | $180.89 | -44% |  |
| 188 | BWXT | BWX Technologies, Inc. | $185.95 | 3.76 | 18% | $104.67 | -44% |  |
| 189 | GNRC | Generac Holdlings Inc. | $261.54 | 3.19 | 30% | $147.09 | -44% |  |
| 190 | RACE | Ferrari N.V. | $346.99 | 10.44 | 8% | $194.5 | -44% |  |
| 191 | E | ENI S.p.A. | $53.8 | 2.31 | 1% | $30.15 | -44% |  |
| 192 | TDG | Transdigm Group Incorporat | $1238.74 | 32.08 | 12% | $686.55 | -45% |  |
| 193 | NVMI | Nova Ltd. | $475.76 | 7.98 | 22% | $263.8 | -45% |  |
| 194 | IDXX | IDEXX Laboratories, Inc. | $562.16 | 13.6 | 13% | $310.21 | -45% |  |
| 195 | GRAB | Grab Holdings Limited | $3.34 | 0.04 | 30% | $1.84 | -45% |  |
| 196 | AIT | Applied Industrial Technol | $315.29 | 10.59 | 6% | $173.93 | -45% |  |
| 197 | SBUX | Starbucks Corporation | $95.29 | 1.31 | 26% | $52.55 | -45% |  |
| 198 | MAR | Marriott International | $392.51 | 9.54 | 13% | $215.68 | -45% |  |
| 199 | BLD | TopBuild Corp. | $401.82 | 17.76 | 0% | $220.55 | -45% |  |
| 200 | CTAS | Cintas Corporation | $179.85 | 4.75 | 11% | $98.59 | -45% |  |
| 201 | WMT | Walmart Inc. | $118.88 | 2.84 | 13% | $65.07 | -45% |  |
| 202 | REG | Regency Centers Corporatio | $77.72 | 2.91 | 3% | $42.53 | -45% |  |
| 203 | CSCO | Cisco Systems, Inc. | $121.64 | 3.0 | 12% | $66.42 | -45% |  |
| 204 | CHT | Chunghwa Telecom Co., Ltd. | $44.56 | 1.59 | 4% | $24.3 | -46% |  |
| 205 | GLW | Corning Incorporated | $177.58 | 2.08 | 30% | $95.91 | -46% |  |
| 206 | BA | Boeing Company (The) | $215.45 | 2.52 | 30% | $116.19 | -46% |  |
| 207 | TPL | Texas Pacific Land Corpora | $389.79 | 7.29 | 18% | $209.76 | -46% |  |
| 208 | CVS | CVS Health Corporation | $95.93 | 2.28 | 13% | $51.39 | -46% |  |
| 209 | BWA | BorgWarner Inc. | $72.63 | 1.72 | 13% | $38.94 | -46% |  |
| 210 | QCOM | QUALCOMM Incorporated | $215.94 | 9.31 | 0% | $115.62 | -46% |  |
| 211 | ON | ON Semiconductor Corporati | $117.26 | 1.36 | 30% | $62.71 | -46% |  |
| 212 | DRS | Leonardo DRS, Inc. | $46.15 | 1.07 | 13% | $24.54 | -47% |  |
| 213 | ETN | Eaton Corporation, PLC | $395.94 | 10.22 | 10% | $209.28 | -47% |  |
| 214 | TRP | TC Energy Corporation | $68.68 | 2.44 | 4% | $36.3 | -47% |  |
| 215 | CLH | Clean Harbors, Inc. | $283.03 | 7.39 | 10% | $149.49 | -47% |  |
| 216 | BN | Brookfield Corporation | $44.6 | 0.51 | 30% | $23.52 | -47% |  |
| 217 | NBIS | Nebius Group N.V. | $227.81 | 2.6 | 30% | $119.88 | -47% |  |
| 218 | HON | Honeywell International In | $213.97 | 6.27 | 8% | $112.36 | -48% |  |
| 219 | SPXC | SPX Technologies, Inc. | $227.8 | 5.24 | 13% | $119.57 | -48% |  |
| 220 | ISRG | Intuitive Surgical, Inc. | $422.06 | 8.23 | 17% | $220.65 | -48% |  |
| 221 | CTVA | Corteva, Inc. | $77.03 | 1.85 | 12% | $40.31 | -48% |  |
| 222 | CHD | Church & Dwight Company, I | $96.74 | 3.04 | 6% | $50.64 | -48% |  |
| 223 | WMS | Advanced Drainage Systems, | $130.15 | 5.45 | 0% | $67.68 | -48% |  |
| 224 | PBA | Pembina Pipeline Corp. | $48.82 | 1.91 | 1% | $25.34 | -48% |  |
| 225 | ASND | Ascendis Pharma A/S | $210.45 | 8.8 | 0% | $109.28 | -48% |  |
| 226 | DHR | Danaher Corporation | $184.3 | 5.16 | 8% | $94.98 | -48% |  |
| 227 | SLB | SLB Limited | $54.87 | 2.27 | 0% | $28.19 | -49% |  |
| 228 | MRVL | Marvell Technology, Inc. | $263.47 | 2.9 | 30% | $133.72 | -49% |  |
| 229 | ESLT | Elbit Systems Ltd. | $823.36 | 12.35 | 22% | $418.6 | -49% |  |
| 230 | VICR | Vicor Corporation | $271.04 | 2.98 | 30% | $137.4 | -49% |  |
| 231 | TTMI | TTM Technologies, Inc. | $167.62 | 1.84 | 30% | $84.84 | -49% |  |
| 232 | ROKU | Roku, Inc. | $122.26 | 1.34 | 30% | $61.79 | -50% |  |
| 233 | TYL | Tyler Technologies, Inc. | $312.07 | 7.24 | 12% | $156.62 | -50% |  |
| 234 | RDY | Dr. Reddy's Laboratories L | $13.24 | 0.53 | 0% | $6.58 | -50% |  |
| 235 | PSA | Public Storage | $309.68 | 9.69 | 5% | $153.0 | -51% |  |
| 236 | FTV | Fortive Corporation | $61.28 | 1.7 | 8% | $30.27 | -51% |  |
| 237 | AAON | AAON, Inc. | $132.62 | 1.42 | 30% | $65.47 | -51% |  |
| 238 | NXT | Nextpower Inc. | $131.57 | 3.84 | 6% | $64.85 | -51% |  |
| 239 | WSO | Watsco, Inc. | $371.38 | 12.18 | 4% | $183.23 | -51% |  |
| 240 | XOM | Exxon Mobil Corporation | $149.92 | 5.94 | 0% | $73.77 | -51% |  |
| 241 | ROL | Rollins, Inc. | $47.1 | 1.09 | 11% | $23.06 | -51% |  |
| 242 | HLT | Hilton Worldwide Holdings  | $343.1 | 6.55 | 16% | $167.12 | -51% |  |
| 243 | FER | Ferrovial N.V. | $66.81 | 1.35 | 14% | $32.46 | -51% |  |
| 244 | CCI | Crown Castle Inc. | $94.49 | 2.37 | 9% | $45.95 | -51% |  |
| 245 | NTNX | Nutanix, Inc. | $53.64 | 0.95 | 17% | $26.09 | -51% |  |
| 246 | PWR | Quanta Services, Inc. | $695.11 | 7.3 | 30% | $336.59 | -52% |  |
| 247 | CCJ | Cameco Corporation | $103.44 | 1.08 | 30% | $49.8 | -52% |  |
| 248 | FFIV | F5, Inc. | $393.35 | 12.19 | 4% | $186.94 | -52% |  |
| 249 | NSC | Norfolk Southern Corporati | $313.45 | 11.88 | 0% | $147.53 | -53% |  |
| 250 | EW | Edwards Lifesciences Corpo | $85.96 | 1.85 | 12% | $40.45 | -53% |  |
| 251 | BDX | Becton, Dickinson and Comp | $151.16 | 5.73 | 0% | $71.16 | -53% |  |
| 252 | WAT | Waters Corporation | $365.36 | 7.86 | 12% | $172.1 | -53% |  |
| 253 | ENB | Enbridge Inc | $56.31 | 2.12 | 0% | $26.33 | -53% |  |
| 254 | HBANM | Huntington Bancshares Inco | $20.68 | 0.778 | 0% | $9.66 | -53% |  |
| 255 | TSN | Tyson Foods, Inc. | $58.73 | 1.27 | 12% | $27.44 | -53% |  |
| 256 | COST | Costco Wholesale Corporati | $971.87 | 19.92 | 13% | $452.96 | -53% |  |
| 257 | CW | Curtiss-Wright Corporation | $733.14 | 13.64 | 15% | $340.25 | -54% |  |
| 258 | WELL | Welltower Inc. | $206.93 | 2.07 | 30% | $95.45 | -54% |  |
| 259 | CMG | Chipotle Mexican Grill, In | $29.34 | 1.09 | 0% | $13.54 | -54% |  |
| 260 | AMH | American Homes 4 Rent | $33.27 | 1.23 | 0% | $15.27 | -54% |  |
| 261 | WCN | Waste Connections, Inc. | $155.22 | 4.1 | 7% | $70.95 | -54% |  |
| 262 | EQR | Equity Residential | $68.19 | 2.5 | 0% | $31.05 | -54% |  |
| 263 | ULS | UL Solutions Inc. | $96.81 | 1.72 | 16% | $44.06 | -54% |  |
| 264 | ELS | Equity Lifestyle Propertie | $62.43 | 2.0 | 3% | $28.35 | -55% |  |
| 265 | RRX | Regal Rexnord Corporation | $204.4 | 4.29 | 12% | $92.22 | -55% |  |
| 266 | GFL | GFL Environmental Inc. Sub | $35.51 | 0.37 | 28% | $16.02 | -55% |  |
| 267 | RMBS | Rambus, Inc. | $145.31 | 2.11 | 20% | $64.9 | -55% |  |
| 268 | KR | Kroger Company (The) | $63.57 | 1.54 | 8% | $28.14 | -56% |  |
| 269 | NKE | Nike, Inc. | $42.98 | 1.52 | 0% | $18.88 | -56% |  |
| 270 | TU | Telus Corporation | $12.31 | 0.43 | 0% | $5.37 | -56% |  |
| 271 | FTNT | Fortinet, Inc. | $144.68 | 2.58 | 14% | $62.72 | -57% |  |
| 272 | IMO | Imperial Oil Limited | $121.72 | 4.25 | 0% | $52.78 | -57% |  |
| 273 | MPWR | Monolithic Power Systems,  | $1481.05 | 13.92 | 30% | $641.83 | -57% |  |
| 274 | SOLS | Solstice Advanced Material | $81.02 | 1.18 | 19% | $35.04 | -57% |  |
| 275 | CL | Colgate-Palmolive Company | $88.58 | 2.58 | 3% | $37.67 | -58% |  |
| 276 | TSEM | Tower Semiconductor Ltd. | $235.48 | 2.16 | 30% | $99.59 | -58% |  |
| 277 | RBA | RB Global, Inc. | $104.49 | 2.15 | 11% | $44.17 | -58% |  |
| 278 | ODFL | Old Dominion Freight Line, | $242.57 | 4.78 | 12% | $102.34 | -58% |  |
| 279 | MDLN | Medline Inc. | $33.61 | 1.14 | 0% | $14.16 | -58% |  |
| 280 | NOW | ServiceNow, Inc. | $112.45 | 1.68 | 18% | $46.65 | -58% |  |
| 281 | BROS | Dutch Bros Inc. | $55.52 | 0.64 | 24% | $23.02 | -58% |  |
| 282 | EQIX | Equinix, Inc. | $1080.95 | 14.48 | 20% | $447.45 | -59% |  |
| 283 | GFS | GlobalFoundries Inc. | $75.53 | 1.48 | 11% | $31.25 | -59% |  |
| 284 | ESS | Essex Property Trust, Inc. | $285.43 | 8.88 | 1% | $116.82 | -59% |  |
| 285 | CARR | Carrier Global Corporation | $67.16 | 1.5 | 8% | $27.26 | -59% |  |
| 286 | CRDO | Credo Technology Group Hol | $206.89 | 1.82 | 30% | $83.92 | -59% |  |
| 287 | ESI | Element Solutions Inc. | $39.84 | 0.62 | 16% | $16.19 | -59% |  |
| 288 | SWKS | Skyworks Solutions, Inc. | $73.57 | 2.4 | 0% | $29.8 | -60% |  |
| 289 | GWRE | Guidewire Software, Inc. | $136.06 | 1.86 | 19% | $54.61 | -60% |  |
| 290 | RBC | RBC Bearings Incorporated | $590.09 | 9.09 | 16% | $236.18 | -60% |  |
| 291 | KLAC | KLA Corporation | $1929.2 | 35.3 | 12% | $765.69 | -60% |  |
| 292 | SHOP | Shopify Inc. | $109.54 | 1.02 | 28% | $43.02 | -61% |  |
| 293 | INVH | Invitation Homes Inc. | $30.04 | 0.95 | 0% | $11.8 | -61% |  |
| 294 | ONTO | Onto Innovation Inc. | $253.24 | 2.15 | 30% | $99.13 | -61% |  |
| 295 | EA | Electronic Arts Inc. | $203.0 | 3.51 | 13% | $79.07 | -61% |  |
| 296 | CVX | Chevron Corporation | $187.31 | 5.73 | 0% | $71.16 | -62% |  |
| 297 | EXR | Extra Space Storage Inc | $145.31 | 4.45 | 0% | $55.26 | -62% |  |
| 298 | MOD | Modine Manufacturing Compa | $276.51 | 2.27 | 30% | $104.67 | -62% |  |
| 299 | DE | Deere & Company | $583.44 | 17.68 | 0% | $219.56 | -62% |  |
| 300 | POWL | Powell Industries, Inc. | $284.87 | 5.13 | 11% | $106.82 | -62% |  |
| 301 | CRBG | Corebridge Financial Inc. | $26.86 | 0.4 | 15% | $9.99 | -63% |  |
| 302 | CNH | CNH Industrial N.V. | $10.75 | 0.32 | 0% | $3.97 | -63% |  |
| 303 | HUBS | HubSpot, Inc. | $212.64 | 1.89 | 27% | $77.94 | -63% |  |
| 304 | MELI | MercadoLibre, Inc. | $1607.8 | 37.94 | 4% | $586.58 | -64% |  |
| 305 | HOOD | Robinhood Markets, Inc. | $82.47 | 2.06 | 3% | $29.23 | -65% |  |
| 306 | SW | Smurfit WestRock plc | $41.28 | 0.72 | 10% | $14.57 | -65% |  |
| 307 | FWONA | Liberty Media Corporation  | $80.94 | 2.29 | 0% | $28.44 | -65% |  |
| 308 | IR | Ingersoll Rand Inc. | $72.25 | 1.48 | 6% | $25.18 | -65% |  |
| 309 | HUM | Humana Inc. | $350.08 | 9.38 | 0% | $116.48 | -67% |  |
| 310 | NOK | Nokia Corporation Sponsore | $14.38 | 0.16 | 19% | $4.69 | -67% |  |
| 311 | CDNS | Cadence Design Systems, In | $376.19 | 4.29 | 18% | $121.88 | -68% |  |
| 312 | FWONK | Liberty Media Corporation  | $87.68 | 2.29 | 0% | $28.44 | -68% |  |
| 313 | P | Everpure, Inc. | $72.17 | 0.66 | 23% | $23.15 | -68% |  |
| 314 | DD | DuPont de Nemours, Inc. | $46.85 | 0.38 | 26% | $14.92 | -68% |  |
| 315 | MTSI | MACOM Technology Solutions | $345.4 | 2.35 | 30% | $108.36 | -69% |  |
| 316 | RVTY | Revvity, Inc. | $98.37 | 2.08 | 4% | $30.92 | -69% |  |
| 317 | DT | Dynatrace, Inc. | $42.19 | 0.54 | 14% | $13.21 | -69% |  |
| 318 | PFGC | Performance Food Group Com | $97.12 | 2.1 | 3% | $30.34 | -69% |  |
| 319 | JHX | James Hardie Industries pl | $22.66 | 0.19 | 24% | $7.05 | -69% |  |
| 320 | LITE | Lumentum Holdings Inc. | $863.66 | 5.7 | 30% | $262.82 | -70% |  |
| 321 | APTV | Aptiv PLC | $68.6 | 1.68 | 0% | $20.86 | -70% |  |
| 322 | PLTR | Palantir Technologies Inc. | $135.53 | 0.89 | 30% | $41.04 | -70% |  |
| 323 | MAA | Mid-America Apartment Comm | $137.54 | 3.3 | 0% | $40.98 | -70% |  |
| 324 | AMD | Advanced Micro Devices, In | $466.38 | 2.98 | 30% | $137.4 | -70% |  |
| 325 | APO | Apollo Global Management,  | $128.03 | 1.59 | 13% | $35.95 | -72% |  |
| 326 | CIEN | Ciena Corporation | $488.21 | 2.98 | 30% | $137.4 | -72% |  |
| 327 | MAIR | Madison Air Solutions Corp | $40.14 | 0.35 | 21% | $11.16 | -72% |  |
| 328 | DASH | DoorDash, Inc. | $156.8 | 2.12 | 10% | $42.83 | -73% |  |
| 329 | COHR | Coherent Corp. | $376.99 | 2.11 | 30% | $97.29 | -74% |  |
| 330 | OWL | Blue Owl Capital Inc. | $9.8 | 0.12 | 11% | $2.53 | -74% |  |
| 331 | OKTA | Okta, Inc. | $118.72 | 1.38 | 11% | $29.35 | -75% |  |
| 332 | AKAM | Akamai Technologies, Inc. | $149.32 | 2.96 | 0% | $36.76 | -75% |  |
| 333 | MOH | Molina Healthcare Inc | $190.86 | 3.72 | 0% | $46.2 | -76% |  |
| 334 | ICLR | ICON plc | $149.45 | 2.9 | 0% | $36.01 | -76% |  |
| 335 | AXON | Axon Enterprise, Inc. | $486.12 | 2.48 | 30% | $114.35 | -76% |  |
| 336 | SNPS | Synopsys, Inc. | $464.85 | 4.37 | 15% | $107.08 | -77% |  |
| 337 | COF | Capital One Financial Corp | $180.67 | 3.25 | 0% | $41.28 | -77% |  |
| 338 | SKM | SK Telecom Co., Ltd. | $37.44 | 0.66 | 0% | $8.2 | -78% |  |
| 339 | ALAB | Astera Labs, Inc. | $317.06 | 1.49 | 30% | $68.7 | -78% |  |
| 340 | ABBV | AbbVie Inc. | $227.23 | 2.05 | 14% | $48.93 | -78% |  |
| 341 | ENLT | Enlight Renewable Energy L | $90.98 | 0.41 | 30% | $18.9 | -79% |  |
| 342 | VTR | Ventas, Inc. | $82.02 | 0.55 | 19% | $16.01 | -80% |  |
| 343 | MGM | MGM Resorts International | $47.51 | 0.73 | 0% | $9.07 | -81% |  |
| 344 | TPG | TPG Inc. | $41.19 | 0.23 | 22% | $7.59 | -82% |  |
| 345 | IRM | Iron Mountain Incorporated | $124.66 | 0.92 | 15% | $22.75 | -82% |  |
| 346 | IREN | IREN LIMITED | $54.35 | 0.77 | 0% | $9.56 | -82% |  |
| 347 | DOCN | DigitalOcean Holdings, Inc | $169.87 | 2.28 | 0% | $28.31 | -83% |  |
| 348 | DKNG | DraftKings Inc. | $24.93 | 0.09 | 30% | $4.15 | -83% |  |
| 349 | NRG | NRG Energy, Inc. | $129.2 | 0.9 | 12% | $19.86 | -85% |  |
| 350 | KTOS | Kratos Defense & Security  | $58.52 | 0.17 | 30% | $7.84 | -87% |  |
| 351 | KNX | Knight-Swift Transportatio | $78.57 | 0.21 | 30% | $9.68 | -88% |  |
| 352 | ARM | Arm Holdings plc | $342.93 | 0.86 | 30% | $39.65 | -88% |  |
| 353 | MCHP | Microchip Technology Incor | $88.34 | 0.22 | 30% | $10.14 | -88% |  |
| 354 | IOT | Samsara Inc. | $34.8 | 0.1 | 26% | $3.99 | -88% |  |
| 355 | STM | STMicroelectronics N.V. | $70.72 | 0.16 | 30% | $7.38 | -90% |  |
| 356 | PSKY | Paramount Skydance Corpora | $10.22 | 0.03 | 23% | $1.05 | -90% |  |
| 357 | CSGP | CoStar Group, Inc. | $33.89 | 0.07 | 30% | $3.23 | -90% |  |
| 358 | TSLA | Tesla, Inc. | $391.0 | 1.09 | 22% | $36.88 | -91% |  |
| 359 | PANW | Palo Alto Networks, Inc. | $272.05 | 1.14 | 11% | $23.75 | -91% |  |
| 360 | IONQ | IonQ, Inc. | $56.78 | 0.39 | 0% | $4.84 | -92% |  |
| 361 | TWLO | Twilio Inc. | $225.99 | 0.66 | 17% | $17.67 | -92% |  |
| 362 | GPC | Genuine Parts Company | $98.15 | 0.44 | 4% | $6.76 | -93% |  |
| 363 | FANG | Diamondback Energy, Inc. | $192.62 | 0.98 | 0% | $12.17 | -94% |  |
| 364 | DDOG | Datadog, Inc. | $234.11 | 0.4 | 18% | $11.41 | -95% |  |
| 365 | LSCC | Lattice Semiconductor Corp | $135.57 | 0.14 | 30% | $6.46 | -95% |  |
| 366 | CBRS | Cerebras Systems Inc. | $201.01 | 0.42 | 8% | $7.66 | -96% |  |
| 367 | JAZZ | Jazz Pharmaceuticals plc | $238.57 | 0.12 | 30% | $5.53 | -98% |  |
| 368 | ARXS | Arxis, Inc. | $39.41 | 0.02 | 24% | $0.72 | -98% |  |
| 369 | FPS | Forgent Power Solutions, I | $59.13 | 0.02 | 30% | $0.92 | -98% |  |
| 370 | INTC | Intel Corporation | $99.17 | -0.6 | — | — | no earnings | no_earnings |
| 371 | CCZ | Comcast Holdings ZONES | $64.11 | None | — | — | no earnings | no_earnings |
| 372 | CRWD | CrowdStrike Holdings, Inc. | $671.02 | -0.13 | — | — | no earnings | no_earnings |
| 373 | TBB | AT&T Inc. 5.350% Global No | $20.69 | None | — | — | no earnings | no_earnings |
| 374 | NET | Cloudflare, Inc. | $250.11 | -0.25 | — | — | no earnings | no_earnings |
| 375 | SNOW | Snowflake Inc. | $238.26 | -3.53 | — | — | no earnings | no_earnings |
| 376 | BE | Bloom Energy Corporation | $263.61 | -0.05 | — | — | no earnings | no_earnings |
| 377 | WBD | Warner Bros. Discovery, In | $26.24 | -0.7 | — | — | no earnings | no_earnings |
| 378 | BRKRP | Bruker Corporation - 6.375 | $421.23 | None | — | — | no earnings | no_earnings |
| 379 | RKLB | Rocket Lab Corporation | $110.08 | -0.32 | — | — | no earnings | no_earnings |
| 380 | F | Ford Motor Company | $14.9 | -1.55 | — | — | no earnings | no_earnings |
| 381 | SOMN | Southern Company (The) 202 | $50.48 | None | — | — | no earnings | no_earnings |
| 382 | CRWV | CoreWeave, Inc. | $100.39 | -2.72 | — | — | no earnings | no_earnings |
| 383 | HBANL | Huntington Bancshares Inco | $25.19 | None | — | — | no earnings | no_earnings |
| 384 | MSTR | Strategy Inc | $120.44 | -36.99 | — | — | no earnings | no_earnings |
| 385 | BIDU | Baidu, Inc. | $121.66 | -0.16 | — | — | no earnings | no_earnings |
| 386 | HBANZ | Huntington Bancshares Inco | $20.11 | None | — | — | no earnings | no_earnings |
| 387 | MCHPP | Microchip Technology Incor | $74.95 | None | — | — | no earnings | no_earnings |
| 388 | TTWO | Take-Two Interactive Softw | $214.39 | -1.63 | — | — | no earnings | no_earnings |
| 389 | HMC | Honda Motor Company, Ltd. | $26.7 | -1.99 | — | — | no earnings | no_earnings |
| 390 | LYV | Live Nation Entertainment, | $160.07 | -1.78 | — | — | no earnings | no_earnings |
| 391 | BTSGU | BrightSpring Health Servic | $190.11 | None | — | — | no earnings | no_earnings |
| 392 | ASTS | AST SpaceMobile, Inc. | $93.6 | -1.8 | — | — | no earnings | no_earnings |
| 393 | PPLC | PPL Corporation Corporate | $48.05 | None | — | — | no earnings | no_earnings |
| 394 | RKT | Rocket Companies, Inc. | $12.65 | -0.03 | — | — | no earnings | no_earnings |
| 395 | VOD | Vodafone Group Plc | $14.7 | -0.14 | — | — | no earnings | no_earnings |
| 396 | SATS | EchoStar Corporation | $116.28 | -50.21 | — | — | no earnings | no_earnings |
| 397 | STRC | Strategy Inc - Variable Ra | $93.4 | None | — | — | no earnings | no_earnings |
| 398 | STRF | Strategy Inc - 10.00% Seri | $92.63 | None | — | — | no earnings | no_earnings |
| 399 | RVMD | Revolution Medicines, Inc. | $149.23 | -7.12 | — | — | no earnings | no_earnings |
| 400 | NTRA | Natera, Inc. | $215.31 | -1.61 | — | — | no earnings | no_earnings |
| 401 | CNC | Centene Corporation | $62.33 | -13.05 | — | — | no earnings | no_earnings |
| 402 | EL | Estee Lauder Companies, In | $83.49 | -0.7 | — | — | no earnings | no_earnings |
| 403 | RBLX | Roblox Corporation | $41.82 | -1.57 | — | — | no earnings | no_earnings |
| 404 | AGNCN | AGNC Investment Corp. - De | $25.82 | -1.86 | — | — | no earnings | no_earnings |
| 405 | AGNCO | AGNC Investment Corp. - De | $25.52 | -1.86 | — | — | no earnings | no_earnings |
| 406 | AGNCZ | AGNC Investment Corp. - De | $25.39 | None | — | — | no earnings | no_earnings |
| 407 | FISV | Fiserv, Inc. | $54.43 | None | — | — | no earnings | no_earnings |
| 408 | AGNCL | AGNC Investment Corp. - De | $25.15 | None | — | — | no earnings | no_earnings |
| 409 | AGNCP | AGNC Investment Corp. - De | $25.08 | -1.86 | — | — | no earnings | no_earnings |
| 410 | AGNCM | AGNC Investment Corp. - De | $25.06 | -1.86 | — | — | no earnings | no_earnings |
| 411 | MDB | MongoDB, Inc. | $350.74 | -0.39 | — | — | no earnings | no_earnings |
| 412 | CPNG | Coupang, Inc. | $15.15 | -0.1 | — | — | no earnings | no_earnings |
| 413 | KHC | The Kraft Heinz Company | $22.58 | -4.86 | — | — | no earnings | no_earnings |
| 414 | SYM | Symbotic Inc. | $44.02 | -0.08 | — | — | no earnings | no_earnings |
| 415 | TEAM | Atlassian Corporation | $99.47 | -0.82 | — | — | no earnings | no_earnings |
| 416 | BEP | Brookfield Renewable Partn | $36.52 | -0.3 | — | — | no earnings | no_earnings |
| 417 | DOW | Dow Inc. | $33.97 | -4.0 | — | — | no earnings | no_earnings |
| 418 | STRD | Strategy Inc - 10.00% Seri | $67.7 | None | — | — | no earnings | no_earnings |
| 419 | FITBM | Fifth Third Bancorp - Depo | $26.02 | None | — | — | no earnings | no_earnings |
| 420 | BNH | Brookfield Finance Inc. 4. | $15.46 | None | — | — | no earnings | no_earnings |
| 421 | STRK | Strategy Inc - 8.00% Serie | $65.4 | None | — | — | no earnings | no_earnings |
| 422 | SOJC | Southern Company (The) Ser | $20.81 | None | — | — | no earnings | no_earnings |
| 423 | BNJ | Brookfield Finance Inc. 4. | $14.89 | None | — | — | no earnings | no_earnings |
| 424 | BNTX | BioNTech SE | $88.08 | -5.88 | — | — | no earnings | no_earnings |
| 425 | OMC | Omnicom Group Inc. | $75.31 | -0.37 | — | — | no earnings | no_earnings |
| 426 | SOJD | Southern Company (The) Ser | $19.31 | None | — | — | no earnings | no_earnings |
| 427 | ZS | Zscaler, Inc. | $130.78 | -0.48 | — | — | no earnings | no_earnings |
| 428 | YPF | YPF Sociedad Anonima | $53.5 | -1.04 | — | — | no earnings | no_earnings |
| 429 | LYB | LyondellBasell Industries  | $64.5 | -2.12 | — | — | no earnings | no_earnings |
| 430 | RIVN | Rivian Automotive, Inc. | $16.35 | -2.92 | — | — | no earnings | no_earnings |
| 431 | STLA | Stellantis N.V. | $7.11 | -8.68 | — | — | no earnings | no_earnings |
| 432 | ROIV | Roivant Sciences Ltd. | $28.58 | -0.54 | — | — | no earnings | no_earnings |
| 433 | INSM | Insmed Incorporated | $94.22 | -5.76 | — | — | no earnings | no_earnings |
| 434 | AQNB | Algonquin Power & Utilitie | $26.03 | None | — | — | no earnings | no_earnings |
| 435 | CRCL | Circle Internet Group, Inc | $80.28 | -0.23 | — | — | no earnings | no_earnings |
| 436 | BPYPM | Brookfield Property Partne | $16.59 | None | — | — | no earnings | no_earnings |
| 437 | MRNA | Moderna, Inc. | $47.44 | -8.14 | — | — | no earnings | no_earnings |
| 438 | DUKB | Duke Energy Corporation 5. | $23.84 | None | — | — | no earnings | no_earnings |
| 439 | VTRS | Viatris Inc. | $15.88 | -0.3 | — | — | no earnings | no_earnings |
| 440 | SOJE | Southern Company (The) Ser | $16.75 | None | — | — | no earnings | no_earnings |
| 441 | ALB | Albemarle Corporation | $155.44 | -3.42 | — | — | no earnings | no_earnings |
| 442 | APG | APi Group Corporation | $41.98 | -0.64 | — | — | no earnings | no_earnings |
| 443 | H | Hyatt Hotels Corporation | $193.06 | -0.35 | — | — | no earnings | no_earnings |
| 444 | IP | International Paper Compan | $33.61 | -5.19 | — | — | no earnings | no_earnings |
| 445 | FLUT | Flutter Entertainment plc | $100.49 | -2.1 | — | — | no earnings | no_earnings |
| 446 | GH | Guardant Health, Inc. | $125.61 | -3.4 | — | — | no earnings | no_earnings |
| 447 | TLN | Talen Energy Corporation | $364.74 | -0.51 | — | — | no earnings | no_earnings |
| 448 | SITM | SiTime Corporation | $625.68 | -0.94 | — | — | no earnings | no_earnings |
| 449 | VNOM | Viper Energy, Inc. | $45.46 | -0.57 | — | — | no earnings | no_earnings |
| 450 | XPEV | XPeng Inc. | $15.95 | -0.35 | — | — | no earnings | no_earnings |
| 451 | SUI | Sun Communities, Inc. | $123.69 | -0.49 | — | — | no earnings | no_earnings |
| 452 | LI | Li Auto Inc. | $14.2 | -0.27 | — | — | no earnings | no_earnings |
| 453 | RBRK | Rubrik, Inc. | $73.41 | -1.46 | — | — | no earnings | no_earnings |
| 454 | BEPC | Brookfield Renewable Corpo | $38.72 | -25.06 | — | — | no earnings | no_earnings |
| 455 | KKRS | KKR Group Finance Co. IX L | $16.22 | None | — | — | no earnings | no_earnings |
| 456 | APOS | Apollo Global Management,  | $25.41 | None | — | — | no earnings | no_earnings |
| 457 | VLYPN | Valley National Bancorp -  | $26.06 | None | — | — | no earnings | no_earnings |
| 458 | PS | Pershing Square Inc. | $35.75 | -0.94 | — | — | no earnings | no_earnings |
| 459 | AAOI | Applied Optoelectronics, I | $177.0 | -0.65 | — | — | no earnings | no_earnings |
| 460 | SMTC | Semtech Corporation | $151.02 | -0.41 | — | — | no earnings | no_earnings |
| 461 | NIO | NIO Inc. | $5.36 | -0.56 | — | — | no earnings | no_earnings |
| 462 | SREA | DBA Sempra 5.750% Junior S | $21.07 | None | — | — | no earnings | no_earnings |
| 463 | BBIO | BridgeBio Pharma, Inc. | $67.61 | -3.74 | — | — | no earnings | no_earnings |
| 464 | U | Unity Software Inc. | $29.17 | -1.57 | — | — | no earnings | no_earnings |
| 465 | HUT | Hut 8 Corp. | $112.24 | -2.82 | — | — | no earnings | no_earnings |
| 466 | AUR | Aurora Innovation, Inc. | $6.31 | -0.43 | — | — | no earnings | no_earnings |
| 467 | IONS | Ionis Pharmaceuticals, Inc | $74.48 | -2.01 | — | — | no earnings | no_earnings |
| 468 | IVZ | Invesco Ltd | $27.35 | -1.47 | — | — | no earnings | no_earnings |
| 469 | AXSM | Axsome Therapeutics, Inc. | $232.32 | -3.72 | — | — | no earnings | no_earnings |
| 470 | HAS | Hasbro, Inc. | $84.18 | -1.61 | — | — | no earnings | no_earnings |
| 471 | WULF | TeraWulf Inc. | $24.0 | -2.51 | — | — | no earnings | no_earnings |
| 472 | ELAN | Elanco Animal Health Incor | $23.63 | -0.5 | — | — | no earnings | no_earnings |
| 473 | LFUS | Littelfuse, Inc. | $457.34 | -1.69 | — | — | no earnings | no_earnings |
| 474 | KLAR | Klarna Group plc | $16.36 | -0.52 | — | — | no earnings | no_earnings |
| 475 | BIPJ | Brookfield Infrastructure  | $24.99 | None | — | — | no earnings | no_earnings |
| 476 | FIG | Figma, Inc. | $21.75 | -4.07 | — | — | no earnings | no_earnings |
| 477 | EQH | Equitable Holdings, Inc. | $40.8 | -2.85 | — | — | no earnings | no_earnings |
| 478 | PL | Planet Labs PBC | $32.22 | -1.16 | — | — | no earnings | no_earnings |
| 479 | SMMT | Summit Therapeutics Inc. | $14.77 | -1.59 | — | — | no earnings | no_earnings |
| 480 | QXO | QXO, Inc. | $15.76 | -0.95 | — | — | no earnings | no_earnings |
| 481 | APLD | Applied Digital Corporatio | $39.62 | -0.38 | — | — | no earnings | no_earnings |
| 482 | MDGL | Madrigal Pharmaceuticals,  | $486.98 | -13.5 | — | — | no earnings | no_earnings |
| 483 | VIAV | Viavi Solutions Inc. | $47.56 | -0.25 | — | — | no earnings | no_earnings |
| 484 | SJM | The J.M. Smucker Company | $103.54 | -11.79 | — | — | no earnings | no_earnings |
| 485 | WLK | Westlake Corporation | $84.64 | -12.7 | — | — | no earnings | no_earnings |
| 486 | FRVO | Fervo Energy Company | $37.22 | -0.21 | — | — | no earnings | no_earnings |
| 487 | MP | MP Materials Corp. | $59.18 | -0.4 | — | — | no earnings | no_earnings |
| 488 | GSAT | Globalstar, Inc. | $81.49 | -0.15 | — | — | no earnings | no_earnings |
| 489 | SAIL | SailPoint, Inc. | $18.24 | -0.54 | — | — | no earnings | no_earnings |
| 490 | ARWR | Arrowhead Pharmaceuticals, | $73.09 | -2.27 | — | — | no earnings | no_earnings |
| 491 | FROG | JFrog Ltd. | $84.0 | -0.53 | — | — | no earnings | no_earnings |
| 492 | OKLO | Oklo Inc. | $58.09 | -0.84 | — | — | no earnings | no_earnings |
| 493 | BAX | Baxter International Inc. | $19.38 | -1.91 | — | — | no earnings | no_earnings |
| 494 | GTLS | Chart Industries, Inc. | $207.31 | -1.02 | — | — | no earnings | no_earnings |
| 495 | RGC | Regencell Bioscience Holdi | $19.99 | -0.01 | — | — | no earnings | no_earnings |
| 496 | GLXY | Galaxy Digital Inc. | $25.14 | -0.24 | — | — | no earnings | no_earnings |
| 497 | LINE | Lineage, Inc. | $42.63 | -0.62 | — | — | no earnings | no_earnings |
| 498 | ONBPO | Old National Bancorp - Dep | $24.86 | None | — | — | no earnings | no_earnings |
| 499 | OC | Owens Corning Inc | $119.2 | -4.74 | — | — | no earnings | no_earnings |
| 500 | SNAP | Snap Inc. | $5.76 | -0.24 | — | — | no earnings | no_earnings |

---
## Global (top ~1000 companies worldwide by market cap)
Valued 992 holdings · **496 most undervalued (BULLISH)** vs **496 most overvalued (BEARISH)** · 0 near-median (neutral, excluded).

### 🟢 BULLISH — 496 most undervalued (price most below Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | SBER.ME | SBERBANK OF RUSSIA | $133.3 | 50.4 | 17% | $1348.93 | +912% |  |
| 2 | CI | The Cigna Group | $289.48 | 113.71 | 10% | $2282.48 | +688% |  |
| 3 | GMKN.ME | MMC NORILSK NICKEL | $16720.0 | 2619.9 | 30% | $120800.31 | +622% |  |
| 4 | BABWF | International Consolidated | $5.8 | 0.84 | 30% | $38.73 | +568% |  |
| 5 | NPSNY | Naspers Ltd. | $10.5 | 1.35 | 30% | $62.25 | +493% |  |
| 6 | ONGC.NS | OIL AND NATURAL GAS CORP. | $264.75 | 32.93 | 30% | $1518.36 | +474% |  |
| 7 | PRX.AS | PROSUS | $40.15 | 4.97 | 30% | $229.16 | +471% |  |
| 8 | 8725.T | MS&AD INS GP HLDGS | $4325.0 | 528.95 | 30% | $24389.22 | +464% |  |
| 9 | GAZP.ME | GAZPROM PJSC | $198.0 | 88.51 | 0% | $1099.15 | +455% |  |
| 10 | 8630.T | SOMPO HOLDINGS INC | $5898.0 | 701.27 | 30% | $32334.68 | +448% |  |
| 11 | 9984.T | SOFTBANK GROUP CORP | $7426.0 | 872.56 | 30% | $40232.65 | +442% |  |
| 12 | VOW3.DE | VOLKSWAGEN AG              | $87.84 | 12.21 | 25% | $460.7 | +424% |  |
| 13 | EMAAR.AE | EMAAR PROPERTIES | $11.34 | 2.14 | 17% | $57.37 | +406% |  |
| 14 | GFI | Gold Fields Limited | $36.62 | 3.94 | 30% | $181.67 | +396% |  |
| 15 | UAL | United Airlines Holdings,  | $105.73 | 11.18 | 30% | $515.5 | +388% |  |
| 16 | 601688.SS | HUATAI SECURITIES CO LTD | $18.85 | 1.86 | 30% | $85.76 | +355% |  |
| 17 | EQT | EQT Corporation | $53.75 | 5.27 | 30% | $242.99 | +352% |  |
| 18 | REP.MC | REPSOL,  S.A. | $23.08 | 2.14 | 30% | $98.67 | +328% |  |
| 19 | B | Barrick Mining Corporation | $39.46 | 3.62 | 30% | $166.91 | +323% |  |
| 20 | 601336.SS | NEW CHINA LIFE INSURANCE C | $56.35 | 11.82 | 10% | $237.48 | +321% |  |
| 21 | KGC | Kinross Gold Corporation | $26.22 | 2.35 | 30% | $108.36 | +313% |  |
| 22 | 6902.T | DENSO CORP | $1887.0 | 163.04 | 30% | $7517.57 | +298% |  |
| 23 | 600030.SS | CITIC SECURITIES CO LTD | $25.67 | 2.2 | 30% | $101.44 | +295% |  |
| 24 | NVTK.ME | NOVATEK PJSC | $993.0 | 144.24 | 16% | $3769.13 | +280% |  |
| 25 | AU | AngloGold Ashanti PLC | $84.12 | 6.81 | 30% | $314.0 | +273% |  |
| 26 | 601600.SS | ALUMINUM CORP OF CHINA(CHA | $10.68 | 0.86 | 30% | $39.65 | +271% |  |
| 27 | TM | Toyota Motor Corporation | $177.16 | 18.46 | 23% | $650.66 | +267% |  |
| 28 | LKOH.ME | OIL CO LUKOIL PJSC | $3911.0 | 1129.04 | 0% | $14020.9 | +258% |  |
| 29 | 8309.T | SUMITOMO MITSUI TRUST GP I | $5828.0 | 451.67 | 30% | $20825.94 | +257% |  |
| 30 | NEM | Newmont Corporation | $99.71 | 7.71 | 30% | $355.5 | +256% |  |
| 31 | LYG | Lloyds Banking Group Plc | $5.31 | 0.41 | 30% | $18.9 | +256% |  |
| 32 | 601899.SS | ZIJIN MINING GROUP CO.LTD | $29.63 | 2.27 | 30% | $104.67 | +253% |  |
| 33 | TCOM | Trip.com Group Limited | $47.69 | 7.04 | 14% | $167.45 | +251% |  |
| 34 | TTE | TotalEnergies SE | $88.71 | 6.74 | 30% | $310.77 | +250% |  |
| 35 | EOG | EOG Resources, Inc. | $137.78 | 10.17 | 30% | $468.93 | +240% |  |
| 36 | 8053.T | SUMITOMO CORP | $6842.0 | 498.78 | 30% | $22998.12 | +236% |  |
| 37 | ROSN.ME | ROSNEFT OIL CO | $351.2 | 92.95 | 0% | $1154.29 | +229% |  |
| 38 | JSWSTEEL.NS | JSW STEEL LIMITED | $1284.0 | 91.29 | 30% | $4209.27 | +228% |  |
| 39 | NTR | Nutrien Ltd. | $67.2 | 4.91 | 29% | $218.58 | +225% |  |
| 40 | 002142.SZ | BANK OF NINGBO CO. LTD. | $30.56 | 4.41 | 13% | $99.17 | +224% |  |
| 41 | 9433.T | KDDI CORPORATION | $2651.5 | 183.48 | 30% | $8460.03 | +219% |  |
| 42 | BPAC3.SA | BTGP BANCO  ON      N2 | $22.23 | 1.51 | 30% | $69.62 | +213% |  |
| 43 | 600919.SS | BANK OF JIANGSU | $11.38 | 1.81 | 9% | $35.22 | +210% |  |
| 44 | MFG | Mizuho Financial Group, In | $9.52 | 0.63 | 30% | $29.05 | +205% |  |
| 45 | VG | Venture Global, Inc. | $12.8 | 0.96 | 27% | $38.92 | +204% |  |
| 46 | CFG | Citizens Financial Group,  | $63.98 | 4.22 | 30% | $194.58 | +204% |  |
| 47 | SHEL | Shell PLC | $85.4 | 6.42 | 27% | $259.28 | +204% |  |
| 48 | 8002.T | MARUBENI CORP | $5044.0 | 329.88 | 30% | $15210.35 | +202% |  |
| 49 | DB | Deutsche Bank AG | $31.51 | 3.67 | 16% | $94.49 | +200% |  |
| 50 | AEM | Agnico Eagle Mines Limited | $163.66 | 10.62 | 30% | $489.67 | +199% |  |
| 51 | 0175.HK | GEELY AUTO | $18.41 | 1.89 | 18% | $54.65 | +197% |  |
| 52 | CVE | Cenovus Energy Inc | $28.22 | 1.81 | 30% | $83.46 | +196% |  |
| 53 | 2328.HK | PICC P&C | $14.27 | 2.1 | 10% | $41.96 | +194% |  |
| 54 | BCS | Barclays PLC | $24.27 | 2.33 | 20% | $71.04 | +193% |  |
| 55 | 000001.SZ | PING AN BANK CO LTD | $10.98 | 2.12 | 3% | $31.06 | +183% |  |
| 56 | C | Citigroup, Inc. | $132.47 | 8.09 | 30% | $373.02 | +182% |  |
| 57 | 3993.HK | CMOC | $18.08 | 1.1 | 30% | $50.72 | +180% |  |
| 58 | GMBXF | Grupo Mexico S.A.B. de C.V | $11.7 | 0.71 | 30% | $32.74 | +180% |  |
| 59 | SU | Suncor Energy  Inc. | $62.22 | 3.78 | 30% | $173.62 | +179% |  |
| 60 | NWG | NatWest Group plc | $15.79 | 1.87 | 13% | $43.61 | +176% |  |
| 61 | LICI.NS | LIFE INSURA CORP OF INDIA | $399.9 | 45.43 | 14% | $1079.13 | +170% |  |
| 62 | DAL | Delta Air Lines, Inc. | $79.42 | 6.85 | 20% | $213.98 | +169% |  |
| 63 | 0267.HK | CITIC | $13.62 | 2.33 | 5% | $36.56 | +168% |  |
| 64 | EQNR | Equinor ASA | $36.94 | 2.21 | 29% | $98.8 | +168% |  |
| 65 | MPC | Marathon Petroleum Corpora | $262.01 | 15.2 | 30% | $700.85 | +168% |  |
| 66 | HINDZINC.NS | HINDUSTAN ZINC LIMITED | $566.8 | 32.76 | 30% | $1508.78 | +166% |  |
| 67 | CMCSA | Comcast Corporation | $23.82 | 5.1 | 0% | $63.33 | +166% |  |
| 68 | UBER | Uber Technologies, Inc. | $70.71 | 4.03 | 30% | $185.82 | +163% |  |
| 69 | 1398.HK | ICBC | $6.83 | 1.17 | 4% | $17.93 | +163% |  |
| 70 | GILD | Gilead Sciences, Inc. | $129.16 | 7.35 | 30% | $338.9 | +162% |  |
| 71 | BBD | Banco Bradesco Sa | $3.36 | 0.41 | 11% | $8.75 | +160% |  |
| 72 | T | AT&T Inc. | $22.75 | 3.04 | 9% | $58.62 | +158% |  |
| 73 | FSLR | First Solar, Inc. | $279.01 | 15.49 | 30% | $714.22 | +156% |  |
| 74 | OMV.F | OMV AG                     | $64.3 | 3.56 | 30% | $164.15 | +155% |  |
| 75 | ALL | Allstate Corporation (The) | $221.01 | 45.2 | 0% | $561.31 | +154% |  |
| 76 | 2259.HK | ZIJIN GOLD INTL | $117.3 | 6.43 | 30% | $296.48 | +153% |  |
| 77 | ITSA3.SA | ITAUSA      ON      N1 | $12.73 | 1.52 | 11% | $32.09 | +152% |  |
| 78 | NU | Nu Holdings Ltd. | $11.97 | 0.65 | 30% | $29.97 | +150% |  |
| 79 | 601066.SS | CHINA SECURITIES CO.  LTD. | $24.54 | 1.33 | 30% | $61.32 | +150% |  |
| 80 | BNP.PA | BNP PARIBAS ACT.A | $93.65 | 10.6 | 12% | $231.99 | +148% |  |
| 81 | BABA | Alibaba Group Holding Limi | $121.06 | 6.5 | 30% | $299.71 | +148% |  |
| 82 | VLO | Valero Energy Corporation | $255.82 | 13.69 | 30% | $631.23 | +147% |  |
| 83 | MT | Arcelor Mittal NY Registry | $67.21 | 3.82 | 28% | $165.82 | +147% |  |
| 84 | ACGL | Arch Capital Group Ltd. | $91.19 | 13.0 | 7% | $224.11 | +146% |  |
| 85 | 600900.SS | CHINA YANGTZE POWER CO | $27.61 | 1.47 | 30% | $67.78 | +146% |  |
| 86 | EBO.F | Erste Group Bank AG        | $101.1 | 8.57 | 18% | $246.59 | +144% |  |
| 87 | GLE.PA | SOCIETE GENERALE | $70.26 | 7.04 | 14% | $169.07 | +141% |  |
| 88 | 002415.SZ | HANGZHOU HIKVISION DIGITAL | $31.28 | 1.63 | 30% | $75.16 | +140% |  |
| 89 | 601668.SS | CHINA CONSTRUCTION ENGINEE | $4.72 | 0.91 | 0% | $11.3 | +139% |  |
| 90 | SAF.PA | SAFRAN | $298.5 | 17.16 | 27% | $713.8 | +139% |  |
| 91 | SHG | Shinhan Financial Group Co | $67.17 | 6.68 | 14% | $159.72 | +138% |  |
| 92 | 002714.SZ | MUYUAN FOODS GROUP CO LTD | $35.06 | 1.8 | 30% | $83.0 | +137% |  |
| 93 | 600028.SS | CHINA PETROLEUM & CHEMICAL | $4.89 | 0.27 | 28% | $11.43 | +134% |  |
| 94 | TLX.DE | Talanx AG                  | $98.8 | 10.26 | 13% | $230.93 | +134% |  |
| 95 | PLZL.ME | POLYUS PJSC | $8376.0 | 1048.52 | 8% | $19220.81 | +130% |  |
| 96 | ITUB | Itau Unibanco Banco Holdin | $7.54 | 0.81 | 11% | $17.26 | +129% |  |
| 97 | UCG.MI | UNICREDIT | $73.15 | 7.27 | 13% | $166.93 | +128% |  |
| 98 | UBS | UBS Group AG Registered | $47.01 | 2.79 | 25% | $106.67 | +127% |  |
| 99 | SCHW | Charles Schwab Corporation | $88.84 | 5.03 | 26% | $201.23 | +126% |  |
| 100 | PBR | Petroleo Brasileiro S.A. P | $17.75 | 3.2 | 0% | $39.74 | +124% |  |
| 101 | 7974.T | NINTENDO CO LTD | $7524.0 | 364.16 | 30% | $16790.96 | +123% |  |
| 102 | 601818.SS | CHINA EVERBRIGHT BANK CO L | $3.13 | 0.56 | 0% | $6.95 | +122% |  |
| 103 | SAN | Banco Santander, S.A. Spon | $12.15 | 1.03 | 16% | $26.78 | +120% |  |
| 104 | 6701.T | NEC CORP | $4253.0 | 202.87 | 30% | $9354.08 | +120% |  |
| 105 | 601601.SS | CHINA PACIFIC INSURANCE (G | $31.05 | 5.48 | 0% | $68.05 | +119% |  |
| 106 | BMW.DE | BAYERISCHE MOTOREN WERKE A | $70.38 | 11.19 | 2% | $154.14 | +119% |  |
| 107 | 9992.HK | POP MART | $176.4 | 11.1 | 23% | $383.36 | +117% |  |
| 108 | 6669.TW | WIWYNN CORPORATION | $5660.0 | 265.45 | 30% | $12239.57 | +116% |  |
| 109 | HIG | The Hartford Insurance Gro | $132.14 | 14.21 | 10% | $284.72 | +116% |  |
| 110 | FNLPF | Fresnillo Plc | $40.34 | 1.88 | 30% | $86.68 | +115% |  |
| 111 | VICI | VICI Properties Inc. | $27.86 | 2.92 | 10% | $59.85 | +115% |  |
| 112 | 7182.T | JAPAN POST BANK CO LTD | $3161.0 | 146.99 | 30% | $6777.52 | +114% |  |
| 113 | 601166.SS | INDUSTRIAL BANK CO LTD | $18.6 | 3.2 | 0% | $39.74 | +114% |  |
| 114 | 600150.SS | CHINA CSSC HOLDINGS LIMITE | $35.95 | 1.65 | 30% | $76.08 | +112% |  |
| 115 | KB | KB Financial Group Inc | $107.91 | 10.46 | 12% | $227.7 | +111% |  |
| 116 | 3968.HK | CM BANK | $48.18 | 6.61 | 4% | $99.73 | +107% |  |
| 117 | 2222.SR | Saudi Arabian Oil Co. | $26.92 | 1.54 | 24% | $55.44 | +106% |  |
| 118 | BAC | Bank of America Corporatio | $53.83 | 4.03 | 17% | $110.71 | +106% |  |
| 119 | EMIRATESNBD.AE | EMIRATES NBD BANK | $26.86 | 3.74 | 4% | $55.16 | +105% |  |
| 120 | INVE-B.ST | Investor AB ser. B | $379.95 | 62.2 | 0% | $772.43 | +103% |  |
| 121 | TECK | Teck Resources Ltd | $61.67 | 2.71 | 30% | $124.95 | +103% |  |
| 122 | HEXA-B.ST | Hexagon AB ser. B | $85.36 | 8.26 | 11% | $172.92 | +103% |  |
| 123 | NTRS | Northern Trust Corporation | $170.47 | 9.55 | 24% | $345.16 | +102% |  |
| 124 | 601998.SS | CHINA CITIC BANK CORPORATI | $7.37 | 1.2 | 0% | $14.9 | +102% |  |
| 125 | CM | Canadian Imperial Bank of  | $108.84 | 7.26 | 19% | $219.06 | +101% |  |
| 126 | 300750.SZ | CONTEMPORARY AMPEREX TECHN | $403.0 | 17.53 | 30% | $808.29 | +101% |  |
| 127 | COALINDIA.NS | COAL INDIA LTD | $472.3 | 50.44 | 9% | $944.04 | +100% |  |
| 128 | 601288.SS | AGRICULTURAL BANK OF CHINA | $6.36 | 0.79 | 5% | $12.7 | +100% |  |
| 129 | 8058.T | MITSUBISHI CORP | $4859.0 | 209.91 | 30% | $9678.69 | +99% |  |
| 130 | 2359.HK | WUXI APPTEC | $124.5 | 7.99 | 20% | $247.0 | +98% |  |
| 131 | TEL | TE Connectivity plc | $212.65 | 9.78 | 28% | $421.73 | +98% |  |
| 132 | MUV2.DE | MUENCHENER RUECKVERS.-GES. | $448.1 | 52.2 | 6% | $884.82 | +98% |  |
| 133 | ABN.AS | ABN AMRO BANK N.V. | $33.82 | 2.54 | 16% | $66.8 | +98% |  |
| 134 | 300059.SZ | EAST MONEY INFORMATION CO  | $18.52 | 0.83 | 29% | $36.48 | +97% |  |
| 135 | AMP | Ameriprise Financial, Inc. | $454.66 | 40.15 | 12% | $894.9 | +97% |  |
| 136 | 1180.SR | The Saudi National Bank | $38.84 | 4.11 | 8% | $76.04 | +96% |  |
| 137 | AXISBANK.BO | AXIS BANK LTD. | $1273.15 | 84.54 | 19% | $2491.67 | +96% |  |
| 138 | ING | ING Group, N.V. | $29.67 | 2.54 | 13% | $57.96 | +95% |  |
| 139 | BAP | Credicorp Ltd. | $322.5 | 26.09 | 14% | $627.39 | +94% |  |
| 140 | 601628.SS | CHINA LIFE INSURANCE CO LT | $32.82 | 5.12 | 0% | $63.58 | +94% |  |
| 141 | 2885.TW | YUANTA FINANCIAL HOLDING C | $65.3 | 2.74 | 30% | $126.34 | +94% |  |
| 142 | TATASTEEL.NS | TATA STEEL LIMITED | $206.77 | 8.64 | 30% | $398.38 | +93% |  |
| 143 | 000651.SZ | GREE ELECTRICAL APP INC OF | $38.46 | 5.22 | 3% | $73.95 | +92% |  |
| 144 | BMPS.MI | BANCA MONTE PASCHI SIENA | $8.95 | 1.38 | 0% | $17.14 | +92% |  |
| 145 | TFC | Truist Financial Corporati | $49.2 | 4.04 | 13% | $94.08 | +91% |  |
| 146 | 0883.HK | CNOOC | $26.54 | 2.98 | 6% | $50.7 | +91% |  |
| 147 | PTT-R.BK | PTT_PTT | $36.75 | 3.25 | 12% | $70.18 | +91% |  |
| 148 | FCNCA | First Citizens BancShares, | $2075.1 | 173.48 | 13% | $3963.98 | +91% |  |
| 149 | 600309.SS | WANHUA CHEMICAL GROUP CO L | $72.46 | 4.2 | 21% | $137.53 | +90% |  |
| 150 | 601328.SS | BANK OF COMMUNICATIONS CO  | $6.83 | 1.04 | 0% | $12.92 | +89% |  |
| 151 | 601319.SS | THE PEOPLE S INSURANCE COM | $6.57 | 1.0 | 0% | $12.42 | +89% |  |
| 152 | 600000.SS | SHANGHAI PUDONG DEVELOPMEN | $9.34 | 1.42 | 0% | $17.63 | +89% |  |
| 153 | CINF | Cincinnati Financial Corpo | $165.29 | 17.49 | 8% | $311.96 | +89% |  |
| 154 | FMG.AX | FORTESCUE FPO [FMG] | $20.53 | 1.7 | 13% | $38.38 | +87% |  |
| 155 | RF | Regions Financial Corporat | $28.54 | 2.41 | 12% | $53.22 | +86% |  |
| 156 | VST | Vistra Corp. | $148.76 | 5.98 | 30% | $275.73 | +85% |  |
| 157 | 000858.SZ | WULIANGYE YIBIN CO. LTD. | $81.08 | 3.24 | 30% | $149.39 | +84% |  |
| 158 | JD | JD.com, Inc. | $28.88 | 1.37 | 26% | $53.2 | +84% |  |
| 159 | CBOE | Cboe Global Markets, Inc. | $281.91 | 11.7 | 29% | $516.03 | +83% |  |
| 160 | QNBTR.IS | QNB BANK | $220.0 | 8.73 | 30% | $402.53 | +83% |  |
| 161 | 601658.SS | POSTAL SAVINGS BANK OF CHI | $4.96 | 0.73 | 0% | $9.07 | +83% |  |
| 162 | NUE | Nucor Corporation | $254.39 | 10.07 | 30% | $464.32 | +82% |  |
| 163 | Z74.SI | Singtel | $4.29 | 0.34 | 13% | $7.8 | +82% |  |
| 164 | PNC | PNC Financial Services Gro | $228.37 | 17.22 | 14% | $413.37 | +81% |  |
| 165 | TEVA | Teva Pharmaceutical Indust | $34.19 | 1.34 | 30% | $61.79 | +81% |  |
| 166 | 4578.T | OTSUKA HLDGS CO LTD | $10580.0 | 685.58 | 18% | $19068.39 | +80% |  |
| 167 | SMCI | Super Micro Computer, Inc. | $41.64 | 1.9 | 26% | $74.9 | +80% |  |
| 168 | PKN.WA | PKNORLEN | $143.0 | 5.56 | 30% | $256.36 | +79% |  |
| 169 | WFC | Wells Fargo & Company | $81.94 | 6.47 | 13% | $146.86 | +79% |  |
| 170 | 2914.T | JAPAN TOBACCO INC | $5973.0 | 281.33 | 25% | $10704.57 | +79% |  |
| 171 | ISP.MI | INTESA SANPAOLO | $5.67 | 0.54 | 9% | $10.14 | +79% |  |
| 172 | U11.SI | UOB | $38.55 | 2.75 | 15% | $68.3 | +77% |  |
| 173 | USB | U.S. Bancorp | $55.69 | 4.77 | 11% | $98.52 | +77% |  |
| 174 | BHP | BHP Group Limited | $82.72 | 4.03 | 24% | $145.66 | +76% |  |
| 175 | BIIB | Biogen Inc. | $195.34 | 9.3 | 24% | $343.52 | +76% |  |
| 176 | EOAN.DE | E.ON SE                    | $18.27 | 1.31 | 14% | $31.99 | +75% |  |
| 177 | 600188.SS | YANKUANG ENERGY GROUP COMP | $25.05 | 0.95 | 30% | $43.8 | +75% |  |
| 178 | 6273.T | SMC CORP | $65260.0 | 2643.03 | 28% | $113660.3 | +74% |  |
| 179 | AIG | American International Gro | $75.49 | 5.68 | 13% | $131.46 | +74% |  |
| 180 | NFLX | Netflix, Inc. | $82.18 | 3.1 | 30% | $142.94 | +74% |  |
| 181 | 1109.HK | CHINA RES LAND | $35.92 | 4.12 | 4% | $62.16 | +73% |  |
| 182 | BNS | Bank Nova Scotia Halifax P | $80.56 | 5.22 | 16% | $139.29 | +73% |  |
| 183 | AMX | America Movil, S.A.B. de C | $24.84 | 1.67 | 16% | $42.89 | +73% |  |
| 184 | CEG | Constellation Energy Corpo | $254.83 | 11.52 | 25% | $439.04 | +72% |  |
| 185 | ACA.PA | CREDIT AGRICOLE | $16.53 | 2.13 | 2% | $28.45 | +72% |  |
| 186 | 6178.T | JAPAN POST HLDGS CO LTD | $2122.5 | 129.05 | 18% | $3650.85 | +72% |  |
| 187 | FMX | Fomento Economico Mexicano | $122.88 | 4.57 | 30% | $210.72 | +72% |  |
| 188 | ADS.DE | adidas AG                  | $161.45 | 7.72 | 24% | $276.78 | +71% |  |
| 189 | MTB | M&T Bank Corporation | $222.44 | 17.82 | 12% | $381.2 | +71% |  |
| 190 | BMO | Bank Of Montreal | $164.37 | 9.37 | 19% | $280.49 | +71% |  |
| 191 | BBVA | Banco Bilbao Vizcaya Argen | $22.22 | 2.11 | 8% | $37.85 | +70% |  |
| 192 | HNR1.DE | HANNOVER RUECK SE NA O.N. | $227.2 | 23.81 | 5% | $385.35 | +70% |  |
| 193 | QNBK.QA | QATAR NATIONAL BANK | $17.06 | 1.75 | 6% | $28.92 | +70% |  |
| 194 | EXPGF | Experian plc | $33.75 | 1.63 | 23% | $57.22 | +70% |  |
| 195 | GEV | GE Vernova Inc. | $933.61 | 34.26 | 30% | $1579.69 | +69% |  |
| 196 | VWS.CO | Vestas Wind Systems A/S | $173.4 | 6.35 | 30% | $292.79 | +69% |  |
| 197 | 601318.SS | PING AN INSURANCE(GROUP)CO | $53.48 | 7.25 | 0% | $90.03 | +68% |  |
| 198 | 5802.T | SUMITOMO ELECTRIC INDUSTRI | $13010.0 | 473.56 | 30% | $21835.26 | +68% |  |
| 199 | 6201.T | TOYOTA INDUSTRIES CORP | $20450.0 | 744.38 | 30% | $34322.43 | +68% |  |
| 200 | CB | Chubb Limited | $326.27 | 28.25 | 9% | $547.25 | +68% |  |
| 201 | FFH.TO | FAIRFAX FINANCIAL HOLDINGS | $2220.71 | 280.92 | 1% | $3723.15 | +68% |  |
| 202 | ZURN.SW | ZURICH INSURANCE N | $550.2 | 37.36 | 15% | $921.47 | +68% |  |
| 203 | GFNORTEO.MX | GRUPO FINANCIERO BANORTE | $177.45 | 21.62 | 2% | $296.58 | +67% |  |
| 204 | A5G.IR | AIB GROUP PLC | $10.12 | 0.93 | 8% | $16.89 | +67% |  |
| 205 | GOOG | Alphabet Inc. | $365.76 | 13.09 | 30% | $603.56 | +65% |  |
| 206 | 601919.SS | COSCO SHIPPING HOLDINGS | $15.0 | 1.98 | 0% | $24.59 | +64% |  |
| 207 | BK | The Bank of New York Mello | $137.16 | 8.06 | 18% | $223.99 | +63% |  |
| 208 | HAL | Halliburton Company | $39.18 | 1.81 | 23% | $63.93 | +63% |  |
| 209 | 5108.T | BRIDGESTONE CORP | $3380.0 | 118.98 | 30% | $5486.02 | +62% |  |
| 210 | HBAN | Huntington Bancshares Inco | $16.52 | 1.3 | 11% | $26.69 | +62% |  |
| 211 | PYPL | PayPal Holdings, Inc. | $41.29 | 5.33 | 0% | $66.19 | +60% |  |
| 212 | STLD | Steel Dynamics, Inc. | $268.5 | 9.32 | 30% | $429.73 | +60% |  |
| 213 | ALV.DE | Allianz SE                 | $372.8 | 30.94 | 9% | $593.9 | +59% |  |
| 214 | BKR | Baker Hughes Company | $62.59 | 3.13 | 21% | $99.66 | +59% |  |
| 215 | 2317.TW | HON HAI PRECISION INDUSTRY | $284.5 | 13.4 | 22% | $452.34 | +59% |  |
| 216 | CS.PA | AXA | $39.52 | 3.42 | 8% | $62.75 | +59% |  |
| 217 | RJF | Raymond James Financial, I | $151.45 | 10.59 | 13% | $239.42 | +58% |  |
| 218 | 601939.SS | CHINA CONSTRUCTION BANK | $10.22 | 1.3 | 0% | $16.14 | +58% |  |
| 219 | EXPE | Expedia Group, Inc. | $228.88 | 11.33 | 21% | $361.04 | +58% |  |
| 220 | SCCO | Southern Copper Corporatio | $172.97 | 5.9 | 30% | $272.04 | +57% |  |
| 221 | WPM | Wheaton Precious Metals Co | $116.23 | 3.95 | 30% | $182.13 | +57% |  |
| 222 | CTSH | Cognizant Technology Solut | $53.21 | 4.61 | 8% | $83.03 | +56% |  |
| 223 | EIX | Edison International | $73.33 | 9.2 | 0% | $114.25 | +56% |  |
| 224 | WTW | Willis Towers Watson Publi | $263.54 | 17.02 | 14% | $410.18 | +56% |  |
| 225 | HCA | HCA Healthcare, Inc. | $372.13 | 29.03 | 10% | $576.13 | +55% |  |
| 226 | 2020.HK | ANTA SPORTS | $74.2 | 5.56 | 11% | $114.73 | +55% |  |
| 227 | 002352.SZ | S.F. HOLDING CO LTD | $34.86 | 2.27 | 14% | $53.66 | +54% |  |
| 228 | JPM | JP Morgan Chase & Co. | $312.37 | 20.9 | 13% | $479.68 | +54% |  |
| 229 | 601988.SS | BANK OF CHINA LTD | $6.05 | 0.74 | 0% | $9.19 | +52% |  |
| 230 | 6098.T | RECRUIT HOLDINGS CO LTD | $10595.0 | 347.52 | 30% | $16023.71 | +51% |  |
| 231 | CCL | Carnival Corporation Ltd. | $27.41 | 2.27 | 8% | $41.35 | +51% |  |
| 232 | WDC | Western Digital Corporatio | $511.72 | 16.73 | 30% | $771.4 | +51% |  |
| 233 | TRV | The Travelers Companies, I | $303.25 | 33.51 | 2% | $456.53 | +50% |  |
| 234 | 2382.TW | QUANTA COMPUTER | $390.5 | 18.9 | 20% | $587.69 | +50% |  |
| 235 | ADBE | Adobe Inc. | $251.44 | 17.15 | 12% | $377.52 | +50% |  |
| 236 | SREN.SW | SWISS RE N | $118.15 | 12.3 | 3% | $177.08 | +50% |  |
| 237 | FNV | Franco-Nevada Corporation | $218.74 | 7.11 | 30% | $327.83 | +50% |  |
| 238 | NESTE.HE | Neste Corporation | $28.63 | 0.93 | 30% | $42.88 | +50% |  |
| 239 | PUK | Prudential Public Limited  | $25.49 | 3.07 | 0% | $38.12 | +50% |  |
| 240 | RCL | Royal Caribbean Cruises Lt | $280.0 | 16.38 | 16% | $418.47 | +50% |  |
| 241 | PCG | Pacific Gas & Electric Co. | $17.11 | 1.29 | 10% | $25.55 | +49% |  |
| 242 | 0992.HK | LENOVO GROUP | $24.88 | 1.09 | 22% | $37.1 | +49% |  |
| 243 | PRY.MI | PRYSMIAN | $145.35 | 4.69 | 30% | $216.25 | +49% |  |
| 244 | OTP.BD | OTP | $40770.0 | 4407.24 | 2% | $60486.7 | +48% |  |
| 245 | TRGP | Targa Resources, Inc. | $264.09 | 9.8 | 26% | $389.57 | +48% |  |
| 246 | VZ | Verizon Communications Inc | $45.37 | 4.1 | 6% | $66.8 | +47% |  |
| 247 | NVDA | NVIDIA Corporation | $205.1 | 6.52 | 30% | $300.63 | +47% |  |
| 248 | DELL | Dell Technologies Inc. | $394.39 | 12.54 | 30% | $578.2 | +47% |  |
| 249 | CBK.F | Commerzbank AG             | $37.2 | 2.17 | 15% | $54.44 | +46% |  |
| 250 | UMC | United Microelectronics Co | $19.7 | 0.62 | 30% | $28.59 | +45% |  |
| 251 | MSFT | Microsoft Corporation | $416.67 | 16.79 | 23% | $595.89 | +43% |  |
| 252 | 2881.TW | FUBON FINANCIAL HLDG CO LT | $118.0 | 8.37 | 10% | $168.54 | +43% |  |
| 253 | RYAAY | Ryanair Holdings plc | $56.98 | 4.74 | 7% | $81.14 | +42% |  |
| 254 | TCEHY | Tencent Holding Ltd. | $56.95 | 3.57 | 13% | $80.53 | +41% |  |
| 255 | 000333.SZ | MIDEA GROUP CO LTD | $81.69 | 5.82 | 10% | $115.35 | +41% |  |
| 256 | BBCA.JK | Bank Central Asia Tbk | $5075.0 | 470.96 | 4% | $7146.54 | +41% |  |
| 257 | SAMPO.HE | Sampo Plc A | $8.88 | 0.61 | 10% | $12.5 | +41% |  |
| 258 | 2338.HK | WEICHAI POWER | $37.96 | 1.51 | 23% | $53.24 | +40% |  |
| 259 | HSBC | HSBC Holdings, plc. | $90.8 | 6.05 | 11% | $126.83 | +40% |  |
| 260 | DTE.DE | DEUTSCHE TELEKOM AG        | $27.66 | 1.81 | 12% | $38.65 | +40% |  |
| 261 | KOTAKBANK.NS | KOTAK MAHINDRA BANK LTD | $377.45 | 19.4 | 17% | $526.17 | +39% |  |
| 262 | PDD | PDD Holdings Inc. | $85.07 | 9.53 | 0% | $118.35 | +39% |  |
| 263 | FCX | Freeport-McMoRan, Inc. | $63.37 | 1.89 | 30% | $87.15 | +38% |  |
| 264 | 0762.HK | CHINA UNICOM | $7.37 | 0.79 | 1% | $10.13 | +38% |  |
| 265 | ZTS | Zoetis Inc. | $79.44 | 6.1 | 8% | $109.16 | +37% |  |
| 266 | 1299.HK | AIA | $74.0 | 4.63 | 12% | $101.56 | +37% |  |
| 267 | IBN | ICICI Bank Limited | $25.95 | 1.55 | 13% | $35.4 | +36% |  |
| 268 | FRE.DE | Fresenius SE & Co. KGaA    | $37.26 | 2.68 | 9% | $50.79 | +36% |  |
| 269 | NMR | Nomura Holdings Inc | $8.41 | 0.74 | 4% | $11.45 | +36% |  |
| 270 | MS | Morgan Stanley | $211.93 | 11.04 | 16% | $288.45 | +36% |  |
| 271 | INTU | Intuit Inc. | $296.76 | 16.38 | 15% | $403.83 | +36% |  |
| 272 | GSK | GSK plc | $51.52 | 3.82 | 8% | $69.86 | +36% |  |
| 273 | MRK | Merck & Company, Inc. | $120.79 | 3.55 | 30% | $163.69 | +36% |  |
| 274 | 1120.SR | Al Rajhi Bank | $66.45 | 4.02 | 12% | $89.96 | +35% |  |
| 275 | CABK.MC | CAIXABANK, S.A. | $11.49 | 0.81 | 9% | $15.5 | +35% |  |
| 276 | AFL | AFLAC Incorporated | $118.24 | 8.75 | 8% | $159.51 | +35% |  |
| 277 | MET | MetLife, Inc. | $84.49 | 5.17 | 12% | $113.5 | +34% |  |
| 278 | HSY | The Hershey Company | $184.58 | 5.37 | 30% | $247.6 | +34% |  |
| 279 | 2882.TW | CATHAY FINANCIAL HLDG CO | $100.0 | 7.06 | 9% | $133.57 | +34% |  |
| 280 | GS | Goldman Sachs Group, Inc.  | $1038.68 | 54.74 | 15% | $1386.42 | +34% |  |
| 281 | NXPI | NXP Semiconductors N.V. | $295.96 | 10.45 | 25% | $395.08 | +34% |  |
| 282 | MPLX | MPLX LP | $56.48 | 4.62 | 6% | $75.41 | +34% |  |
| 283 | NTES | NetEase, Inc. | $119.48 | 7.82 | 10% | $159.12 | +33% |  |
| 284 | BP | BP p.l.c. | $42.97 | 1.24 | 30% | $57.17 | +33% |  |
| 285 | ICE | Intercontinental Exchange  | $141.5 | 6.88 | 17% | $188.28 | +33% |  |
| 286 | G.MI | GENERALI | $38.81 | 2.69 | 9% | $51.53 | +33% |  |
| 287 | ICTEF | International Container Te | $14.39 | 0.54 | 23% | $19.11 | +33% |  |
| 288 | MFC | Manulife Financial Corpora | $38.71 | 2.5 | 10% | $51.24 | +32% |  |
| 289 | EPD | Enterprise Products Partne | $37.81 | 2.7 | 8% | $50.02 | +32% |  |
| 290 | NA.TO | NATIONAL BANK OF CANADA | $204.35 | 11.3 | 14% | $269.83 | +32% |  |
| 291 | MBG.DE | Mercedes-Benz Group AG     | $47.99 | 5.09 | 0% | $63.21 | +32% |  |
| 292 | ABEV | Ambev S.A. | $3.12 | 0.2 | 11% | $4.11 | +32% |  |
| 293 | VIK | Viking Holdings Ltd | $89.94 | 2.69 | 29% | $118.46 | +32% |  |
| 294 | HEI.DE | Heidelberg Materials AG    | $179.25 | 11.17 | 11% | $235.32 | +31% |  |
| 295 | NGG | National Grid Transco, PLC | $81.86 | 4.4 | 14% | $107.07 | +31% |  |
| 296 | FITB | Fifth Third Bancorp | $52.01 | 2.97 | 13% | $68.01 | +31% |  |
| 297 | SPG | Simon Property Group, Inc. | $210.31 | 14.39 | 9% | $274.83 | +31% |  |
| 298 | BUD | Anheuser-Busch Inbev SA Sp | $78.5 | 3.61 | 18% | $102.17 | +30% |  |
| 299 | 1024.HK | KUAISHOU-W | $46.86 | 4.9 | 0% | $60.85 | +30% |  |
| 300 | SGO.PA | SAINT GOBAIN | $77.26 | 5.78 | 7% | $100.2 | +30% |  |
| 301 | TSM | Taiwan Semiconductor Manuf | $415.17 | 11.67 | 30% | $538.09 | +30% |  |
| 302 | 0857.HK | PETROCHINA | $10.55 | 1.0 | 2% | $13.64 | +29% |  |
| 303 | 2802.T | AJINOMOTO CO INC | $4942.0 | 138.38 | 30% | $6380.53 | +29% |  |
| 304 | POWERGRID.NS | POWER GRID CORP. LTD. | $285.65 | 20.11 | 8% | $368.13 | +29% |  |
| 305 | LDO.MI | LEONARDO | $51.86 | 2.24 | 19% | $66.63 | +28% |  |
| 306 | BKNG | Booking Holdings Inc. Comm | $165.84 | 7.58 | 18% | $212.54 | +28% |  |
| 307 | 0941.HK | CHINA MOBILE | $82.4 | 7.29 | 3% | $105.36 | +28% |  |
| 308 | FICO | Fair Isaac Corporation | $1137.33 | 31.5 | 30% | $1452.43 | +28% |  |
| 309 | 601138.SS | FOXCONN INDUSTRIAL INTERNE | $74.06 | 2.05 | 30% | $94.52 | +28% |  |
| 310 | 7011.T | MITSUBISHI HEAVY INDUSTRIE | $3790.0 | 104.6 | 30% | $4822.98 | +27% |  |
| 311 | 6971.T | KYOCERA CORP | $3720.0 | 102.67 | 30% | $4733.99 | +27% |  |
| 312 | AXP | American Express Company | $310.66 | 16.03 | 14% | $391.77 | +26% |  |
| 313 | STT | State Street Corporation | $161.75 | 9.85 | 11% | $203.35 | +26% |  |
| 314 | WRB | W.R. Berkley Corporation | $68.57 | 4.72 | 8% | $85.97 | +25% |  |
| 315 | BTI | British American Tobacco   | $59.72 | 4.69 | 5% | $74.67 | +25% |  |
| 316 | FTI | TechnipFMC plc | $66.82 | 2.61 | 21% | $83.51 | +25% |  |
| 317 | PUB.PA | PUBLICIS GROUPE SA | $87.44 | 6.52 | 6% | $109.12 | +25% |  |
| 318 | DIS | Walt Disney Company (The) | $99.71 | 6.25 | 10% | $123.59 | +24% |  |
| 319 | UI | Ubiquiti Inc. | $567.33 | 15.54 | 30% | $702.86 | +24% |  |
| 320 | BAJFINANCE.NS | BAJAJ FINANCE LIMITED | $889.4 | 30.51 | 24% | $1096.05 | +23% |  |
| 321 | NVO | Novo Nordisk A/S | $42.96 | 4.26 | 0% | $52.9 | +23% |  |
| 322 | 600690.SS | HAIER SMART HOME CO LTD | $20.31 | 2.01 | 0% | $24.96 | +23% |  |
| 323 | UCB.VI | UCB | $262.8 | 8.04 | 26% | $320.88 | +22% |  |
| 324 | RY | Royal Bank Of Canada | $194.04 | 11.06 | 12% | $236.8 | +22% |  |
| 325 | AON | Aon plc | $328.53 | 18.23 | 12% | $400.04 | +22% |  |
| 326 | DNB.OL | DNB BANK ASA | $284.4 | 27.87 | 0% | $346.1 | +22% |  |
| 327 | NDA-FI.HE | Nordea Bank Abp | $16.13 | 1.36 | 3% | $19.62 | +22% |  |
| 328 | AM.PA | DASSAULT AVIATION | $297.8 | 12.51 | 18% | $360.56 | +21% |  |
| 329 | PST.MI | POSTE ITALIANE | $25.75 | 1.88 | 6% | $31.15 | +21% |  |
| 330 | ACN | Accenture plc | $178.25 | 12.19 | 7% | $214.71 | +20% |  |
| 331 | 2388.HK | BOC HONG KONG | $47.38 | 3.8 | 4% | $57.06 | +20% |  |
| 332 | PKO.WA | PKOBP | $98.29 | 8.59 | 2% | $118.36 | +20% |  |
| 333 | PCAR | PACCAR Inc. | $116.68 | 4.7 | 19% | $140.4 | +20% |  |
| 334 | DG.PA | VINCI | $124.25 | 8.65 | 7% | $149.26 | +20% |  |
| 335 | PGR | Progressive Corporation (T | $204.02 | 19.67 | 0% | $244.27 | +20% |  |
| 336 | FDX | FedEx Corporation | $331.0 | 18.73 | 11% | $393.71 | +19% |  |
| 337 | GWO.TO | GREAT-WEST LIFECO INC | $81.87 | 4.65 | 11% | $96.91 | +18% |  |
| 338 | 0016.HK | SHK PPT | $120.9 | 7.59 | 9% | $143.17 | +18% |  |
| 339 | OTIS | Otis Worldwide Corporation | $70.34 | 3.76 | 12% | $83.17 | +18% |  |
| 340 | DEWA.AE | DUBAI ELECTRICITY | $2.61 | 0.17 | 8% | $3.08 | +18% |  |
| 341 | POW.TO | POWER CORPORATION OF CANAD | $83.97 | 4.16 | 14% | $98.9 | +18% |  |
| 342 | MCK | McKesson Corporation | $775.66 | 38.4 | 14% | $905.75 | +17% |  |
| 343 | ARGX | argenx SE | $891.32 | 22.55 | 30% | $1039.75 | +17% |  |
| 344 | DXCM | DexCom, Inc. | $72.86 | 2.33 | 24% | $85.03 | +17% |  |
| 345 | LVS | Las Vegas Sands Corp. | $50.25 | 2.71 | 12% | $58.55 | +16% |  |
| 346 | M&M.NS | MAHINDRA & MAHINDRA LTD | $3040.5 | 152.33 | 13% | $3524.06 | +16% |  |
| 347 | SBIN.NS | STATE BANK OF INDIA | $977.7 | 91.12 | 0% | $1131.57 | +16% |  |
| 348 | RWE.DE | RWE AG                     | $56.0 | 3.26 | 10% | $64.7 | +16% |  |
| 349 | SHB-A.ST | Svenska Handelsbanken ser. | $134.6 | 12.14 | 1% | $155.34 | +15% |  |
| 350 | 6762.T | TDK CORP | $4111.0 | 102.78 | 30% | $4739.06 | +15% |  |
| 351 | PRU | Prudential Financial, Inc. | $104.62 | 9.71 | 0% | $120.58 | +15% |  |
| 352 | LLY | Eli Lilly and Company | $1131.42 | 28.17 | 30% | $1298.88 | +15% |  |
| 353 | OKE | ONEOK, Inc. | $88.25 | 5.61 | 8% | $101.23 | +15% |  |
| 354 | BHARTIARTL.NS | BHARTI AIRTEL LIMITED | $1798.2 | 44.42 | 30% | $2048.15 | +14% |  |
| 355 | LNG | Cheniere Energy, Inc. | $238.82 | 5.9 | 30% | $272.04 | +14% |  |
| 356 | SEB-A.ST | Skandinaviska Enskilda Ban | $185.2 | 15.37 | 2% | $210.53 | +14% |  |
| 357 | TD | Toronto Dominion Bank (The | $113.16 | 6.13 | 11% | $128.39 | +14% |  |
| 358 | ADVANC.BK | ADVANC_ADVANCED INFO SERVI | $361.0 | 17.08 | 14% | $409.29 | +13% |  |
| 359 | EC | Ecopetrol S.A. | $15.15 | 1.38 | 0% | $17.14 | +13% |  |
| 360 | MU | Micron Technology, Inc. | $864.01 | 21.17 | 30% | $976.12 | +13% |  |
| 361 | DANS.VI | DANSKE BANK AS | $44.1 | 3.74 | 1% | $49.79 | +13% |  |
| 362 | DHL.DE | DEUTSCHE POST AG           | $52.16 | 3.09 | 9% | $58.85 | +13% |  |
| 363 | BPE.MI | BPER BANCA | $11.67 | 1.05 | 0% | $13.04 | +12% |  |
| 364 | ES | Eversource Energy (D/B/A) | $70.6 | 4.67 | 6% | $78.71 | +12% |  |
| 365 | 1605.T | INPEX CORPORATION | $3685.0 | 330.54 | 0% | $4104.79 | +11% |  |
| 366 | AENA.MC | AENA, S.M.E., S.A. | $24.92 | 1.44 | 9% | $27.74 | +11% |  |
| 367 | BSBR | Banco Santander Brasil SA | $5.24 | 0.32 | 8% | $5.83 | +11% |  |
| 368 | KKR | KKR & Co. Inc. | $93.4 | 2.94 | 23% | $103.77 | +11% |  |
| 369 | ADANIENT.NS | ADANI ENTERPRISES LIMITED | $3048.2 | 73.46 | 30% | $3387.15 | +11% |  |
| 370 | 0001.HK | CKH HOLDINGS | $68.2 | 3.09 | 15% | $75.75 | +11% |  |
| 371 | KMI | Kinder Morgan, Inc. | $31.68 | 1.49 | 14% | $35.11 | +11% |  |
| 372 | 0728.HK | CHINA TELECOM | $4.99 | 0.42 | 1% | $5.52 | +11% |  |
| 373 | CSL.AX | CSL FPO [CSL] | $97.91 | 8.65 | 0% | $107.42 | +10% |  |
| 374 | TCS.NS | TATA CONSULTANCY SERV LT | $2198.9 | 136.11 | 7% | $2409.72 | +10% |  |
| 375 | 0669.HK | TECHTRONIC IND | $117.0 | 5.12 | 15% | $128.22 | +10% |  |
| 376 | TAK | Takeda Pharmaceutical Comp | $15.6 | 0.37 | 30% | $17.06 | +9% |  |
| 377 | ELE.MC | ENDESA,S.A. | $36.75 | 2.25 | 8% | $40.17 | +9% |  |
| 378 | O39.SI | OCBC Bank | $23.94 | 1.65 | 5% | $26.04 | +9% |  |
| 379 | SPOT | Spotify Technology S.A. | $496.95 | 14.96 | 24% | $539.82 | +9% |  |
| 380 | AMAT | Applied Materials, Inc. | $453.01 | 10.65 | 30% | $491.06 | +8% |  |
| 381 | RMD | ResMed Inc. | $196.04 | 10.37 | 10% | $212.16 | +8% |  |
| 382 | 2891.TW | CTBC FINANCIAL HOLDINGS CO | $66.6 | 4.06 | 7% | $71.88 | +8% |  |
| 383 | GEHC | GE HealthCare Technologies | $64.67 | 4.17 | 6% | $69.79 | +8% |  |
| 384 | TPR | Tapestry, Inc. | $140.1 | 3.28 | 30% | $151.24 | +8% |  |
| 385 | HLN | Haleon plc | $9.12 | 0.5 | 10% | $9.82 | +8% |  |
| 386 | ATO | Atmos Energy Corporation | $170.24 | 8.12 | 13% | $183.25 | +8% |  |
| 387 | VALE | VALE S.A. | $15.23 | 0.66 | 15% | $16.38 | +8% |  |
| 388 | AD.AS | KONINKLIJKE AHOLD DELHAIZE | $35.85 | 2.52 | 4% | $38.55 | +8% |  |
| 389 | 9432.T | NTT INC | $146.0 | 12.61 | 0% | $156.6 | +7% |  |
| 390 | ASM.AS | ASM International N.V. | $867.0 | 20.11 | 30% | $927.25 | +7% |  |
| 391 | HDB | HDFC Bank Limited | $23.41 | 1.4 | 8% | $24.96 | +7% |  |
| 392 | TS | Tenaris S.A. | $61.44 | 3.8 | 7% | $65.48 | +7% |  |
| 393 | CRM | Salesforce, Inc. | $185.66 | 8.63 | 13% | $197.46 | +6% |  |
| 394 | TGT | Target Corporation | $122.57 | 7.57 | 7% | $130.26 | +6% |  |
| 395 | NOC | Northrop Grumman Corporati | $544.4 | 31.9 | 8% | $578.31 | +6% |  |
| 396 | IFC.TO | INTACT FINANCIAL CORPORATI | $275.92 | 18.79 | 5% | $292.46 | +6% |  |
| 397 | AMT | American Tower Corporation | $194.12 | 6.19 | 22% | $205.22 | +6% |  |
| 398 | HEN3.DE | Henkel AG & Co. KGaA       | $67.1 | 4.92 | 3% | $70.9 | +6% |  |
| 399 | SE | Sea Limited | $86.56 | 2.54 | 24% | $91.43 | +6% |  |
| 400 | CNQ | Canadian Natural Resources | $45.7 | 3.88 | 0% | $48.18 | +5% |  |
| 401 | CBRE | CBRE Group Inc | $130.93 | 4.39 | 20% | $137.36 | +5% |  |
| 402 | NTPC.NS | NTPC LTD | $361.65 | 30.45 | 0% | $378.14 | +5% |  |
| 403 | JCI | Johnson Controls Internati | $143.65 | 3.28 | 30% | $150.13 | +4% |  |
| 404 | SWED-A.ST | Swedbank AB ser A | $336.1 | 28.23 | 0% | $350.57 | +4% |  |
| 405 | PEG | Public Service Enterprise  | $79.48 | 4.52 | 8% | $82.7 | +4% |  |
| 406 | MO | Altria Group, Inc. | $72.19 | 4.79 | 5% | $75.09 | +4% |  |
| 407 | ADYEN.AS | ADYEN | $817.4 | 33.6 | 15% | $846.95 | +4% |  |
| 408 | HCLTECH.NS | HCL TECHNOLOGIES LTD | $1154.7 | 61.31 | 9% | $1193.12 | +3% |  |
| 409 | META | Meta Platforms, Inc. | $593.0 | 27.52 | 12% | $609.86 | +3% |  |
| 410 | CLS | Celestica, Inc. | $371.71 | 8.25 | 30% | $380.4 | +2% |  |
| 411 | 4519.T | CHUGAI PHARMACEUTICAL CO | $7554.0 | 263.63 | 19% | $7714.63 | +2% |  |
| 412 | INFY | Infosys Limited | $12.4 | 0.8 | 5% | $12.65 | +2% |  |
| 413 | BSX | Boston Scientific Corporat | $48.55 | 2.39 | 11% | $49.43 | +2% |  |
| 414 | AMZN | Amazon.com, Inc. | $246.03 | 7.77 | 21% | $249.76 | +2% |  |
| 415 | BRK-B | Berkshire Hathaway Inc. Ne | $488.13 | 33.58 | 4% | $495.04 | +1% |  |
| 416 | CSX | CSX Corporation | $46.99 | 1.63 | 19% | $47.66 | +1% |  |
| 417 | CCEP | Coca-Cola Europacific Part | $94.74 | 4.94 | 9% | $96.09 | +1% |  |
| 418 | 002475.SZ | LUXSHARE PRECISION INDUSTR | $68.77 | 2.33 | 19% | $69.63 | +1% |  |
| 419 | AMS.MC | AMADEUS IT GROUP, S.A. | $53.68 | 3.05 | 8% | $54.38 | +1% |  |
| 420 | COR | Cencora, Inc. | $275.04 | 13.04 | 11% | $277.82 | +1% |  |
| 421 | DB1.DE | DEUTSCHE BOERSE AG         | $245.9 | 11.21 | 12% | $247.53 | +1% |  |
| 422 | DVN | Devon Energy Corporation | $44.28 | 3.59 | 0% | $44.58 | +1% |  |
| 423 | HPE | Hewlett Packard Enterprise | $49.2 | 1.07 | 30% | $49.34 | +0% |  |
| 424 | 000725.SZ | BOE TECHNOLOGY GROUP | $6.43 | 0.17 | 25% | $6.44 | +0% |  |
| 425 | KBCSF | KBC Group SA | $127.05 | 10.1 | 0% | $126.69 | -0% |  |
| 426 | 4901.T | FUJIFILM HOLDINGS CORPORAT | $3528.0 | 224.73 | 5% | $3511.24 | -0% |  |
| 427 | REGN | Regeneron Pharmaceuticals, | $635.45 | 40.99 | 4% | $630.41 | -1% |  |
| 428 | ZM | Zoom Communications, Inc. | $101.62 | 6.79 | 4% | $100.83 | -1% |  |
| 429 | PHG | Koninklijke Philips N.V. N | $26.11 | 1.16 | 12% | $25.84 | -1% |  |
| 430 | CRH | CRH PLC | $105.06 | 5.39 | 9% | $103.77 | -1% |  |
| 431 | FTAI | FTAI Aviation Ltd. | $234.05 | 5.01 | 30% | $231.0 | -1% |  |
| 432 | AMRZ | Amrize Ltd | $53.58 | 2.09 | 15% | $52.82 | -1% |  |
| 433 | AZN | AstraZeneca PLC | $185.95 | 6.64 | 17% | $183.04 | -2% |  |
| 434 | ED | Consolidated Edison, Inc. | $106.26 | 5.93 | 7% | $104.45 | -2% |  |
| 435 | SLHN.SW | SWISS LIFE HOLDING AG N | $841.0 | 43.48 | 9% | $824.71 | -2% |  |
| 436 | BAJAJFINSV.NS | BAJAJ FINSERV LTD. | $1703.2 | 60.97 | 17% | $1668.55 | -2% |  |
| 437 | RIO | Rio Tinto Plc | $100.69 | 6.08 | 5% | $98.21 | -2% |  |
| 438 | MLYBY | Malayan Banking Berhad | $5.51 | 0.43 | 0% | $5.34 | -3% |  |
| 439 | CAT | Caterpillar, Inc. | $904.28 | 20.08 | 28% | $875.03 | -3% |  |
| 440 | 8035.T | TOKYO ELECTRON | $59450.0 | 1248.45 | 30% | $57564.47 | -3% |  |
| 441 | STZ | Constellation Brands, Inc. | $140.91 | 9.61 | 3% | $136.25 | -3% |  |
| 442 | BLK | BlackRock, Inc. | $995.6 | 39.72 | 14% | $956.83 | -4% |  |
| 443 | ULTRACEMCO.NS | ULTRATECH CEMENT LIMITED | $10912.0 | 277.16 | 25% | $10478.63 | -4% |  |
| 444 | ADSK | Autodesk, Inc. | $229.96 | 6.85 | 21% | $220.09 | -4% |  |
| 445 | NTGY.MC | NATURGY ENERGY GROUP, S.A. | $28.94 | 2.22 | 0% | $27.57 | -5% |  |
| 446 | KVUE | Kenvue Inc. | $17.71 | 0.84 | 10% | $16.84 | -5% |  |
| 447 | ROP | Roper Technologies, Inc. | $332.18 | 16.01 | 10% | $316.0 | -5% |  |
| 448 | APP | Applovin Corporation | $557.2 | 11.48 | 30% | $529.33 | -5% |  |
| 449 | RELX | RELX PLC PLC | $35.15 | 1.5 | 12% | $33.37 | -5% |  |
| 450 | ADP | Automatic Data Processing, | $231.95 | 10.72 | 10% | $219.32 | -5% |  |
| 451 | TXN | Texas Instruments Incorpor | $285.06 | 5.84 | 30% | $269.28 | -6% |  |
| 452 | WBC.AX | WESTPAC FPO [WBC] | $34.81 | 2.03 | 5% | $32.79 | -6% |  |
| 453 | 300274.SZ | SUNGROW POWER SUPPLY CO LT | $153.75 | 5.8 | 15% | $144.37 | -6% |  |
| 454 | ADANIPOWER.NS | ADANI POWER LTD | $232.6 | 6.63 | 22% | $218.09 | -6% |  |
| 455 | PPG | PPG Industries, Inc. | $113.8 | 6.98 | 4% | $106.48 | -6% |  |
| 456 | LT.NS | LARSEN & TOUBRO LTD. | $3953.2 | 117.01 | 20% | $3697.82 | -6% |  |
| 457 | ATD.TO | ALIMENTATION COUCHE-TARD I | $82.6 | 4.01 | 9% | $77.22 | -6% |  |
| 458 | SAP | SAP  SE | $184.77 | 7.24 | 14% | $172.58 | -7% |  |
| 459 | 4503.T | ASTELLAS PHARMA | $2161.0 | 162.29 | 0% | $2015.39 | -7% |  |
| 460 | 0066.HK | MTR CORPORATION | $31.46 | 2.36 | 0% | $29.31 | -7% |  |
| 461 | ABNB | Airbnb, Inc. | $133.54 | 4.05 | 20% | $124.32 | -7% |  |
| 462 | DLR | Digital Realty Trust, Inc. | $186.79 | 3.77 | 30% | $173.83 | -7% |  |
| 463 | AEE | Ameren Corporation | $109.27 | 5.56 | 8% | $101.69 | -7% |  |
| 464 | RDDT | Reddit, Inc. | $173.45 | 3.5 | 30% | $161.38 | -7% |  |
| 465 | FERG | Ferguson Enterprises Inc. | $229.58 | 10.17 | 11% | $213.29 | -7% |  |
| 466 | ASSA-B.ST | ASSA ABLOY AB ser. B | $326.8 | 14.22 | 11% | $302.69 | -7% |  |
| 467 | 5803.T | FUJIKURA | $4747.0 | 94.94 | 30% | $4377.56 | -8% |  |
| 468 | ORCL | Oracle Corporation | $213.68 | 5.58 | 23% | $195.96 | -8% |  |
| 469 | 7010.SR | Saudi Telecom Co. | $43.42 | 2.99 | 1% | $39.8 | -8% |  |
| 470 | APH | Amphenol Corporation | $138.81 | 3.48 | 24% | $127.21 | -8% |  |
| 471 | 8766.T | TOKIO MARINE HOLDINGS INC | $6996.0 | 515.61 | 0% | $6403.06 | -8% |  |
| 472 | MA | Mastercard Incorporated | $491.08 | 17.29 | 16% | $448.65 | -9% |  |
| 473 | DUK | Duke Energy Corporation (H | $124.22 | 6.5 | 7% | $112.79 | -9% |  |
| 474 | DHI | D.R. Horton, Inc. | $145.6 | 10.64 | 0% | $132.13 | -9% |  |
| 475 | IQV | IQVIA Holdings, Inc. | $183.45 | 8.05 | 11% | $166.41 | -9% |  |
| 476 | 9983.T | FAST RETAILING CO LTD | $78700.0 | 1558.26 | 30% | $71298.43 | -9% |  |
| 477 | 6861.T | KEYENCE CORP | $78070.0 | 1834.65 | 25% | $70649.24 | -10% |  |
| 478 | CRS | Carpenter Technology Corpo | $483.6 | 9.48 | 30% | $437.11 | -10% |  |
| 479 | D05.SI | DBS | $63.78 | 3.83 | 4% | $57.58 | -10% |  |
| 480 | HEIA.AS | HEINEKEN | $66.74 | 3.38 | 8% | $60.26 | -10% |  |
| 481 | KDP | Keurig Dr Pepper Inc. | $30.53 | 1.35 | 10% | $27.57 | -10% |  |
| 482 | ASELS.IS | ASELSAN | $363.0 | 7.11 | 30% | $327.83 | -10% |  |
| 483 | SIKA.SW | SIKA N | $149.35 | 6.5 | 11% | $134.55 | -10% |  |
| 484 | AEP | American Electric Power Co | $129.14 | 6.75 | 7% | $115.93 | -10% |  |
| 485 | 8750.T | DAIICHI LIFE GROUP INC | $1662.5 | 119.87 | 0% | $1488.6 | -10% |  |
| 486 | YUM | Yum! Brands, Inc. | $150.87 | 6.2 | 12% | $134.84 | -11% |  |
| 487 | BAS.DE | BASF SE                    | $50.98 | 1.7 | 17% | $45.5 | -11% |  |
| 488 | BAJAJ-AUTO.NS | BAJAJ AUTO LIMITED | $10342.0 | 384.72 | 14% | $9239.31 | -11% |  |
| 489 | CME | CME Group Inc. | $257.4 | 11.71 | 10% | $229.66 | -11% |  |
| 490 | NEE | NextEra Energy, Inc. | $85.84 | 3.94 | 9% | $76.43 | -11% |  |
| 491 | J36.SI | JMH USD | $62.72 | 3.77 | 4% | $55.62 | -11% |  |
| 492 | ACS.MC | ACS,ACTIVIDADES DE CONSTRU | $125.9 | 3.81 | 19% | $111.49 | -11% |  |
| 493 | 6857.T | ADVANTEST CORP | $26765.0 | 513.89 | 30% | $23694.82 | -12% |  |
| 494 | BMY | Bristol-Myers Squibb Compa | $57.27 | 3.57 | 3% | $50.43 | -12% |  |
| 495 | ASX | ASE Technology Holding Co. | $34.03 | 0.65 | 30% | $29.97 | -12% |  |
| 496 | GD | General Dynamics Corporati | $346.44 | 15.9 | 9% | $304.92 | -12% |  |

### 🔴 BEARISH — 496 most overvalued (price most above Brandon-intrinsic)
| # | Ticker | Name | Price | TTM EPS | Growth g | Intrinsic | Under/Over % | Flag |
|--:|--------|------|------:|--------:|---------:|----------:|-------------:|------|
| 1 | VIE.PA | VEOLIA ENVIRON. | $34.88 | 1.7 | 8% | $30.7 | -12% |  |
| 2 | 9633.HK | NONGFU SPRING | $42.18 | 1.63 | 13% | $36.9 | -12% |  |
| 3 | 002594.SZ | BYD COMPANY LIMITED | $93.01 | 1.95 | 27% | $81.08 | -13% |  |
| 4 | NDAQ | Nasdaq, Inc. | $87.28 | 3.32 | 13% | $76.13 | -13% |  |
| 5 | ROST | Ross Stores, Inc. | $230.37 | 7.16 | 18% | $200.08 | -13% |  |
| 6 | SNDK | Sandisk Corporation | $1559.32 | 29.32 | 30% | $1351.91 | -13% |  |
| 7 | FIX | Comfort Systems USA, Inc. | $1843.94 | 34.67 | 30% | $1598.59 | -13% |  |
| 8 | KEYS | Keysight Technologies Inc. | $329.83 | 6.2 | 30% | $285.87 | -13% |  |
| 9 | 2345.TW | ACCTON TECHNOLOGY CORP | $2490.0 | 46.81 | 30% | $2158.35 | -13% |  |
| 10 | XYZ | Block, Inc. | $68.15 | 1.28 | 30% | $59.02 | -13% |  |
| 11 | PAYX | Paychex, Inc. | $100.53 | 4.53 | 9% | $86.95 | -14% |  |
| 12 | HM-B.ST | Hennes & Mauritz AB, H & M | $166.3 | 7.67 | 9% | $143.88 | -14% |  |
| 13 | EXC | Exelon Corporation | $45.75 | 2.73 | 3% | $39.47 | -14% |  |
| 14 | V | Visa Inc. | $323.57 | 11.45 | 14% | $278.49 | -14% |  |
| 15 | SPGI | S&P Global Inc. | $424.44 | 15.79 | 13% | $364.33 | -14% |  |
| 16 | RHM.F | RHEINMETALL AG             | $1197.2 | 22.27 | 30% | $1026.84 | -14% |  |
| 17 | TMUS | T-Mobile US, Inc. | $178.1 | 9.4 | 6% | $152.64 | -14% |  |
| 18 | SNY | Sanofi | $45.02 | 2.3 | 6% | $38.55 | -14% |  |
| 19 | TRI | Thomson Reuters Corp | $86.04 | 3.48 | 11% | $73.55 | -14% |  |
| 20 | JBL | Jabil Inc. | $353.24 | 7.42 | 27% | $301.45 | -15% |  |
| 21 | QSR | Restaurant Brands Internat | $72.66 | 3.11 | 10% | $61.95 | -15% |  |
| 22 | HO.PA | THALES | $232.4 | 8.13 | 14% | $198.09 | -15% |  |
| 23 | 8001.T | ITOCHU CORP | $1873.5 | 127.96 | 0% | $1589.06 | -15% |  |
| 24 | JBHT | J.B. Hunt Transport Servic | $284.95 | 6.44 | 25% | $240.96 | -15% |  |
| 25 | LONN.SW | LONZA N | $485.6 | 13.01 | 20% | $409.45 | -16% |  |
| 26 | EME | EMCOR Group, Inc. | $817.44 | 29.75 | 13% | $688.25 | -16% |  |
| 27 | CTRA | Coterra Energy Inc. | $32.56 | 2.17 | 0% | $27.41 | -16% |  |
| 28 | AZO | AutoZone, Inc. | $3116.43 | 145.54 | 8% | $2618.95 | -16% |  |
| 29 | 8801.T | MITSUI FUDOSAN | $1495.0 | 101.06 | 0% | $1255.01 | -16% |  |
| 30 | SLF | Sun Life Financial Inc. | $73.72 | 3.86 | 5% | $61.68 | -16% |  |
| 31 | NAB.AX | NAT. BANK FPO [NAB] | $36.59 | 2.0 | 4% | $30.57 | -16% |  |
| 32 | MDT | Medtronic plc. | $81.67 | 3.73 | 8% | $68.09 | -17% |  |
| 33 | VRTX | Vertex Pharmaceuticals Inc | $446.83 | 16.85 | 12% | $371.25 | -17% |  |
| 34 | ANZ.AX | ANZ GROUP FPO [ANZ] | $34.12 | 1.97 | 3% | $28.35 | -17% |  |
| 35 | MUFG | Mitsubishi UFJ Financial G | $19.91 | 1.33 | 0% | $16.52 | -17% |  |
| 36 | MRSH | Marsh | $165.44 | 8.01 | 7% | $137.25 | -17% |  |
| 37 | RO.SW | ROCHE I | $332.2 | 16.05 | 7% | $275.01 | -17% |  |
| 38 | GRMN | Garmin Ltd. | $236.57 | 8.97 | 12% | $195.61 | -17% |  |
| 39 | WDS | Woodside Energy Group Limi | $21.33 | 1.42 | 0% | $17.63 | -17% |  |
| 40 | SMFG | Sumitomo Mitsui Financial  | $23.16 | 1.54 | 0% | $19.12 | -17% |  |
| 41 | MARUTI.NS | MARUTI SUZUKI INDIA LTD. | $13050.0 | 467.19 | 13% | $10755.76 | -18% |  |
| 42 | 003816.SZ | CGN POWER CO LTD | $4.33 | 0.19 | 9% | $3.57 | -18% |  |
| 43 | CQP | Cheniere Energy Partners,  | $64.47 | 4.28 | 0% | $53.15 | -18% |  |
| 44 | CASY | Caseys General Stores, Inc | $761.91 | 17.44 | 24% | $626.52 | -18% |  |
| 45 | PPL | PPL Corporation | $35.74 | 1.63 | 8% | $29.37 | -18% |  |
| 46 | IX | ORIX Corporation | $37.88 | 2.5 | 0% | $31.05 | -18% |  |
| 47 | COIN | Coinbase Global, Inc. | $152.4 | 2.71 | 30% | $124.95 | -18% |  |
| 48 | AWK | American Water Works Compa | $124.47 | 5.64 | 8% | $102.1 | -18% |  |
| 49 | UL | Unilever PLC | $56.72 | 3.01 | 4% | $46.3 | -18% |  |
| 50 | ABBN.SW | ABB LTD N | $83.1 | 2.1 | 21% | $67.61 | -19% |  |
| 51 | CPG.L | COMPASS GROUP PLC ORD 11 1 | $32.81 | 1.19 | 13% | $26.7 | -19% |  |
| 52 | UNP | Union Pacific Corporation | $272.32 | 12.15 | 8% | $221.19 | -19% |  |
| 53 | XIACF | Xiaomi Corp. | $3.53 | 0.23 | 0% | $2.86 | -19% |  |
| 54 | XEL | Xcel Energy Inc. | $79.04 | 3.47 | 8% | $63.93 | -19% |  |
| 55 | VMC | Vulcan Materials Company ( | $281.38 | 8.44 | 17% | $226.38 | -20% |  |
| 56 | EBAY | eBay Inc. | $109.35 | 4.33 | 10% | $87.87 | -20% |  |
| 57 | 601898.SS | CHINA COAL ENERGY COMPANY | $16.84 | 1.09 | 0% | $13.54 | -20% |  |
| 58 | LRCX | Lam Research Corporation | $303.28 | 5.28 | 30% | $243.45 | -20% |  |
| 59 | KNEBV.HE | KONE Corporation | $50.34 | 1.89 | 12% | $40.39 | -20% |  |
| 60 | HINDALCO.NS | HINDALCO  INDUSTRIES  LTD | $1092.6 | 60.2 | 3% | $876.81 | -20% |  |
| 61 | D | Dominion Energy, Inc. | $66.9 | 3.39 | 5% | $53.58 | -20% |  |
| 62 | LR.PA | LEGRAND | $144.0 | 4.85 | 14% | $114.95 | -20% |  |
| 63 | MLM | Martin Marietta Materials, | $575.83 | 15.95 | 18% | $458.35 | -20% |  |
| 64 | 3382.T | SEVEN & I HOLDINGS CO LTD | $1863.5 | 118.89 | 0% | $1476.43 | -21% |  |
| 65 | ERIC | Ericsson | $12.56 | 0.8 | 0% | $9.93 | -21% |  |
| 66 | SRG.MI | SNAM | $6.3 | 0.36 | 2% | $4.98 | -21% |  |
| 67 | CFR.SW | RICHEMONT N | $164.65 | 5.4 | 14% | $129.91 | -21% |  |
| 68 | HWM | Howmet Aerospace Inc. | $251.9 | 4.31 | 30% | $198.73 | -21% |  |
| 69 | ETR | Entergy Corporation | $110.74 | 3.92 | 12% | $87.3 | -21% |  |
| 70 | NTAP | NetApp, Inc. | $167.04 | 6.35 | 11% | $131.63 | -21% |  |
| 71 | FOX | Fox Corporation | $59.88 | 3.8 | 0% | $47.19 | -21% |  |
| 72 | PLD | Prologis, Inc. | $144.54 | 3.97 | 18% | $113.8 | -21% |  |
| 73 | ET | Energy Transfer LP | $19.39 | 1.2 | 0% | $15.25 | -21% |  |
| 74 | URI | United Rentals, Inc. | $1067.77 | 39.08 | 12% | $836.74 | -22% |  |
| 75 | RELIANCE.NS | RELIANCE INDUSTRIES LTD | $1291.0 | 59.64 | 6% | $1011.4 | -22% |  |
| 76 | ITW | Illinois Tool Works Inc. | $252.72 | 10.77 | 8% | $197.16 | -22% |  |
| 77 | WMMVF | Wal-Mart De Mexico S.A.B.  | $2.9 | 0.17 | 1% | $2.26 | -22% |  |
| 78 | WEC | WEC Energy Group, Inc. | $112.95 | 4.99 | 7% | $88.06 | -22% |  |
| 79 | HOT.F | HOCHTIEF AG                | $492.4 | 10.69 | 24% | $381.71 | -22% |  |
| 80 | DSY.PA | DASSAULT SYSTEMES | $19.71 | 0.92 | 6% | $15.2 | -23% |  |
| 81 | ADI | Analog Devices, Inc. | $401.39 | 6.7 | 30% | $308.93 | -23% |  |
| 82 | AVB | AvalonBay Communities, Inc | $189.72 | 8.06 | 8% | $145.17 | -24% |  |
| 83 | 9434.T | SOFTBANK CORP. | $211.7 | 11.26 | 3% | $161.56 | -24% |  |
| 84 | ROK | Rockwell Automation, Inc. | $446.71 | 9.65 | 23% | $340.82 | -24% |  |
| 85 | BG | Bunge Limited | $126.46 | 3.79 | 15% | $96.45 | -24% |  |
| 86 | ASML | ASML Holding N.V. - New Yo | $1641.74 | 30.04 | 27% | $1250.55 | -24% |  |
| 87 | 6301.T | KOMATSU | $6739.0 | 413.77 | 0% | $5138.37 | -24% |  |
| 88 | 2327.TW | YAGEO CORP | $769.0 | 12.69 | 30% | $585.12 | -24% |  |
| 89 | KO | Coca-Cola Company (The) | $79.48 | 3.18 | 9% | $60.4 | -24% |  |
| 90 | LOW | Lowe's Companies, Inc. | $210.74 | 11.82 | 2% | $160.24 | -24% |  |
| 91 | CP | Canadian Pacific Kansas Ci | $89.93 | 3.23 | 11% | $68.35 | -24% |  |
| 92 | PEP | Pepsico, Inc. | $141.92 | 6.37 | 6% | $107.67 | -24% |  |
| 93 | TMO | Thermo Fisher Scientific I | $472.8 | 18.2 | 10% | $358.57 | -24% |  |
| 94 | ENR.F | Siemens Energy AG          | $154.66 | 2.54 | 30% | $117.12 | -24% |  |
| 95 | CSU.TO | CONSTELLATION SOFTWARE INC | $2969.32 | 48.7 | 30% | $2245.5 | -24% |  |
| 96 | ONC | BeOne Medicines Ltd. | $270.1 | 4.43 | 30% | $204.26 | -24% |  |
| 97 | SAAB-B.ST | SAAB AB ser. B | $528.4 | 11.99 | 22% | $398.16 | -25% |  |
| 98 | CMI | Cummins Inc. | $651.22 | 19.28 | 15% | $490.01 | -25% |  |
| 99 | AJG | Arthur J. Gallagher & Co. | $216.14 | 6.18 | 16% | $162.59 | -25% |  |
| 100 | PM | Philip Morris Internationa | $178.29 | 7.1 | 9% | $133.93 | -25% |  |
| 101 | MCD | McDonald's Corporation | $279.84 | 12.12 | 7% | $210.12 | -25% |  |
| 102 | IHG | Intercontinental Hotels Gr | $162.15 | 4.86 | 15% | $121.18 | -25% |  |
| 103 | UNH | UnitedHealth Group Incorpo | $399.47 | 13.26 | 12% | $296.34 | -26% |  |
| 104 | AAPL | Apple Inc. | $307.34 | 8.27 | 17% | $227.78 | -26% |  |
| 105 | SU.PA | SCHNEIDER ELECTRIC SE | $269.05 | 7.96 | 15% | $199.17 | -26% |  |
| 106 | ENGI.PA | ENGIE | $26.94 | 1.51 | 1% | $19.93 | -26% |  |
| 107 | SUNPHARMA.NS | SUN PHARMACEUTICAL IND L | $1782.2 | 47.76 | 17% | $1318.23 | -26% |  |
| 108 | WMB | Williams Companies, Inc. ( | $71.96 | 2.28 | 13% | $53.19 | -26% |  |
| 109 | 300476.SZ | VICTORY GIANT TECHNOLOGY ( | $338.9 | 5.42 | 30% | $249.91 | -26% |  |
| 110 | XYL | Xylem Inc. | $109.94 | 4.02 | 10% | $81.06 | -26% |  |
| 111 | HBAN.SW | HELVETIA BALOISE HOLDING N | $198.1 | 10.32 | 2% | $145.0 | -27% |  |
| 112 | ITC.NS | ITC LTD | $280.7 | 16.51 | 0% | $205.03 | -27% |  |
| 113 | GWW | W.W. Grainger, Inc. | $1300.01 | 37.18 | 15% | $946.99 | -27% |  |
| 114 | IBM | International Business Mac | $284.84 | 11.31 | 8% | $206.66 | -27% |  |
| 115 | CPRT | Copart, Inc. | $30.96 | 1.61 | 2% | $22.4 | -28% |  |
| 116 | MTZ | MasTec, Inc. | $363.89 | 5.71 | 30% | $263.28 | -28% |  |
| 117 | WSM | Williams-Sonoma, Inc. | $204.98 | 8.92 | 6% | $148.03 | -28% |  |
| 118 | AVGO | Broadcom Inc. | $385.73 | 6.02 | 30% | $277.57 | -28% |  |
| 119 | BAM | Brookfield Asset Managemen | $46.18 | 1.56 | 11% | $33.22 | -28% |  |
| 120 | 601211.SS | GUOTAI HAITONG SECURITIES  | $16.25 | 0.94 | 0% | $11.67 | -28% |  |
| 121 | 8031.T | MITSUI & CO | $5039.0 | 290.75 | 0% | $3610.66 | -28% |  |
| 122 | FE | FirstEnergy Corp. | $46.42 | 1.84 | 8% | $33.26 | -28% |  |
| 123 | 300760.SZ | SHENZHEN MINDRAY BIO-MEDIC | $144.39 | 6.47 | 5% | $103.58 | -28% |  |
| 124 | ORLY | O'Reilly Automotive, Inc. | $90.33 | 3.07 | 11% | $64.47 | -29% |  |
| 125 | L.TO | LOBLAW CO | $65.53 | 2.21 | 11% | $46.73 | -29% |  |
| 126 | TLS.AX | TELSTRA FPO [TLS] | $4.97 | 0.2 | 7% | $3.54 | -29% |  |
| 127 | VEEV | Veeva Systems Inc. | $172.61 | 5.64 | 12% | $122.72 | -29% |  |
| 128 | CNP | CenterPoint Energy, Inc (H | $42.69 | 1.63 | 8% | $30.35 | -29% |  |
| 129 | HUBB | Hubbell Inc | $476.82 | 16.93 | 10% | $339.06 | -29% |  |
| 130 | WM | Waste Management, Inc. | $220.4 | 6.92 | 13% | $156.31 | -29% |  |
| 131 | SO | Southern Company (The) | $92.6 | 3.91 | 6% | $65.56 | -29% |  |
| 132 | CEZ.PR | CEZ | $1258.0 | 53.84 | 6% | $890.54 | -29% |  |
| 133 | UPS | United Parcel Service, Inc | $108.54 | 6.18 | 0% | $76.75 | -29% |  |
| 134 | 600111.SS | CHINA NTHN RARE EARTH (GP) | $49.66 | 0.76 | 30% | $35.04 | -29% |  |
| 135 | 600519.SS | KWEICHOW MOUTAI | $1272.86 | 66.06 | 2% | $896.9 | -30% |  |
| 136 | ELV | Elevance Health, Inc. | $415.53 | 23.6 | 0% | $293.07 | -30% |  |
| 137 | DOV | Dover Corporation | $214.76 | 8.01 | 9% | $151.44 | -30% |  |
| 138 | FLEX | Flex Ltd. | $151.92 | 2.32 | 30% | $106.97 | -30% |  |
| 139 | LMT | Lockheed Martin Corporatio | $523.76 | 20.64 | 7% | $367.12 | -30% |  |
| 140 | A | Agilent Technologies, Inc. | $135.44 | 4.98 | 9% | $94.98 | -30% |  |
| 141 | 4568.T | DAIICHI SANKYO COMPANY LIM | $2490.0 | 140.44 | 0% | $1744.04 | -30% |  |
| 142 | ATI | ATI Inc. | $177.47 | 3.03 | 27% | $123.83 | -30% |  |
| 143 | ITX.MC | INDUSTRIA DE DISE...O TEXT | $55.0 | 2.0 | 9% | $38.34 | -30% |  |
| 144 | CDI.PA | CHRISTIAN DIOR | $447.8 | 25.12 | 0% | $311.95 | -30% |  |
| 145 | TER | Teradyne, Inc. | $357.93 | 5.4 | 30% | $248.99 | -30% |  |
| 146 | MSCI | MSCI Inc. | $615.46 | 17.54 | 14% | $427.74 | -30% |  |
| 147 | BIP | Brookfield Infrastructure  | $38.8 | 0.66 | 27% | $26.82 | -31% |  |
| 148 | WRT1V.HE | Wärtsilä Corporation | $35.58 | 1.1 | 12% | $24.54 | -31% |  |
| 149 | TT | Trane Technologies plc | $456.84 | 13.11 | 14% | $314.71 | -31% |  |
| 150 | 300124.SZ | SHENZHEN INOVANCE TECHNOLO | $75.08 | 1.73 | 19% | $51.74 | -31% |  |
| 151 | 300433.SZ | LENS TECHNOLOGY CO LTD | $45.61 | 0.68 | 30% | $31.35 | -31% |  |
| 152 | PSX | Phillips 66 | $183.08 | 10.12 | 0% | $125.67 | -31% |  |
| 153 | SCMN.SW | SWISSCOM N | $649.0 | 23.88 | 8% | $445.3 | -31% |  |
| 154 | IBE.MC | ACCIONES IBERDROLA | $19.85 | 0.8 | 6% | $13.53 | -32% |  |
| 155 | MDLZ | Mondelez International, In | $62.04 | 2.02 | 11% | $42.0 | -32% |  |
| 156 | MQG.AX | MACQ GROUP FPO [MQG] | $236.42 | 9.71 | 6% | $159.85 | -32% |  |
| 157 | 8015.T | TOYOTA TSUSHO CORP | $6456.0 | 351.21 | 0% | $4361.48 | -32% |  |
| 158 | IBKR | Interactive Brokers Group, | $84.4 | 2.33 | 14% | $56.92 | -33% |  |
| 159 | SHL.DE | Siemens Healthineers AG    | $34.84 | 1.89 | 0% | $23.47 | -33% |  |
| 160 | SYY | Sysco Corporation | $76.29 | 3.6 | 3% | $51.4 | -33% |  |
| 161 | CAH | Cardinal Health, Inc. | $205.71 | 6.54 | 11% | $138.28 | -33% |  |
| 162 | RPRX | Royalty Pharma plc | $55.87 | 1.9 | 10% | $37.48 | -33% |  |
| 163 | 0388.HK | HKEX | $396.4 | 14.86 | 8% | $265.42 | -33% |  |
| 164 | DEO | Diageo plc | $80.43 | 4.33 | 0% | $53.77 | -33% |  |
| 165 | AI.PA | AIR LIQUIDE | $183.4 | 6.09 | 10% | $122.35 | -33% |  |
| 166 | 8308.T | RESONA HOLDINGS | $2118.0 | 113.74 | 0% | $1412.47 | -33% |  |
| 167 | ABT | Abbott Laboratories | $91.07 | 3.57 | 6% | $60.66 | -33% |  |
| 168 | KMB | Kimberly-Clark Corporation | $99.04 | 5.17 | 0% | $65.86 | -34% |  |
| 169 | WAB | Westinghouse Air Brake Tec | $260.4 | 7.08 | 14% | $172.96 | -34% |  |
| 170 | PG | Procter & Gamble Company ( | $146.54 | 6.84 | 3% | $97.14 | -34% |  |
| 171 | 601088.SS | CHINA SHENHUA ENERGY COMPA | $48.52 | 2.59 | 0% | $32.16 | -34% |  |
| 172 | WES.AX | WESFARMER FPO [WES] | $78.93 | 2.7 | 9% | $52.3 | -34% |  |
| 173 | MCO | Moody's Corporation | $451.35 | 13.95 | 11% | $296.68 | -34% |  |
| 174 | JNJ | Johnson & Johnson | $232.77 | 8.64 | 7% | $152.4 | -34% |  |
| 175 | DTE | DTE Energy Company | $145.77 | 6.08 | 5% | $95.4 | -35% |  |
| 176 | TDY | Teledyne Technologies Inco | $602.27 | 19.75 | 10% | $392.85 | -35% |  |
| 177 | ANET | Arista Networks, Inc. | $154.27 | 2.92 | 23% | $100.44 | -35% |  |
| 178 | TJX | TJX Companies, Inc. (The) | $160.71 | 5.14 | 10% | $104.68 | -35% |  |
| 179 | CNI | Canadian National Railway  | $120.38 | 5.47 | 3% | $78.1 | -35% |  |
| 180 | ARES | Ares Management Corporatio | $125.65 | 2.17 | 25% | $81.58 | -35% |  |
| 181 | GM | General Motors Company | $82.11 | 2.74 | 9% | $53.01 | -35% |  |
| 182 | UMG.AS | UNIVERSAL MUSIC GROUP | $18.15 | 0.83 | 2% | $11.68 | -36% |  |
| 183 | ADANIPORTS.NS | ADANI PORT & SEZ LTD | $1824.2 | 58.19 | 10% | $1165.39 | -36% |  |
| 184 | 600031.SS | SANY HEAVY INDUSTRY CO | $18.65 | 0.96 | 0% | $11.92 | -36% |  |
| 185 | 600487.SS | HENGTONG OPTIC-ELECTRIC CO | $96.12 | 1.33 | 30% | $61.32 | -36% |  |
| 186 | APD | Air Products and Chemicals | $282.35 | 9.49 | 9% | $179.55 | -36% |  |
| 187 | SCHN.SW | SCHINDLER N | $255.5 | 9.53 | 6% | $162.15 | -36% |  |
| 188 | AMGN | Amgen Inc. | $349.58 | 14.37 | 4% | $221.32 | -37% |  |
| 189 | KNIN.SW | KUEHNE+NAGEL INT N | $191.85 | 7.02 | 7% | $121.25 | -37% |  |
| 190 | GULF.BK | GULF_GULF DEVELOPMENT | $67.0 | 1.86 | 13% | $42.13 | -37% |  |
| 191 | DTG.F | Daimler Truck Holding AG   | $40.75 | 1.57 | 6% | $25.58 | -37% |  |
| 192 | 300502.SZ | EOPTOLINK TECHNOLOGY INC L | $748.0 | 10.17 | 30% | $468.93 | -37% |  |
| 193 | EMR | Emerson Electric Company | $138.12 | 4.32 | 10% | $86.4 | -37% |  |
| 194 | PFE | Pfizer, Inc. | $26.04 | 1.31 | 0% | $16.27 | -38% |  |
| 195 | COP | ConocoPhillips | $117.14 | 5.9 | 0% | $73.27 | -38% |  |
| 196 | WDAY | Workday, Inc. | $144.28 | 3.2 | 18% | $90.11 | -38% |  |
| 197 | VOLV-A.ST | Volvo, AB ser. A | $322.2 | 16.17 | 0% | $200.81 | -38% |  |
| 198 | SAND.ST | Sandvik AB | $379.8 | 11.81 | 10% | $236.74 | -38% |  |
| 199 | VRSN | VeriSign, Inc. | $294.92 | 9.05 | 10% | $183.15 | -38% |  |
| 200 | 0019.HK | SWIRE PACIFIC A | $83.3 | 2.11 | 14% | $51.55 | -38% |  |
| 201 | SDZ.SW | SANDOZ GROUP N | $64.4 | 1.66 | 14% | $39.83 | -38% |  |
| 202 | HD | Home Depot, Inc. (The) | $310.78 | 14.08 | 2% | $191.73 | -38% |  |
| 203 | ILMN | Illumina, Inc. | $162.32 | 5.5 | 8% | $100.17 | -38% |  |
| 204 | SRE | DBA Sempra | $91.42 | 2.94 | 9% | $56.3 | -38% |  |
| 205 | BN.PA | DANONE | $64.42 | 2.82 | 2% | $39.68 | -38% |  |
| 206 | MMM | 3M Company | $153.76 | 5.2 | 8% | $94.44 | -39% |  |
| 207 | EPI-A.ST | Epiroc AB ser. A | $273.2 | 7.05 | 14% | $167.68 | -39% |  |
| 208 | XPO | XPO, Inc. | $218.94 | 2.91 | 30% | $134.18 | -39% |  |
| 209 | MC.PA | LVMH | $479.05 | 21.84 | 2% | $292.47 | -39% |  |
| 210 | HEI | Heico Corporation | $331.43 | 5.6 | 24% | $202.56 | -39% |  |
| 211 | ECL | Ecolab Inc. | $257.97 | 7.38 | 11% | $157.23 | -39% |  |
| 212 | TKO | TKO Group Holdings, Inc. | $203.49 | 2.69 | 30% | $124.03 | -39% |  |
| 213 | GE | GE Aerospace | $328.0 | 8.04 | 15% | $199.86 | -39% |  |
| 214 | SYK | Stryker Corporation | $305.66 | 8.65 | 12% | $186.29 | -39% |  |
| 215 | VRT | Vertiv Holdings, LLC | $300.51 | 3.97 | 30% | $183.05 | -39% |  |
| 216 | 6981.T | MURATA MANUFACTURING CO | $9695.0 | 127.97 | 30% | $5900.54 | -39% |  |
| 217 | SHW | Sherwin-Williams Company ( | $305.3 | 10.41 | 8% | $185.59 | -39% |  |
| 218 | GIVN.SW | GIVAUDAN N | $2869.0 | 115.33 | 4% | $1744.19 | -39% |  |
| 219 | SONY | Sony Group Corporation | $21.89 | 1.07 | 0% | $13.29 | -39% |  |
| 220 | ALNY | Alnylam Pharmaceuticals, I | $303.05 | 3.97 | 30% | $183.05 | -40% |  |
| 221 | ENEL.MI | ENEL | $9.64 | 0.38 | 4% | $5.79 | -40% |  |
| 222 | 600276.SS | JIANGSU HENGRUI PHARMACEUT | $47.08 | 1.22 | 13% | $28.29 | -40% |  |
| 223 | LISP.SW | LINDT PS | $9255.0 | 313.74 | 7% | $5549.35 | -40% |  |
| 224 | OXY | Occidental Petroleum Corpo | $56.93 | 0.74 | 30% | $34.12 | -40% |  |
| 225 | FTS | Fortis Inc. | $55.9 | 2.44 | 2% | $33.41 | -40% |  |
| 226 | NVT | nVent Electric plc | $162.86 | 2.95 | 22% | $97.44 | -40% |  |
| 227 | CBA.AX | CWLTH BANK FPO [CBA] | $160.9 | 6.21 | 4% | $96.1 | -40% |  |
| 228 | 6702.T | FUJITSU | $3591.0 | 172.73 | 0% | $2145.03 | -40% |  |
| 229 | H.TO | HYDRO ONE LIMITED | $56.97 | 2.28 | 4% | $33.94 | -40% |  |
| 230 | 285A.T | KIOXIA HOLDINGS CORPORATIO | $78140.0 | 1008.01 | 30% | $46478.08 | -40% |  |
| 231 | RSG | Republic Services, Inc. | $210.04 | 6.97 | 8% | $124.26 | -41% |  |
| 232 | 002371.SZ | NAURA TECHNOLOGY GROUP CO  | $603.36 | 7.72 | 30% | $355.96 | -41% |  |
| 233 | LIN | Linde plc | $507.9 | 15.08 | 10% | $299.0 | -41% |  |
| 234 | 1211.SR | Saudi Arabian Mining Co. | $62.3 | 2.28 | 5% | $36.55 | -41% |  |
| 235 | PH | Parker-Hannifin Corporatio | $882.34 | 27.09 | 9% | $517.14 | -41% |  |
| 236 | STRL | Sterling Infrastructure, I | $882.43 | 11.21 | 30% | $516.88 | -41% |  |
| 237 | RTX | RTX Corporation | $180.99 | 5.32 | 10% | $105.82 | -42% |  |
| 238 | Q | Qnity Electronics, Inc. | $142.05 | 3.1 | 16% | $82.69 | -42% |  |
| 239 | 603288.SS | FOSHAN HAITIAN FLAVOURING  | $34.03 | 1.25 | 5% | $19.81 | -42% |  |
| 240 | NVS | Novartis AG | $149.16 | 6.98 | 0% | $86.68 | -42% |  |
| 241 | MSI | Motorola Solutions, Inc. | $410.34 | 12.39 | 9% | $238.15 | -42% |  |
| 242 | GALD.SW | GALDERMA GROUP N | $161.5 | 2.03 | 30% | $93.6 | -42% |  |
| 243 | BX | Blackstone Inc. | $115.35 | 3.9 | 7% | $66.61 | -42% |  |
| 244 | MNST | Monster Beverage Corporati | $89.55 | 2.07 | 15% | $51.7 | -42% |  |
| 245 | HAL.NS | HINDUSTAN AERONAUTICS LTD | $4216.9 | 136.21 | 8% | $2431.78 | -42% |  |
| 246 | LHX | L3Harris Technologies, Inc | $307.83 | 9.2 | 9% | $176.51 | -43% |  |
| 247 | AME | AMETEK, Inc. | $226.55 | 6.62 | 10% | $129.71 | -43% |  |
| 248 | STX | Seagate Technology Holding | $847.47 | 10.51 | 30% | $484.6 | -43% |  |
| 249 | FAST | Fastenal Company | $46.79 | 1.13 | 14% | $26.78 | -43% |  |
| 250 | ADM | Archer-Daniels-Midland Com | $80.92 | 2.24 | 11% | $46.12 | -43% |  |
| 251 | ALC | Alcon Inc. | $66.81 | 1.67 | 13% | $38.01 | -43% |  |
| 252 | 8802.T | MITSUBISHI ESTATE CO | $3980.0 | 181.89 | 0% | $2258.79 | -43% |  |
| 253 | CVNA | Carvana Co. | $66.51 | 1.73 | 12% | $37.69 | -43% |  |
| 254 | O | Realty Income Corporation | $60.84 | 1.22 | 18% | $34.51 | -43% |  |
| 255 | NESN.SW | NESTLE N | $76.96 | 3.51 | 0% | $43.59 | -43% |  |
| 256 | WN.TO | WESTON GEORGE | $103.47 | 2.7 | 12% | $58.46 | -44% |  |
| 257 | RACE | Ferrari N.V. | $346.99 | 10.44 | 8% | $194.5 | -44% |  |
| 258 | E | ENI S.p.A. | $53.8 | 2.31 | 1% | $30.15 | -44% |  |
| 259 | TDG | Transdigm Group Incorporat | $1238.74 | 32.08 | 12% | $686.55 | -45% |  |
| 260 | 601985.SS | CHINA NATIONAL NUCLEAR POW | $8.99 | 0.4 | 0% | $4.97 | -45% |  |
| 261 | IDXX | IDEXX Laboratories, Inc. | $562.16 | 13.6 | 13% | $310.21 | -45% |  |
| 262 | SBUX | Starbucks Corporation | $95.29 | 1.31 | 26% | $52.55 | -45% |  |
| 263 | 6367.T | DAIKIN INDUSTRIES | $23700.0 | 938.52 | 2% | $13058.35 | -45% |  |
| 264 | MAR | Marriott International | $392.51 | 9.54 | 13% | $215.68 | -45% |  |
| 265 | CTAS | Cintas Corporation | $179.85 | 4.75 | 11% | $98.59 | -45% |  |
| 266 | WMT | Walmart Inc. | $118.88 | 2.84 | 13% | $65.07 | -45% |  |
| 267 | CSCO | Cisco Systems, Inc. | $121.64 | 3.0 | 12% | $66.42 | -45% |  |
| 268 | CHT | Chunghwa Telecom Co., Ltd. | $44.56 | 1.59 | 4% | $24.3 | -46% |  |
| 269 | 600183.SS | SHENGYI TECHNOLOGY CO LTD | $137.36 | 1.62 | 30% | $74.7 | -46% |  |
| 270 | GLW | Corning Incorporated | $177.58 | 2.08 | 30% | $95.91 | -46% |  |
| 271 | OR.PA | L'OREAL | $375.5 | 11.45 | 7% | $202.24 | -46% |  |
| 272 | BA | Boeing Company (The) | $215.45 | 2.52 | 30% | $116.19 | -46% |  |
| 273 | TPL | Texas Pacific Land Corpora | $389.79 | 7.29 | 18% | $209.76 | -46% |  |
| 274 | CVS | CVS Health Corporation | $95.93 | 2.28 | 13% | $51.39 | -46% |  |
| 275 | QCOM | QUALCOMM Incorporated | $215.94 | 9.31 | 0% | $115.62 | -46% |  |
| 276 | AIR.PA | AIRBUS SE | $178.96 | 6.34 | 4% | $95.7 | -46% |  |
| 277 | ON | ON Semiconductor Corporati | $117.26 | 1.36 | 30% | $62.71 | -46% |  |
| 278 | GMG.AX | GOOD GROUP STAPLED [GMG] | $31.1 | 0.84 | 10% | $16.56 | -47% |  |
| 279 | BEL.NS | BHARAT ELECTRONICS LTD | $408.2 | 8.29 | 16% | $217.72 | -47% |  |
| 280 | 4062.T | IBIDEN CO LTD | $18760.0 | 215.74 | 30% | $9947.5 | -47% |  |
| 281 | ETN | Eaton Corporation, PLC | $395.94 | 10.22 | 10% | $209.28 | -47% |  |
| 282 | EL.PA | ESSILORLUXOTTICA | $174.05 | 4.98 | 8% | $92.05 | -47% |  |
| 283 | TRP | TC Energy Corporation | $68.68 | 2.44 | 4% | $36.3 | -47% |  |
| 284 | MRK.DE | MERCK KGAA                 | $136.85 | 5.83 | 0% | $72.4 | -47% |  |
| 285 | BN | Brookfield Corporation | $44.6 | 0.51 | 30% | $23.52 | -47% |  |
| 286 | 300308.SZ | ZHONGJI INNOLIGHT CO LTD | $1179.99 | 13.45 | 30% | $620.16 | -47% |  |
| 287 | NBIS | Nebius Group N.V. | $227.81 | 2.6 | 30% | $119.88 | -47% |  |
| 288 | HON | Honeywell International In | $213.97 | 6.27 | 8% | $112.36 | -48% |  |
| 289 | ISRG | Intuitive Surgical, Inc. | $422.06 | 8.23 | 17% | $220.65 | -48% |  |
| 290 | CTVA | Corteva, Inc. | $77.03 | 1.85 | 12% | $40.31 | -48% |  |
| 291 | PBA | Pembina Pipeline Corp. | $48.82 | 1.91 | 1% | $25.34 | -48% |  |
| 292 | DHR | Danaher Corporation | $184.3 | 5.16 | 8% | $94.98 | -48% |  |
| 293 | SLB | SLB Limited | $54.87 | 2.27 | 0% | $28.19 | -49% |  |
| 294 | 300408.SZ | CHAOZHOU THREE-CIRCLE (GRO | $134.83 | 1.5 | 30% | $69.16 | -49% |  |
| 295 | MRVL | Marvell Technology, Inc. | $263.47 | 2.9 | 30% | $133.72 | -49% |  |
| 296 | ESLT | Elbit Systems Ltd. | $823.36 | 12.35 | 22% | $418.6 | -49% |  |
| 297 | 7741.T | HOYA CORP | $26340.0 | 742.79 | 8% | $13242.65 | -50% |  |
| 298 | AOT.BK | AOT_AIRPORTS OF THAILAND | $58.0 | 1.27 | 13% | $29.19 | -50% |  |
| 299 | DOL.TO | DOLLARAMA INC | $181.22 | 4.73 | 9% | $89.8 | -50% |  |
| 300 | PSA | Public Storage | $309.68 | 9.69 | 5% | $153.0 | -51% |  |
| 301 | 2360.TW | CHROMA ATE INC | $2565.0 | 27.45 | 30% | $1265.69 | -51% |  |
| 302 | XOM | Exxon Mobil Corporation | $149.92 | 5.94 | 0% | $73.77 | -51% |  |
| 303 | IFX.DE | INFINEON TECHNOLOGIES AG   | $77.3 | 0.82 | 30% | $37.81 | -51% |  |
| 304 | 6954.T | FANUC CORPORATION | $7648.0 | 178.2 | 11% | $3728.97 | -51% |  |
| 305 | HLT | Hilton Worldwide Holdings  | $343.1 | 6.55 | 16% | $167.12 | -51% |  |
| 306 | CCI | Crown Castle Inc. | $94.49 | 2.37 | 9% | $45.95 | -51% |  |
| 307 | PWR | Quanta Services, Inc. | $695.11 | 7.3 | 30% | $336.59 | -52% |  |
| 308 | MAERSK-B.CO | A.P. Møller - Mærsk B A/S | $17815.0 | 694.79 | 0% | $8628.2 | -52% |  |
| 309 | 688012.SS | ADVANCED MICRO-FABRICATION | $276.0 | 2.9 | 30% | $133.72 | -52% |  |
| 310 | CCJ | Cameco Corporation | $103.44 | 1.08 | 30% | $49.8 | -52% |  |
| 311 | NHY.OL | NORSK HYDRO | $116.05 | 3.12 | 8% | $55.78 | -52% |  |
| 312 | NSC | Norfolk Southern Corporati | $313.45 | 11.88 | 0% | $147.53 | -53% |  |
| 313 | EW | Edwards Lifesciences Corpo | $85.96 | 1.85 | 12% | $40.45 | -53% |  |
| 314 | BDX | Becton, Dickinson and Comp | $151.16 | 5.73 | 0% | $71.16 | -53% |  |
| 315 | WAT | Waters Corporation | $365.36 | 7.86 | 12% | $172.1 | -53% |  |
| 316 | 002050.SZ | ZHEJIANG SANHUA INTELLIGEN | $47.51 | 1.01 | 12% | $22.37 | -53% |  |
| 317 | ENB | Enbridge Inc | $56.31 | 2.12 | 0% | $26.33 | -53% |  |
| 318 | COST | Costco Wholesale Corporati | $971.87 | 19.92 | 13% | $452.96 | -53% |  |
| 319 | NZYM.VI | NOVOZYMES AS | $49.07 | 1.28 | 8% | $22.82 | -54% |  |
| 320 | CW | Curtiss-Wright Corporation | $733.14 | 13.64 | 15% | $340.25 | -54% |  |
| 321 | P911.DE | Dr. Ing. h.c. F. Porsche A | $46.86 | 0.47 | 30% | $21.67 | -54% |  |
| 322 | 2308.TW | DELTA ELECTRONIC | $2300.0 | 23.0 | 30% | $1060.5 | -54% |  |
| 323 | WELL | Welltower Inc. | $206.93 | 2.07 | 30% | $95.45 | -54% |  |
| 324 | CMG | Chipotle Mexican Grill, In | $29.34 | 1.09 | 0% | $13.54 | -54% |  |
| 325 | TCL.AX | TRANSURBAN STAPLED [TCL] | $15.08 | 0.15 | 30% | $6.92 | -54% |  |
| 326 | HINDUNILVR.NS | HINDUSTAN UNILEVER LTD. | $2121.5 | 45.19 | 12% | $971.91 | -54% |  |
| 327 | TITAN.NS | TITAN COMPANY LIMITED | $4260.2 | 57.09 | 22% | $1947.75 | -54% |  |
| 328 | WCN | Waste Connections, Inc. | $155.22 | 4.1 | 7% | $70.95 | -54% |  |
| 329 | EQR | Equity Residential | $68.19 | 2.5 | 0% | $31.05 | -54% |  |
| 330 | EQT.ST | EQT AB | $294.1 | 6.73 | 10% | $131.99 | -55% |  |
| 331 | SIE.DE | SIEMENS AG                 | $268.8 | 9.68 | 0% | $120.21 | -55% |  |
| 332 | KR | Kroger Company (The) | $63.57 | 1.54 | 8% | $28.14 | -56% |  |
| 333 | NKE | Nike, Inc. | $42.98 | 1.52 | 0% | $18.88 | -56% |  |
| 334 | WEGE3.SA | WEG         ON      NM | $42.46 | 1.5 | 0% | $18.64 | -56% |  |
| 335 | FTNT | Fortinet, Inc. | $144.68 | 2.58 | 14% | $62.72 | -57% |  |
| 336 | IMO | Imperial Oil Limited | $121.72 | 4.25 | 0% | $52.78 | -57% |  |
| 337 | MPWR | Monolithic Power Systems,  | $1481.05 | 13.92 | 30% | $641.83 | -57% |  |
| 338 | 4063.T | SHIN-ETSU CHEMICAL CO | $7350.0 | 252.84 | 0% | $3139.87 | -57% |  |
| 339 | 0981.HK | SMIC | $75.65 | 0.7 | 30% | $32.28 | -57% |  |
| 340 | CL | Colgate-Palmolive Company | $88.58 | 2.58 | 3% | $37.67 | -58% |  |
| 341 | TSEM | Tower Semiconductor Ltd. | $235.48 | 2.16 | 30% | $99.59 | -58% |  |
| 342 | ODFL | Old Dominion Freight Line, | $242.57 | 4.78 | 12% | $102.34 | -58% |  |
| 343 | MDLN | Medline Inc. | $33.61 | 1.14 | 0% | $14.16 | -58% |  |
| 344 | ATCO-B.ST | Atlas Copco AB ser. B | $159.7 | 5.35 | 0% | $66.44 | -58% |  |
| 345 | NOW | ServiceNow, Inc. | $112.45 | 1.68 | 18% | $46.65 | -58% |  |
| 346 | 6501.T | HITACHI | $5300.0 | 176.49 | 0% | $2191.73 | -59% |  |
| 347 | EQIX | Equinix, Inc. | $1080.95 | 14.48 | 20% | $447.45 | -59% |  |
| 348 | GFS | GlobalFoundries Inc. | $75.53 | 1.48 | 11% | $31.25 | -59% |  |
| 349 | 000063.SZ | ZTE CORPORATION | $39.13 | 0.92 | 7% | $16.13 | -59% |  |
| 350 | 6503.T | MITSUBISHI ELECTRIC CORP | $6014.0 | 198.46 | 0% | $2464.56 | -59% |  |
| 351 | CARR | Carrier Global Corporation | $67.16 | 1.5 | 8% | $27.26 | -59% |  |
| 352 | CRDO | Credo Technology Group Hol | $206.89 | 1.82 | 30% | $83.92 | -59% |  |
| 353 | 603986.SS | GIGA DEVICE SEMICONDUCTOR  | $488.0 | 4.29 | 30% | $197.81 | -60% |  |
| 354 | ASIANPAINT.NS | ASIAN PAINTS LIMITED | $2686.7 | 45.14 | 14% | $1072.71 | -60% |  |
| 355 | KLAC | KLA Corporation | $1929.2 | 35.3 | 12% | $765.69 | -60% |  |
| 356 | RMS.PA | HERMES INTL | $1619.0 | 43.07 | 4% | $638.94 | -60% |  |
| 357 | FER.MC | FERROVIAL N.V. | $58.38 | 1.18 | 10% | $23.06 | -60% |  |
| 358 | SHOP | Shopify Inc. | $109.54 | 1.02 | 28% | $43.02 | -61% |  |
| 359 | EA | Electronic Arts Inc. | $203.0 | 3.51 | 13% | $79.07 | -61% |  |
| 360 | CVX | Chevron Corporation | $187.31 | 5.73 | 0% | $71.16 | -62% |  |
| 361 | EXR | Extra Space Storage Inc | $145.31 | 4.45 | 0% | $55.26 | -62% |  |
| 362 | DE | Deere & Company | $583.44 | 17.68 | 0% | $219.56 | -62% |  |
| 363 | MELI | MercadoLibre, Inc. | $1607.8 | 37.94 | 4% | $586.58 | -64% |  |
| 364 | HOOD | Robinhood Markets, Inc. | $82.47 | 2.06 | 3% | $29.23 | -65% |  |
| 365 | S63.SI | ST Engineering | $10.89 | 0.15 | 16% | $3.85 | -65% |  |
| 366 | IR | Ingersoll Rand Inc. | $72.25 | 1.48 | 6% | $25.18 | -65% |  |
| 367 | NESTLEIND.NS | NESTLE INDIA LIMITED | $1386.2 | 18.16 | 16% | $476.12 | -66% |  |
| 368 | DMART.NS | AVENUE SUPERMARTS LIMITED | $4144.2 | 45.59 | 20% | $1385.45 | -67% |  |
| 369 | HUM | Humana Inc. | $350.08 | 9.38 | 0% | $116.48 | -67% |  |
| 370 | 6146.T | DISCO CORPORATION | $72580.0 | 1248.38 | 9% | $23871.2 | -67% |  |
| 371 | NOK | Nokia Corporation Sponsore | $14.38 | 0.16 | 19% | $4.69 | -67% |  |
| 372 | CDNS | Cadence Design Systems, In | $376.19 | 4.29 | 18% | $121.88 | -68% |  |
| 373 | BESI.AS | BE Semiconductor Industrie | $271.4 | 1.9 | 30% | $87.61 | -68% |  |
| 374 | MTSI | MACOM Technology Solutions | $345.4 | 2.35 | 30% | $108.36 | -69% |  |
| 375 | DELTA.BK | DELTA_DELTA ELECTRONICS | $343.0 | 2.26 | 30% | $104.21 | -70% |  |
| 376 | LITE | Lumentum Holdings Inc. | $863.66 | 5.7 | 30% | $262.82 | -70% |  |
| 377 | PLTR | Palantir Technologies Inc. | $135.53 | 0.89 | 30% | $41.04 | -70% |  |
| 378 | AMD | Advanced Micro Devices, In | $466.38 | 2.98 | 30% | $137.4 | -70% |  |
| 379 | WOW.AX | WOOLWORTHS FPO [WOW] | $35.69 | 0.49 | 12% | $10.54 | -70% |  |
| 380 | ADANIGREEN.NS | ADANI GREEN ENERGY LTD | $1525.7 | 9.61 | 30% | $443.11 | -71% |  |
| 381 | APO | Apollo Global Management,  | $128.03 | 1.59 | 13% | $35.95 | -72% |  |
| 382 | CIEN | Ciena Corporation | $488.21 | 2.98 | 30% | $137.4 | -72% |  |
| 383 | 300394.SZ | SUZHOU TFC OPTICAL COMMUN  | $457.0 | 2.79 | 30% | $128.64 | -72% |  |
| 384 | DSV.VI | DSV AS | $215.4 | 4.76 | 0% | $59.11 | -73% |  |
| 385 | DASH | DoorDash, Inc. | $156.8 | 2.12 | 10% | $42.83 | -73% |  |
| 386 | 6752.T | PANASONIC HOLDINGS CORP | $3754.0 | 81.09 | 0% | $1007.01 | -73% |  |
| 387 | 2408.TW | NANYA TECHNOLOGY CORPORATI | $360.0 | 2.09 | 30% | $96.37 | -73% |  |
| 388 | COHR | Coherent Corp. | $376.99 | 2.11 | 30% | $97.29 | -74% |  |
| 389 | 1303.TW | NAN YA PLASTIC | $104.5 | 0.57 | 30% | $26.28 | -75% |  |
| 390 | AXON | Axon Enterprise, Inc. | $486.12 | 2.48 | 30% | $114.35 | -76% |  |
| 391 | SNPS | Synopsys, Inc. | $464.85 | 4.37 | 15% | $107.08 | -77% |  |
| 392 | COF | Capital One Financial Corp | $180.67 | 3.25 | 0% | $41.28 | -77% |  |
| 393 | HOLN.SW | HOLCIM N | $74.44 | 0.7 | 14% | $16.88 | -77% |  |
| 394 | ALAB | Astera Labs, Inc. | $317.06 | 1.49 | 30% | $68.7 | -78% |  |
| 395 | 3037.TW | UNIMICRON TECHNOLOGY | $933.0 | 4.39 | 30% | $202.42 | -78% |  |
| 396 | KOG.OL | KONGSBERG GRUPPEN | $312.0 | 5.43 | 0% | $67.43 | -78% |  |
| 397 | ABBV | AbbVie Inc. | $227.23 | 2.05 | 14% | $48.93 | -78% |  |
| 398 | 2454.TW | MEDIATEK INC | $4300.0 | 66.22 | 0% | $840.6 | -80% |  |
| 399 | VTR | Ventas, Inc. | $82.02 | 0.55 | 19% | $16.01 | -80% |  |
| 400 | ORA.PA | ORANGE | $17.43 | 0.12 | 17% | $3.28 | -81% |  |
| 401 | IRM | Iron Mountain Incorporated | $124.66 | 0.92 | 15% | $22.75 | -82% |  |
| 402 | 2082.SR | ACWA POWER Co. | $187.4 | 2.33 | 2% | $31.82 | -83% |  |
| 403 | NRG | NRG Energy, Inc. | $129.2 | 0.9 | 12% | $19.86 | -85% |  |
| 404 | 688256.SS | CAMBRICON TECHNOLOGIES COR | $1299.2 | 4.29 | 30% | $197.81 | -85% |  |
| 405 | EBK.DE | ENBW ENERGIE BAD.-WUE. ON | $70.6 | 0.7 | 0% | $8.69 | -88% |  |
| 406 | ARM | Arm Holdings plc | $342.93 | 0.86 | 30% | $39.65 | -88% |  |
| 407 | MCHP | Microchip Technology Incor | $88.34 | 0.22 | 30% | $10.14 | -88% |  |
| 408 | STM | STMicroelectronics N.V. | $70.72 | 0.16 | 30% | $7.38 | -90% |  |
| 409 | TSLA | Tesla, Inc. | $391.0 | 1.09 | 22% | $36.88 | -91% |  |
| 410 | PANW | Palo Alto Networks, Inc. | $272.05 | 1.14 | 11% | $23.75 | -91% |  |
| 411 | VIC.VN | VINGROUP JSC | $207000.0 | 1407.6 | 0% | $17480.18 | -92% |  |
| 412 | 1347.HK | HUA HONG SEMI | $145.3 | 0.25 | 30% | $11.53 | -92% |  |
| 413 | TWLO | Twilio Inc. | $225.99 | 0.66 | 17% | $17.67 | -92% |  |
| 414 | GLCNF | Glencore Plc | $7.91 | 0.03 | 8% | $0.55 | -93% |  |
| 415 | ETERNAL.NS | ETERNAL LIMITED | $256.5 | 0.38 | 30% | $17.52 | -93% |  |
| 416 | FANG | Diamondback Energy, Inc. | $192.62 | 0.98 | 0% | $12.17 | -94% |  |
| 417 | DDOG | Datadog, Inc. | $234.11 | 0.4 | 18% | $11.41 | -95% |  |
| 418 | CBRS | Cerebras Systems Inc. | $201.01 | 0.42 | 8% | $7.66 | -96% |  |
| 419 | III.L | 3I GROUP PLC ORD 73 19/22P | $2209.0 | 5.39 | 0% | $66.94 | -97% |  |
| 420 | STAN.L | STANDARD CHARTERED PLC ORD | $1933.0 | 1.54 | 22% | $50.93 | -97% |  |
| 421 | SBK.JO | Standard Bank Group Ltd | $30698.0 | 29.87 | 11% | $617.77 | -98% |  |
| 422 | FSR.JO | Firstrand Ltd | $9099.0 | 7.85 | 10% | $157.0 | -98% |  |
| 423 | RR.L | ROLLS-ROYCE HOLDINGS PLC O | $1260.0 | 0.69 | 17% | $18.63 | -98% |  |
| 424 | RKT.L | RECKITT BENCKISER GROUP PL | $4549.0 | 4.89 | 1% | $64.54 | -99% |  |
| 425 | IMB.L | IMPERIAL BRANDS PLC ORD 10 | $2761.0 | 2.13 | 7% | $37.38 | -99% |  |
| 426 | SSE.L | SSE PLC ORD 50P | $2400.0 | 1.05 | 20% | $31.92 | -99% |  |
| 427 | LUMI.TA | BK LEUMI LE ISRAEL | $6740.0 | 6.84 | 0% | $84.94 | -99% |  |
| 428 | POLI.TA | BANK HAPOALIM B.M. | $6872.0 | 7.21 | 0% | $89.54 | -99% |  |
| 429 | ANTO.L | ANTOFAGASTA PLC ORD 5P | $3970.0 | 1.0 | 30% | $46.11 | -99% |  |
| 430 | TSCO.L | TESCO PLC ORD 6 1/3P | $454.3 | 0.27 | 9% | $5.08 | -99% |  |
| 431 | CPI.JO | Capitec Bank Hldgs Ltd | $435208.0 | 145.36 | 19% | $4260.85 | -99% |  |
| 432 | BT-A.L | BT GROUP PLC ORD 5P | $201.5 | 0.11 | 6% | $1.82 | -99% |  |
| 433 | AV.L | AVIVA PLC ORD 32 17/19P | $603.2 | 0.26 | 12% | $5.63 | -99% |  |
| 434 | BA.L | BAE SYSTEMS PLC ORD 2.5P | $1930.5 | 0.68 | 10% | $13.85 | -99% |  |
| 435 | LSEG.L | LONDON STOCK EXCHANGE GROU | $9384.0 | 2.37 | 13% | $55.0 | -99% |  |
| 436 | KFH.KW | Kuwait Finance House | $775.0 | 0.03 | 10% | $0.6 | -100% |  |
| 437 | NBK.KW | National Bank of Kuwait | $826.0 | 0.06 | 0% | $0.75 | -100% |  |
| 438 | 005930.KS | SamsungElec | $329000.0 | None | — | — | no earnings | no_earnings |
| 439 | 000660.KS | SK hynix | $2070000.0 | None | — | — | no earnings | no_earnings |
| 440 | INTC | Intel Corporation | $99.17 | -0.6 | — | — | no earnings | no_earnings |
| 441 | CRWD | CrowdStrike Holdings, Inc. | $671.02 | -0.13 | — | — | no earnings | no_earnings |
| 442 | 005380.KS | HyundaiMtr | $700000.0 | None | — | — | no earnings | no_earnings |
| 443 | 402340.KS | SKSQUARE | $1258000.0 | None | — | — | no earnings | no_earnings |
| 444 | NET | Cloudflare, Inc. | $250.11 | -0.25 | — | — | no earnings | no_earnings |
| 445 | SNOW | Snowflake Inc. | $238.26 | -3.53 | — | — | no earnings | no_earnings |
| 446 | BE | Bloom Energy Corporation | $263.61 | -0.05 | — | — | no earnings | no_earnings |
| 447 | RKLB | Rocket Lab Corporation | $110.08 | -0.32 | — | — | no earnings | no_earnings |
| 448 | WBD | Warner Bros. Discovery, In | $26.24 | -0.7 | — | — | no earnings | no_earnings |
| 449 | 3690.HK | MEITUAN-W | $79.95 | -4.54 | — | — | no earnings | no_earnings |
| 450 | 373220.KS | LG Energy Solution | $414000.0 | None | — | — | no earnings | no_earnings |
| 451 | F | Ford Motor Company | $14.9 | -1.55 | — | — | no earnings | no_earnings |
| 452 | AAL.L | ANGLO AMERICAN PLC ORD USD | $3856.0 | -0.78 | — | — | no earnings | no_earnings |
| 453 | CRWV | CoreWeave, Inc. | $100.39 | -2.72 | — | — | no earnings | no_earnings |
| 454 | 6723.T | RENESAS ELECTRONICS CORP | $4568.0 | -28.78 | — | — | no earnings | no_earnings |
| 455 | 028260.KS | SAMSUNG C&T | $460500.0 | None | — | — | no earnings | no_earnings |
| 456 | 032830.KS | SAMSUNG LIFE | $412500.0 | None | — | — | no earnings | no_earnings |
| 457 | 329180.KS | HD HYUNDAI HEAVY INDUSTRIE | $664000.0 | None | — | — | no earnings | no_earnings |
| 458 | 2010.SR | Saudi Basic Industries Cor | $55.85 | -0.19 | — | — | no earnings | no_earnings |
| 459 | 688795.SS | MOORE THREADS TECH CO LTD | $633.97 | -2.16 | — | — | no earnings | no_earnings |
| 460 | MSTR | Strategy Inc | $120.44 | -36.99 | — | — | no earnings | no_earnings |
| 461 | BIDU | Baidu, Inc. | $121.66 | -0.16 | — | — | no earnings | no_earnings |
| 462 | GBTC | Grayscale Bitcoin Trust (B | $46.8 | None | — | — | no earnings | no_earnings |
| 463 | BAYN.DE | Bayer AG                   | $36.16 | -2.19 | — | — | no earnings | no_earnings |
| 464 | 000270.KS | KIA CORP. | $161100.0 | None | — | — | no earnings | no_earnings |
| 465 | 012330.KS | Mobis | $697000.0 | None | — | — | no earnings | no_earnings |
| 466 | TTWO | Take-Two Interactive Softw | $214.39 | -1.63 | — | — | no earnings | no_earnings |
| 467 | 207940.KS | SAMSUNG BIOLOGICS | $1340000.0 | None | — | — | no earnings | no_earnings |
| 468 | 034020.KS | Doosan Enerbility | $95600.0 | None | — | — | no earnings | no_earnings |
| 469 | LYV | Live Nation Entertainment, | $160.07 | -1.78 | — | — | no earnings | no_earnings |
| 470 | ASTS | AST SpaceMobile, Inc. | $93.6 | -1.8 | — | — | no earnings | no_earnings |
| 471 | RKT | Rocket Companies, Inc. | $12.65 | -0.03 | — | — | no earnings | no_earnings |
| 472 | KER.PA | KERING | $249.45 | -0.22 | — | — | no earnings | no_earnings |
| 473 | 066570.KS | LGELECTRONICS | $303000.0 | None | — | — | no earnings | no_earnings |
| 474 | HMC | Honda Motor Company, Ltd. | $26.7 | -1.99 | — | — | no earnings | no_earnings |
| 475 | 012450.KS | HANWHA AEROSPACE | $1049000.0 | None | — | — | no earnings | no_earnings |
| 476 | VOD | Vodafone Group Plc | $14.7 | -0.14 | — | — | no earnings | no_earnings |
| 477 | SATS | EchoStar Corporation | $116.28 | -50.21 | — | — | no earnings | no_earnings |
| 478 | ORSTED.CO | ORSTED A/S | $160.35 | -2.41 | — | — | no earnings | no_earnings |
| 479 | RVMD | Revolution Medicines, Inc. | $149.23 | -7.12 | — | — | no earnings | no_earnings |
| 480 | NTRA | Natera, Inc. | $215.31 | -1.61 | — | — | no earnings | no_earnings |
| 481 | CNC | Centene Corporation | $62.33 | -13.05 | — | — | no earnings | no_earnings |
| 482 | EL | Estee Lauder Companies, In | $83.49 | -0.7 | — | — | no earnings | no_earnings |
| 483 | RBLX | Roblox Corporation | $41.82 | -1.57 | — | — | no earnings | no_earnings |
| 484 | FISV | Fiserv, Inc. | $54.43 | None | — | — | no earnings | no_earnings |
| 485 | 009155.KS | SamsungElecMech(1P) | $597000.0 | None | — | — | no earnings | no_earnings |
| 486 | MDB | MongoDB, Inc. | $350.74 | -0.39 | — | — | no earnings | no_earnings |
| 487 | CPNG | Coupang, Inc. | $15.15 | -0.1 | — | — | no earnings | no_earnings |
| 488 | KHC | The Kraft Heinz Company | $22.58 | -4.86 | — | — | no earnings | no_earnings |
| 489 | SYM | Symbotic Inc. | $44.02 | -0.08 | — | — | no earnings | no_earnings |
| 490 | ML.PA | MICHELIN | $31.88 | None | — | — | no earnings | no_earnings |
| 491 | TEAM | Atlassian Corporation | $99.47 | -0.82 | — | — | no earnings | no_earnings |
| 492 | TEF.MC | TELEFONICA,S.A. | $3.88 | -0.42 | — | — | no earnings | no_earnings |
| 493 | 068270.KS | Celltrion | $171400.0 | None | — | — | no earnings | no_earnings |
| 494 | EXO.AS | EXOR | $65.7 | -18.48 | — | — | no earnings | no_earnings |
| 495 | 035420.KS | NAVER | $255500.0 | None | — | — | no earnings | no_earnings |
| 496 | DOW | Dow Inc. | $33.97 | -4.0 | — | — | no earnings | no_earnings |

