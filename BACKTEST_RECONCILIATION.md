# Decision Back-Test — Our Screen vs Brandon's Actual Stock Calls

**The higher-rigor test John asked for:** instead of checking my *description* of the method, extract every
specific stock Brandon actually calls (bullish/held vs bearish/avoid) from the transcripts and run *our
screen* on those exact tickers. Every disagreement is our bug, a data gap, or a deliberate deviation.

**Result: of ~33 names Brandon gives a clear stance, we agree on ~16 and DIVERGE on ~17.** The divergence
is **systematic**, and it points at a real missing piece — not random noise.

## ✅ Agree (16)
- Bullish & we buy: **NVDA, META, MSFT, NOW** (ServiceNow).
- Bearish & we don't buy: **WMT, SBUX, AVGO, ASML, SOFI, AAPL, TSLA, XOM, CVX, V, INTC, HIMS.**

## ❌ We BUY what Brandon AVOIDS (9) — the biggest problem
| Ticker | Brandon says | Our screen | Why we're wrong |
|--------|--------------|-----------|-----------------|
| PYPL | "value trap, no moat" | BUY (golden +96%, fwd P/E 7) | **no moat gate** — cheap ≠ good |
| NFLX | "no durable moat" | BUY (+73%) | **no moat gate** |
| CRM | "moat question mark" | BUY (+154%) | **no moat gate** |
| WM | "garbage, too expensive" | BUY (+11%) | no moat + slow growth |
| COST | "PE 52, overvalued" | BUY (+11%, fwd P/E 43) | **no absolute-P/E ceiling** |
| PANW | "good company, bad price" | BUY (+56%, fwd P/E 66) | **no absolute-P/E ceiling** |
| AMD | "expensive, can't buy it" (PE 81) | BUY (+74%, fwd P/E 36) | no ceiling (he was bull at the April dip — time-dependent) |
| AMZN | "too much PE for the growth" | BUY (+94%) | no ceiling |
| NKE | "declining profits, no moat" | BUY (+11%) | no moat gate |

## ❌ We MISS Brandon's bulls (8)
| Ticker | Our screen | Cause |
|--------|-----------|-------|
| HOOD, MRVL, MU | no golden verdict | **data gap** — no 2-yr EPS history (recent/volatile); can't be golden-valued |
| TSM, UNH, GOOGL, BAC | golden=bearish (price outran earnings) | defensible disagreement OR time-misalignment (his calls are from Oct'25–Jan'26; UNH crashed, etc.) |

## Root cause (the next systematic error, found empirically)
The golden line is **necessary but not sufficient**. Brandon rejects names for two reasons our buy rule
completely ignores:
1. **No moat / quality gate.** We *compute* `moat_proxy_20` but **never use it in the buy decision.** So
   value-traps (PYPL, NFLX, CRM, WM) sail onto the buy list because they're "cheap vs their own past."
2. **No absolute-valuation ceiling.** The golden line says "cheap relative to its own history" even when
   the absolute multiple is a nosebleed (COST fwd 43, PANW fwd 66, AMD PE 81). Brandon has explicit
   ceilings — "I want ~30x," "below 25x," "PE 48 is a no" — we have none.
3. **Data gap** on recent-IPO / volatile names (HOOD, MRVL, MU) with no 2-yr EPS history.

## The disciplined fix (NOT more invented thresholds)
Both fixes are **Brandon-grounded**, so they don't repeat the skewed-flag mistake:
- **Moat gate:** require `moat_proxy_20` above a floor (and/or fix the moat proxy against his actual moat
  calls) — his scorecard weights moat /20.
- **Absolute-P/E ceiling:** reject buys above a forward-P/E ceiling unless growth justifies it, using
  **his stated numbers (~25–30x)** — not a number I make up.
- **Data gap:** add a fallback EPS source (e.g. quarterly TTM) so HOOD/MRVL/MU get valued.

These should be implemented against this back-test as the regression check: re-run it after each change and
watch the agree-count climb. See ASSUMPTIONS_LEDGER.md for every invented constant feeding these.

**Updated 2026-06-07.** This file is the regression harness — rerun `/tmp/bt.py`-style reconciliation after
any logic change.
