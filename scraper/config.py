# ── API credentials ──────────────────────────────────────────────────────────
# Fill these in before running. All keys are loaded from environment variables
# or from a local .env file (python-dotenv).

import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# CJ Dropshipping  →  https://developers.cjdropshipping.com
CJ_EMAIL    = os.getenv('CJ_EMAIL', '')
CJ_PASSWORD = os.getenv('CJ_PASSWORD', '')

# AliExpress Affiliate API  →  https://portals.aliexpress.com
ALI_APP_KEY    = os.getenv('ALI_APP_KEY', '')
ALI_APP_SECRET = os.getenv('ALI_APP_SECRET', '')
ALI_TRACKING   = os.getenv('ALI_TRACKING_ID', '')

# ── Margin / quality thresholds ───────────────────────────────────────────────
MIN_MARGIN_PCT   = float(os.getenv('MIN_MARGIN_PCT', '25'))   # drop anything below 25 %
MIN_PRICE_USD    = float(os.getenv('MIN_PRICE_USD',  '5'))
MAX_PRICE_USD    = float(os.getenv('MAX_PRICE_USD',  '500'))
MIN_ORDERS       = int(os.getenv('MIN_ORDERS',       '50'))   # social proof floor
MIN_RATING       = float(os.getenv('MIN_RATING',     '4.0'))

# Suggested retail markup over supplier cost (e.g. 2.2 = 120 % markup)
RETAIL_MULTIPLIER = float(os.getenv('RETAIL_MULTIPLIER', '2.2'))

# ── Scraper behaviour ─────────────────────────────────────────────────────────
SCRAPE_INTERVAL_MINUTES = int(os.getenv('SCRAPE_INTERVAL', '60'))
MAX_PRODUCTS_PER_RUN    = int(os.getenv('MAX_PRODUCTS_PER_RUN', '200'))

# Categories to search (mapped to CJ/AliExpress taxonomy)
TARGET_CATEGORIES = [
    'Women\'s Clothing',
    'Men\'s Clothing',
    'Bags & Luggage',
    'Shoes',
    'Jewellery & Accessories',
]

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH      = os.path.join(BASE_DIR, 'data', 'products.db')
EXPORT_PATH  = os.path.join(BASE_DIR, 'data', 'products.json')
