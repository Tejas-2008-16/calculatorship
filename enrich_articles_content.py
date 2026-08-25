import os

def get_bespoke_deep_dive(slug, title, cat):
    # Topic-specific targeted comprehensive additions
    common_regulatory_notice = """
          <h3>Indian Regulatory Oversight &amp; Investor Grievance Architecture</h3>
          <p>Indian retail investors are protected by robust statutory frameworks administered by SEBI (Securities and Exchange Board of India), RBI (Reserve Bank of India), and IRDAI (Insurance Regulatory and Development Authority of India). If you encounter service deficiencies from mutual fund AMCs, registrars (CAMS/KFintech), or banks, file a formal complaint through the unified <strong>SEBI SCORES 2.0 portal</strong> or the <strong>RBI Banking Ombudsman</strong>. Regulators mandate resolution of retail grievances within 21 to 30 calendar days.</p>
    """

    if cat == "SIP & Mutual Funds":
        return f"""
        <section id="institutional-sip-framework">
          <h2>Institutional Asset Allocation &amp; Portfolio Construction Architecture</h2>
          <p>Long-term wealth creation in Indian equities depends fundamentally on strategic asset allocation, total cost minimization, and disciplined rebalancing routines rather than forecasting short-term market fluctuations.</p>

          <h3>Strategic Asset Allocation: Core vs Satellite Design</h3>
          <p>A resilient mutual fund portfolio balances low-cost broad market beta with high-conviction alpha generation:</p>
          <ul>
            <li><strong>Core Portfolio (60% to 70% Allocation):</strong> Broad-market Nifty 50 Index Funds, Nifty Next 50 Index Funds, or diversified Flexi Cap Direct Schemes. This provides foundational exposure across banking, technology, FMCG, and automotive blue-chips with minimal expense drag (&lt;0.25% TER).</li>
            <li><strong>Satellite Portfolio (30% to 40% Allocation):</strong> Actively managed Mid Cap, Small Cap, or Focused Direct Funds. This segment captures emerging domestic manufacturing, chemical, defense, and capital goods leaders during high-growth economic cycles.</li>
          </ul>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Portfolio Dimension</th>
                  <th>Institutional Best Practice</th>
                  <th>Costly Retail Mistake</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Expense Ratio Discipline</td>
                  <td>Direct Plans exclusively (TER 0.1% to 0.7%) saving 1% to 1.5% annually.</td>
                  <td>Investing via Regular Plans paying recurring broker trailing commissions.</td>
                </tr>
                <tr>
                  <td>Folio Concentration</td>
                  <td>Holding 3 to 4 distinct funds with complementary investment mandates.</td>
                  <td>Hoarding 10+ schemes with massive internal stock overlap.</td>
                </tr>
                <tr>
                  <td>Market Correction Behavior</td>
                  <td>Maintaining automated SIPs and adding opportunistic lumpsum tranches.</td>
                  <td>Pausing SIPs in panic during 10-15% routine market corrections.</td>
                </tr>
                <tr>
                  <td>Contribution Cadence</td>
                  <td>Enabling automated 10% annual Step-Up SIPs aligned with appraisal cycles.</td>
                  <td>Leaving monthly SIP amounts stagnant across a 10-year career.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Real-World Metro Case Study: Systematic vs Ad-Hoc Wealth Accumulation</h3>
          <p>To examine the compounding differential over time, consider two salaried IT professionals living in Bengaluru, both earning ₹1,20,000 net monthly take-home:</p>
          <ul>
            <li><strong>Professional A (Disciplined, Automated &amp; Low-Cost):</strong> Automates a ₹30,000 monthly SIP into low-cost direct index and flexi cap funds on the 3rd of every month, stepping up contributions by 10% annually. Over a 15-year career at an illustrative 12% CAGR, Professional A accumulates an extraordinary <strong>₹2.05 Crore</strong> corpus.</li>
            <li><strong>Professional B (Ad-Hoc &amp; Commission-Heavy):</strong> Invests irregular leftovers (averaging ₹10,000 inconsistently) via regular bank distributor plans charging 1.6% TER. Over 15 years, Professional B accumulates barely ₹42 Lakh &mdash; losing over ₹1.6 Crore in potential wealth due to lack of automation and commission drag.</li>
          </ul>

          <h3>Behavioral Finance: Navigating Market Volatility &amp; Drawdowns</h3>
          <p>Historical analysis of the Nifty 50 TRI over the past 25 years reveals that intra-year drawdowns of 10% to 15% occur in almost every single calendar year, yet 7-year rolling returns have never been negative in Indian index history. Successful retail investors recognize that market corrections are not structural losses, but temporary sales that enable Systematic Investment Plans to accumulate surplus units at discounted valuations.</p>

          {common_regulatory_notice}

          <h3>Five-Point Execution Checklist for Indian Mutual Fund Investors</h3>
          <ol>
            <li><strong>Audit Folio Names for 'Direct' and 'Growth':</strong> Ensure every scheme in your portfolio explicitly mentions 'Direct Plan - Growth' on your CAMS/KFintech Consolidated Account Statement.</li>
            <li><strong>Align Debit Dates with Cash Inflows:</strong> Schedule auto-debits within 48 to 72 hours of your monthly salary credit to remove discretionary spending temptation.</li>
            <li><strong>Perform Annual Category Rebalancing:</strong> Review asset allocation every April. If equity surges past your target allocation by more than 5%, rebalance systematically into debt.</li>
            <li><strong>Harvest ₹1.25 Lakh Annual LTCG Exemption:</strong> Take advantage of Section 112A's annual ₹1,25,000 tax-free long-term capital gains threshold by systematically redeeming and reinvesting matured units.</li>
            <li><strong>Protect Capital with Pure Term &amp; Health Covers:</strong> Never treat equity mutual funds as emergency reserves; maintain dedicated risk buffers outside market exposure.</li>
          </ol>
        </section>
        """
    elif cat == "Tax & Financial Planning":
        return f"""
        <section id="tax-optimization-framework">
          <h2>Strategic Tax Optimization Architecture for Indian Taxpayers</h2>
          <p>Navigating the Indian tax code requires integrating income slab analysis, capital gains timing, and statutory exemptions to maximize post-tax take-home pay and net investment returns.</p>

          <h3>Regime Selection &amp; Deduction Threshold Strategy</h3>
          <p>Under FY 2026-27 rules, the default New Tax Regime provides lower tax slabs and zero tax liability up to ₹12.75 Lakh gross salary for individuals via the Section 87A rebate and ₹75,000 Standard Deduction. For higher earners, choosing between regimes requires analyzing your aggregate eligible deductions:</p>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Gross Salary Tier</th>
                  <th>New Regime Baseline (Std Ded ₹75k)</th>
                  <th>Old Regime Break-Even Deduction Required</th>
                  <th>Optimal Filing Strategy</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Up to ₹12.75 Lakh</td>
                  <td><strong>₹0 (Zero Net Tax via 87A Rebate)</strong></td>
                  <td>N/A (New Regime is 100% Tax-Free)</td>
                  <td><strong>New Tax Regime</strong></td>
                </tr>
                <tr>
                  <td>₹15.00 Lakh</td>
                  <td>₹83,200 (Inclusive of Cess)</td>
                  <td>₹3,75,000 in Deductions (80C + 80D + HRA/24b)</td>
                  <td>New Regime unless deductions exceed ₹3.8L</td>
                </tr>
                <tr>
                  <td>₹20.00 Lakh</td>
                  <td>₹1,87,200</td>
                  <td>₹4,50,000 in Deductions</td>
                  <td>New Regime unless large home loan + HRA</td>
                </tr>
                <tr>
                  <td>₹30.00 Lakh</td>
                  <td>₹4,57,600</td>
                  <td>₹5,20,000 in Deductions</td>
                  <td>New Regime saves money for 90%+ taxpayers</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Real-World Salaried Case Study: ₹18 Lakh CTC Analysis</h3>
          <p>Consider a mid-level manager earning ₹18,00,000 gross salary in Pune with ₹1.5L EPF/80C, ₹35,000 health insurance (80D), and ₹1.80L annual HRA:</p>
          <ul>
            <li><strong>Under Old Tax Regime:</strong> Gross Income ₹18.0L &minus; ₹50k Std Ded &minus; ₹1.5L (80C) &minus; ₹35k (80D) &minus; ₹1.8L (HRA) = Net Taxable Income ₹13,85,000. Total Tax = ₹2,28,000 + 4% Cess = <strong>₹2,37,120</strong>.</li>
            <li><strong>Under New Tax Regime:</strong> Gross Income ₹18.0L &minus; ₹75k Std Ded = Net Taxable Income ₹17,25,000. Applying FY 2026-27 slabs (0-4L nil, 4-8L 20k, 8-12L 40k, 12-16L 60k, 16-17.25L 25k) = Base Tax ₹1,45,000 + 4% Cess = <strong>₹1,50,800</strong>.</li>
            <li><strong>Net Annual Tax Saved by Choosing New Regime: ₹86,320 in pure cash savings!</strong></li>
          </ul>

          <h3>Compliance, Documentation &amp; ITR Filing Protocols</h3>
          <p>Salaried taxpayers with capital gains from mutual funds or stocks must file <strong>ITR-2</strong> rather than the simplified ITR-1 (Sahaj). Maintaining accurate digital statements from CAMS, KFintech, and stock brokerages ensures seamless reporting in Schedule CG. Remember that non-reporting of capital gains can attract scrutiny notices under Section 148A of the Income Tax Act.</p>

          {common_regulatory_notice}

          <h3>Capital Gains Harvesting &amp; Set-Off Best Practices</h3>
          <ol>
            <li><strong>Utilize Section 112A Annual Threshold:</strong> Realize up to ₹1,25,000 in long-term equity capital gains each financial year tax-free.</li>
            <li><strong>Harvest Short-Term Losses (Tax-Loss Harvesting):</strong> Offset short-term capital losses against profitable gains before March 31st to minimize net taxable capital gains.</li>
            <li><strong>Track Debt Fund Purchases Post-April 2023:</strong> Ensure debt fund units acquired after April 1, 2023, are accounted for under slab rates without expecting indexation benefits.</li>
            <li><strong>File ITR on Time to Carry Forward Losses:</strong> File ITR-2 before the Section 139(1) deadline to preserve the right to carry forward unadjusted capital losses for up to 8 years.</li>
          </ol>
        </section>
        """
    elif cat == "Personal Finance & Budgeting":
        return f"""
        <section id="cash-flow-framework">
          <h2>Cash Flow Engineering &amp; Financial Firewall Architecture</h2>
          <p>Transforming monthly income into multi-generational wealth requires a structured system that separates essential fixed overheads, lifestyle spending, and wealth accumulation into dedicated accounts.</p>

          <h3>The 3-Account Banking Structure for Salaried Professionals</h3>
          <p>Eliminate manual budgeting friction by configuring automated bank account boundaries:</p>
          <ul>
            <li><strong>Account 1: The Salary &amp; Operations Hub:</strong> Receives monthly salary. Automatically debits rent, utilities, insurance premiums, and SIP mandates within 48 hours of credit.</li>
            <li><strong>Account 2: Discretionary Spending &amp; UPI Account:</strong> Receives a strictly capped monthly lifestyle allowance (e.g., 20-30% of salary) for dining, entertainment, shopping, and fuel. All UPI apps (Google Pay, PhonePe, Paytm) are linked exclusively to this account.</li>
            <li><strong>Account 3: Emergency Reserve &amp; Sinking Fund:</strong> High-yield savings or sweep-in account holding 6 months of mandatory living costs and dedicated sinking funds for annual insurance, travel, and festival expenses.</li>
          </ul>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Financial Pillar</th>
                  <th>Target Allocation</th>
                  <th>Key Implementation Mechanism</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Non-Negotiable Needs</td>
                  <td>50% Max (Rent, Groceries, EMIs)</td>
                  <td>Automated NACH mandates from Primary Account</td>
                </tr>
                <tr>
                  <td>Discretionary Lifestyle</td>
                  <td>20% &ndash; 30% Max (Dining, Leisure)</td>
                  <td>Capped UPI sub-account; zero credit card balance rollover</td>
                </tr>
                <tr>
                  <td>Wealth Accumulation</td>
                  <td>20% &ndash; 30% Min (Equity SIPs, PPF)</td>
                  <td>Automated SIP debits on 3rd of every month</td>
                </tr>
                <tr>
                  <td>Annual Sinking Reserves</td>
                  <td>Divided by 12 monthly</td>
                  <td>High-yield recurring deposits / liquid funds</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Worked Metro Budgeting Case Study: ₹1 Lakh Take-Home Salary</h3>
          <p>A structured implementation for a young couple living in Hyderabad earning ₹1,00,000 net monthly salary:</p>
          <ul>
            <li><strong>Essential Needs (50% = ₹50,000):</strong> 2BHK Rent + Maintenance (₹24,000), Groceries &amp; Cook (₹14,000), Electricity/WiFi/Gas (₹4,500), Term &amp; Health Insurance (₹3,500), Commute/Fuel (₹4,000).</li>
            <li><strong>Discretionary Wants (25% = ₹25,000):</strong> Weekend Dining (₹8,000), Shopping &amp; Leisure (₹7,000), Annual Vacation Sinking Fund (₹7,000), Subscriptions &amp; Hobbies (₹3,000).</li>
            <li><strong>Wealth &amp; Emergency Investments (25% = ₹25,000):</strong> Direct Nifty 50 Index Fund SIP (₹10,000), Flexi Cap Fund SIP (₹10,000), PPF / Emergency Sinking Fund (₹5,000).</li>
          </ul>

          <h3>Eliminating Lifestyle Creep Across Career Milestones</h3>
          <p>Lifestyle inflation is the single greatest threat to wealth accumulation for mid-career professionals in India. As annual appraisals, bonuses, and promotions elevate take-home pay, the human tendency is to expand housing, vehicles, and luxury spending to absorb 100% of the increment. By strictly establishing the '50% Rule' &mdash; routing at least half of every post-tax raise directly into automated investment SIPs &mdash; your wealth compounding accelerates exponentially while lifestyle comfort steadily improves.</p>

          {common_regulatory_notice}

          <h3>Actionable Financial Firewall Rules</h3>
          <ol>
            <li><strong>Zero Credit Card Revolving Balance:</strong> Always pay 100% of the &lsquo;Total Amount Due&rsquo; before the payment due date. Never pay just the &lsquo;Minimum Amount Due&rsquo;.</li>
            <li><strong>Maintain 6 Months Liquid Runway:</strong> Protect your career freedom with 6 months of household fixed expenses in liquid instruments before committing to long-term illiquid assets.</li>
            <li><strong>Automate Investment Escalations:</strong> Increase monthly SIPs by at least 50% of every salary increment before expanding discretionary living standards.</li>
          </ol>
        </section>
        """
    elif cat == "Fixed Income & FDs":
        return f"""
        <section id="fixed-income-architecture">
          <h2>Fixed Income Portfolio Architecture &amp; Sovereign Safety</h2>
          <p>Fixed income assets provide capital preservation, predictable liquidity, and portfolio stability during equity market downturns. Structuring debt investments across sovereign-backed and bank-guaranteed instruments optimizes post-tax returns.</p>

          <h3>Sovereign &amp; Institutional Fixed Income Hierarchy</h3>
          <p>Indian fixed income instruments offer varying trade-offs between sovereign backing, liquidity, and tax treatment:</p>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Fixed Income Instrument</th>
                  <th>Sovereign Guarantee Level</th>
                  <th>Current Return (FY 2026-27)</th>
                  <th>Tax Status on Interest</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Public Provident Fund (PPF)</td>
                  <td>100% Sovereign (Govt of India)</td>
                  <td>7.10% p.a.</td>
                  <td><strong>100% Tax-Free (EEE Status)</strong></td>
                </tr>
                <tr>
                  <td>Senior Citizen Savings Scheme (SCSS)</td>
                  <td>100% Sovereign (Govt of India)</td>
                  <td>8.20% p.a.</td>
                  <td>Taxable at Slab Rate (80TTB applies for seniors)</td>
                </tr>
                <tr>
                  <td>Scheduled Commercial Bank FDs</td>
                  <td>DICGC Insured up to ₹5 Lakh/bank</td>
                  <td>7.00% &ndash; 7.60% p.a.</td>
                  <td>Taxable annually at slab rate (TDS applies)</td>
                </tr>
                <tr>
                  <td>Gilt Mutual Funds / Liquid Funds</td>
                  <td>Sovereign GOI Securities / T-Bills</td>
                  <td>6.50% &ndash; 7.20% YTM</td>
                  <td>Taxable upon redemption at slab rate (Zero TDS)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Worked Case Study: Structuring a ₹25 Lakh Fixed Income Corpus</h3>
          <p>For a conservative investor allocating ₹25,00,000 across fixed income assets for stability and liquidity:</p>
          <ul>
            <li><strong>Sovereign Tax-Free Anchor (₹7.5 Lakh in PPF):</strong> Compounding at 7.10% tax-free interest, providing absolute capital protection.</li>
            <li><strong>DICGC Insured Bank FD Ladder (₹12.5 Lakh across 3 Scheduled Banks):</strong> Split into 5 tranches (1 to 5 years) earning 7.4% average interest, with ₹2.5L maturing annually.</li>
            <li><strong>Liquid Mutual Fund Buffer (₹5.0 Lakh):</strong> Earning 6.75% annualized yield with T+1 redemption access and ₹50,000 instant 30-minute withdrawal capability for emergencies.</li>
          </ul>

          <h3>Understanding Interest Rate Risk in Debt Instruments</h3>
          <p>Fixed income yields fluctuate with the Reserve Bank of India's monetary policy rate cycles. When RBI repo rates rise, bond prices fall, impacting longer-duration debt mutual funds (such as 10-year Gilt funds). Conversely, when rate cuts occur, long-duration gilt funds experience capital gains. Fixed Deposits eliminate this mark-to-market volatility by locking in a contractual interest rate for the entire tenure, provided deposits remain within the ₹5 Lakh DICGC insurance limit.</p>

          {common_regulatory_notice}

          <h3>Optimization Rules for Indian Fixed Income Investors</h3>
          <ol>
            <li><strong>Diversify Across Scheduled Banks:</strong> Never hold more than ₹5,00,000 in principal plus interest in a single bank to ensure 100% DICGC coverage.</li>
            <li><strong>Leverage PPF Before April 5th:</strong> Deposit annual PPF funds between April 1st and April 5th to capture the maximum 12 months of compounding interest.</li>
            <li><strong>Submit Form 15G / 15H Annually:</strong> Eligible individuals with zero taxable income should submit declaration forms in April to prevent unnecessary TDS deductions.</li>
            <li><strong>Use FD Laddering for Multi-Year Portfolios:</strong> Stagger term deposit maturities across 1, 2, 3, 4, and 5-year tenures to capture peak interest rates and maintain annual liquidity.</li>
          </ol>
        </section>
        """
    elif cat == "Retirement & Pension":
        return f"""
        <section id="retirement-execution-framework">
          <h2>Retirement Corpus Engineering &amp; Post-Retirement Cash Flow</h2>
          <p>Achieving a financially secure 30-year retirement in India requires combining aggressive pre-retirement accumulation with structured post-retirement drawdown engineering to outpace medical and lifestyle inflation.</p>

          <h3>The 3-Bucket Post-Retirement Distribution Model</h3>
          <p>Upon retirement, segment your accumulated wealth across 3 strategic liquidity buckets to protect against sequence-of-returns risk:</p>
          <ul>
            <li><strong>Bucket 1: Immediate Cash &amp; Liquidity (Years 1 to 3):</strong> 3 years of living expenses in Bank FDs, Senior Citizen Savings Schemes, and Liquid Mutual Funds. Ensures monthly pension security regardless of stock market fluctuations.</li>
            <li><strong>Bucket 2: Income &amp; Defensive Growth (Years 4 to 8):</strong> 5 years of expenses in Balanced Advantage Funds, Equity Savings Funds, and High-Grade Corporate Bond Funds yielding stable post-tax cash flows.</li>
            <li><strong>Bucket 3: Long-Term Inflation Beater (Years 9 to 30):</strong> Remaining corpus (40% to 50%) invested in broad-market Nifty 50 Index Funds and Flexi Cap Schemes compounding for future decades.</li>
          </ul>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Retirement Dimension</th>
                  <th>Recommended Institutional Strategy</th>
                  <th>Dangerous Retirement Mistake</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Withdrawal Strategy</td>
                  <td>Systematic Withdrawal Plan (SWP) from Equity Hybrid funds (5-6% initial rate).</td>
                  <td>100% Annuity purchase yielding low taxable fixed returns.</td>
                </tr>
                <tr>
                  <td>Healthcare Protection</td>
                  <td>Base Health Insurance + ₹25L to ₹50L Super Top-Up + dedicated emergency reserve.</td>
                  <td>Relying solely on corporate group health cover post-retirement.</td>
                </tr>
                <tr>
                  <td>Inflation Assumption</td>
                  <td>Modeling 6% general inflation + 10-12% healthcare cost inflation.</td>
                  <td>Assuming static living expenses throughout 30 years of retirement.</td>
                </tr>
                <tr>
                  <td>Corpus Multiplier Target</td>
                  <td>30x to 35x annual living expenses at retirement date.</td>
                  <td>Under-saving based on current rather than future inflation-adjusted costs.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Worked Case Study: Managing a ₹3.5 Crore Retirement Corpus</h3>
          <p>A real-world distribution for a 60-year-old retired couple in Chennai with ₹75,000/month living expenses:</p>
          <ul>
            <li><strong>Bucket 1 (₹30 Lakh in SCSS &amp; Sweep FDs):</strong> Generates guaranteed monthly interest covering essential utilities and food.</li>
            <li><strong>Bucket 2 (₹1.20 Crore in Balanced Advantage &amp; Equity Savings SWP):</strong> Generates ₹50,000/month tax-efficient cash flow with low capital volatility.</li>
            <li><strong>Bucket 3 (₹2.00 Crore in Direct Nifty 50 Index &amp; Flexi Cap Funds):</strong> Compounds at 11-12% CAGR, growing to over ₹5.5 Crore by age 75 to fund late-life healthcare and estate inheritance.</li>
          </ul>

          <h3>Healthcare Cost Containment &amp; Longevity Insurance</h3>
          <p>Hospitalization and critical illness treatments represent the largest unbudgeted drain on Indian retirement corpuses. Private hospital room rents, specialized surgical procedures, and post-operative home nursing inflate at 10% to 14% annually in major metros. Securing an individual comprehensive health policy with a high-sum-insured Super Top-Up policy before age 55 ensures that late-life medical emergencies do not force distress liquidations of income-generating mutual fund units.</p>

          {common_regulatory_notice}

          <h3>Essential Pre-Retirement Milestones</h3>
          <ol>
            <li><strong>Clear All Unsecured Liabilities:</strong> Enter retirement with zero high-interest debt, credit card balances, or personal loans.</li>
            <li><strong>Secure Independent Health Insurance Before Age 55:</strong> Purchase comprehensive personal health insurance while in good health to avoid pre-existing disease exclusions.</li>
            <li><strong>Optimize NPS 60:40 Withdrawal:</strong> Withdraw 60% tax-free lump sum at age 60 and allocate the remaining 40% into the highest-yielding annuity provider.</li>
          </ol>
        </section>
        """
    elif cat == "Loans & Real Estate":
        return f"""
        <section id="mortgage-optimization-framework">
          <h2>Mortgage Reduction Engineering &amp; Net Worth Optimization</h2>
          <p>A home loan is typically the largest debt obligation undertaken by an Indian family. Reducing interest drag through disciplined principal prepayment while maintaining parallel equity investments creates significant long-term net worth advantages.</p>

          <h3>The Mathematics of Principal Prepayment</h3>
          <p>Because Indian home loans are structured on an amortization schedule where interest dominates early payments, principal reduction in the first 5 to 7 years produces exponential interest savings:</p>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Prepayment Strategy</th>
                  <th>Implementation Method</th>
                  <th>Impact on a 20-Year ₹50 Lakh Loan @ 9%</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1-Extra-EMI per Year</strong></td>
                  <td>Pay 1 extra monthly installment annually from bonus</td>
                  <td>Saves ~₹16.7 Lakh interest; reduces tenure by ~4.5 years</td>
                </tr>
                <tr>
                  <td><strong>5% Annual EMI Step-Up</strong></td>
                  <td>Increase monthly EMI by 5% with salary increments</td>
                  <td>Saves ~₹24.5 Lakh interest; reduces tenure to under 12 years</td>
                </tr>
                <tr>
                  <td><strong>Hybrid Prepay + SIP</strong></td>
                  <td>Prepay 1 extra EMI + run parallel 20% equity SIP</td>
                  <td>Clears debt 5 years early AND builds ₹80L+ equity corpus</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Worked Case Study: The ₹60 Lakh Home Loan Acceleration</h3>
          <p>Consider a borrower in Noida with a ₹60,00,000 loan at 8.75% interest for 20 years (Monthly EMI: ₹53,030):</p>
          <ul>
            <li><strong>Baseline Scenario (Standard 20-Year Repayment):</strong> Total interest paid across 240 months equals <strong>₹67,27,000 (More than original principal!)</strong>.</li>
            <li><strong>Accelerated Hybrid Strategy:</strong> Borrower prepays ₹53,030 once every year and starts a ₹10,000 monthly Flexi Cap SIP. The loan closes in <strong>15.1 years saving ₹20.5 Lakh in interest</strong>, while the parallel SIP expands to <strong>₹52.8 Lakh</strong>, boosting total household net worth by over ₹73 Lakh!</li>
          </ul>

          <h3>Refinancing, Balance Transfers &amp; Benchmark Spreads</h3>
          <p>Following RBI guidelines on External Benchmark Lending Rates (EBLR), home loans are pegged directly to the RBI Repo Rate. If your existing lender charges a lending spread higher than prevailing market rates for high-CIBIL borrowers, negotiate a spread reduction (paying a nominal internal switching fee of ₹1,000 to ₹5,000) or execute an external balance transfer to save tens of thousands in annual interest.</p>

          <h3>Understanding the True Cost of Long Tenures (30-Year Traps)</h3>
          <p>Opting for a 30-year loan tenure instead of a 20-year tenure reduces the monthly EMI by only 10-12%, but causes the total interest paid to skyrocket by over 60%. Always target a maximum initial tenure of 20 years and utilize annual prepayments to bring effective loan payoff duration under 12 to 14 years.</p>

          {common_regulatory_notice}

          <h3>Key Execution Rules for Indian Borrowers</h3>
          <ol>
            <li><strong>Always Instruct the Bank to 'Reduce Tenure':</strong> When making partial prepayments, ensure the bank adjusts the loan tenure rather than reducing the monthly EMI amount.</li>
            <li><strong>Zero Prepayment Penalty Rights:</strong> Under RBI regulations, banks and NBFCs cannot charge prepayment fees on floating-rate home loans for individual borrowers.</li>
            <li><strong>Balance Debt Payoff with Equity Investing:</strong> Never deplete 100% of your liquidity to prepay a 9% home loan while neglecting 12-14% compounding equity investments.</li>
          </ol>
        </section>
        """
    else: # Goal Planning & Wealth
        return f"""
        <section id="goal-planning-framework">
          <h2>Goal-Linked Wealth Engineering Architecture</h2>
          <p>Disciplined wealth creation requires mapping distinct financial goals &mdash; children's higher education, wedding planning, house down payments, and wealth accumulation &mdash; to specific asset allocation matrices and time horizons.</p>

          <h3>Time Horizon &amp; Asset Allocation Matching Framework</h3>
          <p>Match your financial goals to appropriate investment vehicles based on time to target:</p>

          <div class="table-wrapper">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Goal Horizon</th>
                  <th>Primary Asset Class</th>
                  <th>Recommended Investment Vehicles</th>
                  <th>Target Return (CAGR)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Short-Term (0 to 3 Years)</td>
                  <td>High-Safety Debt / Fixed Income</td>
                  <td>Liquid Funds, Ultra-Short Debt, Auto Sweep FDs</td>
                  <td>6.5% &ndash; 7.2%</td>
                </tr>
                <tr>
                  <td>Medium-Term (4 to 7 Years)</td>
                  <td>Hybrid / Dynamic Allocation</td>
                  <td>Balanced Advantage Funds, Equity Savings, Arbitrage</td>
                  <td>8.5% &ndash; 10.5%</td>
                </tr>
                <tr class="highlight-row">
                  <td>Long-Term (8+ Years)</td>
                  <td>Pure Growth Equities + Sovereign Debt</td>
                  <td>Flexi Cap Funds, Nifty 50 Index, PPF / SSY</td>
                  <td>11.0% &ndash; 14.0%</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>Worked Metro Case Study: Funding a 15-Year Higher Education Goal</h3>
          <p>Planning for a child's overseas master's degree estimated at ₹65 Lakh today, inflating at 10% annual educational inflation:</p>
          <ul>
            <li><strong>Target Future Corpus Needed in 15 Years:</strong> ₹65 Lakh &times; (1.10)^15 = <strong>₹2.71 Crore</strong>.</li>
            <li><strong>Accumulation Strategy:</strong> Allocate ₹25,000/month in Direct Flexi Cap &amp; Mid Cap mutual fund SIPs with an annual 10% step-up. The portfolio reaches ₹2.85 Crore by Year 15.</li>
            <li><strong>Glide Path Protocol:</strong> In Years 13 to 15, systematically transfer ₹8 Lakh per quarter via STP into ultra-short debt funds to immunize the education fund against stock market downturns.</li>
          </ul>

          <h3>Risk Profiling &amp; Dynamic Capacity Across Life Stages</h3>
          <p>An investor's risk tolerance is determined by two separate variables: emotional willingness to take risk and financial capacity to absorb drawdowns. While a 28-year-old single earner has a 30-year runway to recover from market corrections, a 55-year-old within 5 years of retirement cannot afford a 30% unhedged equity loss. Tailoring asset allocation to your changing life stages guarantees financial resilience through all economic seasons.</p>

          <h3>Hedging Against Macro Currency Depreciation</h3>
          <p>For long-term goals involving overseas higher education or foreign travel, factoring in Indian Rupee (INR) depreciation against the US Dollar (historically 3% to 4% annualized) is essential. Allocating 10% to 15% of foreign-bound savings into International Feeder Funds or US Total Stock Market ETFs creates a natural currency hedge that preserves dollar-denominated purchasing power.</p>

          {common_regulatory_notice}

          <h3>Systematic Glide Path &amp; De-Risking Protocol</h3>
          <ol>
            <li><strong>De-Risk 2-3 Years Before Goal Deadline:</strong> Transfer accumulated equity units into liquid funds as goal maturity approaches to protect capital against sudden stock market corrections.</li>
            <li><strong>Incorporate Realistic Education Inflation (10-12%):</strong> Always model higher education and medical goals at double the standard consumer price inflation rate.</li>
            <li><strong>Avoid Low-Yielding Traditional Endowment Plans:</strong> Protect life with pure term insurance and invest differences in transparent, liquid direct mutual funds.</li>
          </ol>
        </section>
        """

print("Updated enrichment module ready with comprehensive depth.")
