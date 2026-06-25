"""
Lightweight Flask API — serves products.json to the frontend.

Endpoints:
  GET /api/products              →  paginated list (status=active)
  GET /api/products/<id>         →  single product
  GET /api/categories            →  distinct categories + counts
  GET /api/stats                 →  deal engine stats (for the dashboard widget)
  POST /api/import/trigger       →  trigger an immediate import run (internal use)
"""

import json
import os
import sys
import threading
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

from db import init_db, get_active_products, get_conn
from importer import run as import_run

app = Flask(__name__)
CORS(app)  # allow the HTML frontend (file://) to call the API


# ── Products ──────────────────────────────────────────────────────────────────

@app.get('/api/products')
def list_products():
    page     = max(1, int(request.args.get('page', 1)))
    per_page = min(100, int(request.args.get('per_page', 24)))
    category = request.args.get('category')
    min_margin = request.args.get('min_margin', type=float)
    tag      = request.args.get('tag')

    offset   = (page - 1) * per_page
    products = get_active_products(
        limit=per_page, offset=offset,
        category=category, min_margin=min_margin,
    )

    # Tag filter (done in Python since tags are JSON-encoded in SQLite)
    if tag:
        products = [p for p in products if tag in json.loads(p.get('tags') or '[]')]

    # Parse JSON fields for the response
    for p in products:
        p['tags']         = json.loads(p.get('tags') or '[]')
        p['extra_images'] = json.loads(p.get('extra_images') or '[]')

    return jsonify({'products': products, 'page': page, 'per_page': per_page})


@app.get('/api/products/<product_id>')
def get_product(product_id):
    with get_conn() as conn:
        row = conn.execute(
            'SELECT * FROM products WHERE id = ? AND status = "active"',
            (product_id,)
        ).fetchone()
    if not row:
        abort(404)
    p = dict(row)
    p['tags']         = json.loads(p.get('tags') or '[]')
    p['extra_images'] = json.loads(p.get('extra_images') or '[]')
    return jsonify(p)


# ── Categories ────────────────────────────────────────────────────────────────

@app.get('/api/categories')
def list_categories():
    with get_conn() as conn:
        rows = conn.execute('''
            SELECT category, COUNT(*) as count
            FROM products WHERE status = "active"
            GROUP BY category ORDER BY count DESC
        ''').fetchall()
    return jsonify([dict(r) for r in rows])


# ── Stats ─────────────────────────────────────────────────────────────────────

@app.get('/api/stats')
def stats():
    with get_conn() as conn:
        total = conn.execute(
            'SELECT COUNT(*) FROM products WHERE status = "active"'
        ).fetchone()[0]
        avg_margin = conn.execute(
            'SELECT AVG(margin_pct) FROM products WHERE status = "active"'
        ).fetchone()[0]
        today_imports = conn.execute('''
            SELECT SUM(inserted) FROM import_log
            WHERE run_at >= date("now")
        ''').fetchone()[0]
        source_counts = conn.execute('''
            SELECT source, COUNT(*) as cnt
            FROM products WHERE status = "active"
            GROUP BY source
        ''').fetchall()

    return jsonify({
        'total_products':   total,
        'avg_margin_pct':   round(avg_margin or 0, 1),
        'deals_today':      today_imports or 0,
        'sources_scanned':  12000,  # representative figure — replace with real crawler metric
        'sources':          {r['source']: r['cnt'] for r in source_counts},
    })


# ── Import trigger (background thread) ───────────────────────────────────────

_import_lock = threading.Lock()

@app.post('/api/import/trigger')
def trigger_import():
    if not _import_lock.acquire(blocking=False):
        return jsonify({'status': 'already_running'}), 409
    def _run():
        try:
            import_run()
        finally:
            _import_lock.release()
    threading.Thread(target=_run, daemon=True).start()
    return jsonify({'status': 'started'})


# ── Boot ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    print('[server] running on http://localhost:5000')
    app.run(host='0.0.0.0', port=5000, debug=False)
