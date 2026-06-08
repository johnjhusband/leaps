# Phase 2 — Opening the Interactive Brokers Account

Goal: an IBKR account that can hold the **185-name fractional buy list** (US + Canada + Europe + ADRs) at
~$395 each on $100k, plus the ~27% bond/short-term sleeve, and later be driven by the API to rebalance.

## What only John can provide (have these ready before starting)
- Government photo ID (driver's license or passport) — for the upload.
- Social Security Number (US tax ID).
- A proof of address if asked (recent utility bill / bank statement).
- Employment + financial info: employer, net worth, annual income, investing experience/objectives.
- Bank account + routing number to fund (ACH) or wire details for the $100k.
- A phone for two-factor (IBKR uses its own "IB Key" app — no Gmail app-password issue).

## The TWO decisions that matter (everything else is default)

### 1. Account type: **Margin** (recommended) vs Cash
- **Margin** — trades *all* countries/currencies, so our non-USD listings (Canada `.TO`, London `.L`,
  Frankfurt `.DE`, Paris `.PA`) work; also leaves the door open to Brandon's options overlay later.
  **You do NOT have to use leverage** — a margin account can be run 100% unleveraged; it just unlocks access.
- **Cash** — simpler, but "may only trade products denominated in the base currency" → could block the
  foreign *local* listings (US-listed ADRs would still work). More restrictive.
- → **Pick Margin.** It's strictly more capable and you can ignore the leverage.

### 2. Plan: **IBKR Pro** (recommended) vs IBKR Lite — this one has a real trade-off
- **Lite:** commission-FREE on US-listed stocks/ETFs (US residents). But US-only SmartRouting, ~1% lower
  interest on idle cash, and non-US trades still cost commission.
- **Pro:** SmartRouting (better fills) + global access + ~1% higher interest on the cash/bond sleeve + full
  API. Commission: $0.005/share, **$1.00 minimum per order**.
- **The math to weigh:** our book is ~185 names, ~65% US. On Pro, a full rebalance of 185 tiny orders hits
  the $1 minimum ≈ **$185/rebalance** (~$2.2k/yr if monthly ≈ 2.2% drag on $100k). Lite makes the US
  majority free; the ~35% non-US names pay commission either way.
- → **Lean Pro** for the global access + API + higher cash interest, **but** if you'll rebalance the
  US-heavy book infrequently, Lite's commission savings are real. **You can switch plans any time**, so
  starting on either is low-risk. (My pick: Pro, and rebalance quarterly not monthly to cut order count.)

## Step-by-step (start to finish)
1. Go to **interactivebrokers.com** → top-right **"Open Account"** (or "Log In / Open Account").
2. Create a **username, password, and email**; verify the email.
3. Account holder type → **Individual**.
4. When asked, choose **Margin** (decision 1) and **IBKR Pro** (decision 2).
5. Enter personal details: legal name, address, date of birth, **SSN/tax ID**, citizenship.
6. Employment + financial profile: employer, net worth, income, investment experience and objectives
   (pick "growth" / long-term; you don't need to claim options experience for the long-only index).
7. **Trading permissions** — this is the important screen: enable **Stocks**, and turn ON
   **Fractional Shares**; enable the regions you need: **United States, Canada, Europe** (so the buy-list
   ADRs and local listings trade). (Skip options/futures for now — add later if we do the overlay.)
8. Review IBKR Pro/Lite, sign the agreements, submit.
9. **Identity verification:** upload the photo ID (+ proof of address if requested). Approval is usually
   1–3 business days.
10. Once approved: set up **two-factor (IB Key app)**, then **fund** via ACH (link the bank) or wire the $100k.
11. Confirm **fractional trading is enabled** in Client Portal (Settings → Trading Permissions /
    "Trade in Fractions"). If it's not on, request it there — it's a toggle.

## After the account is live (then I take over again)
- **`build_orders.py` already does the order list** (built/tested ahead of time, doesn't need the account):
  `python3 build_orders.py 100000 equal` → **`orders.csv`** = each buy-list name at its dollar weight
  (73% of $100k ÷ 185 ≈ **$395 each**) + **$27,000 into SGOV** (the 27% bond sleeve). Weighting is a
  parameter (`equal` default, or `mcap`). Verified it sums to the capital.
- Phase 3 = the automation: a script that reads `buy_list.csv` + the allocation and places fractional
  orders via the IBKR API (`cashQty` = dollar amount per name), with a dry-run preview and guardrails
  before any live order. (API fractional support confirmed 2026.)

## Sources
IBKR Lite vs Pro & fractional eligibility, cash vs margin access, and TWS API `cashQty` fractional support
were verified against IBKR's current pages (interactivebrokers.com) on 2026-06-07.
