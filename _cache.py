"""Shared cache-freshness helper for the fetch_* scripts.

THE BUG THIS FIXES: every fetcher used to skip any ticker already present in its
cache (`if t in cache: continue`). With a fully-populated cache, a rerun therefore
refetched NOTHING and silently reused stale prices — so "regenerate from current
market data before trading" was not actually achievable without manually deleting
the cache (not reproducible). See REPRODUCE.md "Cache freshness".

THE FIX: every cached entry records the date it was fetched (`_fetched`). On rerun,
an entry older than `max_age_days` is treated as stale and refetched. So running
`rebuild_universe.sh` always pulls current data automatically, with no manual steps.
Entries written by the old (un-stamped) pipeline have no `_fetched` and are treated
as stale → refetched once, which self-heals the old caches.

Freshness windows (override via env):
  PRICE_CACHE_MAX_AGE_DAYS    default 1   — prices / EPS / growth (move daily)
  QUALITY_CACHE_MAX_AGE_DAYS  default 30  — margins / ROE / debt (move ~quarterly)
Exchange codes are effectively static and are not aged here.
"""
import os, json, datetime


def _max_age(env_name, default):
    try:
        return int(os.environ.get(env_name, str(default)))
    except ValueError:
        return default


def price_max_age():
    return _max_age('PRICE_CACHE_MAX_AGE_DAYS', 1)


def quality_max_age():
    return _max_age('QUALITY_CACHE_MAX_AGE_DAYS', 30)


def is_fresh(entry, max_age_days):
    """True iff entry exists, is a dict, and was fetched within max_age_days."""
    if not isinstance(entry, dict):
        return False
    stamped = entry.get('_fetched')
    if not stamped:
        return False
    try:
        age = (datetime.date.today() - datetime.date.fromisoformat(stamped)).days
    except (ValueError, TypeError):
        return False
    return 0 <= age <= max_age_days


def stamp(entry):
    """Record today's fetch date on an entry (mutates and returns it)."""
    entry['_fetched'] = datetime.date.today().isoformat()
    return entry


def load(path):
    return json.load(open(path)) if os.path.exists(path) else {}
