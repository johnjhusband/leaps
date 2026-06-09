# Phase 3 — IBKR paper trade (play money)

Buys 1 share of SPY in the IBKR **paper** account end to end, to prove the API path before any real order.

## How it works
- `docker-compose.yml` runs IBKR's IB Gateway headless (gnzsnz image + IBC + Xvfb) in **paper** mode.
  The paper API listens on **127.0.0.1:4002** (localhost only). Paper logins use the `DU…` username and
  do **not** require 2FA, so this runs unattended.
- `buy_one_spy.py` (ib_async) connects to 4002, refuses unless the account id starts `DU` (live-account
  guard), shows the play-money balance, places a market BUY for 1 SPY, waits for the fill, prints it.

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
- Image `ghcr.io/gnzsnz/ib-gateway:stable` pulled.

## Safety
- Paper account only — `buy_one_spy.py` exits if the connected account is not `DU…`.
- `.env` (credentials) and `venv/` are gitignored; the API port is bound to localhost.

## Next (Phase 3 proper, after this proof)
Replace the single hardcoded SPY order with a loop over `../orders.csv`, sending each name's `dollars`
as `cashQty` (IBKR fractional), with a dry-run preview and a total-spend guardrail before live orders.
