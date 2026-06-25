"""
Margin calculator and quality filter.
Turns a raw supplier product dict → a store-ready product dict, or None if it fails.
"""

import re
from config import (
    MIN_MARGIN_PCT, MIN_PRICE_USD, MAX_PRICE_USD,
    MIN_ORDERS, MIN_RATING, RETAIL_MULTIPLIER,
)

# Words that suggest low quality / problematic listings
_BLOCKLIST_RE = re.compile(
    r'(replica|counterfeit|fake|knockoff|copy of|inspired by|dropship|wholesale lot)',
    re.IGNORECASE,
)


def calculate_retail(cost: float) -> float:
    """Apply markup and round to a clean price point."""
    raw = cost * RETAIL_MULTIPLIER
    # Round to nearest .99
    return round(raw - 0.01, 0) + 0.99 if raw > 10 else round(raw, 2)


def margin_pct(cost: float, retail: float) -> float:
    if retail <= 0:
        return 0.0
    return round((retail - cost) / retail * 100, 1)


def qualify(raw: dict) -> dict | None:
    """
    raw keys expected:
        source, source_id, name, cost_usd, image_url,
        (optional) brand, category, original_usd, rating, orders,
                   extra_images, product_url, tags
    Returns enriched product dict or None.
    """
    name = (raw.get('name') or '').strip()
    cost = float(raw.get('cost_usd') or 0)

    # Hard rejects
    if not name or not raw.get('source_id'):
        return None
    if not raw.get('image_url'):
        return None
    if cost < MIN_PRICE_USD or cost > MAX_PRICE_USD:
        return None
    if _BLOCKLIST_RE.search(name):
        return None

    # Soft signals
    rating = float(raw.get('rating') or 0)
    orders = int(raw.get('orders') or 0)
    if rating and rating < MIN_RATING:
        return None
    if orders and orders < MIN_ORDERS:
        return None

    retail = calculate_retail(cost)
    margin = margin_pct(cost, retail)

    if margin < MIN_MARGIN_PCT:
        return None

    # Discount vs supplier's own "original" price
    original = raw.get('original_usd')
    discount_pct = None
    if original and original > cost:
        discount_pct = round((original - cost) / original * 100, 1)

    # Build clean tags
    tags = list(raw.get('tags') or [])
    if margin >= 50:
        tags.append('high-margin')
    if discount_pct and discount_pct >= 30:
        tags.append('sale')
    if orders and orders >= 500:
        tags.append('bestseller')

    return {
        'source':       raw['source'],
        'source_id':    str(raw['source_id']),
        'name':         name,
        'brand':        raw.get('brand') or '',
        'category':     raw.get('category') or 'Uncategorised',
        'cost_usd':     round(cost, 2),
        'retail_usd':   retail,
        'original_usd': round(float(original), 2) if original else None,
        'margin_pct':   margin,
        'discount_pct': discount_pct,
        'rating':       rating or None,
        'orders':       orders or None,
        'image_url':    raw.get('image_url', ''),
        'extra_images': raw.get('extra_images') or [],
        'product_url':  raw.get('product_url', ''),
        'tags':         tags,
    }
