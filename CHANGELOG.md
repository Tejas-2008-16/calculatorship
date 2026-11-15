# Compliance Changelog & Editorial Log

This file tracks per-file compliance edits, rationale, and specific items requiring ongoing verification against official statutory sources (SEBI, RBI, Income Tax Dept, AMFI, EPFO, PFRDA).

---

## Batch 1 (Articles 1–10 + Homepage)

### 1. `best-sip-amount-calculator-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Replaced multiple scattered disclaimers with the unified single statutory disclaimer directly under H1.
  - Aligned Title, H1, Meta Description, and OpenGraph tags to eliminate "how much you should invest" and "best SIP".
  - Reframed salary split table from directive advice into a neutral illustrative mathematical walk-through.
  - Replaced "Recommended Fund Type" table column with "Categorization Example Under SEBI Guidelines".
  - Replaced named broker/app calls with neutral institutional wording ("official AMC portals, registrar platforms like MFCentral/CAMS/KFintech, or SEBI-registered intermediaries").
  - Added standard closing boxes: *"How to think about this yourself"* and *"Where to get personalised help"*.
  - Cleaned FAQ Schema and visible FAQ text.
- **[VERIFY: ...] Items:**
  - Verify official reverse SIP mathematical formulas against AMFI investor education documentation.

### 2. `index.html`
- **Rationale & Changes:**
  - Added prominent student voice disclaimer in the hero section: *"I'm Tejas, a student building financial calculators. This platform is purely educational..."*
  - Neutralized comparison/verdict language in FAQ section and removed prescriptive investment allocation advice.
  - Removed named case studies and replaced prescriptive return promises (12-14%) with illustrative multi-rate disclosures.
  - Added "How to think about this yourself" and "Where to get personalised help" institutional guidance.
- **[VERIFY: ...] Items:**
  - Periodic review of linked calculator outputs to ensure mathematical parity with compound interest formulas.

### 3. `salary-hike-investment-strategy-india.html`
- **Rationale & Changes:**
  - Neutralized title, meta description, and schema: converted prescriptive "strategy" language into mathematical analysis of step-up SIPs and Section 80CCD(2) employer NPS rules.
  - Replaced directive financial allocations with hypothetical arithmetic illustrations.
  - Replaced broker mentions with generic institutional platforms (e.g., eNPS CRA portals).
  - Added student voice disclaimer under H1 and thinking/help boxes.
- **[VERIFY: ...] Items:**
  - Section 80CCD(2) employer contribution limits under the new tax regime (capped at 14% of Basic for central/state govt, 10% for private sector, subject to ₹7.5 Lakh aggregate cap under Sec 17(2)(vii)).

### 4. `nifty-50-index-fund-guide-india.html`
- **Rationale & Changes:**
  - Neutralized headline and schema from "which fund to pick" to educational explanation of passive market replication, Tracking Error, and Total Expense Ratio (TER).
  - Replaced specific fund scheme endorsements with generic SEBI categorization criteria.
  - Formatted compound interest projections into multi-rate mathematical table (6%, 8%, 10%, 12%), removing labels like "realistic".
  - Replaced commercial investment apps with institutional channels (AMC portals, MFCentral, CAMS/KFintech).
  - Added student persona note under H1 and thinking/help boxes.
- **[VERIFY: ...] Items:**
  - Maximum regulatory TER caps for index funds under SEBI Mutual Funds Regulations (currently 1.00%).

### 5. `mutual-fund-exit-strategy-india.html`
- **Rationale & Changes:**
  - Shifted focus from advisory market-timing advice to statutory redemption rules, cut-off timings (SEBI circulars), exit load schedules, and Systematic Withdrawal Plans (SWP).
  - Updated capital gains taxation mechanics post-Finance Act (No. 2) 2024 (LTCG at 12.5% above ₹1.25 Lakh exemption, STCG at 20% for equity-oriented funds).
  - Added student voice disclaimer under H1 and thinking/help framework.
- **[VERIFY: ...] Items:**
  - Verification of cut-off timing for equity funds (15:00 IST for realization of funds rule under SEBI circular).

### 6. `sip-pause-vs-stop-vs-continue.html`
- **Rationale & Changes:**
  - Transformed guide into an operational explanation of NACH/e-mandate cancellation, bank ECS bounce charges, AMC pause facilities, and folio status.
  - Removed advisory directives urging users to "never stop" into neutral financial trade-off analysis.
  - Replaced named broker apps with generic SEBI-registered intermediaries and banking channels.
  - Added student voice and standard thinking/help boxes.
- **[VERIFY: ...] Items:**
  - Bank NACH mandate cancellation timelines (NPCI guidelines require up to 15-30 days advance notice depending on the bank).

### 7. `sip-during-market-crash.html`
- **Rationale & Changes:**
  - Replaced emotional advice ("do not panic", "buy the dip") with mathematical explanations of rupee cost averaging, unit accumulation arithmetic, and historical Nifty 50 drawdown/recovery distributions.
  - Clarified that equity investments carry capital risk and drawdowns can be prolonged.
  - Added multi-rate mathematical compounding table and student voice opening.
- **[VERIFY: ...] Items:**
  - Historical Nifty 50 drawdown recovery durations (2000, 2008, 2020) cross-referenced against NSE historical indices.

### 8. `best-sip-date-mutual-fund-india.html`
- **Rationale & Changes:**
  - Debunked date-selection myths using empirical rolling return data across 1st, 5th, 10th, 15th, and 28th of the month.
  - Explained operational aspects: bank clearing cycles, non-business day NAV allocation rules (SEBI cut-off guidelines).
  - Added multi-rate compounding table (6%, 8%, 10%, 12%) and neutralized prescriptive date recommendations.
- **[VERIFY: ...] Items:**
  - SEBI NAV applicability rules for non-business days and holidays.

### 9. `portfolio-rebalancing-guide-india.html`
- **Rationale & Changes:**
  - Replaced prescriptive asset allocation models (e.g., "keep 70% in equity, 30% in debt") with neutral descriptions of rebalancing mechanisms: calendar-based vs threshold-based (5/25 rule).
  - Clarified tax frictions (STCG/LTCG on equity and slab rate on specified debt funds post-April 2023) and cash-flow redirection as an alternative to asset sales.
  - Added student voice note and thinking/help boxes.
- **[VERIFY: ...] Items:**
  - Debt mutual fund taxation post-Finance Act 2023 (Section 50AA: non-equity oriented mutual funds taxed at slab rate without indexation).

### 10. `how-to-pick-your-first-mutual-fund-india.html`
- **Rationale & Changes:**
  - Renamed from prescriptive "How to Pick Your First Mutual Fund" to educational "How Mutual Fund Categories and Metrics Work in India".
  - Replaced specific fund recommendations (e.g., UTI Nifty 50 Index Fund, Parag Parikh Flexi Cap) with SEBI 2017 categorisation definitions.
  - Replaced broker platforms (Zerodha Coin, Groww, Kuvera, Paytm Money) with institutional infrastructure (AMC websites, MFCentral, RTAs).
  - Detailed the mathematics of Direct vs Regular TER differences over 20 years.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%), student voice disclaimer under H1, and standard thinking/help boxes.
- **[VERIFY: ...] Items:**
  - Categorisation mandates under SEBI Circular SEBI/HO/IMD/DF3/CIR/P/2017/114.

---

## Batch 2: Articles 11 through 20 (Completed 2026-10-26)

### 11. `5-common-sip-mistakes-to-avoid.html`
- **Rationale & Changes:**
  - Added student voice note directly under H1.
  - Replaced prescriptive rules ("Do this", "Stop doing that") with analytical explanations of operational concepts: NAV timing, rupee-cost averaging, pause vs stop options, step-up mechanics.
  - Added multi-rate compounding illustration (6%, 8%, 10%, 12%).
  - Added "How to think about this yourself" and "Where to get personalised help" sections.
  - Updated author bio card to student persona; removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - AMFI operational guidelines on SIP pause tenures and minimum notice periods.

### 12. `50000-salary-how-much-save-invest-spend.html`
- **Rationale & Changes:**
  - Neutralized prescriptive budget allocation rules (e.g. rigid 50/30/20 mandates).
  - Framed budget frameworks as mathematical models rather than universal rules.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%) illustrating various potential savings rates.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Statutory deductions (EPF employee contribution rate 12% under EPFO rules).

### 13. `80c-deductions-guide.html`
- **Rationale & Changes:**
  - Neutralized tax-product recommendations; structured as an educational breakdown of Section 80C instruments (PPF, EPF, ELSS, NPS tier 1 80CCD(1B), Sukanya Samriddhi).
  - Clarified differences between Old Tax Regime and New Tax Regime (Section 115BAC default status).
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Budget / Finance Act 2023 & 2024 revisions to Section 115BAC (standard deduction ₹75,000 in FY 2024-25, default regime status).

### 14. `arbitrage-funds-india-complete-guide.html`
- **Rationale & Changes:**
  - Explained arbitrage fund mechanics: simultaneous buying in cash market and selling in futures market, roll-over risk, interest rate parity.
  - Clarified tax treatment as equity-oriented funds under Section 112A / 111A.
  - Replaced fund selection directives with SEBI risk-o-meter and mandate metrics.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI categorisation rules requiring minimum 65% in equity and equity-related instruments to qualify for equity tax status.

### 15. `capital-gains-tax-india.html`
- **Rationale & Changes:**
  - Updated statutory tax rate explanations post-Budget (July 2024): STCG 20%, LTCG 12.5% with ₹1.25 lakh exemption for listed equity.
  - Replaced commercial app names (Groww, Zerodha) with generic institutional clearing/broker terminology.
  - Neutralized actionable tax-loss harvesting guides into theoretical accounting mechanisms.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Finance (No. 2) Act 2024 effective date (23 July 2024) for revised STCG and LTCG rates under Section 111A and Section 112A.

### 16. `debt-free-strategy-india.html`
- **Rationale & Changes:**
  - Neutralized sensational claims ("36% risk-free return") with mathematical trade-off explanations (cost of debt vs expected return on capital).
  - Compared Avalanche vs Snowball debt repayment methods objectively without prescribing one.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%) for comparison.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - RBI fair practices code for interest rate computation and foreclosure charges on floating-rate loans.

### 17. `direct-vs-regular-mutual-funds.html`
- **Rationale & Changes:**
  - Replaced mentions of commercial discount brokers with institutional options (AMC direct portals, MFCentral, RTAs).
  - Explained the operational role of distributors under AMFI / SEBI regulations and how TER differences compound mathematically.
  - Added multi-rate table (6%, 8%, 10%, 12%) across Direct vs Regular TER spreads.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI circular SEBI/IMD/CIR No. 4/168230/09 (banning entry loads and creating direct plans in Jan 2013).

### 18. `elss-tax-saving.html`
- **Rationale & Changes:**
  - Neutralized schema FAQ questions and answers that gave prescriptive tax advice.
  - Clarified 3-year lock-in statutory mechanics under Equity Linked Savings Scheme Guidelines, 2005.
  - Clarified tax implications under New vs Old tax regimes.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Central Government ELSS Notification 2005 lock-in and redemption norms.

### 19. `emi-vs-sip-extra-money-india.html`
- **Rationale & Changes:**
  - Neutralized "guaranteed return" claims on prepayment and single 12% equity return assumptions.
  - Presented the dual-choice problem purely as a financial mathematics trade-off between guaranteed loan cost reduction and uncertain market returns.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%).
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - RBI master directions on home loan prepayments and penalty waivers for individual floating rate borrowers.

### 20. `fd-vs-mutual-funds-india.html`
- **Rationale & Changes:**
  - Replaced prescriptive "mutual funds consistently outperform FDs" assertion in text and FAQ schema with factual risk/return and liquidity differences.
  - Explained DICGC deposit insurance limit (₹5 lakh per bank) and debt/equity fund market risks.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%) compared to fixed deposit interest models.
  - Added student voice under H1, thinking/help boxes, student bio, removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - DICGC insurance limits under Deposit Insurance and Credit Guarantee Corporation Act.

---

## Batch 3 (Articles 21 to 30) — HIGH Risk Overhaul

### 21. `fd-vs-debt-mutual-funds.html`
- **Rationale & Changes:**
  - Updated H1 from comparative bias to "Fixed Deposits vs Debt Mutual Funds in India: Understanding Tax Rules and Arithmetic Trade-offs".
  - Neutralized tax-drag claims following the Finance Act 2023 amendment to Section 50AA (specified mutual funds taxed at slab rates without indexation).
  - Added student voice disclaimer under H1, multi-rate table (6%, 7%, 8%), thinking/help boxes, student bio card, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Section 50AA of the Income Tax Act effective 1 April 2023 regarding debt funds with less than or equal to 35% equity.

### 22. `fire-movement-india.html`
- **Rationale & Changes:**
  - Updated H1 from prescriptive lifestyle advice to "The FIRE Movement in India: Examining Safe Withdrawal Rates and Retirement Maths".
  - Clarified Trinity Study safe withdrawal rate (SWR) assumptions (3% to 4%) and why Indian inflation (5–7%) creates sequence of returns risk.
  - Added multi-rate accumulation table (6%, 8%, 10%, 12%), annual expense multiplier comparisons (30x, 35x, 40x), student disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Historical Indian CPI inflation data published by RBI and Ministry of Statistics and Programme Implementation (MOSPI).

### 23. `fire-retire-at-50-sip-calculation-india.html`
- **Rationale & Changes:**
  - Neutralized prescriptive FAQ schema question recommending specific equity/debt portfolio allocations.
  - Updated H1 to "Retiring at 50 in India: Target Corpus and Monthly SIP Arithmetic".
  - Modeled monthly SIP requirements across multi-rate compounding scenarios (8%, 10%, 12%) without labeling 12% as expected or realistic.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Life expectancy tables and annuity rates published by Life Insurance Corporation of India (LIC) / IRDAI.

### 24. `gold-vs-mutual-funds.html`
- **Rationale & Changes:**
  - Neutralized FAQ schema Question 5 which advised readers on gold allocation percentages.
  - Updated H1 to "Gold vs Mutual Funds in India: Historical Returns, Risk Characteristics, and Taxation".
  - Provided comprehensive asset-class comparison table (Physical Gold, Sovereign Gold Bonds, Gold ETFs/Mutual Funds, Equity Mutual Funds).
  - Added multi-rate compounding table (6%, 8%, 10%, 12%), student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India sovereign gold bond tranche terms and capital gains tax exemption on redemption under Section 47.

### 25. `got-first-salary-investing-guide-india.html`
- **Rationale & Changes:**
  - Neutralized FAQ schema answers and removed broker app mentions (Zerodha Coin, Groww, Upstox).
  - Updated H1 to "First Salary in India: How to Budget, Build an Emergency Fund, and Understand SIPs".
  - Neutralized prescriptive directives ("Always select Direct", "build 70% savings") into educational frameworks (50/30/20 conceptual model, liquidity buffer fundamentals).
  - Added multi-rate compounding table (6%, 8%, 10%, 12%), student disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - EPFO statutory employee contribution regulations (12% of basic wage + dearness allowance).

### 26. `home-loan-balance-transfer-guide-india.html`
- **Rationale & Changes:**
  - Updated H1 from sensational phrasing ("When Switching Actually Saves Money") to "Home Loan Balance Transfer in India: Examining Break-Even Arithmetic and Switching Costs".
  - Neutralized directives ("switching sounds like a no-brainer") and detailed break-even arithmetic (accounting for processing fees + 18% GST, legal valuation, and state MODT stamp duty).
  - Explained internal spread reset mechanisms with existing lenders as an alternative to external refinancing.
  - Added student disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Master Directions on foreclosure charges / pre-payment penalties on floating-rate individual loans.

### 27. `how-to-apply-ipo-india-upi-asba-guide.html`
- **Rationale & Changes:**
  - Updated H1 to "How IPO Applications Work in India via UPI: ASBA Mechanics, Allotment Math, and Capital Gains Tax".
  - Replaced commercial broker platform names with generic SEBI-registered broker terminology.
  - Detailed the operational ASBA lien mechanism, lot size formula, lottery allotment math for oversubscribed issues, and T+3 listing timelines.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI circular on T+3 listing timeline and NPCI circular on ₹5 Lakh per transaction limit for UPI ASBA applications.

### 28. `how-to-build-1-crore-corpus-30000-salary-india.html`
- **Rationale & Changes:**
  - Updated H1 to "Building a ₹1 Crore Corpus on a ₹30,000 Salary: The Compounding and Step-Up Math".
  - Neutralized directives ("Always opt", "Never stop your SIP") into mathematical models of compound interest and step-up annuities.
  - Added multi-rate compounding table (6%, 8%, 10%, 12%) illustrating 20-year accumulation across varying rate scenarios.
  - Added student disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Future value annuity formula accuracy with annual step-up percentage increments.

### 29. `how-to-read-a-mutual-fund-factsheet.html`
- **Rationale & Changes:**
  - Updated H1 to "How to Read a Mutual Fund Factsheet: Decoding AUM, Ratios, and Holdings".
  - Replaced commercial platform names (Zerodha Coin, Groww) with generic institutional sources (AMC portal, MF Central, AMFI).
  - Explained statistical risk ratios (Sharpe Ratio, Alpha, Beta, Standard Deviation) and portfolio turnover ratio neutrally without stock-picking advice.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI circular standardising mutual fund performance benchmarking against Total Return Indices (TRI).

### 30. `how-to-read-mutual-fund-factsheet.html`
- **Rationale & Changes:**
  - Neutralized FAQ schema Question 4 regarding "ideal Portfolio Turnover Ratio" into factual trade-off explanation.
  - Updated top disclaimer under H1 with humble student persona.
  - Removed duplicate middle disclaimer box and redundant footer educational disclaimers.
  - Added "How to Think About This Yourself" and "Where to Get Personalised Help" sections, and updated student bio card.
- **[VERIFY: ...] Items:**
  - SEBI risk-o-meter standardization circulars (6-level scale from Low to Very High).

---

## Batch 4 (Articles 31 to 40) — HIGH Risk Overhaul

### 31. `how-to-read-mutual-fund-statement-india.html`
- **Rationale & Changes:**
  - Neutralized prescriptive advice and cleaned up broker platform mentions.
  - Added student voice disclaimer under H1, thinking/help boxes, student researcher bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - AMFI guidelines on monthly Consolidated Account Statement (CAS) generation and CDSL/NSDL integration.

### 32. `how-to-redeem-mutual-funds-india.html`
- **Rationale & Changes:**
  - Neutralized schema FAQ questions and answers; reframed prescriptive decision criteria into objective trade-off factors.
  - Replaced commercial broker platforms (Groww, Zerodha Coin) with generic institutional channels (AMC portals, MF Central, RTAs like CAMS and KFintech).
  - Clarified SEBI cut-off rules (1:30 PM for liquid/overnight vs 3:00 PM for equity/debt) and NAV realization mechanics.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI circular on fund realization cut-off timings (SEBI/HO/IMD/DF2/CIR/P/2020/175).

### 33. `how-to-start-sip.html`
- **Rationale & Changes:**
  - Updated H1 from prescriptive promise to "How to Start a Mutual Fund SIP in India: Setup Process, Banking Mandates, and Compounding Arithmetic".
  - Neutralized prescriptive fund recommendations (Parag Parikh Flexi Cap, UTI Nifty 50) and commercial broker platforms (Groww, Zerodha Coin, Kuvera).
  - Added multi-rate compounding illustration table (6%, 8%, 10%, 12%) across 5, 10, 15, and 20 years without expectation labels.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - NPCI regulations governing e-Mandate and National Automated Clearing House (NACH) limits.

### 34. `how-to-start-your-first-sip-step-by-step.html`
- **Rationale & Changes:**
  - Neutralized FAQ schema to remove platform endorsements and fund picks.
  - Replaced commercial broker names with generic institutional terminology.
  - Neutralized prescriptive directives into structural investment processes.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI KYC master circular on In-Person Verification (IPV) and Aadhaar OTP verification bounds.

### 35. `index-funds-vs-active-funds.html`
- **Rationale & Changes:**
  - Neutralized SPIVA performance claims and prescriptive assertions.
  - Added multi-rate compounding illustration table (6%, 8%, 10%, 12%) comparing cost impacts over 10, 20, and 30 years.
  - Removed commercial broker mentions and fund endorsements.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - S&P Dow Jones SPIVA India Scorecard methodology and long-term benchmark underperformance statistics.

### 36. `index-funds-vs-nifty50-etf-india.html`
- **Rationale & Changes:**
  - Neutralized FAQ schema and H1 from prescriptive advice to "Index Funds vs Nifty 50 ETFs in India: Tracking Error, Demat Costs, and Liquidity Mechanics".
  - Replaced commercial broker references with generic market intermediary channels.
  - Reframed advice matrix into objective structural comparisons (Demat requirement, intraday pricing, tracking error vs tracking difference, brokerage/STT costs).
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI guidelines on tracking error thresholds for index funds and ETF market-maker liquidity frameworks.

### 37. `inflation-impact-on-savings-india.html`
- **Rationale & Changes:**
  - Neutralized student disclaimer under H1 and eliminated commercial broker references.
  - Added multi-rate compounding and inflation-adjusted purchasing power tables across varying inflation (4%, 6%, 7%) and nominal return scenarios.
  - Added thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - RBI inflation targeting framework under the RBI Act (4% +/- 2% CPI target band).

### 38. `itr-u-updated-return-section-139-8a-guide.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona ("Hi, I'm Tejas...").
  - Reframed all prescriptive guidance into statutory requirements of Section 139(8A) and Section 140B under the Income Tax Act, 1961.
  - Added "How to Think About This Yourself" and "Where to Get Personalised Help" pointing to ICAI Chartered Accountants.
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - CBDT notification No. 48/2022 notifying Rule 12AC and Form ITR-U schema and challan Minor Head 114.

### 39. `liquid-funds-vs-savings-account-emergency-fund.html`
- **Rationale & Changes:**
  - Updated H1 from sensational title to "How to Build an Emergency Reserve: Liquid Mutual Funds vs Bank Savings Account".
  - Replaced commercial platforms in Section 7 with generic institutional channels (AMC portals, MF Central, RTAs).
  - Clarified SEBI 91-day maturity limits, graded 7-day exit load schedule, instant redemption limits (₹50,000 / 90%), and Section 50AA slab-rate debt taxation.
  - Added student disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI circular on instant access facility for liquid mutual funds up to ₹50,000 or 90% of folio value.

### 40. `mutual-fund-categories-india.html`
- **Rationale & Changes:**
  - Neutralized prescriptive portfolio allocation advice ("A well-constructed portfolio for a 35-year-old...") into objective theoretical models.
  - Replaced platform mentions with generic mutual fund channels and neutralized FAQ schema.
  - Added student voice disclaimer under H1, thinking/help boxes, student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Master Circular on Categorization and Rationalization of Mutual Fund Schemes dated 6 October 2017.

---

## Batch 5 (Articles 41–50)

### 41. `mutual-fund-nav-explained-india.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona ("Hi, I'm Tejas...").
  - Replaced named commercial platforms (Groww, Kuvera, Zerodha) in FAQ 3 with generic institutional channels (AMC direct portals, MF Central, CAMS/KFintech RTAs).
  - Clarified SEBI Net Asset Value calculation formulas, cut-off timings (15:00 IST), and bank realization rules.
  - Added "How to think about this yourself" and "Where to get personalised help" (pointing to SEBI RIA directory).
  - Updated author bio card to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI Master Circular on NAV realization rule (SEBI/HO/IMD/DF2/CIR/P/2020/175).

### 42. `mutual-fund-nomination-guide-india.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona citing legal framework and supreme court precedent (*Sarbati Devi v. Usha Devi*).
  - Replaced Zerodha, Groww, Kuvera, etc. in Section 5 with SEBI-registered brokers, depository participants, and MF Central.
  - Clarified nominee vs legal heir statutory distinction and the 3-nominee allocation cap under SEBI guidelines.
  - Added self-reflection and professional help callout boxes.
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Supreme Court ruling in *Sarbati Devi v. Usha Devi (1984)* and SEBI circulars on mandatory mutual fund nomination / opt-out frameworks.

### 43. `mutual-fund-taxation-india-complete-guide.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona citing Sections 111A, 112A, and 50AA of the Income Tax Act.
  - Replaced commercial platforms (Groww, Zerodha Coin) with generic institutional avenues (AMC portals, MF Central, SEBI-registered intermediaries).
  - Updated equity LTCG (12.5% above ₹1.25 Lakh threshold), STCG (20%), and debt fund slab-rate taxation under Section 50AA post-Finance Act (No. 2) 2024.
  - Added "How to think about this yourself" and "Where to get personalised help" (pointing to SEBI RIAs and ICAI CAs).
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Income Tax Department provisions under Sections 112A, 111A, 50AA, and TDS rules under Section 194K on mutual fund distributions.

### 44. `nps-vatsalya-scheme-complete-guide.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona.
  - Reframed all prescriptive guidance into statutory features of the NPS Vatsalya scheme launched by PFRDA under the Union Budget 2024-25.
  - Explained seamless transition to standard Tier I PRAN at age 18, 75% equity choice caps, and partial withdrawal guidelines.
  - Added "How to think about this yourself" and "Where to get personalised help".
  - Updated author bio to student researcher and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - PFRDA operational guidelines for NPS Vatsalya scheme accounts, guardian KYC requirements, and CRA integration.

### 45. `nps-vs-mutual-funds.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("Retire Richer") to "NPS vs Mutual Funds for Retirement in India: Structural Differences, Taxation, and Annuity Rules".
  - Updated disclaimer under H1 with humble student persona.
  - Added multi-rate compounding illustration table across 6%, 8%, 10%, and 12% illustrative rates.
  - Detailed Section 80CCD(1B) ₹50,000 deduction, Section 80CCD(2) employer limits, 60% tax-free lump-sum, and 40% mandatory annuity rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - PFRDA annuity service provider (ASP) empanelment rules and Section 10(12A) lump-sum withdrawal exemption limits under the Income Tax Act.

### 46. `nri-investment-rules-india.html`
- **Rationale & Changes:**
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial broker names (Zerodha Coin, Groww, Kuvera) in Key Takeaway 3 with generic institutional platforms (AMC direct, MF Central, SEBI-registered brokers).
  - Explained statutory provisions of FEMA, RBI regulations, FATCA/CRS compliance for US/Canada NRIs, and mandatory re-designation of domestic resident accounts to NRO/NRE.
  - Added thinking/help boxes, updated author bio to student researcher, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Foreign Exchange Management (Non-debt Instruments) Rules, 2019 and RBI master directions on deposit accounts for Non-Resident Indians.

### 47. `rupee-cost-averaging.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("How Indian Investors Profit from Market Volatility") to "Rupee Cost Averaging: Mechanics, Mathematics, and Market Volatility in India".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced broker calls (Groww, Zerodha Coin, Kuvera) in Section 4 and FAQ 3 with generic execution channels (direct AMC portals, MF Central, automated UPI AutoPay / bank NACH).
  - Added "How to think about this yourself" and "Where to get personalised help".
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI investor education circulars on rupee cost averaging mechanics and mathematical harmonic mean principles.

### 48. `silver-etf-vs-gold-etf-india-tax-guide.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("Tax, Costs & How to Buy") to "Silver ETF vs Gold ETF in India: Taxation, Mechanics, and Cost Comparisons".
  - Updated disclaimer under H1 with humble student persona.
  - Reframed speculative Budget claims regarding secondary-market SGBs to prevailing statutory provisions under the Income Tax Act.
  - Replaced commercial broker references (Zerodha, Groww, AngelOne, ICICI Direct) with generic SEBI-registered stockbrokers and institutional platforms.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI Operating Norms for Silver ETFs (LBMA 99.9% purity standards) and Income Tax Act Sections 112 and 50AA on listed commodity ETFs.

### 49. `sip-mistakes-to-avoid.html`
- **Rationale & Changes:**
  - Neutralized H1 ("7 Costly SIP Mistakes...") to "7 Common SIP Pitfalls in Indian Mutual Funds: Mechanisms and Portfolio Impact".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial platforms (Groww, Kuvera, MFCentral) and fund-picking recommendations with generic institutional channels and neutral structural analysis.
  - Detailed fee differentials of Direct vs Regular plans, tax drag of IDCW vs Growth options, and portfolio overlap analysis.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI circulars on Total Expense Ratio (TER) caps and AMFI monthly portfolio disclosure mandate guidelines.

### 50. `sip-pause-vs-stop-mutual-fund.html`
- **Rationale & Changes:**
  - Neutralized H1 from sensational wording to "SIP Pause vs SIP Stop: Mechanisms, Mandates, and Compounding Impact".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial app instructions (Groww, Zerodha Coin, Paytm Money, myCAMS) with generic banking, RTA (CAMS/KFintech), and AMC pause facility mechanics.
  - Expanded compounding arithmetic illustration across multiple illustrative rates (8%, 10%, 12%), removing "expected" return claims.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - NPCI NACH / e-mandate cancellation regulations and individual AMC pause facility tenure limits.

---

## Batch 6 (Articles 51 to 60) — HIGH Risk Overhaul

### 51. `sip-vs-lumpsum.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("Strategic Analysis for Indian Investors") to "SIP vs Lumpsum Mutual Fund Investing: Market Cycles, Behavioral Mathematics, and Allocation Frameworks".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced broker references (Groww, Zerodha Coin, Kuvera) in FAQ and conclusion with generic institutional channels.
  - Provided multi-rate compounding scenarios (6%, 8%, 10%, 12%) without labeling any single rate as "expected".
  - Added "How to think about this yourself" and "Where to get personalised help" pointing to SEBI RIA directory.
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI regulations on systematic investment plans and historical rolling return distribution methodology published by AMFI.

### 52. `small-cap-mid-cap-large-cap-funds-india.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 to "Large Cap, Mid Cap, and Small Cap Mutual Funds in India: SEBI Categorization, Risk Profiles, and Allocation Frameworks".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial broker app mentions (Groww, Zerodha, PayTM Money) with SEBI-registered intermediaries and direct AMC avenues.
  - Reframed prescriptive allocation templates into theoretical multi-cap frameworks, highlighting liquidity risks and semi-annual SEBI market-cap reclassification rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI Circular SEBI/HO/IMD/DF3/CIR/P/2017/114 dated October 6, 2017 (Categorization and Rationalization of Mutual Fund Schemes) and AMFI semi-annual market capitalization classification lists.

### 53. `sovereign-gold-bond-guide-india.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 to "Sovereign Gold Bonds (SGB) in India: Statutory Mechanics, 2.5% Interest Taxation, and Secondary Market Liquidity".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial broker references with generic RBI Retail Direct and stock exchange trading channels.
  - Clarified tax exemption under Section 47(viic) for redemption upon RBI maturity vs. LTCG at 12.5% on secondary market exchange sales.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Government of India Sovereign Gold Bond Scheme gazette notifications and Section 47(viic) of the Income Tax Act.

### 54. `sovereign-gold-bond-sgb-guide-india.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 to "Sovereign Gold Bond (SGB) Framework in India: Coupon Taxation, Secondary Trading, and Sovereign Guarantees".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced broker mentions (Zerodha, Groww) with SEBI-registered stockbrokers, scheduled commercial banks, and RBI Retail Direct.
  - Clarified semi-annual 2.5% coupon taxation under ordinary income tax slabs and capital gains treatment across holding horizons.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India SGB issuance master directions and secondary market trading guidelines on NSE/BSE.

### 55. `step-up-sip-guide.html`
- **Rationale & Changes:**
  - Neutralized promotional H1 ("How Annual Top-Ups Accelerate Wealth Creation...") to "Step-Up SIP (Top-Up SIP) Mechanics, Compounding Mathematics, and Contribution Scaling in India".
  - Updated disclaimer under H1 with humble student persona.
  - Removed commercial platforms (Groww, Zerodha Coin, Kuvera, MFCentral) from execution instructions and FAQ; substituted generic institutional portals.
  - Added multi-rate compounding comparative table across 6%, 8%, 10%, and 12% annualized rates, reframing single-rate CAGR claims into objective mathematical models.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI mutual fund operational guidelines on automated electronic debit mandates and NPCI NACH registration limits.

### 56. `swp-systematic-withdrawal-plan-guide.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("Create a Monthly Pension from Your Mutual Fund Corpus") to "Systematic Withdrawal Plan (SWP) Mechanics, Cash Flow Modeling, and Capital Gains Taxation in India".
  - Updated disclaimer under H1 with humble student persona.
  - Removed fund-picking recommendations (named ICICI Pru, HDFC, Nippon funds) and broker mentions (Groww, Zerodha Coin, Paytm Money).
  - Clarified mathematical risks of reverse dollar-cost averaging during market drawdowns, multi-rate sustainability models (6%, 8%, 10%), and Section 112A / 50AA tax mechanisms under FIFO accounting.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 112A (12.5% LTCG on equity funds exceeding ₹1.25 Lakh) and Section 50AA (slab-rate STCG on specified mutual funds) of the Income Tax Act.

### 57. `systematic-transfer-plan-stp-guide.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("Moving Lumpsum Money Into Equity Safely") to "Systematic Transfer Plan (STP) Mechanics, Asset Allocation, and Capital Gains Taxation in India".
  - Updated disclaimer under H1 with humble student persona.
  - Removed commercial broker application setup instructions (Groww, Zerodha Coin) and replaced with generic direct AMC and RTA transaction channels.
  - Emphasized intra-AMC operational boundaries and statutory tax realities under Section 50AA (source debt fund redemptions taxed at slab rates without indexation).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI regulations on inter-scheme systematic transfer plans and CBDT provisions under Section 50AA for debt fund redemptions.

### 58. `tcs-on-lrs-overseas-remittance-guide.html`
- **Rationale & Changes:**
  - Updated H1 to "TCS on LRS: Section 206C(1G) Tax on Overseas Remittances, Forex Cards & Foreign Education Payments in India (FY 2026-27)".
  - Updated disclaimer under H1 with humble student persona.
  - Clarified statutory mechanics of Section 206C(1G), the ₹7 Lakh annual threshold across multiple authorized dealer banks, AIS / Form 26AS verification, and ITR reconciliation.
  - Added "How to think about this yourself" and "Where to get personalised help" pointing to ICAI-registered Chartered Accountants.
  - Updated author bio to student researcher and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 206C(1G) of the Income Tax Act and RBI Master Direction on the Liberalised Remittance Scheme (LRS) USD 250,000 annual threshold.

### 59. `the-power-of-compounding.html`
- **Rationale & Changes:**
  - Neutralized sensational H1 ("How Small Monthly SIPs Build Multi-Crore Wealth") to "The Mathematics of Compounding: Exponential Growth Mechanics and Multi-Decade Asset Accumulation in India".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced single-rate 12% "projected CAGR" assumptions with multi-rate mathematical compounding models (6%, 8%, 10%, 12%).
  - Removed commercial broker names (Groww, Zerodha Coin, MFCentral) and prescriptive commands ("Never Churn", "Always select Direct").
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI investor education circulars on compound interest mathematics and AMFI long-term systematic investment data sets.

### 60. `treasury-bills-india-guide.html`
- **Rationale & Changes:**
  - Neutralized title/H1 to "Treasury Bills (T-Bills) in India: Auction Mechanics, Yield Mathematics, and Short-Term Debt Allocations".
  - Updated disclaimer under H1 with humble student persona.
  - Explained discount pricing formulas, 91/182/364-day sovereign issuance schedules, non-competitive bidding through RBI Retail Direct, and STCG taxation without TDS.
  - Added thinking/help boxes, updated author bio to student researcher, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Master Directions on Government Securities Auctions and Income Tax Department rules on zero-coupon discount securities.

---

## Batch 7 (Articles 61 to 70) — HIGH & MEDIUM Risk Overhaul

### 61. `understanding-expense-ratio.html`
- **Rationale & Changes:**
  - Neutralized promotional H1 to "Understanding Mutual Fund Expense Ratios: SEBI Regulatory Caps, Daily NAV Deductions, and Long-Term Fee Drag".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced single 13% CAGR return assumption with multi-rate mathematical fee-drag matrix (8%, 10%, 12% gross CAGR) comparing direct vs regular plans.
  - Removed commercial platforms (Groww, Zerodha Coin, Kuvera) from text and takeaways.
  - Detailed SEBI Regulation 52 sliding scale TER caps for equity schemes.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Regulation 52 of Mutual Funds Regulations, 1996 for sliding scale TER caps based on scheme AUM brackets.

### 62. `us-stocks-india-tax-schedule-fa-guide.html`
- **Rationale & Changes:**
  - Neutralized informal H1 to "US Stocks Taxation in India: Capital Gains under Section 112, Schedule FA Disclosure, and Foreign Tax Credit".
  - Updated disclaimer under H1 with humble student persona.
  - Removed broker app mentions (Charles Schwab, Vested, Indmoney) from key takeaways and guide body.
  - Detailed Section 112 unlisted classification (24 months, 12.5% LTCG without indexation) and Section 111A non-applicability.
  - Explained DTAA Article 10 withholding tax credit, Form 67 requirements, Rule 115 SBI TT Buying Rate currency conversion, and Section 43 Black Money Act compliance.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Section 112 of the Income Tax Act, Rule 115 of Income Tax Rules, 1962 (currency conversion on the last day of the preceding month), and Section 43 of the Black Money Act, 2015.

### 63. `what-happens-if-you-miss-sip-payment.html`
- **Rationale & Changes:**
  - Neutralized title and H1 to "What Happens If You Miss a SIP Payment in India? (Rules & Bank Charges)".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced commercial investment apps (Groww, Zerodha Coin, Kuvera, MF Central) with generic institutional phrasing (direct AMC portals, RTAs CAMS/KFintech, SEBI-registered intermediaries).
  - Clarified that AMCs levy zero penalties under SEBI voluntary SIP rules, while commercial banks charge NACH/ECS bounce fees (₹250–₹500 + GST).
  - Clarified AMFI best-practice automated cancellation policy after 3 consecutive missed installments without affecting existing units.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - AMFI best practice guidelines on automated electronic SIP clearing mandates and individual bank NACH ECS return tariff schedules.

### 64. `what-is-a-step-up-sip.html`
- **Rationale & Changes:**
  - Neutralized promotional H1 ("How Increasing Monthly Contributions Can Double Your Wealth") to "What is a Step-Up SIP? Mathematical Modeling of Increasing Periodic Contributions".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced single 12% return comparison with multi-rate compounding comparative table across 8%, 10%, and 12% CAGRs.
  - Removed commercial broker names (Zerodha Coin, Groww, Kuvera, INDmoney); replaced with direct AMC websites, RTAs, and SEBI-registered intermediaries.
  - Added NPCI NACH bank mandate ceiling compliance guidance for escalating debit limits.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - National Payments Corporation of India (NPCI) NACH mandate maximum debit limits and SEBI guidelines on Top-Up SIP facilities.

### 65. `what-is-cagr-mutual-fund-returns.html`
- **Rationale & Changes:**
  - Neutralized H1 to "What is CAGR? Mathematical Mechanics & Application in Mutual Funds".
  - Updated disclaimer under H1 with humble student persona.
  - Updated schema FAQ to eliminate commercial platforms (Groww, Zerodha Coin) in favor of AMFI and AMC factsheets.
  - Clarified mathematical distinction between point-to-point lumpsum CAGR and multi-cashflow SIP XIRR.
  - Replaced fund performance promises with SEBI Total Returns Index (TRI) benchmarking rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Circular SEBI/HO/IMD/DF3/CIR/P/2018/04 dated January 4, 2018 (Benchmarking of Mutual Fund Schemes against Total Return Index).

### 66. `what-is-flexi-cap-fund-india-beginners.html`
- **Rationale & Changes:**
  - Neutralized prescriptive H1 ("Why It's the Best First Mutual Fund for Indian Beginners") to "What is a Flexi Cap Fund? SEBI Mandates, Mechanics & Asset Allocation".
  - Updated disclaimer under H1 with humble student persona.
  - Eliminated prescriptive advice ("Always choose Direct", "Always select Growth", named fund picking).
  - Replaced commercial app mentions (Groww, Zerodha Coin, Kuvera) with generic transaction channels.
  - Detailed SEBI circular SEBI/HO/IMD/DF3/CIR/P/2020/228 (65% minimum domestic equity allocation, zero cap restrictions).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Circular SEBI/HO/IMD/DF3/CIR/P/2020/228 dated November 6, 2020 (Introduction of "Flexi Cap Fund" category).

### 67. `what-is-nav-in-mutual-funds.html`
- **Rationale & Changes:**
  - Neutralized H1 to "What is Net Asset Value (NAV) in Mutual Funds? Mathematical Accounting & Pricing Mechanics".
  - Updated disclaimer under H1 with humble student persona.
  - Explained NAV strictly as an end-of-day mathematical book-value divisor: `(Total Assets − Liabilities) / Outstanding Units`.
  - Removed broker app mentions (Zerodha Coin, Groww, Paytm Money).
  - Detailed SEBI cut-off timings (3:00 PM for equity/debt, 1:30 PM for liquid) and fund realization rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Circular SEBI/HO/IMD/DF2/CIR/P/2020/175 dated September 17, 2020 (Applicability of Net Asset Value upon realization of funds).

### 68. `what-is-nps-national-pension-system-guide.html`
- **Rationale & Changes:**
  - Neutralized conversational H1 ("A Complete Guide for Indian Salaried Employees") to "What is NPS (National Pension System)? PFRDA Regulations, Tax Provisions & Mechanics".
  - Updated disclaimer under H1 with humble student persona.
  - Clarified statutory provisions under Sections 80CCD(1), 80CCD(1B) (exclusive ₹50,000 deduction), and 80CCD(2) employer contributions.
  - Detailed PFRDA exit regulations at age 60: 60% tax-exempt lump sum under Section 10(12A), minimum 40% mandatory annuity, and premature exit rules (80% annuitization).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Pension Fund Regulatory and Development Authority (Exits and Withdrawals under the National Pension System) Regulations, 2015, and Section 10(12A) of the Income Tax Act.

### 69. `8th-pay-commission-salary-calculator-fitment-factor.html`
- **Rationale & Changes:**
  - Neutralized speculative title/H1 ("Salary Hike Estimator & Fitment Factor Scenarios") to "8th Pay Commission: Mathematical Modeling of Fitment Factor & Salary Structure".
  - Updated disclaimer under H1 with humble student persona.
  - Reframed all fitment factor scenarios (1.92, 2.28, 2.57, 2.86) as hypothetical illustrative mathematical models rather than confirmed projections.
  - Removed prescriptive investment calls; highlighted Dearness Allowance zero-base reset and Section 89 arrears relief via Form 10E.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Resolution of the Ministry of Finance regarding terms of reference for Central Pay Commissions and Section 89 relief rules under Income Tax Rule 21A.

### 70. `budget-2026-ltcg-stcg-tax-sip-impact.html`
- **Rationale & Changes:**
  - Neutralized speculative H1 ("Budget 2026: What the New LTCG & STCG Tax Slabs Mean...") to "Mutual Fund Capital Gains Taxation: Sections 112A, 111A & SIP Redemption Mechanics".
  - Updated disclaimer under H1 with humble student persona.
  - Anchored all rules to prevailing statutory provisions: Section 112A (12.5% LTCG above ₹1.25 Lakh), Section 111A (20% STCG), FIFO lot accounting under Section 45(4), and Section 50AA debt fund taxation.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Sections 112A, 111A, and 50AA of the Income Tax Act as amended by recent Finance Acts, and CBDT circulars on FIFO cost basis tracking for mutual fund units.

---

## Batch 8 (Articles 71–80)

### 71. `retirement-planning-india.html`
- **Rationale & Changes:**
  - Neutralized prescriptive H1 ("30x Corpus Rule & Math") to "Retirement Planning in India: Mathematical Modeling of Inflation, Corpus Requirements & Sustainable Withdrawals".
  - Updated disclaimer under H1 with humble student persona.
  - Neutralized rigid 4% safe withdrawal rate rule into an empirical 30x–33x expenditure model (~3.0%–3.33% initial withdrawal) adapted for Indian inflation conditions (6% CPI).
  - Replaced single speculative return assumptions with multi-rate compounding illustrations (6%, 8%, 10%, 12%).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Historical CPI inflation trends published by the Ministry of Statistics and Programme Implementation (MOSPI) and safe withdrawal rate research in emerging markets.

### 72. `term-insurance-vs-endowment-plans.html`
- **Rationale & Changes:**
  - Neutralized emotional tone ("mis-sold in Indian history") and conversational H1 to "Term Insurance vs Endowment Policy: Pure Protection vs Bundled Savings Math".
  - Updated disclaimer under H1 with humble student persona.
  - Replaced prescriptive directives with actuarial Internal Rate of Return (IRR) math comparing pure term + debt/equity models against participating endowment bonus yields (~4.2%–5.0%).
  - Added detailed IRDAI Guaranteed Surrender Value (GSV) rules across policy tenures.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - IRDAI (Protection of Policyholders' Interests, Operations and Allied Matters of Insurers) Regulations, 2024, and Master Circular on Life Insurance Products.

### 73. `50-30-20-rule-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Clarified budgeting mechanics: post-tax salary accounting, mandatory EPF inclusion in savings pool, and metro cost adaptations (60/15/25 model).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Household Finance Committee Report guidelines on consumer debt service ratios.

### 74. `80tta-vs-80ttb-interest-exemption-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Clarified statutory mechanics under Income Tax Act: Section 80TTA (₹10,000 savings interest deduction for non-seniors) vs Section 80TTB (₹50,000 aggregate deposit deduction for senior citizens).
  - Highlighted that neither deduction is available under the default New Tax Regime (Section 115BAC).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Sections 80TTA, 80TTB, and 194A of the Income Tax Act, 1961 for FY 2026-27 (AY 2027-28).

### 75. `active-vs-passive-mutual-funds.html`
- **Rationale & Changes:**
  - Neutralized prescriptive H1 ("Which Strategy Deserves Your Capital?") to "Active vs Passive Mutual Funds: Mathematical Performance & Expense Ratio Analysis".
  - Standard student voice opening added under H1.
  - Replaced prescriptive fund category recommendations with empirical SPIVA India Scorecard data and expense ratio hurdle math.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - Semi-annual SPIVA (S&P Indices Versus Active) India Scorecard reports published by S&P Dow Jones Indices.

### 76. `advance-tax-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Clarified statutory provisions under Sections 207 to 219 (₹10,000 threshold under Section 208, 4 quarterly installments) and interest penalties under Sections 234B and 234C.
  - Outlined capital gain/dividend windfall relief provisions and online e-Pay Tax payment procedures.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Sections 208, 211, 234B, and 234C of the Income Tax Act, 1961.

### 77. `atal-pension-yojana-apy-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Documented statutory rules: PFRDA administration, age criteria (18–40), pension slabs (₹1,000 to ₹5,000/mo), and October 2022 income-tax payer exclusion rule.
  - Analyzed inflation erosion on fixed nominal pensions over multi-decade horizons.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance notification dated August 10, 2022, amending Atal Pension Yojana rules regarding income-tax payers.

### 78. `cagr-vs-xirr-vs-absolute-return-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Detailed mathematical formulations: unannualized Absolute Return for periods under 1 year, point-to-point CAGR for lump sums, and money-weighted XIRR for SIPs/irregular cash flows.
  - Included Excel/Sheets implementation formulas and reverse CAGR target calculations.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI Master Circular for Mutual Funds (SEBI/HO/IMD/PoD-1/P/CIR/2024/90) regarding mandatory return disclosure methodologies.

### 79. `car-loan-emi-calculator-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Contrasted reducing balance interest amortization against misleading flat-rate dealer quotations.
  - Highlighted RBI Key Fact Statement (KFS) requirements, Annual Percentage Rate (APR) disclosures, and prepayment/foreclosure charges.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - RBI Master Direction on Regulatory Framework for Microfinance and Retail Advances, and Circular on Key Fact Statement (KFS) for retail loans.

### 80. `child-education-planning.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Modeled higher education inflation compounding (8%–10% p.a.) versus standard CPI inflation.
  - Outlined pre-goal derisking glide path across equity and capital-protected debt (liquid funds, fixed deposits) 3 years prior to college admission.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Small savings interest rates published by the National Savings Institute (Ministry of Finance) for Sukanya Samriddhi Yojana (SSY) and PPF.

---

## Batch 9 (Articles 81–90)

### 81. `cibil-credit-score-improvement-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Clarified Credit Information Companies (Regulation) Act, 2005 (CICRA) statutory framework and RBI-licensed credit bureaus (CIBIL, Experian, Equifax, CRIF High Mark).
  - Outlined mathematical weightings: on-time repayment history (35%), credit utilization ratio (30% threshold), credit age (15%), credit mix (10%), and hard inquiries (10%).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - RBI Master Direction on Credit Information Companies (Regulation) Act, 2005 and free annual credit report entitlement directives.

### 82. `credit-score-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Documented 300–900 score distribution across all four RBI-licensed bureaus.
  - Explained risk-based loan pricing, credit card utilization discipline, co-borrower liability, and official dispute resolution via bureau portals.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - RBI Circular on Compensation mechanism for delayed updating/rectification of credit information by CICs and credit institutions.

### 83. `crypto-vda-tax-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Neutralized commercial exchange references (CoinDCX, WazirX, Binance, Bybit) to generic institutional terms ("FIU-IND registered domestic reporting entities", "offshore virtual asset platforms").
  - Explained mathematical asymmetry under Section 115BBH: flat 30% plus 4% cess on each winning trade with zero loss set-off against other crypto gains or income heads.
  - Clarified 1% TDS surveillance under Section 194S, AIS matching, and transaction reporting under Schedule VDA in ITR-2/ITR-3.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Sections 115BBH and 194S of the Income Tax Act, 1961, and CBDT Circular No. 13/2022 on VDA loss set-off prohibitions.

### 84. `ctc-vs-in-hand-salary-explained.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Detailed breakdown of CTC components: Basic Salary (40–50%), HRA, Special Allowance, Employer EPF (12%), Gratuity provisioning (~4.81%), and variable bonus targets.
  - Clarified Payment of Gratuity Act 5-year continuous service rule and salary deductions (employee EPF, state Professional Tax, and Section 192 TDS).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Payment of Gratuity Act, 1972 statutory formula: (15 × Last Drawn Basic × Tenure) / 26, and EPFO wage ceilings.

### 85. `dividend-income-tax-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Outlined post-Finance Act 2020 regime following Dividend Distribution Tax (DDT) abolition: dividends taxed as "Income from Other Sources" at marginal slab rates.
  - Documented Section 194 / Section 194K 10% TDS above ₹5,000 threshold, Form 15G/15H relief, and Section 57(i) interest deduction capped at 20% of gross dividend income.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Sections 56(2)(i), 57(i), 194, 194K, and 234C of the Income Tax Act, 1961.

### 86. `elss-funds-tax-saving-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Documented SEBI mutual fund categorization mandate: minimum 80% equity asset allocation in ELSS.
  - Explained 3-year statutory lock-in mechanics (each monthly SIP carrying an independent 36-month lock-in).
  - Contrasted Section 80C deduction availability under Old Tax Regime versus non-applicability under the default New Tax Regime.
  - Noted Finance Act 2024 LTCG tax rate (12.5% above ₹1.25 Lakh threshold).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI Categorization and Rationalization circular for ELSS funds, and Section 80C limits under Old vs New Tax Regimes.

### 87. `emergency-fund-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Replaced callout warning disclaimer with standard student voice opening and dedicated thinking/help boxes.
  - Structured 3-tier liquidity architecture: 1 month living expenses in secondary savings account, 2–3 months in bank FDs, and 2–3 months in liquid mutual funds (with instant redemption up to ₹50,000/90% of folio).
  - Highlighted debt-free capital preservation over speculative returns during emergency events.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimer.
- **[VERIFY: ...] Items:**
  - SEBI instant access facility limits for liquid mutual funds (SEBI Circular SEBI/HO/IMD/DF2/CIR/P/2017/39).

### 88. `epf-vs-ppf-vs-vpf.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Detailed comparison across EPF (8.25% sovereign interest), VPF (8.25% with employer eligibility), and PPF (7.10% Fixed, EEE tax status, ₹1.5L annual cap).
  - Highlighted Section 10(11)/10(12) ₹2.5 Lakh annual employee PF contribution interest taxation threshold.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Central Board of Direct Taxes (CBDT) Rule 9D notification governing taxable and non-taxable provident fund contribution accounts.

### 89. `epf-withdrawal-rules-25-percent-minimum-balance.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Documented EPF Scheme 2026 overhaul: mandatory 25% minimum balance ring-fencing to preserve retirement compounding.
  - Detailed 3 consolidated advance categories (housing, personal family milestones, and medical distress).
  - Outlined unemployment rules (75% advance after 1 month; remaining 25% after 2 months of continuous unemployment) and ₹5 Lakh auto-mode settlement engine.
  - Clarified 5-year continuous service rule and Section 192A 10% TDS on premature settlements.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Labour and Employment gazette notifications on Employees' Provident Funds Scheme 2026 and EPFO auto-claim processing circulars.

### 90. `fd-laddering-strategy.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Illustrated 5-year staggered maturity conveyor belt to eliminate interest rate timing risk and premature withdrawal penalties (0.5%–1.0%).
  - Highlighted DICGC ₹5 Lakh sovereign insurance coverage per depositor per bank and Section 194A TDS thresholds (₹40,000 for general savers, ₹50,000 for senior citizens).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - DICGC Act, 1961 insurance limit provisions and Section 194A TDS thresholds under the Income Tax Act.

---

## Batch 10 (Articles 91 to 100) — LOW Risk Overhaul

### 91. `fd-vs-debt-mutual-funds.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Documented post-Finance Act 2023 taxation under Section 50AA: specified mutual funds with equity allocation <=35% taxed at slab rates without indexation benefit, leveling tax treatment with fixed deposits.
  - Emphasized liquidity, credit risk, and mark-to-market NAV fluctuations in debt mutual funds vs DICGC sovereign guarantee on FDs up to ₹5 Lakh.
  - Updated author bio card to student persona; verified presence of thinking and help boxes; removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 50AA of the Income Tax Act, 1961 and DICGC insurance limits under DICGC Act, 1961.

### 92. `fire-movement-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Examined the mathematics of Financial Independence, Retire Early (FIRE) within the Indian economic context, highlighting sequence of returns risk, domestic healthcare inflation (12–14%), and longevity risk.
  - Contrasted standard 25x/30x rule models against higher inflation baselines.
  - Updated author bio card to student persona; verified presence of thinking and help boxes; removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - RBI macroeconomic reports on headline CPI and healthcare inflation indices in India.

### 93. `form-16-tds-on-salary-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Detailed the structural architecture of Form 16: Part A (TRACES-generated tax credit certificate signed by employer with quarterly TDS verification) and Part B (salary breakup, allowances, and tax computation under Section 192).
  - Emphasized reconciliation against AIS and Form 26AS prior to filing ITR-1 or ITR-2.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Sections 192 and 203 of the Income Tax Act, 1961 and Rule 31 of Income Tax Rules.

### 94. `form-26as-vs-ais-vs-tis-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Contrasted the roles of Form 26AS (statutory TDS/TCS ledger), Annual Information Statement (comprehensive financial transactions reporting under SFT rules), and Taxpayer Information Summary (condensed summary feeding directly into pre-filled ITRs).
  - Outlined dispute management protocol via the AIS feedback portal for duplicate or erroneous entries.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 285BB of the Income Tax Act and Rule 114-I governing AIS data collection.

### 95. `freelancer-tax-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Detailed Section 44ADA presumptive taxation mechanics for specified professionals (50% deemed profit calculation on gross receipts up to ₹75 Lakh where cash receipts <=5%).
  - Outlined Advance Tax schedule (15 March single 100% instalment for 44ADA vs quarterly calendar for non-presumptive professionals).
  - Explained GST registration threshold (₹20 Lakh / ₹10 Lakh in special category states) and Letter of Undertaking (LUT) provisions for export of services.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 44ADA, Section 44AB, and Section 208 of the Income Tax Act, and CGST Act Section 22 / Rule 96A on LUT filings.

### 96. `gift-tax-rules-india-section-56-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Demystified Section 56(2)(x) taxing gifts as "Income from Other Sources".
  - Clarified strict definition of exempt "relatives" (lineal ascendants/descendants, siblings, spouse) vs non-exempt family members (cousins, uncles).
  - Emphasized that the ₹50,000 threshold for non-relatives is an all-or-nothing threshold rather than a basic exemption.
  - Explained Section 64 clubbing provisions on gifted assets to spouses or daughters-in-law.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 56(2)(x) and Section 64 of the Income Tax Act, 1961.

### 97. `gratuity-calculation-tax-exemption-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Documented statutory entitlement under the Payment of Gratuity Act, 1972 after 5 years of continuous service (or 4 years and 240 days per judicial interpretations in 6-day establishments).
  - Explained the 15/26 formula: `(Basic + DA) * 15 / 26 * Completed Years of Service`.
  - Clarified Section 10(10)(ii) cumulative lifetime tax exemption limit of ₹20 Lakh for private employees (with full exemption for government personnel).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Payment of Gratuity Act, 1972 Section 4 and Section 10(10) of the Income Tax Act, 1961.

### 98. `health-insurance-80d-tax-deduction-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Structured Section 80D deduction limits under the Old Tax Regime: ₹25,000 for self/family (₹50,000 if senior citizen) and ₹25,000 for parents (₹50,000 if senior citizen).
  - Explained the ₹5,000 preventive health check-up sub-limit and Section 80D(2)(c) medical expenditure deductions for uninsured senior parents.
  - Noted disallowance of Section 80D deductions under the default New Tax Regime (Section 115BAC).
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Section 80D and Section 115BAC of the Income Tax Act, 1961.

### 99. `home-loan-prepayment-vs-sip-strategy.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate educational disclaimer box.
  - Modeled loan prepayment vs parallel equity SIP compounding: guaranteed after-tax borrowing cost reduction vs historical long-term equity growth potential.
  - Explained impact of the default New Tax Regime where Section 24(b) interest deduction is not available on self-occupied properties.
  - Formulated the hybrid framework: 1 extra EMI annually towards principal prepayment combined with continuous SIP discipline.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Master Direction on foreclosure charges / prepayment penalties on floating rate personal home loans.

### 100. `how-gold-price-is-decided-in-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Analyzed the transmission of international bullion rates (LBMA spot + USD/INR exchange rate + import customs duty) into Indian retail benchmarks (IBJA rates).
  - Detailed the mathematics of 22K (91.6% purity) vs 24K (99.9% purity), making charges (flat per gram vs percentage of gold), and dual GST rates (3% on metal, 5% on making charges).
  - Emphasized mandatory 6-digit Hallmark Unique Identification (HUID) and verification via the BIS Care app.
  - Added thinking/help boxes, updated student bio, and removed duplicate bottom disclaimers.
- **[VERIFY: ...] Items:**
  - Bureau of Indian Standards (BIS) Hallmarking Regulations and CBIC GST notifications on precious metals and job work.

---

## Batch 11 (Articles 101–110 — LOW Risk)

### 101. `how-to-file-itr-1-online-salaried-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Clarified strict ITR-1 (Sahaj) eligibility: resident individual with total income up to ₹50 Lakh derived from salary, one house property, and other sources (interest, family pension), and agricultural income up to ₹5,000.
  - Detailed pre-filing reconciliation steps: matching Form 16 Part A/B against AIS, TIS, and 26AS to prevent CPC notices under Section 143(1)(a).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Rule 12 of Income Tax Rules and Income Tax Department instructions for ITR-1 (Sahaj).

### 102. `how-to-save-tax-in-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Replaced prescriptive tax-saving declarations with objective break-even analysis between the Old Tax Regime (deductions via 80C, 80D, 24b, HRA) and New Tax Regime (Section 115BAC with higher standard deduction of ₹75,000 and ₹3 Lakh basic exemption).
  - Outlined statutory deductions portfolio (80C, 80CCD(1B), 80D, 80TTA/TTB, Section 24b) as an arithmetic framework.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 115BAC and Chapter VI-A statutory deduction provisions of the Income Tax Act, 1961.

### 103. `how-to-use-sip-calculator-complete-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Grounded calculator usage in actual compounding formulas: monthly periodic compounding rate vs volatile real-world mutual fund returns.
  - Explained inflation-adjusted future purchasing power math and demonstrated the leverage of annual step-up SIP percentages.
  - Replaced platform endorsements with generic regulatory transaction portals (MFCentral, AMC websites).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Future Value of an Annuity formula against AMFI investor education resources.

### 104. `hra-exemption-calculation-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Detailed the statutory 3-limb minimum formula under Section 10(13A) and Rule 2A of the Income Tax Rules: (1) Actual HRA received, (2) Rent paid in excess of 10% of salary, (3) 50% of salary for metro cities (Mumbai, Delhi, Kolkata, Chennai) or 40% for non-metro locations.
  - Clarified salary definition: Basic + Dearness Allowance (forming part of retirement benefits) + turnover commission.
  - Documented mandatory landlord PAN requirement when annual rent exceeds ₹1,00,000 (CBDT Circular 08/2013).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 10(13A) of the Income Tax Act, 1961 and Rule 2A of the Income Tax Rules, 1962.

### 105. `hra-exemption-rent-paid-to-parents-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Explained legal requirements for bona fide family tenancy: registered/executed rent agreement, verifiable banking trail (NEFT/UPI/cheque), and landlord parents declaring rental income under Schedule HP.
  - Highlighted tax pitfalls: claimant cannot be a legal co-owner of the property, cash payments invite scrutiny, and spouse rent payments are generally disallowed under Section 60-64 clubbing provisions.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 10(13A) and Section 22-27 of the Income Tax Act, 1961.

### 106. `income-tax-act-2025-old-vs-new-section-mapping-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Explored structural architecture of the Direct Tax Code/Income Tax Act 2025 reforms: transition from 1961 section numbers to streamlined unified chapters.
  - Mapped core concepts: Assessment Year vs Previous Year unification into single "Tax Year", Section 115BAC default regime institutionalization, and standard deduction continuity.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Income Tax Bill 2025 draft tables and Ministry of Finance legislative releases.

### 107. `income-tax-slabs-india-2026.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Detailed the revised FY 2025-26 / FY 2026-27 slab structure under Section 115BAC: Nil up to ₹3L, 5% from ₹3L–₹7L, 10% from ₹7L–₹10L, 15% from ₹10L–₹12L, 20% from ₹12L–₹15L, and 30% above ₹15L.
  - Explained Section 87A rebate mechanics (effective zero tax up to ₹7 Lakh taxable income) and the standard deduction of ₹75,000 for salaried individuals.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Finance Act provisions amending Section 115BAC and Section 87A of the Income Tax Act, 1961.

### 108. `joint-home-loan-tax-benefits-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Documented dual tax benefits: each co-owner can independently claim up to ₹2,00,000 for interest under Section 24(b) and up to ₹1,50,000 for principal under Section 80C under the Old Tax Regime.
  - Emphasized mandatory co-ownership rule: claimant must be both a co-borrower on the loan and a registered co-owner on the property deed.
  - Explained proportional deduction sharing matching title deed percentage and bank account repayment trail.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 24(b), Section 26, and Section 80C(2)(xviii) of the Income Tax Act, 1961.

### 109. `kisan-vikas-patra-kvp-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Analyzed compounding mechanics of Kisan Vikas Patra (annual compounding at 7.5% p.a., 115-month doubling period).
  - Clarified lack of Section 80C deduction and full taxability of interest as "Income from Other Sources".
  - Explained lock-in period (minimum 2.5 years / 30 months) and sovereign backing by the Government of India with no upper investment ceiling.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Government of India Ministry of Finance quarterly small savings interest rate circulars and Kisan Vikas Patra Scheme Rules.

### 110. `leave-encashment-tax-exemption-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Outlined statutory tax exemption rules under Section 10(10AA): full exemption for government employees vs least of 4 statutory calculations for non-government employees.
  - Documented the enhanced statutory maximum lifetime ceiling of ₹25,00,000 notified by CBDT Notification S.O. 2276(E) effective April 1, 2023.
  - Explained 30-day statutory leave entitlement cap per year of completed service, 10-month average salary calculation, and full taxability during active service.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 10(10AA) of the Income Tax Act, 1961 and CBDT Notification S.O. 2276(E).

---

## Batch 12 (Articles 111–120 — LOW Risk)

### 111. `life-insurance-tax-deduction-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Detailed statutory premium deduction rules under Section 80C (up to ₹1.5 Lakh limit in Old Regime, 10% premium-to-sum-assured cap under Section 80C(5)).
  - Documented maturity exemption criteria under Section 10(10D) alongside recent statutory thresholds: ₹2.5 Lakh annual premium cap for ULIPs (Finance Act 2021) and ₹5.0 Lakh aggregate annual premium cap for traditional non-unit linked policies issued on or after April 1, 2023 (Finance Act 2023).
  - Clarified Section 194DA TDS rules (5% on net income portion for non-exempt payouts) and confirmed death benefit exemption remains fully intact.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 80C, Section 10(10D), and Section 194DA of the Income Tax Act, 1961 along with CBDT Circular No. 15 of 2023.

### 112. `mahila-samman-savings-certificate-mssc-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Analyzed statutory parameters of Mahila Samman Savings Certificate: fixed interest rate of 7.5% per annum with quarterly compounding, 2-year tenure, and ₹2,00,000 maximum deposit limit per depositor.
  - Clarified tax rules: interest is fully taxable under "Income from Other Sources" at slab rates; Section 80C deduction is not available; CBDT Notification No. 27/2023 exempts TDS under Section 194A.
  - Outlined liquidity rules: partial withdrawal up to 40% of balance permitted after 1 year, and premature closure conditions (death, medical emergencies, or after 6 months at a 2% interest penalty).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance Mahila Samman Savings Certificate Scheme, 2023 Rules and CBDT Notification No. 27/2023.

### 113. `muhurat-trading-2026-diwali-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Replaced speculative stock-picking tips with statutory and operational mechanics of the one-hour Diwali Muhurat trading session.
  - Documented exchange order matching protocols (pre-open call auction, continuous matching), liquidity realities, and wider bid-ask spreads.
  - Outlined settlement cycle obligations (T+1 rolling settlement) and capital gains taxation under Section 111A (STCG at 20%) and Section 112A (LTCG at 12.5% above ₹1.25L).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - NSE and BSE circulars specifying the exact date and timing for Diwali Muhurat Trading 2026.

### 114. `mutual-fund-categories-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Detailed the SEBI Categorization and Rationalization Circular (2017) establishing 36 distinct mutual fund categories across 5 broad groups: Equity (10), Debt (16), Hybrid (6), Solution-Oriented (2), and Other Schemes (2).
  - Documented asset allocation thresholds (e.g., minimum 80% for large caps, 65% for mid/small caps, 65% in equity + 10% in debt for multi-asset).
  - Explained SEBI Riskometer mandates, benchmark alignment rules, and portfolio disclosure norms.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI Master Circular for Mutual Funds (SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/74) and scheme categorization thresholds.

### 115. `mutual-fund-portfolio-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Reframed portfolio construction from prescriptive fund recommendations into an educational exploration of mathematical principles: core-and-satellite structures, risk diversification, asset class correlation, and portfolio overlap.
  - Outlined overlap measurement metrics, portfolio drift mechanics, and periodic rebalancing frameworks based on asset allocation boundaries rather than market timing.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI investor awareness guidelines and AMFI portfolio diversification principles.

### 116. `mutual-fund-types-beginner-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Provided a foundational educational breakdown of mutual fund structures: open-ended vs closed-ended, direct plans vs regular plans (TER differential), and active vs passive indexing.
  - Mapped core asset classes (equity, debt, hybrid, money market) to standard risk-return trade-offs and SEBI Riskometer classifications.
  - Explained NAV calculation mechanics, expense ratios, and capital gains tax brackets post-Finance Act (No. 2) 2024.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - AMFI direct plan NAV disclosure guidelines and SEBI TER disclosure standards.

### 117. `national-savings-certificate-nsc-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Documented statutory terms of National Savings Certificate (NSC VIII Issue): 5-year lock-in, 7.7% interest compounded annually and payable at maturity.
  - Detailed Section 80C deduction mechanics: initial deposit qualifies for deduction; accrued interest for years 1 to 4 is deemed reinvested and also qualifies under Section 80C; 5th year interest is fully taxable.
  - Clarified absence of TDS under Section 194A, certificate pledging facility for commercial loans, and sovereign safety under Government of India rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance Government Savings Certificates (National Savings Certificate - VIII Issue) Rules, 2019.

### 118. `nps-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Mapped structural distinction between Tier I (mandatory retirement account with tax incentives and withdrawal restrictions) and Tier II (voluntary open-access account with no lock-in).
  - Outlined tax provisions under Section 80CCD(1) (part of ₹1.5L cap), Section 80CCD(1B) (exclusive ₹50,000 deduction), and Section 80CCD(2) (employer contribution deduction up to 14% of Basic + DA, available under both regimes).
  - Detailed exit and withdrawal rules: 60% lump sum tax-free at age 60, minimum 40% mandatory annuity purchase, and partial withdrawal provisions under PFRDA regulations.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - PFRDA (Exits and Withdrawals under NPS) Regulations and Sections 80CCD(1), 80CCD(1B), and 80CCD(2) of the Income Tax Act, 1961.

### 119. `old-vs-new-tax-regime.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Removed specific third-party commercial mutual fund recommendations in FAQ.
  - Presented mathematical breakeven deduction analysis for salaried professionals across multiple salary slabs (₹10L, ₹12.5L, ₹15L, ₹20L, ₹25L).
  - Contrasted Section 115BAC default regime (₹75,000 standard deduction, Sec 87A rebate) with Old Regime itemized deductions (Sec 80C, 80D, 24(b), 10(13A)).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 115BAC, Section 87A, and Section 16(ia) of the Income Tax Act, 1961 for FY 2026-27 (AY 2027-28).

### 120. `pmjjby-pmsby-jan-suraksha-scheme-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Documented statutory parameters of Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY): ₹436/yr premium for ₹2 Lakh life cover (age 18–50, coverage up to age 55), 45-day initial waiting period for non-accidental death.
  - Documented Pradhan Mantri Suraksha Bima Yojana (PMSBY): ₹20/yr premium for ₹2 Lakh accidental death / permanent total disability cover (age 18–70).
  - Clarified auto-debit rules (annual renewal on June 1), single-bank restriction (claims capped at ₹2 Lakh across all bank folios), and claim submission protocol (within 30 days to bank branch).
  - Outlined tax provisions: PMJJBY premium qualifies under Section 80C (Old Regime), and death claim payouts are fully exempt under Section 10(10D).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance Department of Financial Services (DFS) scheme rules for PMJJBY and PMSBY as of FY 2026-27.

---

## Batch 13 (Articles 121–130 — LOW Risk)

### 121. `post-office-monthly-income-scheme-pomis-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Documented statutory rules: 7.4% fixed annual interest paid monthly across 5-year tenure; statutory deposit ceilings of ₹9 Lakh (single) and ₹15 Lakh (joint).
  - Clarified premature exit penalty schedule (no exit in Year 1, 2% penalty between Years 1 and 3, 1% penalty between Years 3 and 5).
  - Explained taxability under "Income from Other Sources" and Section 80TTB interest deduction for senior citizens.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance quarterly small savings interest notifications and Government Savings Promotion Act rules for POMIS.

### 122. `post-office-time-deposit-potd-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Detailed tenure options (1, 2, 3, and 5 years) and quarterly compounding mechanics with annual payout.
  - Clarified that only the 5-year tenure qualifies for Section 80C deduction under the Old Tax Regime.
  - Documented premature closure penalties (no withdrawal before 6 months; savings rate 4% between 6–12 months; 2% interest reduction after 1 year).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance National Savings Time Deposit Scheme Rules, 2019 (GSR 922(E)) and quarterly rate notifications.

### 123. `ppf-rules-benefits-wealth-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Highlighted EEE tax privilege: Section 80C deduction, tax-free annual interest under Section 10(11), and tax-free maturity proceeds.
  - Mathematically demonstrated the 5th-of-the-month deposit rule for monthly compounding maximization.
  - Outlined Form H extension requirements (submission within 1 year of 15-year maturity in 5-year blocks) and statutory protection against court attachment under the Government Savings Banks Act.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Ministry of Finance Public Provident Fund Scheme Rules 2019 and Section 10(11) of the Income Tax Act, 1961.

### 124. `ppf-vs-elss-vs-nps-india-2026.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.callout.warn` and redundant bottom disclaimers.
  - Replaced prescriptive product choices with an objective comparison framework: lock-in tenures (ELSS 3 yrs, PPF 15 yrs, NPS age 60), risk profiles, and tax treatment (EEE for PPF vs capital gains for ELSS vs EET structure for NPS).
  - Clarified Section 80CCD(1B) additional ₹50,000 deduction for NPS Tier 1 and 80CCD(2) employer contribution rules.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Finance Act provisions regarding Section 80C, 80CCD(1B), and Section 112A capital gains tax limits.

### 125. `presumptive-taxation-44ada-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Documented statutory provisions of Section 44ADA: 50% deemed profit on gross receipts for specified professions under Section 44AA(1).
  - Detailed turnover caps: ₹50 Lakh statutory limit, enhanced to ₹75 Lakh if cash collections do not exceed 5%.
  - Highlighted administrative reliefs: exemption from maintaining accounting ledgers under Section 44AA, and single advance tax installment on or before March 15 (no Section 234C quarterly penalties).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Section 44ADA, Section 44AA, and Section 211 of the Income Tax Act, 1961.

### 126. `rbi-floating-rate-savings-bonds-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Documented the floating coupon mechanism: pegged at NSC rate + 0.35% (reset semi-annually on 1 January and 1 July).
  - Explained strict 7-year lock-in for non-seniors and graded early encashment windows for senior citizens (ages 60+, 70+, 80+).
  - Detailed taxability under slab rates and mandatory 10% TDS under Section 193.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Floating Rate Savings Bonds, 2020 (Taxable) scheme notifications and Section 193 of the Income Tax Act, 1961.

### 127. `rbi-retail-direct-scheme-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Documented the institutional architecture of the RBI Retail Direct platform: direct Retail Direct Gilt (RDG) accounts with zero fees, no AMC, and no bidding commission.
  - Outlined the four accessible sovereign instruments: Dated G-Secs, Treasury Bills (91, 182, 364 days), State Development Loans (SDLs), and Sovereign Gold Bonds.
  - Explained non-competitive bidding mechanics, NDS-OM secondary market trading, duration risk, and absence of TDS by RBI.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - Reserve Bank of India Retail Direct Scheme guidelines and CCIL NDS-OM trading rules.

### 128. `recurring-deposit-rd-calculator-guide-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Preserved interactive JavaScript calculator logic while explaining Indian Banks' Association (IBA) quarterly compounding mechanics.
  - Contrasted commercial bank RDs with Post Office 5-year RDs (6.7% quarterly compounded).
  - Documented Section 194A TDS thresholds (₹40,000 for regular individuals, ₹50,000 for senior citizens) and Form 15G/15H submission protocols.
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - RBI Master Direction on Interest Rates on Deposits and Section 194A of the Income Tax Act, 1961.

### 129. `reits-and-invits-in-india-guide.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate `.disclaimer-box` callout and redundant bottom disclaimers.
  - Outlined SEBI (Real Estate Investment Trusts) Regulations, 2014 and SEBI (Infrastructure Investment Trusts) Regulations, 2014, including the mandatory 90% Net Distributable Cash Flow (NDCF) payout rule.
  - Detailed the 3-tier distribution tax decomposition: interest component (taxable at slab rates), dividend component (conditional exemption based on SPV tax regime), and repayment of debt / return of capital (taxed as other income above unit issue price under Finance Act 2023).
  - Outlined capital gains tax rules under Section 112A (LTCG at 12.5% above ₹1.25 Lakh, holding period 12 months for listed units).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - SEBI REIT/InvIT Regulations and CBDT notifications regarding distribution component taxation under Section 56(2)(xii) and Section 115UA.

### 130. `repo-rate-hike-home-loan-emi-impact-india.html`
- **Rationale & Changes:**
  - Standard student voice opening added under H1.
  - Removed duplicate bottom disclaimers.
  - Explained the transmission mechanism of RBI Policy Repo Rate adjustments through External Benchmark Lending Rates (EBLR/RLLR) under RBI Circular DBR.Dir.BC.No.14/08.12.001/2019-20.
  - Unpacked the "silent tenure drift" trap where lenders keep EMI constant and lengthen tenure by default, increasing total interest outgo.
  - Provided mathematical prepayment models (e.g., paying 1 extra EMI per year or increasing EMI by 5% to offset rate hikes).
  - Added thinking/help boxes, updated student bio, and removed duplicate disclaimers.
- **[VERIFY: ...] Items:**
  - RBI Monetary Policy Committee resolution statements and RBI master direction on floating rate loans.

---
