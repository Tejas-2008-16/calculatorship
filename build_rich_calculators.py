import os
import json
import html

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

# Shared Global Header Component
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

# Shared Quick Calculator Switcher Bar
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

# Shared "Explore All Other Calculators" Grid
def get_all_calculators_grid(current_slug):
    all_calcs = [
        ("index.html", "SIP Calculator", "Calculate projected compounding returns on your recurring monthly mutual fund investments."),
        ("lumpsum.html", "Lumpsum Calculator", "Project multi-year wealth accumulation on a one-time capital investment."),
        ("step-up.html", "Step-Up SIP Calculator", "See how increasing your SIP by 10% each year with salary hikes multiplies your final corpus."),
        ("goal.html", "Goal Planner Calculator", "Determine the exact monthly SIP required to reach a specific financial goal like retirement or a house."),
        ("fd-calculator.html", "Fixed Deposit (FD) Calculator", "Compute maturity values and quarterly compounding interest on bank fixed deposits."),
        ("budget-planner.html", "50-30-20 Budget Planner", "Divide your take-home salary into Needs, Wants, and Wealth Investments with Indian metro adjustments."),
        ("income-tax-calculator.html", "Income Tax Calculator", "Compare your tax liabilities side-by-side under the Old vs New Tax Regimes.")
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

CALCULATOR_SPECS = [
    {
        "slug": "index.html",
        "title": "SIP Calculator: Systematic Investment Plan Return Calculator India",
        "metaDesc": "Calculate projected returns from your monthly mutual fund SIP in India. View annual compounding breakdown tables, charts, and wealth gain projections.",
        "h1": "SIP Calculator (Systematic Investment Plan)",
        "subtitle": "Calculate projected wealth growth and compounding returns from your monthly mutual fund investments in India.",
        "field1": {"id": "monthly-investment", "label": "Monthly SIP Amount", "min": 500, "max": 1000000, "step": 500, "val": 10000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 10, "prefix": "", "suffix": "Yrs"},
        "calc_type": "sip",
        "insights_title": "Key Principles of Systematic Investment Plans in India",
        "insights_p": "A Systematic Investment Plan (SIP) allows Indian retail investors to invest a fixed sum into mutual funds every month. SIP utilizes Rupee Cost Averaging, automatically purchasing more units when stock markets decline and fewer units when markets rise.",
        "rule_box_title": "The Famous 15-15-15 Rule of Compounding",
        "rule_box_desc": "If you invest ₹15,000 per month for 15 years at an expected annual return of 15% CAGR, your total invested capital of ₹27 Lakh grows into approximately ₹1.00 Crore. If you let that same investment run for 30 years (The 15-15-30 Rule), your corpus expands into over ₹10.38 Crore.",
        "personas": [
            ("Starter Career (Age 23)", "Pooja starts a ₹3,000/month SIP in a Nifty 50 Index Fund. Over 20 years at an illustrative 12% CAGR, her ₹7.2 Lakh investment grows to approximately ₹29.98 Lakh."),
            ("Mid-Career Professional (Age 32)", "Arun commits ₹20,000/month into diversified equity funds. Over 15 years at 12% CAGR, his ₹36 Lakh invested capital reaches approximately ₹1.00 Crore."),
            ("Aggressive Wealth Builder (Age 38)", "Deepak invests ₹50,000/month. Over 12 years at 13% CAGR, his ₹72 Lakh investment expands to roughly ₹1.58 Crore.")
        ],
        "dos": [
            "Link your SIP date to 2-3 days following your monthly salary credit.",
            "Opt for Direct Plans to save 0.5% to 1.5% in annual distributor commissions.",
            "Continue your SIP uninterrupted during market corrections to accumulate cheaper units.",
            "Increase your SIP amount annually by 10% whenever you receive a salary increment."
        ],
        "donts": [
            "Do not stop or pause your SIP when the stock market experiences a temporary dip.",
            "Do not chase short-term sector funds based solely on past 1-year performance.",
            "Do not invest emergency money in equity mutual funds.",
            "Do not withdraw your accumulated corpus before your targeted financial goal timeline."
        ],
        "faqs": [
            ("What is the minimum monthly SIP amount in India?", "Most Indian mutual fund houses allow monthly SIP investments starting from ₹100 to ₹500 across broad-market index and flexi-cap schemes."),
            ("Are returns from mutual fund SIPs guaranteed?", "No. Mutual funds invest in equity and debt securities and are subject to market risks. Calculations are mathematical projections for planning purposes only."),
            ("How is tax calculated on equity mutual fund SIP returns?", "Under post-Budget 2024 tax rules, units held for 12 months or longer qualify for Long-Term Capital Gains (LTCG) tax at 12.5% on gains exceeding ₹1.25 Lakh per financial year. Units held under 12 months are taxed at 20% STCG.")
        ]
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
        "calc_type": "lumpsum",
        "insights_title": "How Lumpsum Compounding Works in Equity & Debt Funds",
        "insights_p": "A lumpsum investment involves deploying a single capital sum in one go. Lumpsum investing is popular when receiving annual bonuses, proceeds from property sales, maturity proceeds from fixed deposits, or inheritance.",
        "rule_box_title": "The Rule of 72: Doubling Your Lumpsum Capital",
        "rule_box_desc": "Divide 72 by your expected annual rate of return to estimate how quickly your lumpsum investment will double. At an illustrative 12% CAGR, ₹5 Lakh doubles to ₹10 Lakh in approximately 6 years, and quadruples to ₹20 Lakh in 12 years without adding another rupee.",
        "personas": [
            ("Bonus Deployment (₹2 Lakh)", "Sneha receives a ₹2 Lakh corporate bonus and deploys it in a Flexi Cap Fund. In 10 years at an illustrative 12% CAGR, it grows to approximately ₹6.22 Lakh."),
            ("Retirement Windfall (₹25 Lakh)", "Mohan parks ₹25 Lakh from a retirement gratuity. In 12 years at 11% CAGR, it expands to approximately ₹87.46 Lakh."),
            ("Child College Seed (₹5 Lakh)", "Kavita invests ₹5 Lakh when her daughter is 3 years old. By age 18 (15 years at 12% CAGR), it reaches approximately ₹27.37 Lakh.")
        ],
        "dos": [
            "Deploy lumpsum funds when market valuations are attractive or during index pullbacks.",
            "Consider a Systematic Transfer Plan (STP) over 6 to 12 months if deploying large sums during high market valuations.",
            "Keep your investment horizon at least 5 to 7 years for equity lumpsum allocations.",
            "Select Direct Plans to maximize net compounding over long holding periods."
        ],
        "donts": [
            "Do not deploy all your emergency reserves or short-term funds in equity lumpsum.",
            "Do not panic and withdraw your lumpsum during short-term market volatility.",
            "Do not attempt to catch the exact market bottom — systematic deployment beats waiting.",
            "Do not ignore the impact of capital gains tax when planning your exit."
        ],
        "faqs": [
            ("When is Lumpsum better than SIP?", "Lumpsum is mathematically advantageous in sustained bull markets or during major market corrections when stock valuations are discounted, as 100% of capital begins compounding immediately."),
            ("What is an STP (Systematic Transfer Plan)?", "An STP allows you to deposit a lumpsum in a safe Liquid Debt Fund and automatically transfer a fixed portion into an Equity Fund monthly, capturing the benefits of both debt yield and Rupee Cost Averaging.")
        ]
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
        "calc_type": "step_up",
        "insights_title": "Why Step-Up SIPs Supercharge Long-Term Wealth",
        "insights_p": "A Step-Up SIP (also called Top-Up SIP) automatically increases your monthly installment by a fixed percentage (such as 10%) every year. This aligns your investments with career salary appraisals, beating lifestyle inflation before surplus cash is spent.",
        "rule_box_title": "The 10% Step-Up Multiplier Effect",
        "rule_box_desc": "A flat ₹10,000 monthly SIP over 20 years at 12% CAGR generates approximately ₹1.00 Crore on ₹24 Lakh invested. By adding a 10% annual step-up, your total investment rises to ₹68.7 Lakh, while your final corpus surges to ₹1.86 Crore — adding an extra ₹86 Lakh in wealth.",
        "personas": [
            ("Early Career Graduate", "Ankit starts with ₹5,000/month and steps up by 10% yearly. In 20 years at 12% CAGR, his corpus reaches approximately ₹93.2 Lakh."),
            ("IT Professional (10% Step-Up)", "Neha starts with ₹15,000/month with a 10% annual top-up. In 15 years at 12% CAGR, her portfolio crosses ₹1.35 Crore."),
            ("Senior Manager (15% Step-Up)", "Ramesh starts with ₹25,000/month stepping up by 15% yearly. In 12 years at 12% CAGR, his corpus reaches approximately ₹1.28 Crore.")
        ],
        "dos": [
            "Set your step-up anniversary date to coincide with your annual salary appraisal cycle.",
            "Use a percentage step-up (e.g., 10%) rather than a fixed amount to match percentage salary hikes.",
            "Set an upper ceiling cap if your platform allows, so the monthly SIP does not exceed your budget.",
            "Automate top-up instructions directly through your mutual fund portal or e-mandate."
        ],
        "donts": [
            "Do not overcommit to an aggressive 25-30% annual step-up that may strain your monthly cash flow.",
            "Do not stop your base SIP if you cannot step up in a year when no salary appraisal occurs.",
            "Do not forget to review your asset allocation as your equity portfolio value expands."
        ],
        "faqs": [
            ("Can I modify or pause the step-up percentage later?", "Yes. You can edit, pause, or disable the step-up instruction online through your mutual fund platform without penalty."),
            ("Is Step-Up SIP better than starting multiple new SIPs?", "Yes. A Step-Up SIP keeps your portfolio streamlined within existing mutual fund folios rather than cluttering your dashboard with dozens of separate schemes.")
        ]
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
        "calc_type": "goal",
        "insights_title": "Goal-Based Investing: Working Backwards to Financial Freedom",
        "insights_p": "Goal-based financial planning shifts the focus from random investing to purposeful capital accumulation. Whether planning for retirement, purchasing a home, or funding higher education, calculating your required monthly savings rate ensures your financial roadmap is achievable.",
        "rule_box_title": "Inflation-Adjusted Target Sizing",
        "rule_box_desc": "Always adjust your target goal for inflation. A higher education degree costing ₹20 Lakh today will require approximately ₹51.8 Lakh in 15 years at an average 6.5% education inflation rate. Always calculate required SIP amounts based on the future inflated goal cost.",
        "personas": [
            ("Retirement Goal (₹3 Crore in 20 Yrs)", "To accumulate ₹3 Crore in 20 years at an illustrative 12% CAGR, you need to invest approximately ₹30,025 per month."),
            ("Child Education (₹50 Lakh in 12 Yrs)", "To build a ₹50 Lakh college fund in 12 years at 12% CAGR, you need a monthly SIP of roughly ₹15,600."),
            ("Home Down Payment (₹25 Lakh in 7 Yrs)", "To accumulate a ₹25 Lakh down payment in 7 years at 10% CAGR in hybrid funds, you need approximately ₹20,600 per month.")
        ],
        "dos": [
            "Categorize goals by time horizon: Short-Term (<3 yrs), Medium-Term (3-7 yrs), Long-Term (7+ yrs).",
            "De-risk your investments by shifting money from equity to liquid debt funds 2 to 3 years before the goal deadline.",
            "Create separate mutual fund folios dedicated to each specific life goal.",
            "Review your goal progress annually and adjust monthly contributions as your income grows."
        ],
        "donts": [
            "Do not mix your emergency fund with long-term financial goal portfolios.",
            "Do not assume constant returns — keep a 10% to 15% safety buffer in your target corpus.",
            "Do not invest short-term money (needed within 2 years) in volatile equity markets."
        ],
        "faqs": [
            ("How do I calculate future inflation on my goals?", "Use the future value formula: FV = PV × (1 + Inflation Rate)^Years. For general living costs, assume 6% inflation; for healthcare and higher education in India, assume 9% to 11% annual inflation.")
        ]
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
        "calc_type": "fd",
        "insights_title": "Understanding Bank Fixed Deposits in India",
        "insights_p": "Bank Fixed Deposits (FDs) offer guaranteed capital safety and predictable interest earnings. In India, scheduled commercial bank FDs are insured up to ₹5,00,000 per depositor per bank by the Deposit Insurance and Credit Guarantee Corporation (DICGC).",
        "rule_box_title": "Quarterly Compounding Standard in Indian Banks",
        "rule_box_desc": "Most Indian banks calculate interest on a quarterly compounding basis for reinvestment (cumulative) FDs. This means your effective annual yield is slightly higher than the stated nominal interest rate. For example, a 7.5% nominal rate compounded quarterly yields an effective 7.71% per year.",
        "personas": [
            ("Emergency Reserve (₹3 Lakh for 1 Yr)", "Rohan deposits ₹3 Lakh in a 1-year FD at 7.0% p.a. (quarterly compounding). Maturity value: ₹3,21,566 (Interest: ₹21,566)."),
            ("Senior Citizen Corpus (₹10 Lakh for 3 Yrs)", "Smt. Sharma deposits ₹10 Lakh in a senior citizen FD at 7.75% p.a. Maturity value: ₹12,58,450 (Interest: ₹2,58,450)."),
            ("5-Year Tax-Saving FD (₹1.5 Lakh)", "Vikas deposits ₹1.5 Lakh in a 5-year tax-saving FD at 7.1% under Section 80C. Maturity value: ₹2,13,180 (Interest: ₹63,180).")
        ],
        "dos": [
            "Use the FD Laddering strategy (splitting capital across 1, 2, 3, 4, 5-year tenures) to maintain liquidity.",
            "Senior citizens should claim the ₹50,000 interest deduction under Section 80TTB.",
            "Submit Form 15G or Form 15H if your total annual taxable income is below the taxable limit to avoid TDS.",
            "Distribute large deposits across different scheduled commercial banks to maximize the ₹5 Lakh DICGC insurance coverage."
        ],
        "donts": [
            "Do not break your FD prematurely for minor expenses — use an overdraft facility against the FD instead.",
            "Do not forget that FD interest is taxable at your marginal income tax slab rate.",
            "Do not keep all your multi-decade retirement savings in FDs, as inflation will erode real purchasing power."
        ],
        "faqs": [
            ("What is the TDS threshold on Bank FD interest?", "Banks deduct 10% TDS under Section 194A if total interest across branch deposits exceeds ₹40,000 per financial year for regular depositors, or ₹50,000 for senior citizens.")
        ]
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
        "calc_type": "budget",
        "insights_title": "The 50-30-20 Budget Blueprint for Indian Households",
        "insights_p": "The 50-30-20 rule divides your post-tax monthly take-home salary into three functional buckets: 50% for essential Needs (rent, groceries, bills, EMIs), 30% for discretionary Wants (dining out, travel, gadgets), and 20% for Savings and Investments (emergency fund, SIPs, PPF).",
        "rule_box_title": "Metro City Adaptation: The 60-20-20 Rule",
        "rule_box_desc": "If high rental costs in metro cities (Mumbai, Bengaluru, Delhi NCR) consume over 35-40% of your income, adapt the framework to 60% Needs, 20% Wants, and 20% Savings. Never reduce the 20% savings portion below baseline.",
        "personas": [
            ("Entry-Level Salary (₹35,000/mo)", "Needs (50%): ₹17,500 | Wants (30%): ₹10,500 | Savings (20%): ₹7,000 / month. In 10 years at 12% CAGR, savings grow to ₹16.26 Lakh."),
            ("Mid-Career Earner (₹80,000/mo)", "Needs (50%): ₹40,000 | Wants (30%): ₹24,000 | Savings (20%): ₹16,000 / month. In 10 years at 12% CAGR, savings reach ₹37.17 Lakh."),
            ("Senior Professional (₹1,50,000/mo)", "Needs (50%): ₹75,000 | Wants (30%): ₹45,000 | Savings (20%): ₹30,000 / month. In 15 years at 12% CAGR, savings reach ₹1.51 Crore.")
        ],
        "dos": [
            "Automate your 20% savings transfer to investments on the day your salary is credited.",
            "Track your discretionary spending (dining, online shopping) using digital banking categories.",
            "Build an emergency fund of 3 to 6 months of essential expenses before aggressive investing.",
            "Reallocate any annual bonus directly toward debt reduction and investment goals."
        ],
        "donts": [
            "Do not treat credit card limits as part of your monthly disposable budget.",
            "Do not compromise your 20% savings rate to finance lifestyle luxury upgrades.",
            "Do not forget to account for irregular annual expenses like insurance premiums."
        ],
        "faqs": [
            ("Is the 50-30-20 rule calculated on gross CTC or net in-hand salary?", "The rule applies strictly to your post-tax net take-home salary credited to your bank account after all PF and tax deductions.")
        ]
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
        "calc_type": "tax",
        "insights_title": "Old vs New Tax Regime: Key Differences & Slabs",
        "insights_p": "The New Tax Regime is the default regime under Indian tax law, featuring lower tax slab rates and an enhanced ₹75,000 standard deduction, but disallowing itemized deductions. The Old Tax Regime allows extensive deductions (80C, 80D, HRA, Home Loan interest) but has higher tax slab rates.",
        "rule_box_title": "The Deduction Break-Even Threshold",
        "rule_box_desc": "For annual salaries between ₹12 Lakh and ₹25 Lakh, the Old Regime is typically advantageous only if your total eligible deductions (80C + 80D + HRA + Home Loan interest) exceed approximately ₹3.75 Lakh to ₹4.25 Lakh per year.",
        "personas": [
            ("Salary ₹7.5 Lakh (Zero Tax in New Regime)", "With the Section 87A rebate and ₹75,000 standard deduction, salary income up to ₹7.75 Lakh incurs zero tax under the New Tax Regime without needing any investments."),
            ("Salary ₹12 Lakh (Moderate Deductions)", "Under New Regime: Tax ~₹83,200. Under Old Regime (with ₹2L deductions): Tax ~₹98,800. New Regime saves ₹15,600."),
            ("Salary ₹18 Lakh (Heavy Deductions ₹4.5L)", "Under Old Regime (with ₹4.5L deductions + HRA): Tax ~₹1,87,200. Under New Regime: Tax ~₹2,08,000. Old Regime saves ₹20,800.")
        ],
        "dos": [
            "Salaried individuals can choose between Old and New regimes every year while filing their ITR.",
            "Compare your deductions using this calculator before submitting your annual tax declarations to your employer.",
            "Utilize Section 80CCD(1B) for an additional ₹50,000 NPS deduction under the Old Regime.",
            "Keep rent receipts and home loan interest certificates organized for HRA and Section 24b claims."
        ],
        "donts": [
            "Do not buy low-yielding traditional insurance policies solely to claim Section 80C deductions.",
            "Do not forget that the New Regime offers an automatic ₹75,000 standard deduction for salaried staff.",
            "Do not delay your tax planning until March — start systematic tax-saving investments in April."
        ],
        "faqs": [
            ("Can self-employed professionals switch regimes every year?", "No. Individuals with business or professional income can switch to the Old Regime only once in their lifetime, after which switching back has strict limitations.")
        ]
    }
]

def build_rich_calculators():
    for c in CALCULATOR_SPECS:
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

        personas_html = "".join([f"""
          <div class="scenario-box">
            <h4>{p_title}</h4>
            <p>{p_desc}</p>
          </div>
        """ for p_title, p_desc in c["personas"]])

        dos_html = "".join([f"<li>{item}</li>" for item in c["dos"]])
        donts_html = "".join([f"<li>{item}</li>" for item in c["donts"]])

        faq_items_html = "".join([f"""
          <details class="faq-item" style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:12px;">
            <summary style="font-weight:700; cursor:pointer; font-size:0.98rem; color:var(--text-primary);">{html.escape(q)}</summary>
            <p style="margin-top:12px; color:var(--text-secondary); line-height:1.6; margin-bottom:0;">{ans}</p>
          </details>
        """ for q, ans in c["faqs"]])

        page_html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']} | Calculatorship</title>
  <meta name="description" content="{c['metaDesc']}">
  <link rel="canonical" href="{c['slug']}">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['metaDesc']}">
  <meta property="og:url" content="{c['slug']}">
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
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "{c['h1']}",
    "url": "{c['slug']}",
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

      <!-- Section 1: Key Financial Insights & Rules -->
      <div class="info-section-card">
        <h2>{c['insights_title']}</h2>
        <p>{c['insights_p']}</p>
        
        <div style="background:var(--emerald-soft); border:1.5px solid var(--emerald-border); border-radius:var(--radius-md); padding:20px; margin:20px 0;">
          <h3 style="margin:0 0 6px; font-size:1.1rem; color:var(--emerald-dark);">{c['rule_box_title']}</h3>
          <p style="margin:0; font-size:0.92rem; color:var(--text-primary); line-height:1.6;">{c['rule_box_desc']}</p>
        </div>
      </div>

      <!-- Section 2: Worked Real-World Scenarios -->
      <div class="info-section-card">
        <h2>Real-World Indian Scenarios &amp; Case Studies</h2>
        <p>Explore how different savings amounts and compounding horizons impact real wealth building across career stages:</p>
        <div class="scenario-grid">
          {personas_html}
        </div>
      </div>

      <!-- Section 3: Mistakes & Pro Tips Checklist -->
      <div class="info-section-card">
        <h2>Best Practices vs Common Pitfalls</h2>
        <p>Follow these disciplined principles to maximize your long-term compounding efficiency:</p>
        <div class="checklist-grid">
          <div class="checklist-box dos">
            <h4>Recommended Practices</h4>
            <ul>{dos_html}</ul>
          </div>
          <div class="checklist-box donts">
            <h4>Mistakes to Avoid</h4>
            <ul>{donts_html}</ul>
          </div>
        </div>
      </div>

      <!-- Section 4: FAQ Accordion -->
      <div class="info-section-card">
        <h2>Frequently Asked Questions</h2>
        {faq_items_html}
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

        with open(os.path.join(SITE_DIR, c["slug"]), "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"Generated Rich Calculator: {c['slug']}")

if __name__ == "__main__":
    build_rich_calculators()
