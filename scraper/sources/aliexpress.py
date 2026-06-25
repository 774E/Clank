"""
AliExpress Affiliate API source adapter.
Docs: https://portals.aliexpress.com  (AliExpress Portals → API)

Uses the Affiliate Product Query API (aliexpress.affiliate.product.query)
via the top-level gateway: https://api-sg.aliexpress.com/sync

Requires:
  ALI_APP_KEY    — your app key from the portals dashboard
  ALI_APP_SECRET — your app secret
  ALI_TRACKING   — your tracking ID (affiliate tag)
"""

import hashlib
import hmac
import time
import requests
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from config import ALI_APP_KEY, ALI_APP_SECRET, ALI_TRACKING, MAX_PRODUCTS_PER_RUN

GATEWAY = 'https://api-sg.aliexpress.com/sync'

# AliExpress category IDs for fashion
CATEGORY_MAP = {
    "Women's Clothing": '200000345',
    "Men's Clothing":   '200000343',
    "Bags & Luggage":   '200000342',
    "Shoes":            '200000788',
    "Jewellery & Accessories": '200000437',
}


def _sign(params: dict, secret: str) -> str:
    """HMAC-SHA256 signature required by the AliExpress gateway."""
    sorted_params = sorted(params.items())
    base = ''.join(f'{k}{v}' for k, v in sorted_params)
    sig = hmac.new(secret.encode(), base.encode(), hashlib.sha256).hexdigest().upper()
    return sig


def _call(method: str, extra: dict) -> dict:
    if not ALI_APP_KEY or not ALI_APP_SECRET:
        return {}
    ts = str(int(time.time() * 1000))
    params = {
        'app_key':    ALI_APP_KEY,
        'timestamp':  ts,
        'sign_method':'hmac-sha256',
        'method':     method,
        **extra,
    }
    params['sign'] = _sign(params, ALI_APP_SECRET)
    resp = requests.get(GATEWAY, params=params, timeout=20)
    return resp.json()


def _map_product(item: dict, category: str) -> dict:
    price_str = (item.get('target_sale_price') or item.get('sale_price') or '0 USD').split(' ')[0]
    orig_str  = (item.get('original_price') or '0 USD').split(' ')[0]
    try:
        cost = float(price_str)
        original = float(orig_str) if orig_str != price_str else None
    except ValueError:
        cost, original = 0.0, None

    images = [item.get('product_main_image_url', '')]
    if item.get('product_small_image_urls'):
        images += item['product_small_image_urls'].get('string', [])

    return {
        'source':       'aliexpress',
        'source_id':    str(item.get('product_id', '')),
        'name':         item.get('product_title', ''),
        'brand':        item.get('shop_name', ''),
        'category':     category,
        'cost_usd':     cost,
        'original_usd': original,
        'rating':       float(item.get('evaluate_rate', '0').replace('%', '') or 0) / 20 or None,
        'orders':       int(item.get('lastest_volume', 0) or 0),
        'image_url':    images[0] if images else '',
        'extra_images': images[1:5],
        'product_url':  item.get('promotion_link') or item.get('product_detail_url', ''),
        'tags':         [],
    }


def fetch(category: str = "Women's Clothing", page_size: int = 50) -> list[dict]:
    if not ALI_APP_KEY:
        print('[aliexpress] credentials not set — skipping')
        return []

    cat_id = CATEGORY_MAP.get(category, '')
    products = []
    page = 1

    while len(products) < MAX_PRODUCTS_PER_RUN:
        body = _call('aliexpress.affiliate.product.query', {
            'tracking_id':   ALI_TRACKING,
            'category_ids':  cat_id,
            'sort':          'SALE_PRICE_ASC',
            'page_no':       str(page),
            'page_size':     str(min(page_size, 50)),
            'currency':      'USD',
            'ship_to_country': 'US',
            'fields': ','.join([
                'product_id', 'product_title', 'target_sale_price',
                'original_price', 'sale_price', 'evaluate_rate',
                'lastest_volume', 'product_main_image_url',
                'product_small_image_urls', 'promotion_link',
                'shop_name',
            ]),
        })

        resp_key = 'aliexpress_affiliate_product_query_response'
        result = body.get(resp_key, {}).get('resp_result', {})
        if result.get('resp_code') != 200:
            print(f'[aliexpress] error: {result.get("resp_msg")}')
            break

        items = result.get('result', {}).get('products', {}).get('product', [])
        if not items:
            break
        for item in items:
            products.append(_map_product(item, category))
        if len(items) < page_size:
            break
        page += 1

    print(f'[aliexpress] fetched {len(products)} products for "{category}"')
    return products


def fetch_all_categories() -> list[dict]:
    all_products = []
    for cat in CATEGORY_MAP:
        all_products.extend(fetch(cat))
    return all_products
