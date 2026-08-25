import os
import json
import re
import datetime

from articles_data_group1 import GROUP1_ARTICLES
from articles_data_group2 import GROUP2_ARTICLES
from articles_data_group3 import GROUP3_ARTICLES
from articles_data_group4 import GROUP4_ARTICLES
from articles_data_group5 import GROUP5_ARTICLES
from articles_data_group6 import GROUP6_ARTICLES
from articles_data_group7 import GROUP7_ARTICLES

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

ALL_ARTICLES = (
    GROUP1_ARTICLES +
    GROUP2_ARTICLES +
    GROUP3_ARTICLES +
    GROUP4_ARTICLES +
    GROUP5_ARTICLES +
    GROUP6_ARTICLES +
    GROUP7_ARTICLES
)

print(f"Total Unique Articles to compile: {len(ALL_ARTICLES)}")

def format_display_date(iso_date_str):
    # iso_date_str: "2026-07-11" -> "11 Jul 2026"
    dt = datetime.datetime.strptime(iso_date_str, "%Y-%m-%d")
    return dt.strftime("%d %b %Y")

AUTHOR_BIO_HTML = """        <div class="author-bio-card">
          <div class="author-bio-header">
            <div class="author-avatar">T</div>
            <div>
              <h3 class="author-name">Tejas</h3>
              <p class="author-title">Finance Researcher &amp; Editor, Calculatorship</p>
            </div>
          </div>
          <p class="author-desc">Tejas researches SEBI guidelines, AMFI data, AMC reports, and RBI circulars to write plain-English financial guides for Indian retail investors. All content is for educational purposes and does not constitute SEBI-registered investment advice.</p>
        </div>"""

from enrich_articles_content import get_bespoke_deep_dive

def build_article_html(art):
    slug = art["slug"]
    title = art["title"]
    h1 = art["h1"]
    meta_desc = art["metaDesc"]
    cat = art["cat"]
    pub_date = art["pubDate"]
    mod_date = art.get("modDate", "2026-08-25")
    intro = art["intro"]
    toc = art["toc"]
    content = art["content"]
    if "Institutional Asset Allocation" not in content and "Strategic Tax Optimization" not in content and "Cash Flow Engineering" not in content and "Fixed Income Portfolio Architecture" not in content and "Retirement Corpus Engineering" not in content and "Mortgage Reduction Engineering" not in content and "Goal-Linked Wealth Engineering" not in content:
        content = content + "\n" + get_bespoke_deep_dive(slug, title, cat)
    faqs = art["faqs"]

    display_pub_date = format_display_date(pub_date)
    
    # JSON-LD Schema
    faq_entities = []
    for q, a in faqs:
        clean_a = re.sub(r'<[^>]+>', '', a)
        clean_q = re.sub(r'<[^>]+>', '', q)
        faq_entities.append({
            "@type": "Question",
            "name": clean_q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })
    
    schema_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title.split(" | ")[0],
                "description": meta_desc,
                "image": "https://calculatorship.in/og-image.png",
                "datePublished": f"{pub_date}T08:00:00+05:30",
                "dateModified": f"{mod_date}T12:00:00+05:30",
                "author": {
                    "@type": "Person",
                    "name": "Tejas",
                    "url": "https://calculatorship.in/about.html"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Calculatorship",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://calculatorship.in/logo-light.svg"
                    }
                },
                "mainEntityOfPage": f"https://calculatorship.in/{slug}"
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }
    schema_json_str = json.dumps(schema_obj, indent=2, ensure_ascii=False)

    # Table of Contents
    toc_items = []
    for anchor, label in toc:
        toc_items.append(f'<li><a href="#{anchor}">{label}</a></li>')
    toc_html = f"""        <div class="toc-box">
          <h2 style="font-size:1.05rem; font-weight:800; margin:0 0 12px; color:var(--text-primary);">Table of Contents</h2>
          <ol style="margin:0; padding-left:22px; line-height:1.9;">{''.join(toc_items)}</ol>
        </div>"""

    # FAQ HTML
    faq_items = []
    for q, a in faqs:
        faq_items.append(f"""          <details class="faq-item" style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:12px;">
            <summary style="font-weight:700; cursor:pointer; font-size:1.02rem; color:var(--text-primary);">{q}</summary>
            <p style="margin-top:12px; color:var(--text-secondary); line-height:1.65; margin-bottom:0;">{a}</p>
          </details>""")
    faq_html = "\n".join(faq_items)

    # Sidebar links
    sidebar_links = []
    # pick 8 other articles
    other_arts = [a for a in ALL_ARTICLES if a["slug"] != slug][:8]
    for oa in other_arts:
        short_title = oa["title"].split(" | ")[0]
        if len(short_title) > 55:
            short_title = short_title[:52] + "..."
        sidebar_links.append(f'<li><a href="{oa["slug"]}">{short_title}</a></li>')
    sidebar_links_html = "".join(sidebar_links)

    html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://calculatorship.in/{slug}">
  <meta property="og:title" content="{title.split(' | ')[0]}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://calculatorship.in/{slug}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://calculatorship.in/og-image.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://calculatorship.in/og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" media="print" onload="this.media='all'" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap"></noscript>
  <link rel="stylesheet" href="style.css?v=2.2">
  <script type="application/ld+json">
{schema_json_str}
  </script>
</head>
<body>

  <div class="reading-progress-bar" id="reading-progress"></div>
  <a class="skip-link" href="#main-article">Skip to article content</a>

  <header class="site-header">
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
            <li><a href="ppf-calculator.html">PPF Calculator</a></li>
            <li><a href="swp-calculator.html">SWP Calculator</a></li>
            <li><a href="emi-calculator.html">Loan EMI &amp; Prepay</a></li>
            <li class="nav-dropdown-divider" role="separator"></li>
            <li><a href="fd-calculator.html">FD Calculator</a></li>
            <li><a href="budget-planner.html">Budget Planner</a></li>
            <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
          </ul>
        </div>
        <a href="blog.html" class="active">Blog &amp; Guides</a>
        <a href="about.html" class="">About</a>
        <a href="contact.html" class="">Contact</a>
      </nav>
      <div class="header-actions">
        <button class="nav-toggle" id="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="blog.html">{cat}</a></li>
        <li aria-current="page">{title.split(' | ')[0][:45]}...</li>
      </ol>
    </nav>
  </div>

  <main id="main-content">

    <header class="article-header">
      <div class="article-meta">
        <span class="meta-cat">{cat}</span>
        <span class="article-date-tag">Published: {display_pub_date}</span>
        <span>Updated for FY 2026-27</span>
      </div>
      <h1>{h1}</h1>
      <p style="font-size:1.15rem; color:var(--text-secondary); line-height:1.7; max-width:980px; margin-top:12px;">{intro}</p>
      <div class="article-byline">
        <span class="byline-author">Tejas</span> | Published: {display_pub_date} | Verified Educational Resource
      </div>
    </header>

    <!-- Top In-Article AdSense -->
    <div class="ad-slot ad-slot-banner" style="max-width:1540px; margin:16px auto 28px; padding:0 36px;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <div class="article-page">
      
      <article class="article-main" id="main-article">
        
{toc_html}

{content}

        <!-- Mid-Article AdSense -->
        <div class="ad-slot ad-slot-infeed" style="margin:36px 0;">
          <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
        </div>

        <!-- FAQ Section -->
        <section id="faq" style="margin-top:40px;">
          <h2>Frequently Asked Questions</h2>
{faq_html}
        </section>

        <!-- Interactive Calculator CTA -->
        <div class="cta-box">
          <h3>Simulate Your Exact Financial Numbers</h3>
          <p>Use our free, fast, and independent calculators to model your wealth growth, SIP returns, or tax savings.</p>
          <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
            <a href="index.html" class="btn btn-primary btn-lg">SIP Calculator &rarr;</a>
            <a href="ppf-calculator.html" class="btn btn-ghost btn-lg">PPF Calculator &rarr;</a>
            <a href="swp-calculator.html" class="btn btn-ghost btn-lg">SWP Calculator &rarr;</a>
          </div>
        </div>

{AUTHOR_BIO_HTML}

        <div style="font-size:0.84rem; color:var(--text-muted); border-top:1px solid var(--border-soft); padding-top:20px; margin-top:36px; line-height:1.6;">
          <strong>Educational Disclaimer:</strong> All content, financial formulas, and scenario simulations published on Calculatorship are strictly for educational and informational purposes. They do not constitute personalized investment, tax, or legal advice. Mutual fund investments are subject to market risks. Please consult a SEBI-registered Investment Advisor (RIA) or Chartered Accountant before executing financial transactions.
        </div>
      </article>

      <!-- Sidebar -->
      <aside class="article-sidebar" aria-label="Related Guides">
        <div class="sidebar-card">
          <h3>Explore Related Guides</h3>
          <ul class="sidebar-links">
            {sidebar_links_html}
          </ul>
        </div>

        <!-- Sidebar AdSense Slot -->
        <div class="sidebar-card" style="padding:16px; text-align:center;">
          <span style="display:block; font-size:0.72rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:8px;">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
        </div>

        <div class="sidebar-card" style="background:var(--emerald-soft); border-color:var(--emerald-border);">
          <h3 style="color:var(--emerald-dark); border-color:var(--emerald-border);">Financial Calculators</h3>
          <p style="font-size:0.92rem; color:var(--text-secondary); margin-bottom:14px;">Instant math for smart wealth decisions in India.</p>
          <a href="index.html" class="btn btn-primary" style="width:100%; text-align:center; box-sizing:border-box;">Open All Calculators</a>
        </div>
      </aside>

    </div>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html"><img src="logo-footer.svg" alt="Calculatorship Logo" width="200" height="36" style="display:block;"></a>
          <p class="footer-tagline">Independent financial calculators and educational guides for Indian investors, salaried professionals, and wealth builders.</p>
        </div>
        <div class="footer-links">
          <div class="footer-col">
            <h3>Calculators</h3>
            <ul>
              <li><a href="index.html">SIP Calculator</a></li>
              <li><a href="lumpsum.html">Lumpsum Calculator</a></li>
              <li><a href="step-up.html">Step-Up SIP</a></li>
              <li><a href="goal.html">Goal Planner</a></li>
              <li><a href="ppf-calculator.html">PPF Calculator</a></li>
              <li><a href="swp-calculator.html">SWP Calculator</a></li>
              <li><a href="emi-calculator.html">Loan EMI &amp; Prepay</a></li>
              <li><a href="fd-calculator.html">FD Calculator</a></li>
              <li><a href="budget-planner.html">Budget Planner</a></li>
              <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h3>Legal &amp; Policy</h3>
            <ul>
              <li><a href="disclaimer.html">Disclaimer</a></li>
              <li><a href="terms.html">Terms of Use</a></li>
              <li><a href="privacy.html">Privacy Policy</a></li>
              <li><a href="cookies.html">Cookie Policy</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h3>Platform</h3>
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
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0C93Q0VBQP');
  </script>
  <script src="theme.js?v=2.2"></script>

</body>
</html>
"""
    return html

def build_blog_hub(articles):
    total_count = len(articles)
    
    # Sort articles descending by publication date (newest first)
    sorted_articles = sorted(articles, key=lambda x: x["pubDate"], reverse=True)
    
    # Generate cards
    cards_html = []
    for art in sorted_articles:
        slug = art["slug"]
        title = art["title"].split(" | ")[0]
        meta_desc = art["metaDesc"]
        cat = art["cat"]
        pub_date = art["pubDate"]
        display_date = format_display_date(pub_date)
        
        cards_html.append(f"""        <article class="blog-card" data-category="{cat}">
          <div class="blog-card-meta">
            <span class="meta-cat">{cat}</span>
            <span class="article-date-tag">Published: {display_date}</span>
          </div>
          <h2 class="blog-card-title"><a href="{slug}">{title}</a></h2>
          <p class="blog-card-excerpt">{meta_desc}</p>
          <div class="blog-card-footer">
            <a href="{slug}" class="blog-read-link">Read Full Guide &rarr;</a>
          </div>
        </article>""")
    
    blog_grid_content = "\n".join(cards_html)
    
    # Category counts
    cat_counts = {}
    for art in articles:
        c = art["cat"]
        cat_counts[c] = cat_counts.get(c, 0) + 1
    
    filter_pills = [f'<button class="filter-pill-btn active" data-category="All">All ({total_count})</button>']
    for cat_name, count in sorted(cat_counts.items()):
        filter_pills.append(f'<button class="filter-pill-btn" data-category="{cat_name}">{cat_name} ({count})</button>')
    filter_pills_html = "".join(filter_pills)
    
    html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Financial Planning &amp; Wealth Growth Guides | Calculatorship</title>
  <meta name="description" content="Explore {total_count} comprehensive, independent financial guides on SIPs, Mutual Funds, Income Tax, PPF, SWP, Home Loans, and Retirement Planning for Indian investors.">
  <link rel="canonical" href="https://calculatorship.in/blog.html">
  <meta property="og:title" content="Financial Planning &amp; Wealth Growth Guides | Calculatorship">
  <meta property="og:description" content="Explore {total_count} comprehensive, independent financial guides for Indian investors.">
  <meta property="og:url" content="https://calculatorship.in/blog.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://calculatorship.in/og-image.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://calculatorship.in/og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#F3F7F5">
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" media="print" onload="this.media='all'" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap"></noscript>
  <link rel="stylesheet" href="style.css?v=2.2">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Calculatorship",
    "url": "https://calculatorship.in/",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://calculatorship.in/logo-light.svg",
      "width": 220,
      "height": 40
    }}
  }}
  </script>

</head>
<body>

  <div class="reading-progress-bar" id="reading-progress"></div>

  <header class="site-header">
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
            <li><a href="ppf-calculator.html">PPF Calculator</a></li>
            <li><a href="swp-calculator.html">SWP Calculator</a></li>
            <li><a href="emi-calculator.html">Loan EMI &amp; Prepay</a></li>
            <li class="nav-dropdown-divider" role="separator"></li>
            <li><a href="fd-calculator.html">FD Calculator</a></li>
            <li><a href="budget-planner.html">Budget Planner</a></li>
            <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
          </ul>
        </div>
        <a href="blog.html" class="active">Blog &amp; Guides</a>
        <a href="about.html" class="">About</a>
        <a href="contact.html" class="">Contact</a>
      </nav>
      <div class="header-actions">
        <button class="nav-toggle" id="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">Blog &amp; Knowledge Hub</li>
      </ol>
    </nav>
  </div>

  <main id="main-content">
    <div class="calc-hero">
      <h1>Financial Planning &amp; Wealth Guides</h1>
      <p>Browse <strong id="total-articles-count" style="color:var(--emerald-dark); font-weight:800;">{total_count}</strong> mathematical, actionable, and independent guides written for Indian salaried professionals, investors, and retirees.</p>
    </div>

    <!-- Live Search & Category Filter Controls -->
    <div class="blog-controls-wrapper">
      <div class="blog-search-box">
        <svg class="blog-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="blogSearchInput" class="blog-search-input" placeholder="Search guides by title, category, or keyword (e.g. SWP, PPF, Section 80C, Home Loan)..." aria-label="Search financial guides">
        <button id="blogSearchClear" class="blog-search-clear" type="button" aria-label="Clear search">&times;</button>
      </div>

      <div class="blog-filter-pills" id="categoryFilterBar">
        {filter_pills_html}
      </div>

      <div class="blog-meta-stats">
        <span>Showing <strong id="visible-articles-count" style="color:var(--text-primary);">{total_count}</strong> of <span id="total-count-badge">{total_count}</span> comprehensive guides</span>
        <span style="font-size:0.85rem;">Updated for latest Indian Fiscal Rules &amp; Tax Laws</span>
      </div>
    </div>

    <!-- Top In-Blog AdSense -->
    <div class="ad-slot ad-slot-banner" style="max-width:1540px; margin:24px auto; padding:0 36px;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <!-- Blog Articles Grid -->
    <div class="blog-grid" id="blogGrid">
{blog_grid_content}
    </div>

    <!-- Bottom In-Blog AdSense -->
    <div class="ad-slot ad-slot-banner" style="max-width:1540px; margin:40px auto 24px; padding:0 36px;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <!-- Bottom CTA -->
    <div class="cta-box" style="max-width:1100px; margin:40px auto 60px;">
      <h3>Looking for Instant Financial Calculations?</h3>
      <p>Simulate your SIP returns, PPF growth, tax liabilities, or loan prepayment benefits with our free calculators.</p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin-top:16px;">
        <a href="index.html" class="btn btn-primary btn-lg">SIP Calculator &rarr;</a>
        <a href="income-tax-calculator.html" class="btn btn-ghost btn-lg">Tax Calculator &rarr;</a>
        <a href="ppf-calculator.html" class="btn btn-ghost btn-lg">PPF Calculator &rarr;</a>
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html"><img src="logo-footer.svg" alt="Calculatorship Logo" width="200" height="36" style="display:block;"></a>
          <p class="footer-tagline">Independent financial calculators and educational guides for Indian investors, salaried professionals, and wealth builders.</p>
        </div>
        <div class="footer-links">
          <div class="footer-col">
            <h3>Calculators</h3>
            <ul>
              <li><a href="index.html">SIP Calculator</a></li>
              <li><a href="lumpsum.html">Lumpsum Calculator</a></li>
              <li><a href="step-up.html">Step-Up SIP</a></li>
              <li><a href="goal.html">Goal Planner</a></li>
              <li><a href="ppf-calculator.html">PPF Calculator</a></li>
              <li><a href="swp-calculator.html">SWP Calculator</a></li>
              <li><a href="emi-calculator.html">Loan EMI &amp; Prepay</a></li>
              <li><a href="fd-calculator.html">FD Calculator</a></li>
              <li><a href="budget-planner.html">Budget Planner</a></li>
              <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h3>Legal &amp; Policy</h3>
            <ul>
              <li><a href="disclaimer.html">Disclaimer</a></li>
              <li><a href="terms.html">Terms of Use</a></li>
              <li><a href="privacy.html">Privacy Policy</a></li>
              <li><a href="cookies.html">Cookie Policy</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h3>Platform</h3>
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

  <!-- Interactive Search & Filter Client Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const searchInput = document.getElementById('blogSearchInput');
      const searchClear = document.getElementById('blogSearchClear');
      const filterPills = document.querySelectorAll('.filter-pill-btn');
      const cards = document.querySelectorAll('.blog-card');
      const visibleCountEl = document.getElementById('visible-articles-count');
      let activeCategory = 'All';

      function filterArticles() {{
        const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
        let visibleCount = 0;

        cards.forEach(card => {{
          const cardCat = card.getAttribute('data-category') || '';
          const title = (card.querySelector('.blog-card-title')?.innerText || '').toLowerCase();
          const excerpt = (card.querySelector('.blog-card-excerpt')?.innerText || '').toLowerCase();
          const matchesCat = (activeCategory === 'All' || cardCat === activeCategory);
          const matchesQuery = !query || title.includes(query) || excerpt.includes(query) || cardCat.toLowerCase().includes(query);

          if (matchesCat && matchesQuery) {{
            card.style.display = 'flex';
            visibleCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});

        if (visibleCountEl) visibleCountEl.textContent = visibleCount;
        if (searchClear) searchClear.style.display = query ? 'block' : 'none';
      }}

      filterPills.forEach(btn => {{
        btn.addEventListener('click', function() {{
          filterPills.forEach(b => b.classList.remove('active'));
          this.classList.add('active');
          activeCategory = this.getAttribute('data-category');
          filterArticles();
        }});
      }});

      if (searchInput) {{
        searchInput.addEventListener('input', filterArticles);
      }}

      if (searchClear) {{
        searchClear.addEventListener('click', function() {{
          searchInput.value = '';
          filterArticles();
          searchInput.focus();
        }});
      }}
    }});
  </script>

  <!-- Google Analytics 4 (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0C93Q0VBQP"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0C93Q0VBQP');
  </script>
  <script src="theme.js?v=2.2"></script>

</body>
</html>
"""
    return html

def build_sitemap_xml(articles):
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    # Core pages
    core_pages = [
        ("https://calculatorship.in/", "2026-08-25", "daily", "1.0"),
        ("https://calculatorship.in/blog.html", "2026-08-25", "daily", "0.9"),
        ("https://calculatorship.in/lumpsum.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/step-up.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/goal.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/ppf-calculator.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/swp-calculator.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/emi-calculator.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/fd-calculator.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/budget-planner.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/income-tax-calculator.html", "2026-08-25", "weekly", "0.9"),
        ("https://calculatorship.in/about.html", "2026-08-25", "monthly", "0.6"),
        ("https://calculatorship.in/contact.html", "2026-08-25", "monthly", "0.6"),
        ("https://calculatorship.in/disclaimer.html", "2026-08-25", "monthly", "0.4"),
        ("https://calculatorship.in/terms.html", "2026-08-25", "monthly", "0.4"),
        ("https://calculatorship.in/privacy.html", "2026-08-25", "monthly", "0.4"),
        ("https://calculatorship.in/cookies.html", "2026-08-25", "monthly", "0.4"),
    ]
    
    for url, lastmod, freq, priority in core_pages:
        xml_lines.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")
        
    for art in articles:
        slug = art["slug"]
        lastmod = art.get("modDate", "2026-08-25")
        xml_lines.append(f"""  <url>
    <loc>https://calculatorship.in/{slug}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
        
    xml_lines.append('</urlset>')
    return "\n".join(xml_lines)

# Execution
print(f"Compiling {len(ALL_ARTICLES)} articles...")
for art in ALL_ARTICLES:
    slug = art["slug"]
    filepath = os.path.join(SITE_DIR, slug)
    content = build_article_html(art)
    with open(filepath, "w", encoding="utf-8") as fp:
        fp.write(content)
    print(f"Generated: {slug} ({len(content)} bytes)")

# Compile blog.html
blog_content = build_blog_hub(ALL_ARTICLES)
with open(os.path.join(SITE_DIR, "blog.html"), "w", encoding="utf-8") as fp:
    fp.write(blog_content)
print(f"Generated blog.html ({len(blog_content)} bytes)")

# Compile sitemap.xml
sitemap_content = build_sitemap_xml(ALL_ARTICLES)
with open(os.path.join(SITE_DIR, "sitemap.xml"), "w", encoding="utf-8") as fp:
    fp.write(sitemap_content)
print(f"Generated sitemap.xml ({len(sitemap_content)} bytes)")

print("\n--- MASTER SITE BUILD COMPLETE ---")
