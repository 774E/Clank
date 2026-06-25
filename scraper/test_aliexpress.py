"""
Run this to test your AliExpress credentials before running the full scraper.
  python test_aliexpress.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

# ── 1. Check .env loads ───────────────────────────────────────────────────────
print('\n[1/4] Checking .env file...')
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
    print('      ✓ python-dotenv loaded')
except ImportError:
    print('      ✗ python-dotenv not installed. Run: pip install -r requirements.txt')
    sys.exit(1)

ALI_APP_KEY    = os.getenv('ALI_APP_KEY', '')
ALI_APP_SECRET = os.getenv('ALI_APP_SECRET', '')
ALI_TRACKING   = os.getenv('ALI_TRACKING_ID', '')

if not ALI_APP_KEY or not ALI_APP_SECRET:
    print('\n      ✗ ALI_APP_KEY or ALI_APP_SECRET not set in .env')
    print('      → Follow the guide in START.txt to get your credentials.')
    sys.exit(1)

print(f'      ✓ App Key   : {ALI_APP_KEY[:4]}{"*" * (len(ALI_APP_KEY)-4)}')
print(f'      ✓ App Secret: {"*" * len(ALI_APP_SECRET)}')
print(f'      ✓ Tracking  : {ALI_TRACKING or "(not set — optional for browsing)"}')

# ── 2. Check requests is available ───────────────────────────────────────────
print('\n[2/4] Checking requests library...')
try:
    import requests
    print('      ✓ requests available')
except ImportError:
    print('      ✗ requests not installed. Run: pip install -r requirements.txt')
    sys.exit(1)

# ── 3. Attempt a real API call ────────────────────────────────────────────────
print('\n[3/4] Making a test API call to AliExpress...')

import hashlib, hmac, time

GATEWAY = 'https://api-sg.aliexpress.com/sync'

def sign(params, secret):
    sorted_params = sorted(params.items())
    base = ''.join(f'{k}{v}' for k, v in sorted_params)
    return hmac.new(secret.encode(), base.encode(), hashlib.sha256).hexdigest().upper()

ts = str(int(time.time() * 1000))
params = {
    'app_key':    ALI_APP_KEY,
    'timestamp':  ts,
    'sign_method':'hmac-sha256',
    'method':     'aliexpress.affiliate.product.query',
    'tracking_id': ALI_TRACKING or 'default',
    'keywords':   'dress',
    'page_no':    '1',
    'page_size':  '3',
    'currency':   'USD',
    'ship_to_country': 'US',
    'fields':     'product_id,product_title,target_sale_price,product_main_image_url',
}
params['sign'] = sign(params, ALI_APP_SECRET)

try:
    resp = requests.get(GATEWAY, params=params, timeout=15)
    body = resp.json()
except Exception as e:
    print(f'      ✗ Network error: {e}')
    sys.exit(1)

resp_key = 'aliexpress_affiliate_product_query_response'
result   = body.get(resp_key, {}).get('resp_result', {})
code     = result.get('resp_code')
msg      = result.get('resp_msg', '')

if code == 200:
    products = result.get('result', {}).get('products', {}).get('product', [])
    print(f'      ✓ API responded with code 200')
    print(f'      ✓ Got {len(products)} sample products')
else:
    print(f'      ✗ API error {code}: {msg}')
    print(f'\n      Full response:\n      {body}')
    sys.exit(1)

# ── 4. Print sample products ─────────────────────────────────────────────────
print('\n[4/4] Sample products returned:')
for i, p in enumerate(products[:3], 1):
    price = p.get('target_sale_price', 'N/A')
    name  = p.get('product_title', 'N/A')[:60]
    print(f'      {i}. {name}...')
    print(f'         Price: {price}')

print('\n✓ All checks passed — AliExpress API is working!\n')
print('Next step: python importer.py')
