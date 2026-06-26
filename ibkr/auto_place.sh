#!/usr/bin/env bash
# Auto-placer: runs on the VPS via cron (*/12 * * * *). Probes whether fractional trading is live for the
# API; while it's still pending (IBKR Error 10243) it does nothing. The moment fractional activates, it
# places the full orders.csv portfolio ONCE on the paper account, then self-disables via PLACED.done.
# Armed 2026-06-26 because John enabled Fractional Shares but the permission was still "pending".
cd /root/ibkr
[ -f PLACED.done ] && exit 0
echo "=== $(date -u) probe ===" >> place_retry.log
./venv/bin/python place_orders.py /root/orders.csv --probe >> place_retry.log 2>&1
if [ $? -eq 0 ]; then
  echo "=== $(date -u) FRACTIONAL LIVE -> placing full portfolio ===" >> place_retry.log
  ./venv/bin/python place_orders.py /root/orders.csv --execute >> place_retry.log 2>&1
  touch PLACED.done
  echo "=== $(date -u) PLACEMENT COMPLETE (self-disabled) ===" >> place_retry.log
fi
