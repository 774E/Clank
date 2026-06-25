"""
SQLite layer — products, import_log, price_history tables.
"""

import sqlite3
import os
import json
from datetime import datetime
from config import DB_PATH


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA foreign_keys=ON')
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS products (
                id              TEXT PRIMARY KEY,
                source          TEXT NOT NULL,          -- 'cj' | 'aliexpress'
                source_id       TEXT NOT NULL,
                name            TEXT NOT NULL,
                brand           TEXT,
                category        TEXT,
                cost_usd        REAL NOT NULL,          -- supplier price
                retail_usd      REAL NOT NULL,          -- our listed price
                original_usd    REAL,                   -- supplier's "original" (for strikethrough)
                margin_pct      REAL NOT NULL,
                discount_pct    REAL,
                rating          REAL,
                orders          INTEGER,
                image_url       TEXT,
                extra_images    TEXT,                   -- JSON array
                product_url     TEXT,
                tags            TEXT,                   -- JSON array
                status          TEXT DEFAULT 'active',  -- active | paused | delisted
                imported_at     TEXT NOT NULL,
                updated_at      TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_products_status   ON products(status);
            CREATE INDEX IF NOT EXISTS idx_products_margin   ON products(margin_pct DESC);
            CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);

            CREATE TABLE IF NOT EXISTS price_history (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id  TEXT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
                cost_usd    REAL NOT NULL,
                retail_usd  REAL NOT NULL,
                recorded_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS import_log (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                run_at      TEXT NOT NULL,
                source      TEXT NOT NULL,
                fetched     INTEGER DEFAULT 0,
                passed      INTEGER DEFAULT 0,
                inserted    INTEGER DEFAULT 0,
                updated     INTEGER DEFAULT 0,
                errors      INTEGER DEFAULT 0,
                notes       TEXT
            );
        ''')
    print(f'[db] initialised → {DB_PATH}')


def upsert_product(p: dict) -> str:
    """Insert or update a product. Returns 'inserted' | 'updated' | 'skipped'."""
    now = datetime.utcnow().isoformat()
    pid = f"{p['source']}_{p['source_id']}"

    with get_conn() as conn:
        existing = conn.execute(
            'SELECT id, cost_usd FROM products WHERE id = ?', (pid,)
        ).fetchone()

        if existing:
            if existing['cost_usd'] == p['cost_usd']:
                return 'skipped'
            conn.execute('''
                UPDATE products SET
                    name=?, brand=?, category=?, cost_usd=?, retail_usd=?,
                    original_usd=?, margin_pct=?, discount_pct=?, rating=?,
                    orders=?, image_url=?, extra_images=?, product_url=?,
                    tags=?, updated_at=?
                WHERE id=?
            ''', (
                p['name'], p.get('brand'), p.get('category'),
                p['cost_usd'], p['retail_usd'], p.get('original_usd'),
                p['margin_pct'], p.get('discount_pct'), p.get('rating'),
                p.get('orders'), p.get('image_url'),
                json.dumps(p.get('extra_images', [])),
                p.get('product_url'),
                json.dumps(p.get('tags', [])),
                now, pid
            ))
            conn.execute(
                'INSERT INTO price_history (product_id, cost_usd, retail_usd, recorded_at) VALUES (?,?,?,?)',
                (pid, p['cost_usd'], p['retail_usd'], now)
            )
            return 'updated'
        else:
            conn.execute('''
                INSERT INTO products
                    (id, source, source_id, name, brand, category, cost_usd,
                     retail_usd, original_usd, margin_pct, discount_pct, rating,
                     orders, image_url, extra_images, product_url, tags,
                     imported_at, updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                pid, p['source'], p['source_id'], p['name'], p.get('brand'),
                p.get('category'), p['cost_usd'], p['retail_usd'],
                p.get('original_usd'), p['margin_pct'], p.get('discount_pct'),
                p.get('rating'), p.get('orders'), p.get('image_url'),
                json.dumps(p.get('extra_images', [])),
                p.get('product_url'),
                json.dumps(p.get('tags', [])),
                now, now
            ))
            return 'inserted'


def log_run(source, fetched, passed, inserted, updated, errors, notes=''):
    now = datetime.utcnow().isoformat()
    with get_conn() as conn:
        conn.execute('''
            INSERT INTO import_log
                (run_at, source, fetched, passed, inserted, updated, errors, notes)
            VALUES (?,?,?,?,?,?,?,?)
        ''', (now, source, fetched, passed, inserted, updated, errors, notes))


def get_active_products(limit=500, offset=0, category=None, min_margin=None):
    q = 'SELECT * FROM products WHERE status = "active"'
    params = []
    if category:
        q += ' AND category = ?'
        params.append(category)
    if min_margin:
        q += ' AND margin_pct >= ?'
        params.append(min_margin)
    q += ' ORDER BY margin_pct DESC, orders DESC LIMIT ? OFFSET ?'
    params += [limit, offset]
    with get_conn() as conn:
        return [dict(r) for r in conn.execute(q, params).fetchall()]
