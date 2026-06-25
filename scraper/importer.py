"""
Import pipeline — runs all sources, filters, upserts to DB, exports JSON.
"""

import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from db import init_db, upsert_product, log_run, get_active_products
from filter import qualify
from sources import cj, aliexpress
from config import EXPORT_PATH


def run_source(name: str, raw_products: list[dict]) -> dict:
    stats = {'fetched': len(raw_products), 'passed': 0, 'inserted': 0, 'updated': 0, 'errors': 0}
    for raw in raw_products:
        try:
            clean = qualify(raw)
            if clean is None:
                continue
            stats['passed'] += 1
            result = upsert_product(clean)
            if result == 'inserted':
                stats['inserted'] += 1
            elif result == 'updated':
                stats['updated'] += 1
        except Exception as e:
            stats['errors'] += 1
            print(f'[importer] error on {raw.get("source_id")}: {e}')
    log_run(name, **stats)
    return stats


def export_json(limit: int = 500):
    """Write active products to data/products.json for the frontend."""
    products = get_active_products(limit=limit)
    os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)
    with open(EXPORT_PATH, 'w', encoding='utf-8') as f:
        json.dump({'products': products, 'count': len(products)}, f, indent=2)
    print(f'[importer] exported {len(products)} products → {EXPORT_PATH}')


def run():
    print('\n── Import run starting ──────────────────────────────────────────')
    init_db()

    totals = {'fetched': 0, 'passed': 0, 'inserted': 0, 'updated': 0, 'errors': 0}

    # CJ Dropshipping
    try:
        cj_raw = cj.fetch_all_categories()
        s = run_source('cj', cj_raw)
        for k in totals:
            totals[k] += s[k]
    except Exception as e:
        print(f'[importer] CJ source failed: {e}')

    # AliExpress
    try:
        ali_raw = aliexpress.fetch_all_categories()
        s = run_source('aliexpress', ali_raw)
        for k in totals:
            totals[k] += s[k]
    except Exception as e:
        print(f'[importer] AliExpress source failed: {e}')

    export_json()

    print(f'''
── Run complete ─────────────────────────────────────────────────
  Fetched : {totals["fetched"]}
  Passed  : {totals["passed"]}
  Inserted: {totals["inserted"]}
  Updated : {totals["updated"]}
  Errors  : {totals["errors"]}
─────────────────────────────────────────────────────────────────
''')
    return totals


if __name__ == '__main__':
    run()
