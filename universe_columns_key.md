# Column Key — `universe_fractional.csv` / `universe_full.csv`

Each row is one company. Columns explain *why* it got its rating.

| Column heading | Full name | Definition |
|----------------|-----------|------------|
| `rank` | Rank by market cap | Position in the list, largest company = 1. |
| `golden_verdict` | **Golden-line verdict (Brandon's actual method)** | bullish if the stock is undervalued by the golden line (EPS outgrew price over 2yr), else bearish. **This is the primary, faithful verdict.** |
| `golden_pct` | Golden-line under/over % | How far below (+) or above (−) the EPS line the price sits. + = cheap. |
| `golden_valid` | Golden-line validity | `Y` = start vs end P/E are similar (apples-to-apples, reliable); `skewed` = the P/E re-rated a lot, so the read is unreliable. |
| `eps_2y` / `eps_now` | EPS 2 years ago / now | Annual diluted EPS at the two endpoints of the window. |
| `eps_growth_2y` | EPS growth over 2yr | (eps_now/eps_2y − 1). |
| `price_growth_2y` | Price growth over 2yr | (price_now/price_2y − 1). Undervalued when eps_growth_2y > price_growth_2y. |
| `pe_then` / `pe_now` | P/E 2yr ago / now | Used for the validity check. |
| `proxy_verdict` / `proxy_pct` | My earlier proxy method | Kept for comparison; superseded by golden_*. |
| `ticker` | Ticker symbol | The trading symbol (e.g. `NVDA`; foreign suffixes like `.TO` = Toronto, `.L` = London). |
| `name` | Company name | The company's name. |
| `country` | Country of domicile | Where the company is headquartered/domiciled (not where it's listed). |
| `mktcap_B` | Market capitalization (USD billions) | Total value of the company's shares, in billions of US dollars. |
| `verdict` | Valuation verdict | `bullish` = undervalued (buy candidate); `bearish` = overvalued; `no_earnings` = no positive earnings, can't be valued this way. |
| `under_over_pct` | Under/over-valuation percent | How far intrinsic value sits above (+) or below (−) the current price. +50 means intrinsic is 50% above price (cheap). |
| `price` | Current share price | Latest market price per share (local currency for foreign listings). |
| `intrinsic_value` | Intrinsic value per share | What the share is "worth" by Brandon's method: `ttm_eps × (1 + g_used)^5 × 20 ÷ 1.10^5`. |
| `ttm_eps` | Trailing-twelve-month earnings per share | Actual reported profit per share over the last 12 months. |
| `fwd_eps` | Forward earnings per share | Analysts' estimate of next year's earnings per share. |
| `trailing_pe` | Trailing price-to-earnings ratio | Price ÷ ttm_eps. How many dollars you pay per dollar of current earnings; high = expensive unless growth justifies it. |
| `growth_curr_yr` | Current-year earnings growth estimate | Analysts' expected earnings growth for this fiscal year (0.32 = 32%). |
| `growth_next_yr` | Next-year earnings growth estimate | Analysts' expected earnings growth for next fiscal year. |
| `growth_ttm_yoy` | Trailing-twelve-month year-over-year earnings growth | Actual earnings growth over the last year vs the prior year. |
| `g_used` | Growth rate used in the calculation | The **median** of the three growth columns, floored at 0 and capped at 0.30 (30%). This is the rate plugged into the intrinsic-value formula. |
| `moat_proxy_20` | Moat proxy score (out of 20) | Systematic stand-in for Brandon's qualitative "moat" — built from margins + ROE + debt. Higher = stronger pricing power / durable advantage. NOT his exact call; a quality filter. See `wiki/strategy/scorecard.md`. |
| `gross_margin` | Gross profit margin | Gross profit ÷ revenue (0.60 = 60%). High, stable gross margin signals pricing power. |
| `oper_margin` | Operating margin | Operating profit ÷ revenue. Efficiency of the core business. |
| `roe` | Return on equity | Net profit ÷ shareholder equity. How much profit the company generates per dollar of equity; high = moat-like returns. |
| `debt_to_equity` | Debt-to-equity ratio | Total debt ÷ equity (as a %). High debt erodes durability (docks the moat proxy above ~200). |
| `fractional` | IBKR fractional-tradable (full file only) | `Y` = can be bought as a fraction at Interactive Brokers; `N` = cannot. (`universe_fractional.csv` contains only `Y`.) |
| `exchange` | Listing exchange (full file only) | Exchange code for US-listed names (`NYQ` = NYSE, `NMS` = Nasdaq, `PNK`/`OQX` = OTC/pink) or the foreign-suffix code. |

## How to read a rating in one line
`verdict` follows from `intrinsic_value` vs `price`: if intrinsic ≥ price → **bullish**. Intrinsic is
driven by earnings (`ttm_eps`) times growth (`g_used`) — so a high `trailing_pe` only stays bullish if
`g_used` is high enough to justify it.

**Examples:**
- AAPL **bearish**: `trailing_pe` 37, `g_used` 0.17 → intrinsic $228 < price $307.
- NVDA **bullish**: `g_used` capped at 0.30 on `ttm_eps` $6.52 → intrinsic $301 > price $205.
- KO **bearish**: `g_used` 0.09 can't justify `trailing_pe` 25 → intrinsic $60 < price $79.
