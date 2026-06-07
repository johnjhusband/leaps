# Assumptions Ledger — every magic number, and where it came from

**Why this exists:** the NVDA error was an *invented threshold* that sounded reasonable. The audit checked
my prose, not my constants. This ledger lists every number the code decides with, classified by source:
**[B]** = Brandon's words, **[J]** = John's directive, **[?]** = my invention (← where the next error hides).

| # | Constant | Where | Value | Source | Risk |
|---|----------|-------|-------|--------|------|
| 1 | golden-line window | goldenline | 2 fiscal years (`eps[0]` vs `eps[2]`) | **[B]** "2-year time period" | Low — but FY alignment is approximate |
| 2 | **P/E skew threshold** | goldenline | `\|pe_now/pe_then−1\| > 0.5` → skewed | **[?]** Brandon says "apples to apples"; the **50% is mine** | **HIGH — caused the NVDA exclusion** |
| 3 | market gate | goldenline | median valid golden < **−20%** | **[B]** ">20% overvalued"; *median-of-S&P-constituents proxy is **[?]*** | Med — the proxy for "market valuation" is mine |
| 4 | **forward-confirm** | build_universe | forward P/E ≤ **1.5 × growth%**, growth floor **8%** | **[?]** Brandon uses fwd P/E + "growth justifies multiple"; **1.5 and 8 are mine** | **HIGH — sets the 63 rescued names** |
| 5 | growth cap (proxy) | _valuate | **GCAP=30%** | **[?]** Brandon haircut NVDA 100→**60%**; my 30% is stricter | Med — may understate high-growth names; feeds #4 |
| 6 | proxy intrinsic | _valuate | FAIR_PE=**20**, DISCOUNT=**10%**, HAIRCUT=**0.6** | **[?]** market norm 15–20 loosely [B]; formula is mine | Low now — **proxy is secondary**, golden line is primary |
| 7 | moat proxy bands | build_universe | gross 0.6/0.4/0.25/0.12; ROE 0.35/0.20/0.10; debt>200 | **[?]** all mine — Brandon's moat is qualitative | Med — a rough quality stand-in, not his call |
| 8 | allocation pivot | build_universe | stock = min(100%, undervalued% ÷ **50%**) | **[J]** John's explicit rule | None — John's directive |
| 9 | IBKR fractional | build_universe | EU_CA suffix set; OTC = PNK/OQX/OID… | **[B/research]** IBKR rules; suffix mapping is my approximation | Low–Med |
| 10 | no-EPS / no-data drop | build_universe | trailingEps None/≤0 | mechanical | Low |

## The invented numbers that most need Brandon-grounding or a sensitivity check
- **#2 (50% skew)** and **#4 (PEG-fwd 1.5 / 8% floor)** together decide who's on the buy list among
  re-rated names. Both are mine. They should be (a) sensitivity-tested (does the buy list lurch if 0.5→0.4
  or 1.5→1.2?) and (b) validated against Brandon's actual picks (see the decision back-test).
- **#5 (30% growth cap)** is stricter than Brandon's own 60% on NVDA — likely understates fast growers.
- **#3 market gate proxy** — "market is >20% overvalued" should ideally be measured on the index's own
  EPS line, not the median of constituents; flag as an approximation.

## Status
Ledger created 2026-06-07. Next: sensitivity-test #2/#4/#5 and reconcile every number against the
decision back-test (does our verdict match Brandon's stated call on the same ticker?).
