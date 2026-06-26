# Phase 3 — IBKR paper trade (play money)

Buys 1 share of SPY in the IBKR **paper** account end to end, to prove the API path before any real order.

## Result (proven)
**Done.** Placed 2026-06-09 ~20:13 ET as a resting GTC marketable limit; **filled 2026-06-10 08:00 UTC
(pre-market open), 1 share SPY @ $737.00** in paper account `DUQ691670`. The position is held and the VPS
cron has re-confirmed it every 15 min since (`/root/ibkr/fill_confirmation.log`). The full path —
API login → order placed → rested overnight → filled at open → position confirmed — works.

## Where it runs
Hosted on a dedicated **Hetzner VPS** (not a laptop — hosts come and go; the gateway should be permanent
and reachable by whatever machine/AI drives it next). Box: `leaps-ibkr`, **167.233.34.83**, cx23 (2 vCPU /
4 GB, x86 — the gateway image is x86-only), Ubuntu 24.04, SSH-only firewall, key `~/.ssh/leaps-ibkr`.
Deploy dir on the VPS: `/root/ibkr/` (compose + `.env` + `venv` + `buy_one_spy.py`). The gateway API is
bound to `127.0.0.1:4002` **on the VPS** and never exposed; the order script runs on the VPS too, so the
only open port is SSH. Manage: `ssh -i ~/.ssh/leaps-ibkr root@167.233.34.83 'cd /root/ibkr && docker compose ...'`.

Login uses the **live** username + password with the gateway's paper toggle (`TRADING_MODE=paper`); IBKR
then serves the simulated paper account **`DUQ691670`** ($1,000,000 play money). No 2FA is prompted for the
paper login.

## How it works
- `docker-compose.yml` runs IBKR's IB Gateway headless (gnzsnz image + IBC + Xvfb) in **paper** mode.
  The paper API listens on **127.0.0.1:4002** (localhost only). Paper logins use the `DU…` username and
  do **not** require 2FA, so this runs unattended.
- `buy_one_spy.py` (ib_async) connects to 4002, refuses unless the account id starts `DU` (live-account
  guard), shows the play-money balance, sizes a marketable limit off a delayed quote, places a **GTC**
  marketable-limit BUY for 1 SPY (`outsideRth=True`), waits for the fill, prints it.

## Gotcha: market data + after-hours fills
- The paper account has **no live market-data subscription** → `reqMktData` returns NaN. The script calls
  `reqMarketDataType(4)` (delayed-frozen) first, which returns the last/close price with no subscription.
- A plain MKT order won't fill outside regular hours. The default is a **GTC marketable limit** (1% over
  the reference price) with `outsideRth=True`: it fills instantly during RTH and otherwise **rests and
  fills at the next session open** (pre-market ~4am ET). `--market` forces pure MKT; `--limit P` sets a price.

## Run it
```bash
cd ibkr
cp .env.example .env          # then put the paper DU username + password in .env (gitignored)
sudo docker compose up -d     # start the gateway; first login takes ~1–2 min
sudo docker compose logs -f   # wait for "IBKR API ... listening" / login complete
venv/bin/python buy_one_spy.py          # market order, fills instantly during US RTH
# outside market hours, force a fill with a limit at/above the ask:
venv/bin/python buy_one_spy.py 1 --limit 650
sudo docker compose down      # stop the gateway when done
```

## Prereqs (already done on this box)
- Docker Engine + compose (installed 2026-06-09).
- `venv/` with `ib_async` 2.1.0 (`python3 -m venv venv && venv/bin/pip install ib_async`).
- Image **pinned to `ghcr.io/gnzsnz/ib-gateway:10.34.1c`** (see gotcha below).

## Confirming the fill (after-hours orders)
`check_fill.py` logs whether the resting order has filled — fill signal is the account **SPY position ≥ 1**
(reliable no matter which client placed the order; it also calls `reqAllOpenOrders`/`reqExecutions` to see
orders from other clients). A VPS cron runs it every 15 min from 08:00–15:00 UTC (covers pre-market ~4am ET
through late-morning RTH), appending to `/root/ibkr/fill_confirmation.log`. Check it:
`ssh -i ~/.ssh/leaps-ibkr root@167.233.34.83 'cat /root/ibkr/fill_confirmation.log'` — a `FILLED` line = done.

## Gotcha: pin the gateway version
`:stable` currently ships IB Gateway **10.45.1g**, whose bundled IBC hangs at "Invoking config
dialog menu" right after login (jxbrowser/IBC mismatch, IbcAlpha/IBC#285) — the API socket never
opens and connections time out. Pinned to **10.34.1c**, which ships a working IBC and reaches the
server cleanly. Don't move back to `:stable`/`:latest` without re-testing the full login → API path.

## Gotcha: credentials & auto-retry
Paper mode logs in with the **live** username + password (the gateway's paper toggle). A bad login
returns "Connection to server failed: Invalid username or password" and IBC exits — and with
`restart: unless-stopped` the container relaunches and retries, which can **lock the live account**.
If credentials are unverified, start with `restart: "no"` or run `up` once and watch the log before
trusting the restart policy. Note: a fresh account's IBKR-issued password is **temporary**; the first
browser login forces a reset, after which the temp password is dead — use the reset one.

## Safety
- Paper account only — `buy_one_spy.py` exits if the connected account is not `DU…`.
- `.env` (credentials) and `venv/` are gitignored; the API port is bound to localhost.

## Placing an arbitrary trade
`buy_one.py TICKER [QTY] [--limit P] [--market]` — same logic as the SPY proof but for any symbol.
Verified 2026-06-26: `buy_one.py NVDA 1` filled immediately @ $193.71 in-hours. Paper account currently
holds 1 NVDA + 1 SPY.
```
ssh -i ~/.ssh/leaps-ibkr root@167.233.34.83 'cd /root/ibkr && ./venv/bin/python buy_one.py NVDA 1'
```

## Next (Phase 3 proper, after this proof)
Replace the single-name order with a loop over `../orders.csv`, sending each name's `dollars`
as `cashQty` (IBKR fractional), with a dry-run preview and a total-spend guardrail before live orders.
