import os
import json
import html

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

# Shared Global Header Component (Using clean relative links)
def get_header(active_page=""):
    return f"""  <header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="brand" aria-label="Calculatorship Homepage">
        <img src="logo-light.svg" alt="Calculatorship Logo" width="220" height="38">
      </a>
      <nav class="main-nav" aria-label="Primary Navigation">
        <div class="nav-dropdown">
          <a href="index.html" class="nav-dropdown-toggle">Calculators</a>
          <ul class="nav-dropdown-menu" role="menu">
            <li><a href="index.html">SIP Calculator</a></li>
            <li><a href="lumpsum.html">Lumpsum Calculator</a></li>
            <li><a href="step-up.html">Step-Up SIP</a></li>
            <li><a href="goal.html">Goal Planner</a></li>
            <li class="nav-dropdown-divider" role="separator"></li>
            <li><a href="fd-calculator.html">FD Calculator</a></li>
            <li><a href="budget-planner.html">Budget Planner</a></li>
            <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
          </ul>
        </div>
        <a href="blog.html" class="{'active' if active_page == 'blog' else ''}">Blog</a>
        <a href="about.html" class="{'active' if active_page == 'about' else ''}">About</a>
        <a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a>
      </nav>
      <div class="header-actions">
        <button class="nav-toggle" id="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>"""

# Shared Contained Global Footer (Using logo-footer.svg and relative links)
def get_footer():
    return """  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html"><img src="logo-footer.svg" alt="Calculatorship Logo" width="200" height="36" style="display:block;"></a>
          <p class="footer-tagline">Independent financial calculators and educational guides for Indian investors, salaried professionals, and wealth builders.</p>
        </div>
        <div class="footer-links">
          <div class="footer-col">
            <h4>Calculators</h4>
            <ul>
              <li><a href="index.html">SIP Calculator</a></li>
              <li><a href="lumpsum.html">Lumpsum Calculator</a></li>
              <li><a href="step-up.html">Step-Up SIP</a></li>
              <li><a href="goal.html">Goal Planner</a></li>
              <li><a href="fd-calculator.html">FD Calculator</a></li>
              <li><a href="budget-planner.html">Budget Planner</a></li>
              <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Legal &amp; Policy</h4>
            <ul>
              <li><a href="disclaimer.html">Disclaimer</a></li>
              <li><a href="terms.html">Terms of Use</a></li>
              <li><a href="privacy.html">Privacy Policy</a></li>
              <li><a href="cookies.html">Cookie Policy</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Platform</h4>
            <ul>
              <li><a href="about.html">About Us</a></li>
              <li><a href="contact.html">Contact Us</a></li>
              <li><a href="blog.html">Blog &amp; Guides</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-disclaimer">
          <strong>Important Regulatory Notice:</strong> Calculatorship is an independent financial education platform not affiliated with or registered under SEBI, AMFI, or RBI. All content and calculation tools are strictly for informational and educational purposes. Nothing on this website constitutes personalized financial, investment, tax, or legal advice. Mutual fund investments are subject to market risks. Calculatorship and its authors shall not be liable for any financial decisions or losses arising from use of this website.
        </div>
        <div class="footer-copy">
          &copy; 2026 Calculatorship. All rights reserved. | <a href="disclaimer.html">Disclaimer</a> | <a href="terms.html">Terms</a> | <a href="privacy.html">Privacy</a>
        </div>
      </div>
    </div>
  </footer>

  <button class="back-to-top" id="back-to-top" aria-label="Back to top">
    <svg viewBox="0 0 24 24" stroke-width="2.5" fill="none" stroke="currentColor"><polyline points="18 15 12 9 6 15"/></svg>
  </button>

  <!-- Google Analytics 4 (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0C93Q0VBQP"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0C93Q0VBQP');
  </script>
  <script src="theme.js"></script>"""

# Import the 25 articles from generate_final_site.py
from generate_final_site import ARTICLES_DATA

def build_article_page(a):
    faq_schema = []
    faq_html = []
    for q, ans in a.get("faqs", []):
        faq_schema.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": ans}
        })
        faq_html.append(f"""
          <details class="faq-item" style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:12px;">
            <summary style="font-weight:700; cursor:pointer; font-size:0.98rem; color:var(--text-primary);">{html.escape(q)}</summary>
            <p style="margin-top:12px; color:var(--text-secondary); line-height:1.6; margin-bottom:0;">{ans}</p>
          </details>
        """)

    toc_html = ""
    if a.get("toc"):
        toc_items = "".join([f'<li><a href="#{tid}">{title}</a></li>' for tid, title in a["toc"]])
        toc_html = f"""
        <div class="toc-box">
          <h4 style="font-size:0.95rem; margin:0 0 10px; color:var(--text-primary);">Table of Contents</h4>
          <ol style="margin:0; padding-left:20px; line-height:1.8;">{toc_items}</ol>
        </div>
        """

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": a["title"],
                "description": a["metaDesc"],
                "url": a['slug'],
                "datePublished": "2026-08-01",
                "dateModified": "2026-08-22",
                "author": {"@type": "Organization", "name": "Calculatorship Research Desk"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Calculatorship",
                    "logo": {"@type": "ImageObject", "url": "logo-light.svg"}
                },
                "image": "og-image.webp",
                "mainEntityOfPage": a['slug']
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "index.html"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "blog.html"},
                    {"@type": "ListItem", "position": 3, "name": a["title"], "item": a['slug']}
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_schema
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(a['title'])} | Calculatorship</title>
  <meta name="description" content="{html.escape(a['metaDesc'])}">
  <link rel="canonical" href="{a['slug']}">
  <meta property="og:title" content="{html.escape(a['title'])}">
  <meta property="og:description" content="{html.escape(a['metaDesc'])}">
  <meta property="og:url" content="{a['slug']}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="og-image.webp">
  <meta property="article:published_time" content="2026-08-01">
  <meta property="article:modified_time" content="2026-08-22">
  <meta property="article:author" content="Calculatorship Research Desk">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(a['title'])}">
  <meta name="twitter:image" content="og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" media="print" onload="this.media='all'" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap"></noscript>
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json.dumps(schema_json, indent=2)}
  </script>
</head>
<body>

  <div class="reading-progress-bar" id="reading-progress"></div>
  <a class="skip-link" href="#main-content">Skip to content</a>

{get_header(active_page="blog")}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li aria-current="page">{html.escape(a['title'])}</li>
      </ol>
    </nav>
  </div>

  <main id="main-content">

    <div class="article-header">
      <div class="article-meta">
        <span class="meta-cat">{html.escape(a['cat'])}</span>
        <span>August 2026 Edition</span>
      </div>
      <h1>{html.escape(a['h1'])}</h1>
      <p style="font-size:1.05rem; color:var(--text-secondary); line-height:1.7;">{a['intro']}</p>
    </div>

    <!-- Clean Disclaimer Banner -->
    <div class="disclaimer-banner" data-banner-id="{a['slug']}">
      <div>
        <span class="disc-badge">Educational</span>
        <span>All calculations and articles are strictly for informational and educational purposes. Projected figures represent mathematical illustrations and not guaranteed returns. Please consult a SEBI-registered financial advisor before making investment decisions.</span>
      </div>
      <button class="disc-dismiss" type="button">Dismiss</button>
    </div>

    <!-- Top AdSense Slot -->
    <div class="ad-slot ad-slot-banner" style="max-width:1200px; margin:16px auto 28px;">
      <span class="ad-label">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <div class="article-page">
      <article class="article-main">

        <!-- Regulatory Notice Box -->
        <div style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-left:4px solid var(--emerald-dark); border-radius:var(--radius-md); padding:16px 20px; margin:0 0 24px;">
          <div style="font-weight:700; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.06em; color:var(--emerald-dark); margin-bottom:6px;">Regulatory &amp; Editorial Notice</div>
          <p style="font-size:0.84rem; color:var(--text-secondary); line-height:1.6; margin:0;">Calculatorship is an independent financial education portal not affiliated with or registered under SEBI, AMFI, or RBI. Content published here is for general financial literacy only and does not constitute personalized investment, tax, or legal advice. Mutual fund investments are subject to market risks.</p>
        </div>

        <div class="article-byline">
          <span>Published by <span class="byline-author">Calculatorship Research Desk</span></span>
          <span style="color:var(--border-medium);">&bull;</span>
          <span>Verified for Indian Regulatory Guidelines</span>
          <span style="color:var(--border-medium);">&bull;</span>
          <span>Updated August 2026</span>
        </div>

        {toc_html}

        {a['content']}

        <!-- Mid-Article Ad Slot -->
        <div class="ad-slot ad-slot-inline">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
        </div>

        <!-- Share Buttons -->
        <div class="share-buttons">
          <span class="share-label">Share Guide:</span>
          <a href="https://wa.me/?text={html.escape(a['title'])}" target="_blank" rel="noopener" class="share-btn wa">
            WhatsApp
          </a>
          <button class="share-btn cp" data-url="{a['slug']}">
            Copy Link
          </button>
        </div>

        <!-- FAQ Section -->
        <section id="faq" style="margin-top:32px;">
          <h2>Frequently Asked Questions</h2>
          {"".join(faq_html)}
        </section>

        <!-- CTA Box -->
        <div class="cta-box">
          <h3>Put This Knowledge Into Action</h3>
          <p>Test real-world financial projections with our free, independent, and accurate calculators.</p>
          <a href="index.html" class="btn btn-primary btn-lg">Explore Calculators &rarr;</a>
        </div>

        <p style="font-size:0.8rem; color:var(--text-muted); border-top:1px solid var(--border-soft); padding-top:16px; margin-top:24px; text-align:center;"><em>For educational purposes only. Not financial advice. Consult a SEBI-registered advisor before investing.</em></p>

      </article>

      <!-- Sidebar -->
      <aside class="article-sidebar">
        <div style="background:var(--bg-card); border:1px solid var(--border-soft); border-radius:var(--radius-lg); padding:24px; box-shadow:var(--shadow-sm); margin-bottom:24px;">
          <h4 style="font-size:0.86rem; text-transform:uppercase; letter-spacing:0.06em; color:var(--text-muted); margin:0 0 16px;">Featured Calculators</h4>
          <div style="display:flex; flex-direction:column; gap:10px;">
            <a href="index.html" class="btn btn-primary" style="font-size:0.88rem;">SIP Calculator</a>
            <a href="lumpsum.html" class="btn btn-ghost" style="font-size:0.88rem;">Lumpsum Calculator</a>
            <a href="step-up.html" class="btn btn-ghost" style="font-size:0.88rem;">Step-Up SIP</a>
            <a href="goal.html" class="btn btn-ghost" style="font-size:0.88rem;">Goal Planner</a>
            <a href="income-tax-calculator.html" class="btn btn-ghost" style="font-size:0.88rem;">Tax Calculator</a>
            <a href="fd-calculator.html" class="btn btn-ghost" style="font-size:0.88rem;">FD Calculator</a>
          </div>
        </div>
        <div class="ad-slot">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
        </div>
      </aside>
    </div>

  </main>

{get_footer()}
</body>
</html>"""

def generate_blog_index(articles):
    cards_html = []
    for a in articles:
        cards_html.append(f"""
        <article class="calc-link-card" data-category="{html.escape(a['cat'])}" style="background:var(--bg-card); padding:24px;">
          <div>
            <span class="meta-cat" style="margin-bottom:12px; display:inline-block;">{html.escape(a['cat'])}</span>
            <h3 style="font-size:1.15rem; font-weight:700; margin-bottom:10px; line-height:1.4;"><a href="{a['slug']}" style="color:var(--text-primary); text-decoration:none;">{html.escape(a['title'])}</a></h3>
            <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:16px;">{html.escape(a['metaDesc'])}</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border-soft); padding-top:12px;">
            <span style="font-size:0.80rem; color:var(--text-muted);">August 2026</span>
            <a href="{a['slug']}" style="font-weight:700; font-size:0.85rem; color:var(--emerald-dark);">Read Guide &rarr;</a>
          </div>
        </article>
        """)

    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog &amp; Financial Educational Guides | Calculatorship</title>
  <meta name="description" content="In-depth financial education guides for Indian investors. Master SIP compounding, mutual funds, tax planning under Section 80C, salary budgeting, and retirement calculations.">
  <link rel="canonical" href="blog.html">
  <meta property="og:title" content="Blog & Financial Educational Guides | Calculatorship">
  <meta property="og:description" content="Comprehensive financial education guides for Indian investors. SIPs, mutual funds, tax planning, and retirement.">
  <meta property="og:url" content="blog.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="og-image.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" media="print" onload="this.media='all'" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap"></noscript>
  <link rel="stylesheet" href="style.css">
  <style>
    .blog-controls {{
      max-width: 1200px;
      margin: 0 auto 32px;
      padding: 0 24px;
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: space-between;
      align-items: center;
    }}
    .blog-search {{
      flex: 1;
      min-width: 260px;
      max-width: 400px;
      position: relative;
    }}
    .blog-search input {{
      width: 100%;
      padding: 12px 16px 12px 40px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-soft);
      background: var(--bg-card);
      color: var(--text-primary);
      font-size: 0.92rem;
    }}
    .blog-search svg {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}
    .blog-filters {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .filter-btn {{
      padding: 8px 16px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-soft);
      background: var(--bg-card);
      color: var(--text-secondary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--emerald-dark);
      color: #ffffff;
      border-color: var(--emerald-dark);
    }}
    .blog-grid {{
      max-width: 1200px;
      margin: 0 auto 64px;
      padding: 0 24px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 24px;
    }}
  </style>
</head>
<body>

  <div class="reading-progress-bar" id="reading-progress"></div>
  <a class="skip-link" href="#main-content">Skip to content</a>

{get_header(active_page="blog")}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">Blog</li>
      </ol>
    </nav>
  </div>

  <main id="main-content">

    <div class="calc-hero">
      <h1>Blog &amp; Financial Educational Guides</h1>
      <p>Data-driven, compliant financial literacy guides designed for Indian salaried professionals and wealth builders.</p>
    </div>

    <!-- Clean Disclaimer Banner -->
    <div class="disclaimer-banner" data-banner-id="blog-index">
      <div>
        <span class="disc-badge">Educational Notice</span>
        <span>All articles are strictly for informational and literacy purposes. Mutual fund investments are subject to market risks. Please consult a SEBI-registered financial advisor before investing.</span>
      </div>
      <button class="disc-dismiss" type="button">Dismiss</button>
    </div>

    <div class="blog-controls">
      <div class="blog-search">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="blog-search-input" placeholder="Search guides by keyword..." aria-label="Search articles">
      </div>
      <div class="blog-filters">
        <button class="filter-btn active" data-cat="all">All Topics</button>
        <button class="filter-btn" data-cat="SIP &amp; Mutual Funds">SIP &amp; Mutual Funds</button>
        <button class="filter-btn" data-cat="Tax Planning">Tax Planning</button>
        <button class="filter-btn" data-cat="Budgeting &amp; Savings">Budgeting</button>
        <button class="filter-btn" data-cat="Fixed Deposits">Fixed Deposits</button>
        <button class="filter-btn" data-cat="Retirement Planning">Retirement</button>
        <button class="filter-btn" data-cat="Goal Planning">Goal Planning</button>
      </div>
    </div>

    <div class="blog-grid" id="blog-grid">
      {"".join(cards_html)}
    </div>

  </main>

{get_footer()}

  <script>
    const searchInput = document.getElementById('blog-search-input');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.blog-grid article');

    let currentCat = 'all';
    let currentQuery = '';

    function filterCards() {{
      cards.forEach(card => {{
        const cat = card.getAttribute('data-category');
        const text = card.textContent.toLowerCase();
        const matchesCat = currentCat === 'all' || cat.includes(currentCat);
        const matchesQuery = currentQuery === '' || text.includes(currentQuery);

        if (matchesCat && matchesQuery) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    filterBtns.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCat = btn.getAttribute('data-cat');
        filterCards();
      }});
    }});

    if (searchInput) {{
      searchInput.addEventListener('input', (e) => {{
        currentQuery = e.target.value.toLowerCase().trim();
        filterCards();
      }});
    }}
  </script>
</body>
</html>"""

def build_info_pages():
    # about.html
    about_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Calculatorship: Mission, Principles &amp; Editorial Standards</title>
  <meta name="description" content="Learn about Calculatorship — India's independent financial education and calculation platform. Transparent mathematical models and financial literacy.">
  <link rel="canonical" href="about.html">
  <meta property="og:title" content="About Calculatorship">
  <meta property="og:description" content="Independent financial tools and education for Indian investors.">
  <meta property="og:url" content="about.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header(active_page="about")}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">About Us</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>About Calculatorship</h1>
      <p>Democratizing financial mathematics and empowering Indian investors with transparent, independent calculation tools.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:860px; margin:0 auto; padding:40px;">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>Our Mission</h2>
          <p>Calculatorship was founded to provide transparent, mathematically accurate, and independent financial calculation tools and educational resources for Indian retail investors, salaried professionals, and families.</p>
          
          <h2>Regulatory Status &amp; SEBI Non-Registration Disclosure</h2>
          <div style="background:var(--bg-elevated); border-left:4px solid var(--emerald-dark); padding:16px 20px; border-radius:var(--radius-sm); margin:20px 0;">
            <p style="margin:0; font-size:0.92rem; color:var(--text-primary);"><strong>Notice:</strong> Calculatorship is strictly a financial education and calculation portal. We are <strong>not registered as an Investment Advisor or Research Analyst under the Securities and Exchange Board of India (SEBI)</strong>. We do not sell mutual fund schemes, distribute insurance products, or provide personalized stock or portfolio recommendations.</p>
          </div>

          <h2>Editorial &amp; Calculation Standards</h2>
          <p>All financial calculators on this website use standard compound interest, annuity, and Indian tax formulae defined by regulatory and academic standards. Projections are strictly mathematical models based on user-supplied assumptions and do not guarantee actual portfolio outcomes.</p>

          <h2>Contact &amp; Inquiries</h2>
          <p>For questions, editorial corrections, or feedback, please reach out to us via our <a href="contact.html" style="color:var(--emerald-dark); font-weight:700;">Contact Page</a>.</p>
        </div>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_html)

    # contact.html
    contact_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us | Calculatorship</title>
  <meta name="description" content="Contact the Calculatorship team for support, calculation inquiries, editorial corrections, or partnership questions.">
  <link rel="canonical" href="contact.html">
  <meta property="og:title" content="Contact Us | Calculatorship">
  <meta property="og:description" content="Get in touch with the Calculatorship team.">
  <meta property="og:url" content="contact.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header(active_page="contact")}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">Contact Us</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Contact Us</h1>
      <p>Have questions, feedback, or calculator feature requests? We would love to hear from you.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:640px; margin:0 auto; padding:36px;">
        <form id="contact-form">
          <div class="calc-field-group">
            <label for="name" style="font-weight:700; font-size:0.92rem; display:block; margin-bottom:8px;">Your Full Name</label>
            <div class="calc-input-box">
              <input type="text" id="name" placeholder="Rahul Sharma" style="text-align:left; font-family:var(--font-sans); font-size:0.95rem; font-weight:500;" required>
            </div>
          </div>
          <div class="calc-field-group">
            <label for="email" style="font-weight:700; font-size:0.92rem; display:block; margin-bottom:8px;">Email Address</label>
            <div class="calc-input-box">
              <input type="email" id="email" placeholder="rahul@example.com" style="text-align:left; font-family:var(--font-sans); font-size:0.95rem; font-weight:500; width:100%; border:none; outline:none; background:transparent;" required>
            </div>
          </div>
          <div class="calc-field-group">
            <label for="subject" style="font-weight:700; font-size:0.92rem; display:block; margin-bottom:8px;">Subject</label>
            <div class="calc-input-box">
              <input type="text" id="subject" placeholder="Calculator Feedback / Inquiry" style="text-align:left; font-family:var(--font-sans); font-size:0.95rem; font-weight:500;" required>
            </div>
          </div>
          <div class="calc-field-group">
            <label for="message" style="font-weight:700; font-size:0.92rem; display:block; margin-bottom:8px;">Your Message</label>
            <textarea id="message" rows="5" placeholder="Write your message here..." style="width:100%; background:var(--bg-elevated); border:1.5px solid var(--border-soft); border-radius:var(--radius-md); padding:12px; font-family:var(--font-sans); font-size:0.95rem; outline:none;" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-lg" style="width:100%; border-radius:var(--radius-md);">Send Message</button>
        </form>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(contact_html)

    # disclaimer.html
    disclaimer_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer &amp; Terms of Limitation | Calculatorship</title>
  <meta name="description" content="Important regulatory disclaimer and SEBI non-registration disclosure for Calculatorship.">
  <link rel="canonical" href="disclaimer.html">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header()}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">Disclaimer</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Important Legal Disclaimer</h1>
      <p>Please read these regulatory disclosures carefully before utilizing Calculatorship tools.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:860px; margin:0 auto; padding:40px;">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>1. General Educational Purpose</h2>
          <p>All calculators, numerical simulations, and articles published on Calculatorship are provided strictly for general informational, educational, and financial literacy purposes. Nothing contained on this website constitutes personalized financial advice, investment advisory services, legal advice, or tax consulting.</p>

          <h2>2. SEBI Non-Registration Notice</h2>
          <p>Calculatorship, its website creators, and contributors are <strong>not registered as Investment Advisers or Research Analysts under the Securities and Exchange Board of India (SEBI) Regulations</strong>. We do not recommend, endorse, or promote any specific mutual fund schemes, stocks, securities, or financial products.</p>

          <h2>3. Market Risk Disclosure</h2>
          <p>Mutual fund investments are subject to market risks. Read all scheme-related documents carefully before investing. Past performance is not an indicator of future returns.</p>

          <h2>4. Limitation of Liability</h2>
          <p>Calculatorship makes no warranties regarding the accuracy, completeness, or suitability of calculations. Calculatorship and its operators shall not be liable for any direct, indirect, or consequential financial losses arising from actions taken based on calculations on this website.</p>
        </div>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "disclaimer.html"), "w", encoding="utf-8") as f:
        f.write(disclaimer_html)

    # terms.html
    terms_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Use | Calculatorship</title>
  <meta name="description" content="Terms of Use governing the access and usage of Calculatorship calculators and guides.">
  <link rel="canonical" href="terms.html">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header()}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">Terms of Use</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Terms of Use</h1>
      <p>Terms governing your access to and utilization of the Calculatorship platform.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:860px; margin:0 auto; padding:40px;">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>1. Acceptance of Terms</h2>
          <p>By accessing or using Calculatorship, you agree to be bound by these Terms of Use and our Disclaimer. If you do not agree, please discontinue use immediately.</p>

          <h2>2. Use of Calculation Tools</h2>
          <p>Calculators are provided free of charge for personal, non-commercial educational use. Automated scraping, reverse-engineering, or unauthorized commercial reproduction of calculation code without explicit written consent is strictly prohibited.</p>

          <h2>3. Intellectual Property</h2>
          <p>All content, branding, logos, calculation scripts, and written guides are the intellectual property of Calculatorship and protected under Indian copyright laws.</p>
        </div>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "terms.html"), "w", encoding="utf-8") as f:
        f.write(terms_html)

    # privacy.html
    privacy_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Calculatorship</title>
  <meta name="description" content="Privacy Policy for Calculatorship explaining data collection, Google AdSense cookies, and analytics.">
  <link rel="canonical" href="privacy.html">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header()}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">Privacy Policy</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Privacy Policy</h1>
      <p>How Calculatorship protects your privacy and handles web analytics data.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:860px; margin:0 auto; padding:40px;">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>1. Information We Collect</h2>
          <p>Calculatorship does not require user registration or personal account creation. Financial inputs entered into our calculator sliders are processed locally in your web browser and are never transmitted to or stored on our servers.</p>

          <h2>2. Cookies &amp; Advertising (Google AdSense)</h2>
          <p>We use Google AdSense to serve advertisements when you visit our website. Google and its partner advertising networks use cookies (such as the DoubleClick cookie) to serve ads based on prior visits to our site or other websites across the Internet.</p>

          <h2>3. Web Analytics (Google Analytics 4)</h2>
          <p>We utilize Google Analytics 4 (GA4) to aggregate anonymized usage data (such as page views and browser types) to improve site performance and user experience.</p>
        </div>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "privacy.html"), "w", encoding="utf-8") as f:
        f.write(privacy_html)

    # cookies.html
    cookies_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Calculatorship</title>
  <meta name="description" content="Cookie Policy explaining how cookies and local storage are utilized on Calculatorship.">
  <link rel="canonical" href="cookies.html">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="reading-progress-bar" id="reading-progress"></div>
{get_header()}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol><li><a href="index.html">Home</a></li><li aria-current="page">Cookie Policy</li></ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Cookie Policy</h1>
      <p>Explanation of cookies and web storage technologies utilized on this website.</p>
    </div>

    <div class="calc-main-container">
      <div class="calc-card" style="max-width:860px; margin:0 auto; padding:40px;">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>1. What Are Cookies?</h2>
          <p>Cookies are small text files stored on your browser to enhance website functionality and collect anonymized analytics data.</p>

          <h2>2. How We Use Cookies</h2>
          <p>We use essential cookies to remember disclaimer dismissal preferences (via browser localStorage), analytics cookies (GA4), and advertising cookies (Google AdSense).</p>
        </div>
      </div>
    </div>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "cookies.html"), "w", encoding="utf-8") as f:
        f.write(cookies_html)

    # 404.html
    not_found_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Not Found (404) | Calculatorship</title>
  <meta name="robots" content="noindex, follow">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
{get_header()}
  <main id="main-content" style="text-align:center; padding:80px 24px;">
    <h1 style="font-size:3rem; font-weight:800; color:var(--text-primary); margin-bottom:12px;">404 - Page Not Found</h1>
    <p style="font-size:1.1rem; color:var(--text-secondary); max-width:500px; margin:0 auto 28px;">The page or calculator you are looking for does not exist or has been moved.</p>
    <a href="index.html" class="btn btn-primary btn-lg">Return to Homepage &rarr;</a>
  </main>
{get_footer()}
</body>
</html>"""
    with open(os.path.join(SITE_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(not_found_html)

def generate_sitemap(articles):
    core_urls = [
        ("index.html", "1.0", "daily"),
        ("lumpsum.html", "0.9", "weekly"),
        ("step-up.html", "0.9", "weekly"),
        ("goal.html", "0.9", "weekly"),
        ("fd-calculator.html", "0.9", "weekly"),
        ("budget-planner.html", "0.9", "weekly"),
        ("income-tax-calculator.html", "0.9", "weekly"),
        ("blog.html", "0.9", "daily"),
        ("about.html", "0.7", "monthly"),
        ("contact.html", "0.7", "monthly"),
        ("disclaimer.html", "0.5", "monthly"),
        ("terms.html", "0.5", "monthly"),
        ("privacy.html", "0.5", "monthly"),
        ("cookies.html", "0.5", "monthly"),
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    for url, prio, freq in core_urls:
        xml.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    for a in articles:
        xml.append(f"""  <url>
    <loc>{a['slug']}</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    xml.append('</urlset>')
    return "\n".join(xml)

def main():
    print(f"Building {len(ARTICLES_DATA)} humanized, exhaustive articles...")
    for a in ARTICLES_DATA:
        html_out = build_article_page(a)
        filepath = os.path.join(SITE_DIR, a["slug"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"Generated: {a['slug']}")

    print("\nGenerating blog.html...")
    blog_html = generate_blog_index(ARTICLES_DATA)
    with open(os.path.join(SITE_DIR, "blog.html"), "w", encoding="utf-8") as f:
        f.write(blog_html)
    print(f"Generated: blog.html")

    print("\nGenerating Info & Legal pages...")
    build_info_pages()
    print("Generated all info and legal pages.")

    print("\nGenerating sitemap.xml...")
    sitemap_xml = generate_sitemap(ARTICLES_DATA)
    with open(os.path.join(SITE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"Generated: sitemap.xml")

if __name__ == "__main__":
    main()
