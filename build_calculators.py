import os
import json
import html

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

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

def get_calc_switcher(active_slug):
    calcs = [
        ("index.html", "SIP Calculator"),
        ("lumpsum.html", "Lumpsum"),
        ("step-up.html", "Step-Up SIP"),
        ("goal.html", "Goal Planner"),
        ("fd-calculator.html", "FD Calculator"),
        ("budget-planner.html", "Budget Planner"),
        ("income-tax-calculator.html", "Income Tax")
    ]
    tabs = []
    for slug, label in calcs:
        is_active = " active" if slug == active_slug else ""
        tabs.append(f'<a href="{slug}" class="calc-tab{is_active}">{label}</a>')
    return f"""  <div class="calc-switcher-wrapper">
    <div class="calc-switcher-bar">
      {''.join(tabs)}
    </div>
  </div>"""

def get_all_calculators_grid(current_slug):
    all_calcs = [
        ("index.html", "SIP Calculator", "Calculate projected returns from regular monthly mutual fund investments with compounding breakdowns."),
        ("lumpsum.html", "Lumpsum Calculator", "Project total growth and returns on a one-time lumpsum mutual fund investment."),
        ("step-up.html", "Step-Up SIP Calculator", "Model wealth growth when increasing your monthly SIP contributions annually with salary hikes."),
        ("goal.html", "Goal Planner Calculator", "Calculate the exact monthly SIP required to reach target financial goals (retirement, house, college)."),
        ("fd-calculator.html", "Fixed Deposit (FD) Calculator", "Compute maturity proceeds and interest earnings across quarterly, monthly, and annual compounding."),
        ("budget-planner.html", "50-30-20 Budget Planner", "Allocate your net take-home salary into Needs, Wants, and Savings using the 50-30-20 rule."),
        ("income-tax-calculator.html", "Income Tax Calculator", "Compare tax liability side-by-side under the Old vs New Tax Regimes with full deductions.")
    ]
    
    cards = []
    for slug, title, desc in all_calcs:
        if slug == current_slug:
            continue
        cards.append(f"""      <a href="{slug}" class="calc-link-card">
        <div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
        <span class="card-action">Open Calculator &rarr;</span>
      </a>""")
      
    return f"""  <section class="all-calculators-section">
    <div class="section-title-wrap">
      <h2>Explore Other Financial Calculators</h2>
      <p>Free, accurate, and independent financial simulation tools for Indian investors.</p>
    </div>
    <div class="all-calculators-grid">
      {''.join(cards)}
    </div>
  </section>"""

def get_footer():
    return """  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html"><img src="logo-light.svg" alt="Calculatorship Logo" width="180" height="32"></a>
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

# -------------------------------------------------------------
# BUILD 7 CALCULATOR PAGES
# -------------------------------------------------------------
def build_calculators():
    calcs = [
        {
            "slug": "index.html",
            "title": "SIP Calculator: Systematic Investment Plan Return Calculator India",
            "metaDesc": "Calculate projected returns from your monthly mutual fund SIP in India. View annual compounding breakdown tables, charts, and wealth gain projections.",
            "h1": "SIP Calculator (Systematic Investment Plan)",
            "subtitle": "Calculate projected wealth growth and compounding returns from your monthly mutual fund investments.",
            "field1": {"id": "monthly-investment", "label": "Monthly Investment", "min": 500, "max": 1000000, "step": 500, "val": 10000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 10, "prefix": "", "suffix": "Yrs"},
            "calc_type": "sip"
        },
        {
            "slug": "lumpsum.html",
            "title": "Lumpsum Calculator: One-Time Mutual Fund Investment Calculator",
            "metaDesc": "Calculate projected returns on one-time lumpsum mutual fund investments in India. Year-by-year compounding growth table and charts.",
            "h1": "Lumpsum Investment Calculator",
            "subtitle": "Project total growth, interest earned, and maturity corpus on your one-time mutual fund investments.",
            "field1": {"id": "monthly-investment", "label": "Total Lumpsum Investment", "min": 5000, "max": 10000000, "step": 5000, "val": 100000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 10, "prefix": "", "suffix": "Yrs"},
            "calc_type": "lumpsum"
        },
        {
            "slug": "step-up.html",
            "title": "Step-Up SIP Calculator: Top-Up SIP Growth Calculator India",
            "metaDesc": "Calculate how increasing your monthly SIP amount annually with salary increments multiplies your final wealth corpus. Step-Up calculator with yearly schedule.",
            "h1": "Step-Up SIP Calculator",
            "subtitle": "Model wealth compounding when you increase your monthly SIP contribution annually alongside salary raises.",
            "field1": {"id": "monthly-investment", "label": "Starting Monthly Investment", "min": 500, "max": 1000000, "step": 500, "val": 10000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 15, "prefix": "", "suffix": "Yrs"},
            "field4": {"id": "step-up-pct", "label": "Annual Step-Up Increment", "min": 1, "max": 50, "step": 1, "val": 10, "prefix": "", "suffix": "%"},
            "calc_type": "step_up"
        },
        {
            "slug": "goal.html",
            "title": "Goal Planner Calculator: Target Corpus SIP Calculator India",
            "metaDesc": "Calculate the exact monthly SIP required to achieve your financial goals (retirement, house, child education). Target corpus goal planner.",
            "h1": "Goal Planner & Target Corpus Calculator",
            "subtitle": "Work backwards from your target wealth goal to determine the required monthly SIP investment amount.",
            "field1": {"id": "monthly-investment", "label": "Target Wealth Corpus", "min": 100000, "max": 500000000, "step": 100000, "val": 10000000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Years to Achieve Goal", "min": 1, "max": 40, "step": 1, "val": 15, "prefix": "", "suffix": "Yrs"},
            "calc_type": "goal"
        },
        {
            "slug": "fd-calculator.html",
            "title": "Fixed Deposit (FD) Calculator: Bank FD Interest & Maturity Calculator",
            "metaDesc": "Calculate maturity value and interest earnings on Bank Fixed Deposits across monthly, quarterly, and annual compounding frequencies in India.",
            "h1": "Fixed Deposit (FD) Calculator",
            "subtitle": "Compute total interest earnings and maturity proceeds on bank fixed deposits across compounding frequencies.",
            "field1": {"id": "monthly-investment", "label": "Total Deposit Principal", "min": 5000, "max": 50000000, "step": 5000, "val": 500000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Annual Interest Rate", "min": 2, "max": 15, "step": 0.1, "val": 7.2, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Deposit Tenure", "min": 1, "max": 20, "step": 1, "val": 5, "prefix": "", "suffix": "Yrs"},
            "calc_type": "fd"
        },
        {
            "slug": "budget-planner.html",
            "title": "50-30-20 Budget Planner: Salary Expense & Savings Calculator",
            "h1": "50-30-20 Salary Budget Planner",
            "metaDesc": "Plan your monthly budget using the 50-30-20 rule adapted for Indian salaries. Allocate take-home pay into Needs, Wants, and Wealth Investments.",
            "subtitle": "Allocate your net take-home salary into Needs, Wants, and Savings using the proven 50-30-20 budgeting framework.",
            "field1": {"id": "monthly-investment", "label": "Net Take-Home Salary (Monthly)", "min": 10000, "max": 2000000, "step": 1000, "val": 75000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Target Savings Percentage", "min": 10, "max": 50, "step": 1, "val": 20, "prefix": "", "suffix": "%"},
            "field3": {"id": "time-period", "label": "Planning Horizon", "min": 1, "max": 30, "step": 1, "val": 10, "prefix": "", "suffix": "Yrs"},
            "calc_type": "budget"
        },
        {
            "slug": "income-tax-calculator.html",
            "title": "Income Tax Calculator India: Old vs New Tax Regime Comparison 2026",
            "h1": "Income Tax Calculator (Old vs New Regime)",
            "metaDesc": "Compare your income tax liability under the Old vs New Tax Regime in India for FY 2025-26 & 2026-27. Compute exact tax savings with 80C, 80D, HRA, and standard deductions.",
            "subtitle": "Compare your exact tax liabilities side-by-side under the Old and New Tax Regimes to identify maximum tax savings.",
            "field1": {"id": "monthly-investment", "label": "Gross Annual Income / CTC", "min": 300000, "max": 10000000, "step": 25000, "val": 1500000, "prefix": "₹", "suffix": ""},
            "field2": {"id": "expected-return", "label": "Section 80C Deductions (PPF, ELSS, EPF)", "min": 0, "max": 150000, "step": 5000, "val": 150000, "prefix": "₹", "suffix": ""},
            "field3": {"id": "time-period", "label": "Other Deductions (80D + HRA + Home Loan)", "min": 0, "max": 500000, "step": 10000, "val": 150000, "prefix": "₹", "suffix": ""},
            "calc_type": "tax"
        }
    ]

    for c in calcs:
        extra_field_html = ""
        if "field4" in c:
            f4 = c["field4"]
            extra_field_html = f"""
          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{f4['id']}">{f4['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{f4['prefix']}</span>
                <input type="number" id="{f4['id']}-num" value="{f4['val']}" min="{f4['min']}" max="{f4['max']}" step="{f4['step']}">
                <span class="calc-input-suffix">{f4['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{f4['id']}" min="{f4['min']}" max="{f4['max']}" step="{f4['step']}" value="{f4['val']}">
          </div>"""

        label1 = "Invested Capital"
        label2 = "Estimated Growth"
        label3 = "Total Projected Value"
        if c["calc_type"] == "goal":
            label1 = "Target Corpus Goal"
            label2 = "Estimated Total Returns"
            label3 = "Required Monthly SIP"
        elif c["calc_type"] == "fd":
            label1 = "Principal Deposited"
            label2 = "Total Interest Earned"
            label3 = "Maturity Proceeds"
        elif c["calc_type"] == "budget":
            label1 = "50% Essential Needs"
            label2 = "30% Discretionary Wants"
            label3 = "20% Monthly Savings"
        elif c["calc_type"] == "tax":
            label1 = "Tax (New Regime)"
            label2 = "Tax (Old Regime)"
            label3 = "Net Tax Difference"

        html_content = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']} | Calculatorship</title>
  <meta name="description" content="{c['metaDesc']}">
  <link rel="canonical" href="https://www.calculatorship.in/{c['slug']}">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['metaDesc']}">
  <meta property="og:url" content="https://www.calculatorship.in/{c['slug']}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.calculatorship.in/og-image.webp">
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
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "{c['h1']}",
    "url": "https://www.calculatorship.in/{c['slug']}",
    "description": "{c['metaDesc']}",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "All",
    "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "INR" }}
  }}
  </script>
</head>
<body>

  <div class="reading-progress-bar" id="reading-progress"></div>
  <a class="skip-link" href="#calculator-card">Skip to calculator</a>

{get_header()}

  <div class="breadcrumb-bar">
    <nav class="breadcrumb" aria-label="Breadcrumbs">
      <ol>
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html">Calculators</a></li>
        <li aria-current="page">{c['h1']}</li>
      </ol>
    </nav>
  </div>

  <main id="main-content">

    <div class="calc-hero">
      <h1>{c['h1']}</h1>
      <p>{c['subtitle']}</p>
    </div>

{get_calc_switcher(c['slug'])}

    <!-- Clean Disclaimer Banner -->
    <div class="disclaimer-banner" data-banner-id="{c['slug']}">
      <div>
        <span class="disc-badge">Educational Tool</span>
        <span>Calculations shown are mathematical projections for educational planning only and do not guarantee actual returns. Mutual fund investments are subject to market risks. Please consult a SEBI-registered financial advisor before investing.</span>
      </div>
      <button class="disc-dismiss" type="button">Dismiss</button>
    </div>

    <!-- Top AdSense Slot -->
    <div class="ad-slot ad-slot-banner" style="max-width:1200px; margin:16px auto 28px;">
      <span class="ad-label">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <div class="calc-main-container">
      <div class="calc-grid" id="calculator-card">
        
        <!-- Left: Inputs -->
        <div class="calc-card">
          <h2 style="font-size:1.25rem; font-weight:700; margin-bottom:20px; color:var(--text-primary);">Configure Investment Parameters</h2>
          
          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field1']['id']}">{c['field1']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field1']['prefix']}</span>
                <input type="number" id="{c['field1']['id']}-num" value="{c['field1']['val']}" min="{c['field1']['min']}" max="{c['field1']['max']}" step="{c['field1']['step']}">
                <span class="calc-input-suffix">{c['field1']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field1']['id']}" min="{c['field1']['min']}" max="{c['field1']['max']}" step="{c['field1']['step']}" value="{c['field1']['val']}">
          </div>

          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field2']['id']}">{c['field2']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field2']['prefix']}</span>
                <input type="number" id="{c['field2']['id']}-num" value="{c['field2']['val']}" min="{c['field2']['min']}" max="{c['field2']['max']}" step="{c['field2']['step']}">
                <span class="calc-input-suffix">{c['field2']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field2']['id']}" min="{c['field2']['min']}" max="{c['field2']['max']}" step="{c['field2']['step']}" value="{c['field2']['val']}">
          </div>

          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field3']['id']}">{c['field3']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field3']['prefix']}</span>
                <input type="number" id="{c['field3']['id']}-num" value="{c['field3']['val']}" min="{c['field3']['min']}" max="{c['field3']['max']}" step="{c['field3']['step']}">
                <span class="calc-input-suffix">{c['field3']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field3']['id']}" min="{c['field3']['min']}" max="{c['field3']['max']}" step="{c['field3']['step']}" value="{c['field3']['val']}">
          </div>

          {extra_field_html}
        </div>

        <!-- Right: Summary Results & Visuals -->
        <div class="calc-summary-card">
          <div>
            <h3 style="font-size:1.1rem; font-weight:700; color:var(--text-primary); margin-bottom:16px;">Projected Growth Summary</h3>
            
            <div class="result-row">
              <span class="result-label">{label1}</span>
              <span class="result-val" id="res-invested">₹0</span>
            </div>

            <div class="result-row">
              <span class="result-label">{label2}</span>
              <span class="result-val" id="res-returns" style="color:#059669;">₹0</span>
            </div>

            <div class="result-row" style="padding-top:16px;">
              <span class="result-label" style="font-weight:700; color:var(--text-primary);">{label3}</span>
              <span class="result-val highlight" id="res-total">₹0</span>
            </div>

            <!-- SVG Visual Donut Ratio -->
            <div style="margin:24px 0 10px; display:flex; align-items:center; justify-content:center; gap:24px;">
              <svg width="120" height="120" viewBox="0 0 42 42" class="donut">
                <circle class="donut-ring" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#E2E8F0" stroke-width="5"></circle>
                <circle id="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#00D09C" stroke-width="5" stroke-dasharray="70 30" stroke-dashoffset="25"></circle>
              </svg>
              <div style="font-size:0.82rem; line-height:1.8;">
                <div style="display:flex; align-items:center; gap:6px;"><span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#00D09C;"></span> <span id="donut-leg-gain">Returns: 0%</span></div>
                <div style="display:flex; align-items:center; gap:6px;"><span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#E2E8F0;"></span> <span id="donut-leg-inv">Principal: 0%</span></div>
              </div>
            </div>
          </div>

          <div class="calc-result-disclaimer">
            Projected returns are mathematical calculations based on the rate of return you entered and assume continuous periodic compounding without intermittent withdrawals. Mutual fund investments are subject to market risks.
          </div>
        </div>

      </div>

      <!-- Annual Growth Schedule Table -->
      <div style="margin-top:36px; background:var(--bg-card); border:1px solid var(--border-soft); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-sm);">
        <h3 style="font-size:1.2rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">Year-by-Year Compounding Progression</h3>
        <p style="font-size:0.90rem; color:var(--text-secondary); margin-bottom:16px;">Detailed annual accumulation breakdown illustrating how interest outpaces deposits over time.</p>
        <div class="table-wrapper">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>Year</th>
                <th>Opening Capital</th>
                <th>Annual Deposit</th>
                <th>Interest Accrued</th>
                <th>Closing Portfolio Value</th>
              </tr>
            </thead>
            <tbody id="schedule-tbody">
              <!-- Dynamically Populated by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Educational & Regulatory Guide Section -->
    <div class="calc-main-container">
      <div style="background:var(--bg-card); border:1px solid var(--border-soft); border-radius:var(--radius-lg); padding:40px; box-shadow:var(--shadow-sm);">
        <div class="article-main" style="border:none; padding:0; box-shadow:none;">
          <h2>How This Financial Calculation Works</h2>
          <p>This calculator simulates the mathematics of recurring or lumpsum financial investments in the Indian economic environment. For equity-linked mutual funds, returns compound as underlying portfolio corporate earnings expand over multi-year business cycles.</p>
          
          <h3>Mathematical Formula &amp; Assumptions</h3>
          <p>For monthly Systematic Investment Plans (SIP), the future value is computed using the monthly annuity compounding formula:</p>
          <div style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px; text-align:center; font-family:var(--font-mono); font-size:1.05rem; margin:16px 0;">
            FV = P &times; [ ( (1 + r)^n - 1 ) / r ] &times; (1 + r)
          </div>
          <p>Where <strong>P</strong> represents the recurring monthly contribution, <strong>r</strong> represents the periodic monthly return rate (Annual CAGR / 12), and <strong>n</strong> represents the cumulative monthly compounding periods.</p>

          <h3>Strategic Guidelines for Indian Investors</h3>
          <ul>
            <li><strong>Match Investment Horizons to Asset Classes:</strong> Maintain high equity allocations for financial goals with horizons exceeding 5 to 7 years. For horizons under 3 years, utilize fixed-income debt funds or bank fixed deposits.</li>
            <li><strong>Automate with Direct Plans:</strong> Ensure your mutual fund investments are executed through Direct Plans rather than Regular Plans to eliminate distributor trailing commissions (saving 0.5% to 1.5% annually).</li>
            <li><strong>Account for Real Inflation:</strong> Long-term consumer price inflation in India averages between 5% and 6.5%. Use aggressive compounding tools to build purchasing power ahead of inflation.</li>
          </ul>
        </div>
      </div>
    </div>

{get_all_calculators_grid(c['slug'])}

  </main>

{get_footer()}

  <script>
    // Universal Live Calculator Engine
    (function() {{
      const type = "{c['calc_type']}";
      
      const in1 = document.getElementById("{c['field1']['id']}");
      const in1Num = document.getElementById("{c['field1']['id']}-num");
      
      const in2 = document.getElementById("{c['field2']['id']}");
      const in2Num = document.getElementById("{c['field2']['id']}-num");
      
      const in3 = document.getElementById("{c['field3']['id']}");
      const in3Num = document.getElementById("{c['field3']['id']}-num");
      
      const in4 = document.getElementById("step-up-pct");
      const in4Num = document.getElementById("step-up-pct-num");

      function formatINR(val) {{
        return '₹' + Math.round(val).toLocaleString('en-IN');
      }}

      function sync(slider, num) {{
        if (!slider || !num) return;
        slider.addEventListener('input', () => {{ num.value = slider.value; calculate(); }});
        num.addEventListener('input', () => {{ slider.value = num.value; calculate(); }});
      }}

      sync(in1, in1Num);
      sync(in2, in2Num);
      sync(in3, in3Num);
      if (in4 && in4Num) sync(in4, in4Num);

      function calculate() {{
        const v1 = parseFloat(in1.value) || 0;
        const v2 = parseFloat(in2.value) || 0;
        const v3 = parseFloat(in3.value) || 0;
        const v4 = in4 ? (parseFloat(in4.value) || 0) : 0;

        let totalInvested = 0;
        let totalValue = 0;
        let scheduleRows = [];

        if (type === "sip") {{
          const p = v1;
          const r = (v2 / 100) / 12;
          const n = v3 * 12;
          totalInvested = p * n;
          totalValue = p * ((Math.pow(1 + r, n) - 1) / r) * (1 + r);
          
          let curBal = 0;
          for (let y = 1; y <= v3; y++) {{
            const yrDep = p * 12;
            const openBal = curBal;
            for (let m = 1; m <= 12; m++) {{
              curBal = (curBal + p) * (1 + r);
            }}
            const yrGain = curBal - openBal - yrDep;
            scheduleRows.push({{ yr: y, open: openBal, dep: yrDep, gain: yrGain, close: curBal }});
          }}
        }} else if (type === "lumpsum") {{
          const p = v1;
          const r = v2 / 100;
          const n = v3;
          totalInvested = p;
          totalValue = p * Math.pow(1 + r, n);
          
          let curBal = p;
          for (let y = 1; y <= n; y++) {{
            const openBal = curBal;
            curBal = curBal * (1 + r);
            const yrGain = curBal - openBal;
            scheduleRows.push({{ yr: y, open: openBal, dep: 0, gain: yrGain, close: curBal }});
          }}
        }} else if (type === "step_up") {{
          let curP = v1;
          const r = (v2 / 100) / 12;
          const step = v4 / 100;
          let curBal = 0;
          
          for (let y = 1; y <= v3; y++) {{
            const yrDep = curP * 12;
            totalInvested += yrDep;
            const openBal = curBal;
            for (let m = 1; m <= 12; m++) {{
              curBal = (curBal + curP) * (1 + r);
            }}
            const yrGain = curBal - openBal - yrDep;
            scheduleRows.push({{ yr: y, open: openBal, dep: yrDep, gain: yrGain, close: curBal }});
            curP = curP * (1 + step);
          }}
          totalValue = curBal;
        }} else if (type === "goal") {{
          const target = v1;
          const r = (v2 / 100) / 12;
          const n = v3 * 12;
          const reqP = target / (((Math.pow(1 + r, n) - 1) / r) * (1 + r));
          totalValue = reqP;
          totalInvested = target;
          const estDep = reqP * n;
          
          let curBal = 0;
          for (let y = 1; y <= v3; y++) {{
            const yrDep = reqP * 12;
            const openBal = curBal;
            for (let m = 1; m <= 12; m++) {{
              curBal = (curBal + reqP) * (1 + r);
            }}
            const yrGain = curBal - openBal - yrDep;
            scheduleRows.push({{ yr: y, open: openBal, dep: yrDep, gain: yrGain, close: curBal }});
          }}
          
          document.getElementById("res-invested").textContent = formatINR(target);
          document.getElementById("res-returns").textContent = formatINR(Math.max(0, target - estDep));
          document.getElementById("res-total").textContent = formatINR(reqP) + ' / mo';
          updateSchedule(scheduleRows);
          return;
        }} else if (type === "fd") {{
          const p = v1;
          const r = v2 / 100;
          const n = v3;
          const m = 4; // Quarterly compounding standard
          totalInvested = p;
          totalValue = p * Math.pow(1 + (r / m), m * n);
          
          let curBal = p;
          for (let y = 1; y <= n; y++) {{
            const openBal = curBal;
            curBal = curBal * Math.pow(1 + (r / m), m);
            const yrGain = curBal - openBal;
            scheduleRows.push({{ yr: y, open: openBal, dep: 0, gain: yrGain, close: curBal }});
          }}
        }} else if (type === "budget") {{
          const income = v1;
          const savPct = v2 / 100;
          const needs = income * 0.50;
          const wants = income * (1 - 0.50 - savPct);
          const savings = income * savPct;
          
          document.getElementById("res-invested").textContent = formatINR(needs);
          document.getElementById("res-returns").textContent = formatINR(wants);
          document.getElementById("res-total").textContent = formatINR(savings) + ' / mo';
          
          const r = 0.12 / 12;
          let curBal = 0;
          for (let y = 1; y <= v3; y++) {{
            const yrDep = savings * 12;
            const openBal = curBal;
            for (let m = 1; m <= 12; m++) {{
              curBal = (curBal + savings) * (1 + r);
            }}
            const yrGain = curBal - openBal - yrDep;
            scheduleRows.push({{ yr: y, open: openBal, dep: yrDep, gain: yrGain, close: curBal }});
          }}
          updateSchedule(scheduleRows);
          return;
        }} else if (type === "tax") {{
          const income = v1;
          const d80c = Math.min(150000, v2);
          const dOther = v3;
          
          // New Regime Calculation (FY 2024-25 / 2025-26)
          const stdNew = 75000;
          const taxIncomeNew = Math.max(0, income - stdNew);
          let taxNew = 0;
          if (taxIncomeNew <= 300000) taxNew = 0;
          else if (taxIncomeNew <= 700000) taxNew = (taxIncomeNew - 300000) * 0.05;
          else if (taxIncomeNew <= 1000000) taxNew = 20000 + (taxIncomeNew - 700000) * 0.10;
          else if (taxIncomeNew <= 1200000) taxNew = 50000 + (taxIncomeNew - 1000000) * 0.15;
          else if (taxIncomeNew <= 1500000) taxNew = 80000 + (taxIncomeNew - 1200000) * 0.20;
          else taxNew = 140000 + (taxIncomeNew - 1500000) * 0.30;
          
          // Rebate 87A for New Regime (tax zero if taxable income <= 7L)
          if (taxIncomeNew <= 700000) taxNew = 0;
          else taxNew = taxNew * 1.04; // 4% cess

          // Old Regime Calculation
          const stdOld = 50000;
          const taxIncomeOld = Math.max(0, income - stdOld - d80c - dOther);
          let taxOld = 0;
          if (taxIncomeOld <= 250000) taxOld = 0;
          else if (taxIncomeOld <= 500000) taxOld = (taxIncomeOld - 250000) * 0.05;
          else if (taxIncomeOld <= 1000000) taxOld = 12500 + (taxIncomeOld - 500000) * 0.20;
          else taxOld = 112500 + (taxIncomeOld - 1000000) * 0.30;
          
          if (taxIncomeOld <= 500000) taxOld = 0;
          else taxOld = taxOld * 1.04;

          document.getElementById("res-invested").textContent = formatINR(taxNew);
          document.getElementById("res-returns").textContent = formatINR(taxOld);
          const diff = taxOld - taxNew;
          document.getElementById("res-total").textContent = (diff >= 0 ? 'New Saves ' : 'Old Saves ') + formatINR(Math.abs(diff));
          return;
        }}

        const totalReturns = Math.max(0, totalValue - totalInvested);
        document.getElementById("res-invested").textContent = formatINR(totalInvested);
        document.getElementById("res-returns").textContent = formatINR(totalReturns);
        document.getElementById("res-total").textContent = formatINR(totalValue);

        // Update Donut Visual
        const gainPct = totalValue > 0 ? Math.round((totalReturns / totalValue) * 100) : 0;
        const invPct = 100 - gainPct;
        const donut = document.getElementById("donut-segment");
        if (donut) {{
          donut.setAttribute("stroke-dasharray", `${{gainPct}} ${{invPct}}`);
        }}
        const legGain = document.getElementById("donut-leg-gain");
        const legInv = document.getElementById("donut-leg-inv");
        if (legGain) legGain.textContent = `Returns: ${{gainPct}}%`;
        if (legInv) legInv.textContent = `Principal: ${{invPct}}%`;

        updateSchedule(scheduleRows);
      }}

      function updateSchedule(rows) {{
        const tbody = document.getElementById("schedule-tbody");
        if (!tbody || !rows || rows.length === 0) return;
        tbody.innerHTML = rows.map(r => `
          <tr>
            <td>Year ${{r.yr}}</td>
            <td>${{formatINR(r.open)}}</td>
            <td>${{formatINR(r.dep)}}</td>
            <td style="color:#059669;">+${{formatINR(r.gain)}}</td>
            <td style="font-weight:700;">${{formatINR(r.close)}}</td>
          </tr>
        `).join('');
      }}

      calculate();
    }})();
  </script>
</body>
</html>"""

        filepath = os.path.join(SITE_DIR, c["slug"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated Calculator: {c['slug']}")

if __name__ == "__main__":
    build_calculators()
