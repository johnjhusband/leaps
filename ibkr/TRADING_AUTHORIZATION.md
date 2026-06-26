# TRADING AUTHORIZATION — read before placing ANY order (hard rule, no exceptions)

This is the single most important rule for any AI (or person) operating this account. It outranks every
other doc. If anything here conflicts with a script's convenience or another doc, **this wins.**

## The rule
**Never place an order — paper or live — without explicit, specific authorization for THAT order.**

An order is a state-changing, outward-facing action. The default is to **describe or preview and STOP**,
never to execute. Execution requires a human instruction that you can quote.

## A question is NOT authorization
These are questions. Answer them in words and **do not trade**:
- "Can you make a trade?" / "Could you buy X?" / "Are you able to…?"
- "What would it cost to…?" / "What would happen if…?" / "Is it possible to…?"
- "Show me / tell me / explain how you'd place an order."

Treating "can you make a trade?" as a command and placing one is the exact incident this doc exists to
prevent (2026-06-26: an AI was *asked whether it could* trade and instead *placed* an unapproved 1-share
NVDA buy on the paper account — harmless on play money, a real problem on live money).

## What DOES authorize an order
A direct, unambiguous instruction to act, specifying enough to act on:
- the **side** (buy/sell), the **ticker(s)**, and the **quantity or dollar amount**.
- Examples that authorize: "Buy 1 share of NVDA." "Execute orders.csv." "Place the buy list."
- Ambiguous directives ("make a trade", "do something") are NOT enough — they name no security/size.
  Confirm the specifics first; do not pick one yourself.

## Live money raises the bar
For a **live** (funded, non-`DU`) account, an instruction must also be unmistakably about real money and,
for anything beyond a trivial test, name the **dollar amount or share count**. When in doubt on live money,
preview the order and wait for a "yes, place it" that names the size. Not trading is reversible; an
executed live trade is not — bias hard toward not acting.

## The check before any order (paste-in-your-head)
1. Did the human tell me to *place this specific order*, in words I can quote? If not → **stop, don't trade.**
2. Was it a question or a hypothetical? → **answer it, don't trade.**
3. Is it live money? → require the size to be named; preview first.
4. Only all-clear → place exactly what was authorized, nothing more.

> Scope note: this is the human-authorization gate. The technical guardrails (dry-run preview,
> max-order-size, only-on-meaningful-drift) in `INDEX_PLAN.md`/`ACCOUNT_SETUP.md` are additional and do
> not replace this rule.
