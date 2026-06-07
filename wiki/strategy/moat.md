---
id: moat
title: Moat — What It Means for a Company to Have One
type: concept
dimensions: [instrument-selection, scorecard]
updated: 2026-06-07
---

# Moat — What It Means for a Company to Have One

## Brandon's definition
> "A moat is really just any competition that could come in and wipe their business out. Who is the
> competition?"

A moat is a **durable competitive advantage** — the thing that stops rivals from taking the company's
profits. Brandon pairs it with **pricing power**: a moated company can raise prices and customers still
stay. His shorthand checklist for a buy is *"pricing power, a durable competitive advantage, and you have
to be okay to hold them for the long [term], and you have to get it for a good valuation."*

## The three questions he asks
1. **Do they have a durable competitive advantage?** Something hard to copy (scale, network, brand, IP, switching costs).
2. **Do they have pricing power?** Can they raise prices without losing customers? (Apple: *"raise the price on an iPhone… are most people still going to buy iPhones? Yes."*)
3. **Will competition wipe them out?** *"Is the competition going to wipe them out?"* If a rival "could pop up immediately and suck away" the business, there's **no moat**.

## Why it's a gate, not a nicety
Moat is one of the ~five scored components ([[scorecard]], Moat /20), but functionally it's a **veto**:
Brandon refuses to buy "**crap companies at crap prices with no moat**" — *cheap is not enough.* A
low-priced company with no moat is a **value trap**: it looks undervalued, then the business erodes and
the "discount" was real for a reason.

## Examples
| Has a moat | No moat (value-trap risk) |
|---|---|
| **Apple** — iPhone pricing power / ecosystem lock-in | **PayPal** — *"no moat, no pricing power… PayPal's going to be a no"* |
| **NVIDIA** — best chip, best margins, best pricing power | **Netflix** — no durable moat / pricing power (his call) |
| **UnitedHealth** — biggest health insurer in the world (scale) | **Nike** — declining, no moat |
| **Meta** — network effects (who's the competition?) | **Airlines** — the textbook "no moat" example |
| **TSM** — ~90% of advanced chip fabrication | **Hims** — *"when their ads dry up, the business collapses"* |

## How this connects to our screen (a known gap)
Our [[valuation-method]] (the golden line) measures **price vs earnings only** — it has **no moat gate**.
The decision back-test (`BACKTEST_RECONCILIATION.md`) proved this matters: our screen *bought*
PayPal, Netflix, CRM — names Brandon rejects for having no moat — because they screened "cheap."
- We compute a `moat_proxy_20` column from margins + ROE, but it is a **weak stand-in**: PayPal and
  Netflix have *fine* margins, so the proxy doesn't flag them the way Brandon's qualitative judgment does.
- Moat is genuinely **qualitative** — it's about *future* competitive durability, not current
  profitability. A faithful moat gate needs a real competitive-position read (or human judgment), not a
  margin threshold. This is the open piece of matching Brandon. See [[scorecard]].
