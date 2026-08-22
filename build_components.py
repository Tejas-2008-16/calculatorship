import os
import json
import html
import re

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

# Shared Global Header Component (Using new logo and 10 calculators)
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
            <li><a href="ppf-calculator.html">PPF Calculator</a></li>
            <li><a href="swp-calculator.html">SWP Calculator</a></li>
            <li><a href="emi-calculator.html">Loan EMI & Prepay</a></li>
            <li class="nav-dropdown-divider" role="separator"></li>
            <li><a href="fd-calculator.html">FD Calculator</a></li>
            <li><a href="budget-planner.html">Budget Planner</a></li>
            <li><a href="income-tax-calculator.html">Tax Calculator</a></li>
          </ul>
        </div>
        <a href="blog.html" class="{'active' if active_page == 'blog' else ''}">Blog & Guides</a>
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

# Shared Quick Calculator Switcher Bar (All 10 Calculators)
def get_calc_switcher(active_slug):
    calcs = [
        ("index.html", "SIP Calculator"),
        ("lumpsum.html", "Lumpsum"),
        ("step-up.html", "Step-Up SIP"),
        ("goal.html", "Goal Planner"),
        ("ppf-calculator.html", "PPF"),
        ("swp-calculator.html", "SWP"),
        ("emi-calculator.html", "Loan EMI"),
        ("fd-calculator.html", "FD Calculator"),
        ("budget-planner.html", "50-30-20 Budget"),
        ("income-tax-calculator.html", "Tax Calculator")
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

# Shared "Explore All Other Calculators" Grid
def get_all_calculators_grid(current_slug):
    all_calcs = [
        ("index.html", "SIP Calculator", "Calculate projected compounding returns from regular monthly mutual fund investments with year-by-year tables."),
        ("lumpsum.html", "Lumpsum Calculator", "Project total growth and returns on a one-time lumpsum mutual fund investment across multiple market horizons."),
        ("step-up.html", "Step-Up SIP Calculator", "Model wealth growth when increasing your monthly SIP contributions by 10% annually with salary increments."),
        ("goal.html", "Goal Planner Calculator", "Calculate the exact monthly SIP required to achieve target financial milestones like retirement, higher education, or home purchase."),
        ("ppf-calculator.html", "Public Provident Fund (PPF) Calculator", "Compute 15-year guaranteed compounding interest and maturity proceeds with 100% tax-free EEE benefits."),
        ("swp-calculator.html", "Systematic Withdrawal Plan (SWP) Calculator", "Simulate tax-efficient monthly retirement pensions, total withdrawals, and remaining portfolio balances."),
        ("emi-calculator.html", "Loan EMI & Prepayment Calculator", "Compute monthly EMI payments and model how part prepayments save lakhs in interest and reduce tenure."),
        ("fd-calculator.html", "Fixed Deposit (FD) Calculator", "Compute bank fixed deposit maturity proceeds with cumulative quarterly compounding and interest breakdowns."),
        ("budget-planner.html", "50-30-20 Budget Planner", "Allocate your take-home salary into Essential Needs, Lifestyle Wants, and Wealth Investments with Indian metro adjustments."),
        ("income-tax-calculator.html", "Income Tax Calculator", "Compare your net tax liabilities side-by-side under the Old vs New Tax Regimes with full deductions.")
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
      <p>Free, fast, and independent simulation tools designed specifically for Indian investors.</p>
    </div>
    <div class="all-calculators-grid">
      {''.join(cards)}
    </div>
  </section>"""

# Shared Contained Global Footer
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
            <h3>Calculators</h3>
            <ul>
              <li><a href="index.html">SIP Calculator</a></li>
              <li><a href="lumpsum.html">Lumpsum Calculator</a></li>
              <li><a href="step-up.html">Step-Up SIP</a></li>
              <li><a href="goal.html">Goal Planner</a></li>
              <li><a href="ppf-calculator.html">PPF Calculator</a></li>
              <li><a href="swp-calculator.html">SWP Calculator</a></li>
              <li><a href="emi-calculator.html">Loan EMI & Prepay</a></li>
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
  <script src="theme.js"></script>"""

print("Components loaded.")
