import os
import json
import html
import re
from build_components import get_header, get_calc_switcher, get_all_calculators_grid, get_footer, SITE_DIR

# ============================================================
# 10 RICH CALCULATOR SPECIFICATIONS
# ============================================================
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
        "title": "Lumpsum Calculator: One-Time Mutual Fund Return Calculator",
        "metaDesc": "Project future returns on one-time lumpsum mutual fund investments in India. Calculate total gains and compounding growth across 1 to 30 years.",
        "h1": "Lumpsum Investment Calculator",
        "subtitle": "Calculate projected maturity wealth from a one-time capital investment in mutual funds or market instruments.",
        "field1": {"id": "lumpsum-amount", "label": "Total Lumpsum Investment", "min": 5000, "max": 10000000, "step": 5000, "val": 100000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 10, "prefix": "", "suffix": "Yrs"},
        "calc_type": "lumpsum",
        "insights_title": "Understanding Lumpsum Compounding Dynamics",
        "insights_p": "Unlike periodic SIPs where capital is deployed gradually, a lumpsum investment exposes 100% of your capital to compound growth from Day 1. This generates massive compounding momentum over 10-20 years, provided the investor remains invested through market fluctuations.",
        "rule_box_title": "The Rule of 72 for Lumpsum Investments",
        "rule_box_desc": "Divide 72 by your expected annual return rate to discover how fast your lumpsum doubles. At 12% CAGR, your money doubles every 6 years. A ₹5 Lakh lumpsum becomes ₹10 Lakh in 6 years, ₹20 Lakh in 12 years, and ₹40 Lakh in 18 years.",
        "personas": [
            ("Annual Bonus Deployment", "Neha receives an annual bonus of ₹2,50,000 and invests it in a diversified flexi-cap fund. Over 10 years at 12% CAGR, it grows to ₹7,76,462."),
            ("Matured Fixed Deposit Reinvestment", "Ramesh reinvests a matured ₹10 Lakh FD into an equity index fund. Over 15 years at 12% CAGR, his capital expands to ₹54,73,566."),
            ("Inheritance Allocation", "Kavita deploys a ₹25 Lakh corpus into a balanced hybrid fund. Over 20 years at 11% CAGR, it compounds to ₹2.01 Crore.")
        ],
        "dos": [
            "Use Systematic Transfer Plans (STP) if you are hesitant about deploying large lump sums at all-time market highs.",
            "Maintain a minimum 5-to-7 year investment horizon when making lumpsum equity investments.",
            "Choose Direct growth plans to prevent intermediary fee leakage over multi-decade tenures."
        ],
        "donts": [
            "Do not deploy your entire emergency fund into a single equity lumpsum.",
            "Do not panic sell your portfolio when market cycles produce temporary unrealized paper losses.",
            "Do not attempt to time market bottoms with your entire life savings."
        ],
        "faqs": [
            ("When is the best time to invest a lumpsum amount?", "Statistically, time in the market beats timing the market. However, deploying lumpsum capital during market corrections or spreading it over 6-12 months via an STP offers peace of mind."),
            ("How does lumpsum compounding differ from SIP?", "In lumpsum investing, the entire capital earns interest from day one. In SIP, capital enters periodically, so later contributions compound for shorter durations.")
        ]
    },
    {
        "slug": "step-up.html",
        "title": "Step-Up SIP Calculator: Top-Up SIP Growth Calculator India",
        "metaDesc": "Calculate exponential wealth growth when increasing your monthly SIP by 5% to 20% annually with salary hikes.",
        "h1": "Step-Up SIP Calculator (Top-Up SIP)",
        "subtitle": "Discover how increasing your monthly SIP contributions annually with career salary increments supercharges your wealth.",
        "field1": {"id": "monthly-investment", "label": "Initial Monthly SIP Amount", "min": 500, "max": 1000000, "step": 500, "val": 10000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "Investment Duration", "min": 1, "max": 40, "step": 1, "val": 15, "prefix": "", "suffix": "Yrs"},
        "field4": {"id": "step-up-pct", "label": "Annual Step-Up Rate", "min": 1, "max": 50, "step": 1, "val": 10, "prefix": "", "suffix": "%"},
        "calc_type": "step_up",
        "insights_title": "The Supercharged Multiplier Effect of Step-Up SIPs",
        "insights_p": "Salaried professionals typically experience annual income growth of 7% to 15%. By stepping up your monthly SIP by just 10% each year, your final accumulated corpus often doubles compared to a flat SIP over a 15-20 year horizon.",
        "rule_box_title": "Flat SIP vs 10% Step-Up SIP Comparison",
        "rule_box_desc": "A constant ₹10,000/month SIP for 15 years at 12% CAGR yields approximately ₹50.2 Lakh (Invested: ₹18.0 L). Stepping up that same SIP by 10% annually yields approximately ₹89.2 Lakh (Invested: ₹38.1 L) — creating an additional ₹39.0 Lakh in wealth.",
        "personas": [
            ("Early IT Professional", "Vikram starts with ₹5,000/month and steps up by 10% each year. Over 20 years at 12% CAGR, his corpus exceeds ₹1.17 Crore compared to just ₹49.9 Lakh in a flat SIP."),
            ("Senior Manager", "Sneha begins with ₹25,000/month with a 10% annual top-up. Over 15 years at 12% CAGR, she accumulates ₹2.23 Crore."),
            ("Aggressive Saver", "Aditya steps up his ₹15,000/month SIP by 15% annually. Over 15 years, his portfolio crosses ₹1.65 Crore.")
        ],
        "dos": [
            "Set up automated Annual Step-Up mandates with your mutual fund platform.",
            "Align your annual step-up percentage with your expected corporate appraisal cycle.",
            "Use career bonuses to make occasional ad-hoc top-up investments."
        ],
        "donts": [
            "Do not inflate your living expenses without increasing your monthly investment allocation.",
            "Do not set an unrealistic step-up rate (>30%) that strains your essential cash flows."
        ],
        "faqs": [
            ("How do I activate a step-up SIP in Indian mutual funds?", "Most platforms like Groww, Zerodha Coin, MF Central, and AMC portals offer an 'Annual Top-Up' checkbox when starting a new SIP."),
            ("Can I cap the maximum monthly SIP in a step-up plan?", "Yes. You can specify a maximum monthly limit (e.g., stop stepping up once monthly SIP reaches ₹50,000).")
        ]
    },
    {
        "slug": "goal.html",
        "title": "Goal Planner Calculator: Target Wealth & SIP Calculator India",
        "metaDesc": "Calculate the exact monthly SIP investment required to reach your target financial corpus for retirement, house purchase, or child education.",
        "h1": "Goal-Based SIP Planner",
        "subtitle": "Calculate the exact monthly investment needed to reach your dream target wealth milestone within your chosen timeline.",
        "field1": {"id": "target-amount", "label": "Target Corpus Goal", "min": 100000, "max": 100000000, "step": 50000, "val": 10000000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 1, "max": 30, "step": 0.5, "val": 12, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "Years to Achieve Goal", "min": 1, "max": 40, "step": 1, "val": 15, "prefix": "", "suffix": "Yrs"},
        "calc_type": "goal",
        "insights_title": "Reverse Financial Engineering: Goal-First Planning",
        "insights_p": "Goal-based financial planning eliminates guesswork by working backwards from your desired financial target. By knowing the exact monthly contribution required, you can budget effectively and track your progress objectively.",
        "rule_box_title": "Inflation Factoring Rule",
        "rule_box_desc": "Always account for inflation when setting future goals. A higher education degree costing ₹25 Lakh today will cost approximately ₹53.8 Lakh in 10 years at a 8% education inflation rate.",
        "personas": [
            ("Targeting ₹1.00 Crore for Retirement", "To build ₹1.00 Crore in 15 years at 12% CAGR, you need a monthly SIP of ₹19,910."),
            ("Targeting ₹50 Lakh for Child College (10 Yrs)", "To accumulate ₹50 Lakh in 10 years at 12% CAGR, you need a monthly SIP of ₹21,520."),
            ("Targeting ₹25 Lakh for House Downpayment (5 Yrs)", "To save ₹25 Lakh in 5 years at 10% CAGR, you need a monthly SIP of ₹30,320.")
        ],
        "dos": [
            "Tag every mutual fund investment to a specific milestone (Retirement, Child, House).",
            "De-risk your portfolio from equity to debt 2-3 years prior to reaching the goal deadline.",
            "Review your goal progression annually against target milestones."
        ],
        "donts": [
            "Do not mix short-term goals (<3 years) with volatile high-risk small-cap equities.",
            "Do not withdraw from a long-term goal fund for impulsive discretionary expenses."
        ],
        "faqs": [
            ("What if I cannot afford the calculated monthly SIP?", "Start with whatever amount you can afford today and use an annual step-up of 10-15% to close the gap as your salary grows.")
        ]
    },
    {
        "slug": "ppf-calculator.html",
        "title": "PPF Calculator: Public Provident Fund Maturity & Interest Calculator",
        "metaDesc": "Calculate Public Provident Fund (PPF) maturity amount, total interest earned, and 100% tax-free wealth across 15 to 30 years in India.",
        "h1": "Public Provident Fund (PPF) Calculator",
        "subtitle": "Calculate guaranteed compounding returns, annual interest accumulation, and 100% tax-free maturity proceeds under Section 80C EEE.",
        "field1": {"id": "yearly-investment", "label": "Yearly PPF Deposit", "min": 500, "max": 150000, "step": 500, "val": 150000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Current PPF Interest Rate", "min": 5, "max": 10, "step": 0.1, "val": 7.1, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "PPF Tenure (Years)", "min": 15, "max": 30, "step": 5, "val": 15, "prefix": "", "suffix": "Yrs"},
        "calc_type": "ppf",
        "insights_title": "The Triple Tax Advantage (EEE) of Public Provident Fund",
        "insights_p": "Public Provident Fund (PPF) is backed by the Government of India, offering sovereign safety with zero credit risk. PPF enjoys the coveted Exempt-Exempt-Exempt (EEE) tax status: deposits qualify for Section 80C deductions, annual interest accrued is 100% tax-free, and maturity proceeds are completely exempt from income tax.",
        "rule_box_title": "The Crucial 5th of the Month PPF Rule",
        "rule_box_desc": "PPF interest is calculated monthly on the lowest balance between the close of the 5th day and the end of the month, but credited annually on March 31st. Always deposit your yearly contribution before April 5th to earn interest for all 12 months.",
        "personas": [
            ("Maximum 80C Saver (15 Years)", "Ankit deposits the statutory maximum ₹1,50,000 every year before April 5th. Over 15 years at 7.1% interest, his ₹22.5 Lakh investment generates ₹18.18 Lakh in tax-free interest, yielding a maturity corpus of ₹40.68 Lakh."),
            ("Extended 25-Year Compounder", "Meera extends her PPF in 5-year blocks for a total of 25 years. Her ₹37.5 Lakh total deposits compound into a guaranteed tax-free corpus of ₹1.03 Crore."),
            ("Moderate Disciplined Saver", "Rajesh deposits ₹5,000 per month (₹60,000/year). Over 15 years, his ₹9.0 Lakh investment grows into ₹16.27 Lakh completely tax-free.")
        ],
        "dos": [
            "Deposit your annual PPF contribution between April 1st and April 5th to maximize interest earnings.",
            "Submit Form H within 1 year of maturity if you wish to extend your PPF account in 5-year blocks with contributions.",
            "Open a PPF account for minor children to build guaranteed long-term education funds."
        ],
        "donts": [
            "Do not deposit more than ₹1,50,000 in a single financial year as excess funds earn zero interest.",
            "Do not allow your PPF account to become inactive by missing the minimum annual deposit of ₹500.",
            "Do not close your PPF prematurely unless facing specified medical or higher education emergencies."
        ],
        "faqs": [
            ("What is the maximum yearly limit in PPF?", "The statutory maximum limit is ₹1,50,000 per financial year across all PPF accounts held by an individual (including accounts opened as a guardian for minors)."),
            ("Can PPF be extended after the mandatory 15-year period?", "Yes. You can extend your PPF account indefinitely in blocks of 5 years, with or without continuing fresh deposits."),
            ("Is PPF interest taxable in India?", "No. PPF interest is 100% tax-free under Section 10(11) of the Income Tax Act under both Old and New Tax Regimes.")
        ]
    },
    {
        "slug": "swp-calculator.html",
        "title": "SWP Calculator: Systematic Withdrawal Plan Calculator Mutual Funds",
        "metaDesc": "Simulate monthly pension withdrawals, total cashflow, and remaining mutual fund portfolio balance with our free SWP calculator.",
        "h1": "SWP Calculator (Systematic Withdrawal Plan)",
        "subtitle": "Plan tax-efficient monthly income and retirement pension withdrawals while keeping your mutual fund corpus growing.",
        "field1": {"id": "total-corpus", "label": "Initial Investment Corpus", "min": 100000, "max": 50000000, "step": 50000, "val": 5000000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "monthly-withdrawal", "label": "Monthly Withdrawal Amount", "min": 1000, "max": 500000, "step": 1000, "val": 30000, "prefix": "₹", "suffix": ""},
        "field3": {"id": "expected-return", "label": "Expected Annual Return (CAGR)", "min": 4, "max": 20, "step": 0.5, "val": 10, "prefix": "", "suffix": "%"},
        "field4": {"id": "time-period", "label": "Withdrawal Duration", "min": 1, "max": 35, "step": 1, "val": 20, "prefix": "", "suffix": "Yrs"},
        "calc_type": "swp",
        "insights_title": "Why SWP Beats Traditional Bank FDs and Annuities for Retirees",
        "insights_p": "A Systematic Withdrawal Plan (SWP) allows retirees to withdraw a fixed monthly cash flow from mutual funds while the remaining capital continues generating market returns. Unlike bank FD interest which is taxed at your highest income slab rate, SWP redemptions are taxed only on the capital gains proportion, resulting in massive tax savings.",
        "rule_box_title": "The Golden 6% Safe Withdrawal Rate Rule in India",
        "rule_box_desc": "To ensure your retirement corpus never depletes over a 25-30 year retirement in India, maintain your initial annual withdrawal rate at or below 6% of your starting corpus (e.g., ₹25,000 to ₹30,000/month from a ₹60 Lakh corpus invested in hybrid funds).",
        "personas": [
            ("Senior Citizen Pension (₹50 Lakh Corpus)", "Suresh retires at 60 with ₹50 Lakh in a Conservative Hybrid Fund. Withdrawing ₹30,000/month for 20 years at a 9% return yields ₹72 Lakh in total pension, while his ending balance still stands at ₹56.4 Lakh."),
            ("Early FIRE Retiree (₹1.50 Crore Corpus)", "Amit achieves financial independence at 42. Withdrawing ₹75,000/month from a balanced portfolio at 11% CAGR for 25 years provides ₹2.25 Crore in cash flow, with a closing corpus of ₹4.82 Crore."),
            ("Rental Income Alternative (₹25 Lakh Corpus)", "Priya invests ₹25 Lakh and withdraws ₹15,000/month. Over 15 years at 10% CAGR, she receives ₹27 Lakh in payouts with ₹27.6 Lakh remaining.")
        ],
        "dos": [
            "Maintain 2-3 years of living expenses in liquid debt funds to avoid withdrawing from equities during sharp market dips.",
            "Park your primary SWP corpus in Balanced Advantage or Multi-Asset Allocation funds for low-volatility stability.",
            "Re-evaluate your monthly withdrawal rate every 2-3 years against prevailing inflation."
        ],
        "donts": [
            "Do not withdraw more than 8% annually from your corpus, as high withdrawal rates cause premature capital exhaustion.",
            "Do not park 100% of your SWP retirement money in high-beta small-cap funds.",
            "Do not opt for the mutual fund Dividend option when SWP gives you complete control over payout dates and amounts."
        ],
        "faqs": [
            ("How is tax calculated on SWP withdrawals?", "Each SWP withdrawal is treated as a partial redemption of units. Only the capital gains portion of the withdrawn amount is taxed (equity LTCG at 12.5% above ₹1.25L/yr exemption), making SWP vastly more tax-efficient than FD interest."),
            ("What happens if the market crashes during SWP?", "If equity markets crash, withdrawing from equity funds liquidates more units. Having a debt fund buffer protects your equity units during market corrections.")
        ]
    },
    {
        "slug": "emi-calculator.html",
        "title": "Loan EMI & Prepayment Calculator: Home & Personal Loan Savings",
        "metaDesc": "Calculate loan EMI and simulate how part prepayments save lakhs in interest and reduce your loan tenure by years.",
        "h1": "Loan EMI & Prepayment Calculator",
        "subtitle": "Calculate monthly loan EMIs and see how smart extra prepayments save lakhs of rupees in interest and cut years off your tenure.",
        "field1": {"id": "loan-amount", "label": "Loan Amount", "min": 100000, "max": 50000000, "step": 50000, "val": 5000000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "interest-rate", "label": "Annual Interest Rate", "min": 5, "max": 20, "step": 0.1, "val": 8.5, "prefix": "", "suffix": "%"},
        "field3": {"id": "loan-tenure", "label": "Loan Tenure (Years)", "min": 1, "max": 30, "step": 1, "val": 20, "prefix": "", "suffix": "Yrs"},
        "field4": {"id": "monthly-prepay", "label": "Extra Monthly Prepayment", "min": 0, "max": 100000, "step": 1000, "val": 5000, "prefix": "₹", "suffix": ""},
        "calc_type": "emi",
        "insights_title": "The Staggering Cost of Long-Term Loan Interest",
        "insights_p": "On a standard 20-year home loan of ₹50 Lakh at 8.5% interest, your total interest paid amounts to over ₹54.1 Lakh — which is greater than the original principal borrowed! Making small, consistent prepayments directly slashes your principal balance, resulting in compounding interest savings.",
        "rule_box_title": "The Power of Paying Just 1 Extra EMI Every Year",
        "rule_box_desc": "Paying just 1 additional EMI every calendar year on a 20-year home loan reduces your total loan tenure from 20 years down to approximately 16.5 years and saves over ₹10 Lakh in interest payments.",
        "personas": [
            ("Home Loan Prepayment (₹50 Lakh Loan)", "Rohan takes a ₹50 Lakh home loan at 8.5% for 20 years (EMI: ₹43,391). By prepaying ₹5,000 extra every month, he cuts his tenure by 4.5 years and saves ₹11.2 Lakh in interest."),
            ("Car Loan Acceleration (₹10 Lakh Loan)", "Karthik prepays ₹2,500/month on a 5-year ₹10 Lakh auto loan at 9.0%, closing the loan 7 months earlier and saving ₹38,000 in interest."),
            ("Lumpsum Bonus Prepayment", "Ananya prepays ₹2 Lakh from her annual bonus in Year 3 of her home loan, saving over ₹6.5 Lakh in overall interest.")
        ],
        "dos": [
            "Ensure part-prepayments are credited toward Principal reduction rather than future advance EMIs.",
            "Check that your bank charges zero prepayment penalties on floating-rate home loans (as mandated by RBI).",
            "Automate a small monthly prepayment alongside your regular EMI."
        ],
        "donts": [
            "Do not exhaust your emergency liquid reserves to prepay a low-interest home loan.",
            "Do not choose high-interest fixed-rate personal loans when lower-rate secured alternatives exist."
        ],
        "faqs": [
            ("Are there any prepayment penalties on home loans in India?", "Under RBI guidelines, commercial banks and housing finance companies cannot levy prepayment or foreclosure charges on floating-rate home loans taken by individual borrowers."),
            ("Should I prepay my home loan or invest in mutual funds?", "If your loan interest rate is 8.5% and expected mutual fund returns are 12%, investing offers a mathematical advantage. However, prepaying guarantees an 8.5% risk-free return and psychological debt freedom.")
        ]
    },
    {
        "slug": "fd-calculator.html",
        "title": "Fixed Deposit (FD) Calculator: Bank FD Interest & Maturity Value",
        "metaDesc": "Calculate maturity value and interest earnings on bank Fixed Deposits with quarterly compounding for general and senior citizens.",
        "h1": "Fixed Deposit (FD) Calculator",
        "subtitle": "Calculate maturity value and cumulative quarterly compounding interest earnings on bank fixed deposits in India.",
        "field1": {"id": "fd-principal", "label": "Fixed Deposit Amount", "min": 5000, "max": 10000000, "step": 5000, "val": 500000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "expected-return", "label": "Annual Interest Rate", "min": 2, "max": 12, "step": 0.1, "val": 7.2, "prefix": "", "suffix": "%"},
        "field3": {"id": "time-period", "label": "Deposit Tenure", "min": 1, "max": 10, "step": 1, "val": 5, "prefix": "", "suffix": "Yrs"},
        "calc_type": "fd",
        "insights_title": "Quarterly Compounding Mechanics in Indian Fixed Deposits",
        "insights_p": "Indian commercial banks compound FD interest on a quarterly basis (4 times per year). Consequently, the annual effective yield on your fixed deposit is slightly higher than the nominal stated interest rate.",
        "rule_box_title": "Senior Citizen Interest Premium",
        "rule_box_desc": "Indian banks typically offer an additional 0.50% to 0.75% higher interest rate on fixed deposits for senior citizens (age 60+), and special super-senior rates (age 80+) across public and private banks.",
        "personas": [
            ("Emergency Reserve Parking", "Sandeep keeps ₹3 Lakh in a 1-year bank FD at 7.0% for immediate emergency liquidity, earning ₹21,556 in annual interest."),
            ("Senior Citizen Retirement Capital", "Kamla Devi (age 64) deposits ₹15 Lakh for 5 years at 7.75%. Her maturity corpus reaches ₹22.04 Lakh with quarterly compounding."),
            ("Tax Saving 5-Year FD", "Varun deposits ₹1.5 Lakh in a 5-year tax-saving FD under Section 80C at 7.1%, earning ₹63,338 in total interest.")
        ],
        "dos": [
            "Use FD laddering across different maturity buckets to optimize liquidity and interest rate cycles.",
            "Submit Form 15G (or Form 15H for senior citizens) to prevent TDS deduction if your total income is below the taxable threshold.",
            "Check DICGC insurance coverage (up to ₹5 Lakh per depositor per bank)."
        ],
        "donts": [
            "Do not park 100% of your long-term wealth (>10 years) in FDs, as inflation and tax drag will erode real purchasing power.",
            "Do not break FDs prematurely without checking penalty clauses (usually 0.5% - 1.0%)."
        ],
        "faqs": [
            ("How is interest compounded on bank FDs in India?", "Most Indian banks compute and compound interest on cumulative FDs at the end of every calendar quarter (March, June, September, December)."),
            ("Is FD interest taxable?", "Yes. FD interest is fully taxable at your applicable income tax slab rate. Banks deduct 10% TDS if annual interest exceeds ₹40,000 (₹50,000 for senior citizens).")
        ]
    },
    {
        "slug": "budget-planner.html",
        "title": "50-30-20 Budget Calculator: Salary Allocation & Expense Planner",
        "metaDesc": "Plan your monthly household budget using the 50-30-20 rule. Divide take-home salary into Needs, Wants, and Wealth Savings in India.",
        "h1": "50-30-20 Budget Planner",
        "subtitle": "Structure your take-home salary into Essential Needs (50%), Lifestyle Wants (30%), and Future Wealth Investments (20%).",
        "field1": {"id": "monthly-income", "label": "Monthly Take-Home Salary", "min": 10000, "max": 2000000, "step": 1000, "val": 75000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "needs-pct", "label": "Essential Needs Allocation", "min": 30, "max": 70, "step": 5, "val": 50, "prefix": "", "suffix": "%"},
        "field3": {"id": "wants-pct", "label": "Discretionary Wants Allocation", "min": 10, "max": 50, "step": 5, "val": 30, "prefix": "", "suffix": "%"},
        "calc_type": "budget",
        "insights_title": "Adapting the 50-30-20 Rule to Indian Metro Realities",
        "insights_p": "The 50-30-20 budgeting framework provides a clear guideline to prevent lifestyle inflation. In high-cost Indian metro cities like Bengaluru, Mumbai, or Delhi-NCR, high rent may push Needs to 60%, requiring you to adjust Wants to 20% while safeguarding the vital 20% Savings allocation.",
        "rule_box_title": "The Golden Pay-Yourself-First Principle",
        "rule_box_desc": "Do not save whatever remains after spending. Instead, invest your 20% savings allocation on the very day your salary is credited, and live on the remaining 80%.",
        "personas": [
            ("₹50,000 Take-Home Salary", "Needs (50%): ₹25,000 (Rent, Groceries, Utilities) | Wants (30%): ₹15,000 (Dining, OTT, Shopping) | Savings (20%): ₹10,000 (SIP & Emergency Fund)."),
            ("₹1,20,000 Take-Home Salary", "Needs (50%): ₹60,000 | Wants (30%): ₹36,000 | Savings (20%): ₹24,000 (Multiplies to ₹1.2 Crore in 15 years at 12% CAGR)."),
            ("₹2,50,000 Senior Executive", "Aggressive 40-20-40 Rule: Needs (40%): ₹1,00,000 | Wants (20%): ₹50,000 | Savings (40%): ₹1,00,000/month.")
        ],
        "dos": [
            "Automate mutual fund SIP debits within 48 hours of salary credit.",
            "Track your discretionary spending monthly using mobile banking apps.",
            "Increase your savings percentage to 30-40% as your salary rises with seniority."
        ],
        "donts": [
            "Do not use credit card EMIs for discretionary wants that exceed your monthly 30% allowance.",
            "Do not dip into your 20% savings allocation for impulse shopping."
        ],
        "faqs": [
            ("What expenses are classified as 'Needs'?", "Rent/home loan EMI, groceries, electricity, water, health insurance, children's school fees, and essential transportation."),
            ("What if my essential needs exceed 50%?", "If high housing costs push needs to 60%, trim discretionary wants to 20% rather than reducing your 20% savings buffer.")
        ]
    },
    {
        "slug": "income-tax-calculator.html",
        "title": "Income Tax Calculator: Old vs New Tax Regime Comparison FY 2024-25 / 2025-26",
        "metaDesc": "Compare income tax liability under Old vs New Tax Regimes with Standard Deductions, Section 80C, 80D, HRA, and home loan interest exemptions.",
        "h1": "Income Tax Calculator (Old vs New Regime)",
        "subtitle": "Compare your tax liabilities side-by-side under the Old vs New Tax Regimes with full deductions and exemptions.",
        "field1": {"id": "annual-salary", "label": "Gross Annual Salary / Income", "min": 300000, "max": 10000000, "step": 25000, "val": 1500000, "prefix": "₹", "suffix": ""},
        "field2": {"id": "deductions-80c", "label": "Section 80C Deductions (PPF, ELSS, EPF)", "min": 0, "max": 150000, "step": 5000, "val": 150000, "prefix": "₹", "suffix": ""},
        "field3": {"id": "other-exemptions", "label": "Other Deductions (HRA, 80D, Home Loan 24b)", "min": 0, "max": 1000000, "step": 10000, "val": 200000, "prefix": "₹", "suffix": ""},
        "calc_type": "tax",
        "insights_title": "Budget 2024 Revised Tax Slab Structure in India",
        "insights_p": "The New Tax Regime offers revised concessional tax slabs with an automatic ₹75,000 standard deduction for salaried individuals and full tax rebate on taxable income up to ₹7,00,000 under Section 87A. The Old Regime allows deductions for HRA, Section 80C (₹1.5L), 80D Mediclaim, and Home Loan Interest (₹2L under Section 24b).",
        "rule_box_title": "The Breakeven Deduction Rule",
        "rule_box_desc": "If your total eligible deductions under Old Regime exceed ₹3.75 Lakh to ₹4.25 Lakh (HRA + 80C + 80D + Home Loan), the Old Regime generally saves more tax. If your total deductions are below ₹3.5 Lakh, the New Regime is overwhelmingly more beneficial.",
        "personas": [
            ("₹10 Lakh Salary with No Deductions", "New Regime Tax: ₹44,200 | Old Regime Tax: ₹1,06,600. Winner: New Tax Regime saves ₹62,400."),
            ("₹15 Lakh Salary with Max Deductions (₹4.25L)", "Old Regime Tax: ₹1,56,000 | New Regime Tax: ₹1,40,400. Winner: New Regime saves ₹15,600."),
            ("₹25 Lakh Salary with Heavy Home Loan & HRA (₹6.5L Deductions)", "Old Regime Tax: ₹3,97,800 | New Regime Tax: ₹4,52,400. Winner: Old Regime saves ₹54,600.")
        ],
        "dos": [
            "Calculate your exact tax under both regimes before submitting your employer tax declaration in April.",
            "Utilize Section 80CCD(1B) for an additional ₹50,000 deduction in NPS under the Old Regime."
        ],
        "donts": [
            "Do not forget that the New Regime offers an automatic ₹75,000 standard deduction for salaried staff.",
            "Do not delay your tax planning until March — start systematic tax-saving investments in April."
        ],
        "faqs": [
            ("Can salaried employees switch regimes every year?", "Yes. Salaried employees without business income can freely choose between Old and New Regimes each financial year when filing their ITR.")
        ]
    }
]

print(f"Loaded {len(CALCULATOR_SPECS)} calculator specs.")
