<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CLANK — Editorial Commerce</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --black: #0a0a0a;
      --off-white: #f5f3ef;
      --warm-gray: #c8c4bc;
      --accent: #b8a68a;
      --accent-dark: #8c7a62;
      --red: #c0392b;
      --text: #1a1a1a;
      --muted: #888;
      --border: #e0ddd8;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Inter', sans-serif;
      background: var(--off-white);
      color: var(--text);
      font-size: 13px;
      letter-spacing: 0.01em;
      overflow-x: hidden;
    }

    /* ── MARQUEE TICKER ── */
    .ticker {
      background: var(--black);
      color: var(--off-white);
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 8px 0;
      overflow: hidden;
      white-space: nowrap;
    }
    .ticker-inner {
      display: inline-block;
      animation: marquee 28s linear infinite;
    }
    .ticker-inner span { margin: 0 48px; }
    @keyframes marquee {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }

    /* ── NAV ── */
    nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(245, 243, 239, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 48px;
      height: 64px;
    }
    .nav-logo {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 300;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--black);
      text-decoration: none;
    }
    .nav-links {
      display: flex;
      gap: 36px;
      list-style: none;
    }
    .nav-links a {
      font-size: 10px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--accent-dark); }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 24px;
    }
    .nav-actions button {
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text);
      font-size: 10px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      transition: color 0.2s;
    }
    .nav-actions button:hover { color: var(--accent-dark); }
    .cart-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .badge-dot {
      width: 16px; height: 16px;
      background: var(--black);
      color: var(--off-white);
      border-radius: 50%;
      font-size: 9px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* ── HERO ── */
    .hero {
      display: grid;
      grid-template-columns: 1fr 1fr;
      min-height: calc(100vh - 88px);
    }
    .hero-left {
      background: var(--black);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 72px 64px;
      position: relative;
      overflow: hidden;
    }
    .hero-left::before {
      content: '';
      position: absolute;
      inset: 0;
      background: url('https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=900&q=80&auto=format') center/cover no-repeat;
      opacity: 0.45;
    }
    .hero-label {
      position: relative;
      font-size: 9px;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--warm-gray);
      margin-bottom: 20px;
    }
    .hero-heading {
      position: relative;
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(52px, 7vw, 88px);
      font-weight: 300;
      line-height: 0.95;
      color: #fff;
      margin-bottom: 32px;
    }
    .hero-heading em { font-style: italic; color: var(--accent); }
    .hero-sub {
      position: relative;
      color: var(--warm-gray);
      font-size: 12px;
      line-height: 1.7;
      max-width: 340px;
      margin-bottom: 40px;
    }
    .btn-primary {
      position: relative;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: var(--off-white);
      color: var(--black);
      border: none;
      padding: 14px 28px;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      transition: background 0.25s, color 0.25s;
      text-decoration: none;
      width: fit-content;
    }
    .btn-primary:hover { background: var(--accent); color: #fff; }
    .btn-primary svg { transition: transform 0.25s; }
    .btn-primary:hover svg { transform: translateX(4px); }

    .hero-right {
      display: grid;
      grid-template-rows: 1fr 1fr;
      gap: 2px;
      background: var(--border);
    }
    .hero-card {
      background: var(--off-white);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    .hero-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .hero-card:hover img { transform: scale(1.04); }
    .hero-card-label {
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: var(--off-white);
      padding: 6px 12px;
      font-size: 9px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }
    .new-badge {
      position: absolute;
      top: 16px;
      right: 16px;
      background: var(--red);
      color: #fff;
      font-size: 8px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 4px 8px;
    }

    /* ── SECTION HEADERS ── */
    .section-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      padding: 64px 48px 32px;
    }
    .section-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 40px;
      font-weight: 300;
      letter-spacing: 0.05em;
    }
    .section-title em { font-style: italic; color: var(--accent-dark); }
    .section-link {
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      text-decoration: none;
      border-bottom: 1px solid var(--border);
      padding-bottom: 2px;
      transition: color 0.2s, border-color 0.2s;
    }
    .section-link:hover { color: var(--text); border-color: var(--text); }

    /* ── PRODUCT GRID ── */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2px;
      background: var(--border);
      margin: 0 48px;
    }
    .product-card {
      background: var(--off-white);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    .product-card:hover .product-actions { opacity: 1; transform: translateY(0); }
    .product-card:hover .product-img { transform: scale(1.04); }

    .product-img-wrap {
      aspect-ratio: 3/4;
      overflow: hidden;
      background: #e8e5e0;
    }
    .product-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.55s ease;
      display: block;
    }
    .product-tag {
      position: absolute;
      top: 12px;
      left: 12px;
      font-size: 8px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 4px 8px;
    }
    .tag-sale { background: var(--red); color: #fff; }
    .tag-new  { background: var(--black); color: var(--off-white); }
    .tag-hot  { background: var(--accent); color: #fff; }

    .product-info {
      padding: 16px 16px 20px;
    }
    .product-brand {
      font-size: 9px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 4px;
    }
    .product-name {
      font-family: 'Cormorant Garamond', serif;
      font-size: 17px;
      font-weight: 400;
      margin-bottom: 8px;
      line-height: 1.3;
    }
    .product-price {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .price-current { font-weight: 500; font-size: 13px; }
    .price-original {
      font-size: 11px;
      color: var(--muted);
      text-decoration: line-through;
    }
    .price-save {
      font-size: 9px;
      color: var(--red);
      letter-spacing: 0.1em;
    }

    .product-actions {
      position: absolute;
      bottom: 72px;
      left: 0; right: 0;
      display: flex;
      gap: 2px;
      padding: 0 16px;
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 0.25s, transform 0.25s;
    }
    .btn-add {
      flex: 1;
      background: var(--black);
      color: var(--off-white);
      border: none;
      padding: 10px;
      font-size: 9px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      transition: background 0.2s;
    }
    .btn-add:hover { background: var(--accent-dark); }
    .btn-wish {
      background: var(--off-white);
      border: 1px solid var(--border);
      padding: 10px 12px;
      cursor: pointer;
      transition: background 0.2s;
      color: var(--text);
    }
    .btn-wish:hover { background: var(--border); }

    /* ── DEALS BANNER ── */
    .deals-banner {
      margin: 48px;
      background: var(--black);
      display: grid;
      grid-template-columns: 1fr 1fr;
      overflow: hidden;
      min-height: 320px;
    }
    .deals-text {
      padding: 56px 56px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .deals-label {
      font-size: 9px;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 16px;
    }
    .deals-heading {
      font-family: 'Cormorant Garamond', serif;
      font-size: 52px;
      font-weight: 300;
      line-height: 1;
      color: #fff;
      margin-bottom: 16px;
    }
    .deals-heading em { font-style: italic; color: var(--accent); }
    .deals-desc {
      color: var(--warm-gray);
      font-size: 12px;
      line-height: 1.7;
      margin-bottom: 32px;
      max-width: 320px;
    }
    .deals-countdown {
      display: flex;
      gap: 24px;
      margin-bottom: 36px;
    }
    .countdown-unit { text-align: center; }
    .countdown-num {
      font-family: 'Cormorant Garamond', serif;
      font-size: 36px;
      font-weight: 300;
      color: #fff;
      line-height: 1;
      display: block;
    }
    .countdown-label {
      font-size: 8px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      display: block;
      margin-top: 4px;
    }
    .countdown-sep {
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      color: var(--accent);
      align-self: flex-start;
      padding-top: 2px;
    }
    .btn-ghost {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: transparent;
      color: var(--off-white);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 13px 28px;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      transition: border-color 0.25s, background 0.25s;
      width: fit-content;
    }
    .btn-ghost:hover { border-color: var(--accent); background: rgba(184,166,138,0.1); }

    .deals-image {
      position: relative;
      overflow: hidden;
    }
    .deals-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.7;
    }
    .deals-image-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, var(--black) 0%, transparent 40%);
    }

    /* ── CATEGORIES ── */
    .categories {
      padding: 0 48px;
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 2px;
      background: var(--border);
    }
    .category-card {
      background: var(--off-white);
      position: relative;
      overflow: hidden;
      aspect-ratio: 1;
      cursor: pointer;
    }
    .category-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.55s ease;
    }
    .category-card:hover img { transform: scale(1.06); }
    .category-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 50%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 20px;
    }
    .category-name {
      font-family: 'Cormorant Garamond', serif;
      font-size: 18px;
      font-weight: 400;
      color: #fff;
      margin-bottom: 2px;
    }
    .category-count {
      font-size: 9px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.6);
    }

    /* ── AUTO-IMPORT STATUS ── */
    .auto-import {
      margin: 48px;
      background: var(--off-white);
      border: 1px solid var(--border);
      padding: 40px 48px;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 32px;
      align-items: center;
    }
    .auto-import-left {}
    .ai-label {
      font-size: 9px;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--accent-dark);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pulse-dot {
      width: 7px; height: 7px;
      background: #27ae60;
      border-radius: 50%;
      position: relative;
    }
    .pulse-dot::after {
      content: '';
      position: absolute;
      inset: -3px;
      border-radius: 50%;
      background: #27ae60;
      opacity: 0.35;
      animation: pulse 1.8s ease-in-out infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.35; }
      50%       { transform: scale(1.7); opacity: 0; }
    }
    .ai-heading {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 300;
      margin-bottom: 8px;
    }
    .ai-desc {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.7;
      max-width: 560px;
    }
    .ai-stats {
      display: flex;
      gap: 40px;
    }
    .ai-stat {}
    .ai-stat-num {
      font-family: 'Cormorant Garamond', serif;
      font-size: 36px;
      font-weight: 300;
      color: var(--black);
      display: block;
    }
    .ai-stat-label {
      font-size: 9px;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--muted);
    }

    /* ── NEWSLETTER ── */
    .newsletter {
      background: var(--black);
      padding: 80px 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    .newsletter-label {
      font-size: 9px;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 16px;
    }
    .newsletter-heading {
      font-family: 'Cormorant Garamond', serif;
      font-size: 48px;
      font-weight: 300;
      color: #fff;
      line-height: 1.1;
      margin-bottom: 12px;
    }
    .newsletter-heading em { font-style: italic; color: var(--accent); }
    .newsletter-sub {
      color: var(--warm-gray);
      font-size: 12px;
      line-height: 1.7;
      margin-bottom: 36px;
    }
    .newsletter-form {
      display: flex;
      gap: 0;
      max-width: 440px;
      width: 100%;
    }
    .newsletter-form input {
      flex: 1;
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.15);
      border-right: none;
      color: #fff;
      padding: 14px 20px;
      font-size: 12px;
      font-family: 'Inter', sans-serif;
      outline: none;
      transition: border-color 0.2s;
    }
    .newsletter-form input::placeholder { color: rgba(255,255,255,0.3); }
    .newsletter-form input:focus { border-color: var(--accent); }
    .newsletter-form button {
      background: var(--accent);
      color: #fff;
      border: none;
      padding: 14px 24px;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      transition: background 0.25s;
      white-space: nowrap;
    }
    .newsletter-form button:hover { background: var(--accent-dark); }

    /* ── FOOTER ── */
    footer {
      background: var(--off-white);
      border-top: 1px solid var(--border);
      padding: 56px 48px 32px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 48px;
      margin-bottom: 48px;
    }
    .footer-brand {
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      font-weight: 300;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }
    .footer-tagline {
      font-size: 11px;
      color: var(--muted);
      line-height: 1.7;
      max-width: 260px;
    }
    .footer-col-title {
      font-size: 9px;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: var(--black);
      margin-bottom: 16px;
    }
    .footer-links { list-style: none; }
    .footer-links li { margin-bottom: 8px; }
    .footer-links a {
      font-size: 12px;
      color: var(--muted);
      text-decoration: none;
      transition: color 0.2s;
    }
    .footer-links a:hover { color: var(--text); }
    .footer-bottom {
      border-top: 1px solid var(--border);
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .footer-copy {
      font-size: 10px;
      color: var(--muted);
      letter-spacing: 0.05em;
    }
    .footer-legal {
      display: flex;
      gap: 24px;
    }
    .footer-legal a {
      font-size: 10px;
      color: var(--muted);
      text-decoration: none;
      transition: color 0.2s;
    }
    .footer-legal a:hover { color: var(--text); }

    /* ── RESPONSIVE ── */
    @media (max-width: 1100px) {
      .product-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 860px) {
      .hero { grid-template-columns: 1fr; min-height: auto; }
      .hero-right { grid-template-rows: 240px; grid-template-columns: 1fr 1fr; }
      nav { padding: 0 24px; }
      .nav-links { display: none; }
      .product-grid { grid-template-columns: repeat(2, 1fr); margin: 0 24px; }
      .section-header { padding: 48px 24px 24px; }
      .categories { grid-template-columns: repeat(3, 1fr); padding: 0 24px; }
      .deals-banner { grid-template-columns: 1fr; margin: 24px; }
      .deals-image { display: none; }
      .auto-import { margin: 24px; padding: 28px; grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; gap: 32px; }
    }
  </style>
</head>
<body>

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-inner">
    <span>Free shipping on orders over $75</span>
    <span>·</span>
    <span>New deals imported every hour</span>
    <span>·</span>
    <span>AI-curated selection — best price guaranteed</span>
    <span>·</span>
    <span>Free returns within 30 days</span>
    <span>·</span>
    <span>Free shipping on orders over $75</span>
    <span>·</span>
    <span>New deals imported every hour</span>
    <span>·</span>
    <span>AI-curated selection — best price guaranteed</span>
    <span>·</span>
    <span>Free returns within 30 days</span>
    <span>·</span>
  </div>
</div>

<!-- NAV -->
<nav>
  <a class="nav-logo" href="#">Clank</a>
  <ul class="nav-links">
    <li><a href="#">New In</a></li>
    <li><a href="#">Clothing</a></li>
    <li><a href="#">Accessories</a></li>
    <li><a href="#">Deals</a></li>
    <li><a href="#">Brands</a></li>
    <li><a href="#">Sale</a></li>
  </ul>
  <div class="nav-actions">
    <button>Search</button>
    <button>Account</button>
    <button class="cart-badge">
      Bag
      <span class="badge-dot">3</span>
    </button>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-left">
    <p class="hero-label">SS26 — Editorial Drop</p>
    <h1 class="hero-heading">
      Wear<br /><em>the world</em><br />differently.
    </h1>
    <p class="hero-sub">
      AI-sourced. Human-curated. Every piece selected for quality, price, and presence — refreshed hourly from global suppliers.
    </p>
    <a class="btn-primary" href="#">
      Explore Collection
      <svg width="16" height="10" viewBox="0 0 16 10" fill="none">
        <path d="M1 5h14M10 1l4 4-4 4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
  </div>
  <div class="hero-right">
    <div class="hero-card">
      <img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=700&q=80&auto=format" alt="Look 1" />
      <span class="hero-card-label">Outerwear</span>
      <span class="new-badge">New</span>
    </div>
    <div class="hero-card">
      <img src="https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=700&q=80&auto=format" alt="Look 2" />
      <span class="hero-card-label">Accessories</span>
    </div>
  </div>
</section>

<!-- TRENDING -->
<div class="section-header">
  <h2 class="section-title">Trending <em>Now</em></h2>
  <a class="section-link" href="#">View All →</a>
</div>
<div class="product-grid" id="trending-grid">

  <!-- Product 1 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600&q=80&auto=format" alt="Oversized Wool Coat" />
    </div>
    <span class="product-tag tag-hot">Hot</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Studio Oslo</p>
      <p class="product-name">Oversized Wool Coat</p>
      <div class="product-price">
        <span class="price-current">$189</span>
        <span class="price-original">$320</span>
        <span class="price-save">−41%</span>
      </div>
    </div>
  </div>

  <!-- Product 2 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1544441893-675973e31985?w=600&q=80&auto=format" alt="Structured Blazer" />
    </div>
    <span class="product-tag tag-new">New</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Maison Vell</p>
      <p class="product-name">Structured Double-Breasted Blazer</p>
      <div class="product-price">
        <span class="price-current">$245</span>
      </div>
    </div>
  </div>

  <!-- Product 3 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600&q=80&auto=format" alt="Minimalist Sneakers" />
    </div>
    <span class="product-tag tag-sale">Sale</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Form Studio</p>
      <p class="product-name">Minimalist Low-Top Sneakers</p>
      <div class="product-price">
        <span class="price-current">$88</span>
        <span class="price-original">$145</span>
        <span class="price-save">−39%</span>
      </div>
    </div>
  </div>

  <!-- Product 4 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80&auto=format" alt="Satin Slip Dress" />
    </div>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Atelier Soir</p>
      <p class="product-name">Bias-Cut Satin Slip Dress</p>
      <div class="product-price">
        <span class="price-current">$162</span>
        <span class="price-original">$210</span>
        <span class="price-save">−23%</span>
      </div>
    </div>
  </div>

</div>

<!-- DEALS BANNER -->
<div class="deals-banner">
  <div class="deals-text">
    <p class="deals-label">Flash Deals — Ends Soon</p>
    <h2 class="deals-heading">Up to <em>70% off</em><br />today only.</h2>
    <p class="deals-desc">Our AI scans thousands of suppliers every hour. When prices drop, we pass the savings directly to you.</p>
    <div class="deals-countdown">
      <div class="countdown-unit">
        <span class="countdown-num" id="cd-h">08</span>
        <span class="countdown-label">Hours</span>
      </div>
      <span class="countdown-sep">:</span>
      <div class="countdown-unit">
        <span class="countdown-num" id="cd-m">34</span>
        <span class="countdown-label">Min</span>
      </div>
      <span class="countdown-sep">:</span>
      <div class="countdown-unit">
        <span class="countdown-num" id="cd-s">17</span>
        <span class="countdown-label">Sec</span>
      </div>
    </div>
    <button class="btn-ghost">
      Shop Flash Deals
      <svg width="16" height="10" viewBox="0 0 16 10" fill="none">
        <path d="M1 5h14M10 1l4 4-4 4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>
  <div class="deals-image">
    <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800&q=80&auto=format" alt="Deals" />
    <div class="deals-image-overlay"></div>
  </div>
</div>

<!-- CATEGORIES -->
<div class="section-header">
  <h2 class="section-title">Shop by <em>Category</em></h2>
  <a class="section-link" href="#">All Categories →</a>
</div>
<div class="categories">
  <div class="category-card">
    <img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400&q=80&auto=format" alt="Dresses" />
    <div class="category-overlay">
      <p class="category-name">Dresses</p>
      <p class="category-count">248 items</p>
    </div>
  </div>
  <div class="category-card">
    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80&auto=format" alt="Menswear" />
    <div class="category-overlay">
      <p class="category-name">Menswear</p>
      <p class="category-count">312 items</p>
    </div>
  </div>
  <div class="category-card">
    <img src="https://images.unsplash.com/photo-1547949003-9792a18a2601?w=400&q=80&auto=format" alt="Bags" />
    <div class="category-overlay">
      <p class="category-name">Bags</p>
      <p class="category-count">184 items</p>
    </div>
  </div>
  <div class="category-card">
    <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&q=80&auto=format" alt="Footwear" />
    <div class="category-overlay">
      <p class="category-name">Footwear</p>
      <p class="category-count">207 items</p>
    </div>
  </div>
  <div class="category-card">
    <img src="https://images.unsplash.com/photo-1492707892479-7bc8d5a4ee93?w=400&q=80&auto=format" alt="Jewellery" />
    <div class="category-overlay">
      <p class="category-name">Jewellery</p>
      <p class="category-count">93 items</p>
    </div>
  </div>
</div>

<!-- NEW ARRIVALS -->
<div class="section-header">
  <h2 class="section-title">New <em>Arrivals</em></h2>
  <a class="section-link" href="#">View All →</a>
</div>
<div class="product-grid" id="arrivals-grid" style="margin-bottom:0">

  <!-- Product 5 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=600&q=80&auto=format" alt="Knit Cardigan" />
    </div>
    <span class="product-tag tag-new">New</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Knitwear Co.</p>
      <p class="product-name">Open-Stitch Merino Cardigan</p>
      <div class="product-price">
        <span class="price-current">$118</span>
      </div>
    </div>
  </div>

  <!-- Product 6 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=600&q=80&auto=format" alt="Trench Coat" />
    </div>
    <span class="product-tag tag-hot">Hot</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Revere Paris</p>
      <p class="product-name">Classic Belted Trench Coat</p>
      <div class="product-price">
        <span class="price-current">$299</span>
        <span class="price-original">$450</span>
        <span class="price-save">−34%</span>
      </div>
    </div>
  </div>

  <!-- Product 7 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1554568218-0f1715e72254?w=600&q=80&auto=format" alt="Leather Tote" />
    </div>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">Grain & Hide</p>
      <p class="product-name">Full-Grain Leather Tote</p>
      <div class="product-price">
        <span class="price-current">$220</span>
        <span class="price-original">$280</span>
        <span class="price-save">−21%</span>
      </div>
    </div>
  </div>

  <!-- Product 8 -->
  <div class="product-card">
    <div class="product-img-wrap">
      <img class="product-img" src="https://images.unsplash.com/photo-1591185560567-9f3e7e1e3e1e?w=600&q=80&auto=format" alt="Wide Leg Trousers" />
    </div>
    <span class="product-tag tag-new">New</span>
    <div class="product-actions">
      <button class="btn-add">Add to Bag</button>
      <button class="btn-wish">♡</button>
    </div>
    <div class="product-info">
      <p class="product-brand">The Line</p>
      <p class="product-name">Pleated Wide-Leg Trousers</p>
      <div class="product-price">
        <span class="price-current">$134</span>
      </div>
    </div>
  </div>

</div>

<!-- AUTO-IMPORT STATUS -->
<div class="auto-import">
  <div class="auto-import-left">
    <div class="ai-label">
      <span class="pulse-dot"></span>
      AI Deal Engine — Live
    </div>
    <h3 class="ai-heading">Deals found automatically, 24/7.</h3>
    <p class="ai-desc">
      Our engine monitors thousands of suppliers, compares market prices, and imports only the products with verified margins and real discounts. Every listing you see has been algorithmically qualified — no filler, no fluff.
    </p>
  </div>
  <div class="ai-stats">
    <div class="ai-stat">
      <span class="ai-stat-num" id="stat-sources">12k+</span>
      <span class="ai-stat-label">Sources Scanned</span>
    </div>
    <div class="ai-stat">
      <span class="ai-stat-num" id="stat-deals">847</span>
      <span class="ai-stat-label">Deals Today</span>
    </div>
    <div class="ai-stat">
      <span class="ai-stat-num" id="stat-margin">38%</span>
      <span class="ai-stat-label">Avg. Margin</span>
    </div>
  </div>
</div>

<!-- NEWSLETTER -->
<div class="newsletter">
  <p class="newsletter-label">Inner Circle</p>
  <h2 class="newsletter-heading">Get the best deals<br /><em>before anyone else.</em></h2>
  <p class="newsletter-sub">Drop alerts, exclusive pricing, and editorial edits — straight to your inbox.</p>
  <div class="newsletter-form">
    <input type="email" placeholder="Your email address" />
    <button>Subscribe</button>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="footer-grid">
    <div>
      <div class="footer-brand">Clank</div>
      <p class="footer-tagline">AI-curated fashion commerce. The best deals from global suppliers, imported automatically and styled for you.</p>
    </div>
    <div>
      <p class="footer-col-title">Shop</p>
      <ul class="footer-links">
        <li><a href="#">New In</a></li>
        <li><a href="#">Clothing</a></li>
        <li><a href="#">Accessories</a></li>
        <li><a href="#">Footwear</a></li>
        <li><a href="#">Sale</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">Help</p>
      <ul class="footer-links">
        <li><a href="#">Shipping & Returns</a></li>
        <li><a href="#">Size Guide</a></li>
        <li><a href="#">Track Order</a></li>
        <li><a href="#">Contact Us</a></li>
        <li><a href="#">FAQ</a></li>
      </ul>
    </div>
    <div>
      <p class="footer-col-title">Company</p>
      <ul class="footer-links">
        <li><a href="#">About</a></li>
        <li><a href="#">Suppliers</a></li>
        <li><a href="#">Careers</a></li>
        <li><a href="#">Press</a></li>
        <li><a href="#">Sustainability</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">© 2026 Clank. All rights reserved.</p>
    <div class="footer-legal">
      <a href="#">Privacy Policy</a>
      <a href="#">Terms of Use</a>
      <a href="#">Cookie Settings</a>
    </div>
  </div>
</footer>

<script>
  const API = 'http://localhost:5000/api';

  // ── Countdown ────────────────────────────────────────────────────────────
  (function () {
    let total = 8 * 3600 + 34 * 60 + 17;
    const h = document.getElementById('cd-h');
    const m = document.getElementById('cd-m');
    const s = document.getElementById('cd-s');
    function pad(n) { return String(n).padStart(2, '0'); }
    setInterval(function () {
      if (total <= 0) return;
      total--;
      h.textContent = pad(Math.floor(total / 3600));
      m.textContent = pad(Math.floor((total % 3600) / 60));
      s.textContent = pad(total % 60);
    }, 1000);
  })();

  // ── Scroll-in animation ───────────────────────────────────────────────────
  const observer = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    }),
    { threshold: 0.08 }
  );
  function observeCards() {
    document.querySelectorAll('.product-card, .category-card').forEach(el => {
      if (el.dataset.observed) return;
      el.dataset.observed = '1';
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      observer.observe(el);
    });
  }
  observeCards();

  // ── Product card builder ──────────────────────────────────────────────────
  function tagClass(tags) {
    if (tags.includes('sale'))        return 'tag-sale';
    if (tags.includes('high-margin')) return 'tag-hot';
    return 'tag-new';
  }
  function tagLabel(tags) {
    if (tags.includes('sale'))        return 'Sale';
    if (tags.includes('bestseller'))  return 'Hot';
    return 'New';
  }
  function formatPrice(n) { return '$' + n.toFixed(0); }

  function buildCard(p) {
    const tags        = p.tags || [];
    const showTag     = tags.length > 0;
    const hasSale     = p.original_usd && p.original_usd > p.retail_usd;
    const discountPct = hasSale
      ? Math.round((p.original_usd - p.retail_usd) / p.original_usd * 100)
      : null;

    return `
      <div class="product-card" data-id="${p.id}">
        <div class="product-img-wrap">
          <img class="product-img" src="${p.image_url}" alt="${p.name}"
               onerror="this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80&auto=format'" />
        </div>
        ${showTag ? `<span class="product-tag ${tagClass(tags)}">${tagLabel(tags)}</span>` : ''}
        <div class="product-actions">
          <button class="btn-add" onclick="addToBag('${p.id}', event)">Add to Bag</button>
          <button class="btn-wish">♡</button>
        </div>
        <div class="product-info">
          <p class="product-brand">${p.brand || 'Imported'}</p>
          <p class="product-name">${p.name}</p>
          <div class="product-price">
            <span class="price-current">${formatPrice(p.retail_usd)}</span>
            ${hasSale ? `<span class="price-original">${formatPrice(p.original_usd)}</span>
                         <span class="price-save">−${discountPct}%</span>` : ''}
          </div>
        </div>
      </div>`;
  }

  // ── Load products from API ────────────────────────────────────────────────
  async function loadProducts(gridId, params = {}) {
    const grid = document.getElementById(gridId);
    if (!grid) return;
    try {
      const qs  = new URLSearchParams({ per_page: 4, ...params }).toString();
      const res = await fetch(`${API}/products?${qs}`);
      if (!res.ok) throw new Error(res.status);
      const { products } = await res.json();
      if (products && products.length) {
        grid.innerHTML = products.map(buildCard).join('');
        observeCards();
      }
    } catch {
      // API not running — keep the static demo cards
    }
  }

  // ── Load stats for the AI widget ─────────────────────────────────────────
  async function loadStats() {
    try {
      const res  = await fetch(`${API}/stats`);
      if (!res.ok) return;
      const data = await res.json();
      const el = id => document.getElementById(id);
      if (el('stat-sources')) el('stat-sources').textContent = (data.sources_scanned || 12000).toLocaleString() + '+';
      if (el('stat-deals'))   el('stat-deals').textContent   = (data.deals_today || 0).toLocaleString();
      if (el('stat-margin'))  el('stat-margin').textContent  = (data.avg_margin_pct || 0) + '%';
    } catch { /* server offline — static values shown */ }
  }

  // ── Cart (localStorage) ───────────────────────────────────────────────────
  function getCart()  { return JSON.parse(localStorage.getItem('clank_cart') || '[]'); }
  function saveCart(c){ localStorage.setItem('clank_cart', JSON.stringify(c)); }

  function addToBag(productId, e) {
    e.stopPropagation();
    const cart = getCart();
    if (!cart.includes(productId)) cart.push(productId);
    saveCart(cart);
    updateBadge();
    const btn = e.target;
    btn.textContent = 'Added ✓';
    setTimeout(() => btn.textContent = 'Add to Bag', 1400);
  }

  function updateBadge() {
    const dot = document.querySelector('.badge-dot');
    if (dot) dot.textContent = getCart().length;
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  updateBadge();
  loadProducts('trending-grid', { tag: 'bestseller' });
  loadProducts('arrivals-grid', { page: 2 });
  loadStats();
</script>
</body>
</html>
