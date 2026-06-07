#!/usr/bin/env bash
# Rebuild the entire investable universe from scratch. Run periodically (e.g. monthly) to refresh.
# Usage:  bash rebuild_universe.sh
set -euo pipefail
cd "$(dirname "$0")"
PY=python3

echo "[1/6] constituents (SPY, QQQ, Russell1000, Global1000)..."
$PY build_constituents.py

echo "[2/6] fundamentals + growth (yfinance, ~1500 tickers, SLOW ~15-20 min)..."
$PY _fetch_all.py

echo "[3/7] exchange codes for ADRs (for OTC filtering)..."
$PY _fetch_exchange.py

echo "[4/8] quality metrics for the moat proxy (margins, ROE, debt)..."
$PY _fetch_quality.py

echo "[5/8] historical EPS + price for the golden line (Brandon's actual valuation)..."
$PY _fetch_goldenline.py

echo "[6/8] proxy valuation (secondary)..."
$PY _valuate.py

echo "[7/8] assemble universe CSVs (golden line + market gate + moat + fractional filter)..."
$PY build_universe.py

echo "[8/9] write the bullish/bearish screen report..."
$PY _write_report.py

echo "[9/9] snapshot into SQLite (appends dated row -> rebalance history)..."
$PY build_db.py "$(date +%F)"

echo
echo "DONE. Key outputs:"
echo "  leaps.db                              <- queryable data + rebalance history (SQL)"
echo "  universe_fractional.csv               <- the investable universe (rebalance from this)"
echo "  universe_full.csv                     <- audit: everything with data + flags"
echo "  QQQ_SPY_valuation_bullish_bearish.md  <- per-index bullish/bearish screen"
echo
echo "NOTE: caches (_fundamentals.json, _growth.json, _exchange.json) are reused if present."
echo "      To force a full refresh of prices/growth, delete them first:"
echo "      rm -f _fundamentals.json _growth.json _exchange.json"
