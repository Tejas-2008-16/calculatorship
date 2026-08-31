# TEMPLATE_SPEC.md — Calculatorship Site & Article Specifications

This internal reference document reverse-engineers and documents the exact structure, tags, markup, and conventions used across **calculatorship.in**. Every new article and page created on the platform must adhere to this specification byte-for-byte.

---

## 1. Global Metadata & Verification Tags

### 1.1 Google Verification, AdSense & Analytics
- **Google Site Verification:**
  ```html
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  ```
- **Google AdSense Publisher Meta & Script:**
  ```html
  <meta name="google-adsense-account" content="ca-pub-7598871729388798">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7598871729388798" crossorigin="anonymous"></script>
  ```
- **Google Analytics 4 (GA4):** Placed at bottom of `<body>` right before `theme.js`:
  ```html
  <!-- Google Analytics 4 (GA4) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0C93Q0VBQP"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0C93Q0VBQP');
  </script>
  <script src="theme.js?v=2.2"></script>
  ```

---

## 2. `<head>` Specification for Article Pages

```html
<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Title Under 65 chars] | Calculatorship</title>
  <meta name="description" content="[Compelling SEO description between 130 and 160 characters summarizing key calculations, rules, and takeaways.]">
  <link rel="canonical" href="https://www.calculatorship.in/[article-slug].html">
  <meta property="og:title" content="[Social Title - punchy and concise]">
  <meta property="og:description" content="[Social description under 150 characters.]">
  <meta property="og:url" content="https://www.calculatorship.in/[article-slug].html">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Calculatorship" />
  <meta property="og:image" content="https://calculatorship.in/og-image.webp">
  <meta property="og:image:alt" content="[Article Title] — Guide for Indian Investors on Calculatorship" />
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://calculatorship.in/og-image.webp">
  <meta name="robots" content="index, follow">
  <meta name="googlebot" content="index, follow">
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
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "[Article Headline]",
      "description": "[Article Description]",
      "image": "https://calculatorship.in/og-image.png",
      "datePublished": "2026-08-31T08:00:00+05:30",
      "dateModified": "2026-08-31T12:00:00+05:30",
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
      "mainEntityOfPage": "https://calculatorship.in/[article-slug].html"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "[Question 1]",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "[Answer 1]"
          }
        }
        /* 4 to 5 FAQ items */
      ]
    }
  ]
}
  </script>
</head>
```

---

## 3. Header, Navigation & Breadcrumbs

### 3.1 Header / Navigation Markup (Byte-for-byte exact)
```html
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
```

### 3.2 Breadcrumb Bar Markup
```html
  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li><a href="blog.html">Blog</a></li>
        <li><a href="blog.html">[Category Name]</a></li>
        <li aria-current="page">[Truncated Article Title / Short Title]...</li>
      </ol>
    </nav>
  </div>
```

---

## 4. Article Header & In-Article Ad Slots

### 4.1 Article Header & Hero
```html
  <main id="main-content">

    <header class="article-header">
      <div class="article-meta">
        <span class="meta-cat">[Category Name]</span>
        <span class="article-date-tag">Published: 31 Aug 2026</span>
        <span>Updated for FY 2026-27</span>
      </div>
      <h1>[Full H1 Article Title]</h1>
      <p style="font-size:1.15rem; color:var(--text-secondary); line-height:1.7; max-width:980px; margin-top:12px;">[Executive summary paragraph capturing core premise, mathematical insight, and regulatory context.]</p>
      <div class="article-byline">
        <span class="byline-author">Tejas</span> | Published: 31 Aug 2026 | Verified Educational Resource
      </div>
    </header>

    <!-- Top In-Article AdSense -->
    <div class="ad-slot ad-slot-banner" style="max-width:1540px; margin:16px auto 28px; padding:0 36px;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
```

### 4.2 Mid-Article AdSense Slot
Placed between major core sections:
```html
    <!-- Mid-Article AdSense -->
    <div class="ad-slot ad-slot-infeed" style="margin:36px 0;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
    </div>
```

---

## 5. Body Components & Styling Conventions

### 5.1 Main Article Layout Grid
```html
    <div class="article-page">
      <article class="article-main" id="main-article">
        ...
      </article>

      <!-- Sidebar -->
      <aside class="article-sidebar" aria-label="Related Guides">
        <div class="sidebar-card">
          <h3>Explore Related Guides</h3>
          <ul class="sidebar-links">
            <li><a href="...">...</a></li>
            <!-- 6 to 8 contextual links -->
          </ul>
        </div>

        <!-- Sidebar AdSense Slot -->
        <div class="sidebar-card" style="padding:16px; text-align:center;">
          <span style="display:block; font-size:0.72rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:8px;">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
        </div>

        <div class="sidebar-card" style="background:var(--emerald-soft); border-color:var(--emerald-border);">
          <h3 style="color:var(--emerald-dark); border-color:var(--emerald-border);">Financial Calculators</h3>
          <p style="font-size:0.92rem; color:var(--text-secondary); margin-bottom:14px;">Instant math for smart wealth decisions in India.</p>
          <a href="index.html" class="btn btn-primary" style="width:100%; text-align:center; box-sizing:border-box;">Open All Calculators</a>
        </div>
      </aside>
    </div>
```

### 5.2 Table of Contents (TOC)
```html
<div class="toc-box">
  <h2 style="font-size:1.05rem; font-weight:800; margin:0 0 12px; color:var(--text-primary);">Table of Contents</h2>
  <ol style="margin:0; padding-left:22px; line-height:1.9;">
    <li><a href="#section-1">1. Section Name</a></li>
    <li><a href="#section-2">2. Section Name</a></li>
    <li><a href="#section-3">3. Section Name</a></li>
    <li><a href="#faq">Frequently Asked Questions</a></li>
  </ol>
</div>
```

### 5.3 Educational Disclaimer Callout
```html
<div class="disclaimer-box" style="background:#fffbeb; border:2px solid #f59e0b; border-radius:12px; padding:20px 24px; margin:0 0 32px; display:flex; gap:16px; align-items:flex-start;">
  <span style="font-size:1.5rem; flex-shrink:0;">⚠️</span>
  <div>
    <strong style="color:#92400e; font-size:1rem; display:block; margin-bottom:6px;">Educational Content Only</strong>
    <p style="margin:0; font-size:0.93rem; color:#78350f; line-height:1.65;">This article is written by a personal finance researcher, not a SEBI-registered investment advisor or certified financial planner. The calculations and information provided here are strictly for educational and awareness purposes. Please consult a qualified SEBI-registered advisor or Chartered Accountant before making financial decisions.</p>
  </div>
</div>
```

### 5.4 Comparison & Data Tables
```html
<div class="table-wrapper">
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Dimension / Feature</th>
        <th>Option A</th>
        <th>Option B</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Key Parameter</td>
        <td>Value / Description</td>
        <td>Value / Description</td>
      </tr>
      <tr class="highlight-row">
        <td>Critical Highlight</td>
        <td>Advantage</td>
        <td>Disadvantage</td>
      </tr>
    </tbody>
  </table>
</div>
```

### 5.5 FAQ Section (Schema-Aligned Accordions)
```html
<section id="faq" style="margin-top:40px;">
  <h2>Frequently Asked Questions</h2>
  <details class="faq-item" style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:12px;">
    <summary style="font-weight:700; cursor:pointer; font-size:1.02rem; color:var(--text-primary);">[Question 1]?</summary>
    <p style="margin-top:12px; color:var(--text-secondary); line-height:1.65; margin-bottom:0;">[Concise, authoritative answer matching JSON-LD schema text.]</p>
  </details>
  <!-- 4 to 5 FAQ items -->
</section>
```

### 5.6 Related Calculator CTA Block
```html
<div class="cta-box">
  <h3>[Contextual CTA Headline, e.g. Simulate Your Tax Savings / Retirement Numbers]</h3>
  <p>[Description of how the calculator helps test personalized scenarios.]</p>
  <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
    <a href="[primary-calculator].html" class="btn btn-primary btn-lg">[Primary Calculator] &rarr;</a>
    <a href="[secondary-calculator].html" class="btn btn-ghost btn-lg">[Secondary Calculator] &rarr;</a>
    <a href="[tertiary-calculator].html" class="btn btn-ghost btn-lg">[Tertiary Calculator] &rarr;</a>
  </div>
</div>
```

### 5.7 Author Bio & Educational Bottom Disclaimer
```html
<div class="author-bio-card">
  <div class="author-bio-header">
    <div class="author-avatar">T</div>
    <div>
      <h3 class="author-name">Tejas</h3>
      <p class="author-title">Finance Researcher &amp; Editor, Calculatorship</p>
    </div>
  </div>
  <p class="author-desc">Tejas is the founder of Calculatorship and a self-taught personal finance enthusiast. He is not a SEBI-registered investment advisor, Chartered Accountant, or certified financial planner. All articles on this website are written for general educational awareness only, based on publicly available SEBI guidelines, AMFI data, and RBI circulars. Nothing written here should be treated as personalized financial advice. Always consult a qualified financial professional before making any investment decisions.</p>
</div>

<div style="font-size:0.84rem; color:var(--text-muted); border-top:1px solid var(--border-soft); padding-top:20px; margin-top:36px; line-height:1.6;">
  <strong>Educational Disclaimer:</strong> All content, financial formulas, and scenario simulations published on Calculatorship are strictly for educational and informational purposes. They do not constitute personalized investment, tax, or legal advice. Mutual fund investments are subject to market risks. Please consult a SEBI-registered Investment Advisor (RIA) or Chartered Accountant before executing financial transactions.
</div>
```

---

## 6. Footer & Back-to-Top Markup (Byte-for-byte exact)

```html
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
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0C93Q0VBQP');
  </script>
  <script src="theme.js?v=2.2"></script>

</body>
</html>
```

---

## 7. `blog.html` Card Markup Specification

Each card inside `#articlesGrid` on `blog.html` must follow this exact markup:

```html
<article class="calc-link-card article-card-item" data-category="[Category Name]" data-desc="[lowercase keywords and excerpt for live search filter]" data-title="[lowercase article title for search filter]" style="padding:32px;">
  <div>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; gap:8px; flex-wrap:wrap;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span class="meta-cat">[Category Name]</span>
        <!-- Include NEW badge for newest articles -->
        <span style="background:var(--emerald); color:#fff; font-size:0.72rem; font-weight:800; padding:2px 8px; border-radius:4px; text-transform:uppercase; letter-spacing:0.5px;">NEW</span>
      </div>
      <span class="article-date-tag">Published: 31 Aug 2026</span>
    </div>
    <h3 style="font-size:1.28rem; font-weight:800; line-height:1.4;"><a href="[article-slug].html" style="color:var(--text-primary);">[Card Heading]</a></h3>
    <p style="margin:14px 0 22px; font-size:0.98rem; color:var(--text-secondary); line-height:1.65;">[Engaging card summary between 120-180 characters highlighting mathematical insight.]</p>
  </div>
  <a class="card-action" href="[article-slug].html" style="font-size:0.96rem; font-weight:700;">Read Full Guide &rarr;</a>
</article>
```

### 7.1 Existing Categories on `blog.html`:
1. `SIP & Mutual Funds`
2. `Tax & Financial Planning`
3. `Retirement & Pension`
4. `Fixed Income & FDs`
5. `Personal Finance & Budgeting`
6. `Goal Planning & Wealth`
7. `Loans & Real Estate`

---

## 8. Sitemap Entry Specification

```xml
  <url>
    <loc>https://www.calculatorship.in/[article-slug].html</loc>
    <lastmod>2026-08-31</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
```
