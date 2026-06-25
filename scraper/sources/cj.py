"""
CJ Dropshipping source adapter.
Docs: https://developers.cjdropshipping.com/api2.0/v1/product/list

Flow:
  1. POST /authentication/getAccessToken  →  access_token (valid 24 h)
  2. GET  /product/list                   →  paginated product list
  3. GET  /product/query                  →  detail (images, variants)
"""

import requests
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from config import CJ_EMAIL, CJ_PASSWORD, MAX_PRODUCTS_PER_RUN, TARGET_CATEGORIES

BASE = 'https://developers.cjdropshipping.com/api2.0/v1'

_token_cache: dict = {}


def _get_token() -> str | None:
    if _token_cache.get('token'):
        return _token_cache['token']
    if not CJ_EMAIL or not CJ_PASSWORD:
        print('[cj] credentials not set — skipping')
        return None
    resp = requests.post(f'{BASE}/authentication/getAccessToken', json={
        'email': CJ_EMAIL, 'password': CJ_PASSWORD
    }, timeout=15)
    data = resp.json()
    if data.get('result') and data['data'].get('accessToken'):
        token = data['data']['accessToken']
        _token_cache['token'] = token
        return token
    print(f'[cj] auth failed: {data.get("message")}')
    return None


def _headers(token: str) -> dict:
    return {'CJ-Access-Token': token, 'Content-Type': 'application/json'}


def _map_product(item: dict, category: str) -> dict:
    """Map a CJ list item to our raw product schema."""
    return {
        'source':       'cj',
        'source_id':    item.get('pid') or item.get('productId', ''),
        'name':         item.get('productNameEn') or item.get('productName', ''),
        'brand':        '',
        'category':     category,
        'cost_usd':     float(item.get('sellPrice') or item.get('productPrice') or 0),
        'original_usd': float(item.get('suggestSellingPrice') or 0) or None,
        'rating':       float(item.get('productEvaluation') or 0) or None,
        'orders':       int(item.get('productSku') or 0) if isinstance(item.get('productSku'), int) else None,
        'image_url':    item.get('productImage') or item.get('productImageUrl', ''),
        'extra_images': [],
        'product_url':  f"https://app.cjdropshipping.com/product-detail.html?id={item.get('pid', '')}",
        'tags':         [],
    }


def fetch(category: str = TARGET_CATEGORIES[0], page_size: int = 20) -> list[dict]:
    token = _get_token()
    if not token:
        return []

    products = []
    page = 1
    while len(products) < MAX_PRODUCTS_PER_RUN:
        resp = requests.get(f'{BASE}/product/list', headers=_headers(token), params={
            'categoryKeyword': category,
            'pageNum': page,
            'pageSize': min(page_size, 50),
        }, timeout=20)
        body = resp.json()
        if not body.get('result'):
            print(f'[cj] list error page {page}: {body.get("message")}')
            break
        items = body.get('data', {}).get('list') or []
        if not items:
            break
        for item in items:
            products.append(_map_product(item, category))
        if len(items) < page_size:
            break
        page += 1

    print(f'[cj] fetched {len(products)} products for "{category}"')
    return products


def fetch_all_categories() -> list[dict]:
    all_products = []
    for cat in TARGET_CATEGORIES:
        all_products.extend(fetch(cat))
    return all_products
