import os
import json
import html
from calc_specs import CALCULATOR_SPECS
from build_components import get_header, get_calc_switcher, get_all_calculators_grid, get_footer, SITE_DIR

def build_all_calculators():
    print(f"Building {len(CALCULATOR_SPECS)} production calculators...")
    
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
                <input type="number" id="{f4['id']}-num" value="{f4['val']}" min="{f4['min']}" max="{f4['max']}" step="{f4['step']}" aria-label="{f4['label']} Input">
                <span class="calc-input-suffix">{f4['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{f4['id']}" min="{f4['min']}" max="{f4['max']}" step="{f4['step']}" value="{f4['val']}" aria-label="{f4['label']} Slider">
          </div>"""

        label1 = "Invested Capital"
        label2 = "Estimated Growth"
        label3 = "Total Projected Value"
        table_th1 = "Year"
        table_th2 = "Opening Capital"
        table_th3 = "Annual Deposit"
        table_th4 = "Interest / Growth"
        table_th5 = "Closing Balance"

        if c["calc_type"] == "goal":
            label1 = "Target Corpus Goal"
            label2 = "Estimated Total Returns"
            label3 = "Required Monthly SIP"
        elif c["calc_type"] == "ppf":
            label1 = "Total Capital Deposited"
            label2 = "Total Tax-Free Interest"
            label3 = "Maturity Proceeds (EEE)"
            table_th3 = "Yearly PPF Deposit"
            table_th4 = "7.1% Tax-Free Interest"
            table_th5 = "PPF Closing Balance"
        elif c["calc_type"] == "swp":
            label1 = "Initial Investment Corpus"
            label2 = "Total Amount Withdrawn"
            label3 = "Final Remaining Balance"
            table_th2 = "Starting Corpus"
            table_th3 = "Annual Withdrawals"
            table_th4 = "Returns Generated"
            table_th5 = "Remaining Balance"
        elif c["calc_type"] == "emi":
            label1 = "Monthly Regular EMI"
            label2 = "Total Interest Saved"
            label3 = "Net Interest Payable"
            table_th2 = "Opening Principal"
            table_th3 = "Principal Repaid"
            table_th4 = "Interest Charged"
            table_th5 = "Remaining Loan"
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
            <summary style="font-weight:700; cursor:pointer; font-size:1.02rem; color:var(--text-primary);">{html.escape(q)}</summary>
            <p style="margin-top:12px; color:var(--text-secondary); line-height:1.65; margin-bottom:0;">{ans}</p>
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
  <link rel="canonical" href="https://calculatorship.in/{c['slug']}">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['metaDesc']}">
  <meta property="og:url" content="https://calculatorship.in/{c['slug']}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://calculatorship.in/og-image.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://calculatorship.in/og-image.webp">
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
    "url": "https://calculatorship.in/{c['slug']}",
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
    <div class="ad-slot ad-slot-banner" style="max-width:1540px; margin:16px auto 28px; padding:0 36px;">
      <span class="ad-label" style="display:block; font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; margin-bottom:4px;">Advertisement</span>
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-7598871729388798" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <div class="calc-main-container">
      <div class="calc-grid" id="calculator-card">
        
        <!-- Left: Inputs -->
        <div class="calc-card">
          <h2 style="font-size:1.35rem; font-weight:800; margin-bottom:24px; color:var(--text-primary);">Configure Financial Parameters</h2>
          
          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field1']['id']}">{c['field1']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field1']['prefix']}</span>
                <input type="number" id="{c['field1']['id']}-num" value="{c['field1']['val']}" min="{c['field1']['min']}" max="{c['field1']['max']}" step="{c['field1']['step']}" aria-label="{c['field1']['label']} Input">
                <span class="calc-input-suffix">{c['field1']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field1']['id']}" min="{c['field1']['min']}" max="{c['field1']['max']}" step="{c['field1']['step']}" value="{c['field1']['val']}" aria-label="{c['field1']['label']} Slider">
          </div>

          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field2']['id']}">{c['field2']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field2']['prefix']}</span>
                <input type="number" id="{c['field2']['id']}-num" value="{c['field2']['val']}" min="{c['field2']['min']}" max="{c['field2']['max']}" step="{c['field2']['step']}" aria-label="{c['field2']['label']} Input">
                <span class="calc-input-suffix">{c['field2']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field2']['id']}" min="{c['field2']['min']}" max="{c['field2']['max']}" step="{c['field2']['step']}" value="{c['field2']['val']}" aria-label="{c['field2']['label']} Slider">
          </div>

          <div class="calc-field-group">
            <div class="calc-field-header">
              <label for="{c['field3']['id']}">{c['field3']['label']}</label>
              <div class="calc-input-box">
                <span class="calc-input-prefix">{c['field3']['prefix']}</span>
                <input type="number" id="{c['field3']['id']}-num" value="{c['field3']['val']}" min="{c['field3']['min']}" max="{c['field3']['max']}" step="{c['field3']['step']}" aria-label="{c['field3']['label']} Input">
                <span class="calc-input-suffix">{c['field3']['suffix']}</span>
              </div>
            </div>
            <input type="range" id="{c['field3']['id']}" min="{c['field3']['min']}" max="{c['field3']['max']}" step="{c['field3']['step']}" value="{c['field3']['val']}" aria-label="{c['field3']['label']} Slider">
          </div>

          {extra_field_html}
        </div>

        <!-- Right: Summary Results & Visuals -->
        <div class="calc-summary-card">
          <div>
            <h3 style="font-size:1.2rem; font-weight:800; color:var(--text-primary); margin-bottom:18px;">Simulation Results</h3>
            
            <div class="result-row">
              <span class="result-label">{label1}</span>
              <span class="result-val" id="res-invested">₹0</span>
            </div>

            <div class="result-row">
              <span class="result-label">{label2}</span>
              <span class="result-val" id="res-returns" style="color:#059669;">₹0</span>
            </div>

            <div class="result-row" style="padding-top:18px;">
              <span class="result-label" style="font-weight:800; color:var(--text-primary);">{label3}</span>
              <span class="result-val highlight" id="res-total">₹0</span>
            </div>

            <!-- SVG Visual Donut Ratio -->
            <div style="margin:28px 0 12px; display:flex; align-items:center; justify-content:center; gap:28px;">
              <svg width="130" height="130" viewBox="0 0 42 42" class="donut">
                <circle class="donut-ring" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#E2E8F0" stroke-width="5.5"></circle>
                <circle id="donut-segment" cx="21" cy="21" r="15.91549430918954" fill="transparent" stroke="#00D09C" stroke-width="5.5" stroke-dasharray="70 30" stroke-dashoffset="25"></circle>
              </svg>
              <div style="font-size:0.90rem; line-height:1.9;">
                <div style="display:flex; align-items:center; gap:8px;"><span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#00D09C;"></span> <span id="donut-leg-gain">Growth: 0%</span></div>
                <div style="display:flex; align-items:center; gap:8px;"><span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#CBD5E1;"></span> <span id="donut-leg-inv">Capital: 0%</span></div>
              </div>
            </div>
          </div>

          <div class="calc-result-disclaimer">
            Mathematical simulation for financial planning purposes. Tax rules and interest yields subject to government and market regulatory amendments.
          </div>
        </div>

      </div>

      <!-- Annual Growth Schedule Table -->
      <div style="margin-top:42px; background:var(--bg-card); border:1px solid var(--border-soft); border-radius:var(--radius-lg); padding:36px; box-shadow:var(--shadow-sm);">
        <h3 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:8px;">Year-by-Year Financial Schedule</h3>
        <p style="font-size:0.96rem; color:var(--text-secondary); margin-bottom:20px;">Detailed annual accumulation breakdown illustrating balance progression and interest accruals.</p>
        <div class="table-wrapper">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>{table_th1}</th>
                <th>{table_th2}</th>
                <th>{table_th3}</th>
                <th>{table_th4}</th>
                <th>{table_th5}</th>
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
        
        <div style="background:var(--emerald-soft); border:1.5px solid var(--emerald-border); border-radius:var(--radius-md); padding:24px; margin:24px 0;">
          <h3 style="margin:0 0 8px; font-size:1.2rem; color:var(--emerald-dark);">{c['rule_box_title']}</h3>
          <p style="margin:0; font-size:1.02rem; color:var(--text-primary); line-height:1.7;">{c['rule_box_desc']}</p>
        </div>
      </div>

      <!-- Section 2: Worked Real-World Scenarios -->
      <div class="info-section-card">
        <h2>Real-World Indian Scenarios &amp; Case Studies</h2>
        <p>Explore how different capital contributions and compounding horizons impact wealth accumulation across life stages:</p>
        <div class="scenario-grid">
          {personas_html}
        </div>
      </div>

      <!-- Section 3: Mistakes & Pro Tips Checklist -->
      <div class="info-section-card">
        <h2>Best Practices vs Common Pitfalls</h2>
        <p>Follow these disciplined principles to maximize your financial planning efficiency:</p>
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
    // Universal Live Calculator Engine for {c['calc_type']}
    (function() {{
      const type = "{c['calc_type']}";
      
      const in1 = document.getElementById("{c['field1']['id']}");
      const in1Num = document.getElementById("{c['field1']['id']}-num");
      
      const in2 = document.getElementById("{c['field2']['id']}");
      const in2Num = document.getElementById("{c['field2']['id']}-num");
      
      const in3 = document.getElementById("{c['field3']['id']}");
      const in3Num = document.getElementById("{c['field3']['id']}-num");
      
      const in4 = document.getElementById("{'monthly-prepay' if c['calc_type'] == 'emi' else ('step-up-pct' if c['calc_type'] == 'step_up' else 'time-period')}");
      const in4Num = in4 ? document.getElementById(in4.id + "-num") : null;

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
        let totalGain = 0;
        let totalValue = 0;
        let scheduleRows = [];

        if (type === "sip") {{
          const p = v1;
          const r = (v2 / 100) / 12;
          const n = v3 * 12;
          totalInvested = p * n;
          totalValue = p * ((Math.pow(1 + r, n) - 1) / r) * (1 + r);
          totalGain = totalValue - totalInvested;
          
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
          totalGain = totalValue - totalInvested;
          
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
          totalGain = totalValue - totalInvested;
        }} else if (type === "goal") {{
          const target = v1;
          const r = (v2 / 100) / 12;
          const n = v3 * 12;
          const reqP = target / (((Math.pow(1 + r, n) - 1) / r) * (1 + r));
          totalValue = reqP;
          totalInvested = target;
          const estDep = reqP * n;
          totalGain = target - estDep;
          
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
        }} else if (type === "ppf") {{
          const yrDep = v1;
          const rate = v2 / 100;
          const years = v3;
          totalInvested = yrDep * years;
          
          let curBal = 0;
          for (let y = 1; y <= years; y++) {{
            const openBal = curBal;
            const interest = (openBal + yrDep) * rate;
            curBal = openBal + yrDep + interest;
            scheduleRows.push({{ yr: y, open: openBal, dep: yrDep, gain: interest, close: curBal }});
          }}
          totalValue = curBal;
          totalGain = totalValue - totalInvested;
        }} else if (type === "swp") {{
          const corpus = v1;
          const monthlyW = v2;
          const rate = (v3 / 100) / 12;
          const years = v4 || 20;
          totalInvested = corpus;
          
          let curBal = corpus;
          let totalWithdrawn = 0;
          
          for (let y = 1; y <= years; y++) {{
            const openBal = curBal;
            let yrWithdrawn = 0;
            let yrGain = 0;
            
            for (let m = 1; m <= 12; m++) {{
              if (curBal <= 0) break;
              const interest = curBal * rate;
              yrGain += interest;
              const w = Math.min(curBal + interest, monthlyW);
              yrWithdrawn += w;
              totalWithdrawn += w;
              curBal = Math.max(0, curBal + interest - w);
            }}
            scheduleRows.push({{ yr: y, open: openBal, dep: yrWithdrawn, gain: yrGain, close: curBal }});
          }}
          totalGain = totalWithdrawn;
          totalValue = curBal;
        }} else if (type === "emi") {{
          const P = v1;
          const r = (v2 / 100) / 12;
          const n = v3 * 12;
          const extraM = v4 || 0;
          
          const emi = (P * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
          const totalNormalInterest = (emi * n) - P;
          
          let curP = P;
          let totalInterestPaid = 0;
          let totalPaidWithPrepay = 0;
          let monthsCount = 0;
          
          let yrOpen = P;
          let yrPrin = 0;
          let yrInt = 0;
          
          for (let m = 1; m <= n; m++) {{
            if (curP <= 0) break;
            monthsCount++;
            const monthInt = curP * r;
            let monthPrin = (emi - monthInt) + extraM;
            if (monthPrin > curP) monthPrin = curP;
            
            totalInterestPaid += monthInt;
            curP -= monthPrin;
            yrPrin += monthPrin;
            yrInt += monthInt;
            
            if (m % 12 === 0 || curP <= 0 || m === n) {{
              const yrNum = Math.ceil(m / 12);
              scheduleRows.push({{ yr: yrNum, open: yrOpen, dep: yrPrin, gain: yrInt, close: Math.max(0, curP) }});
              yrOpen = curP;
              yrPrin = 0;
              yrInt = 0;
            }}
          }}
          
          const interestSaved = Math.max(0, totalNormalInterest - totalInterestPaid);
          totalInvested = emi;
          totalGain = interestSaved;
          totalValue = totalInterestPaid;
        }} else if (type === "fd") {{
          const p = v1;
          const r = v2 / 100;
          const n = v3;
          totalInvested = p;
          totalValue = p * Math.pow(1 + r / 4, 4 * n);
          totalGain = totalValue - totalInvested;
          
          let curBal = p;
          for (let y = 1; y <= n; y++) {{
            const openBal = curBal;
            curBal = openBal * Math.pow(1 + r / 4, 4);
            const yrGain = curBal - openBal;
            scheduleRows.push({{ yr: y, open: openBal, dep: 0, gain: yrGain, close: curBal }});
          }}
        }} else if (type === "budget") {{
          const income = v1;
          const nPct = v2 / 100;
          const wPct = v3 / 100;
          const sPct = Math.max(0, 1 - nPct - wPct);
          
          totalInvested = income * nPct;
          totalGain = income * wPct;
          totalValue = income * sPct;
          
          for (let m = 1; m <= 12; m++) {{
            scheduleRows.push({{ yr: m, open: income, dep: totalInvested, gain: totalGain, close: totalValue }});
          }}
        }} else if (type === "tax") {{
          const salary = v1;
          const d80c = v2;
          const dOther = v3;
          
          // New Regime (Standard deduction ₹75,000)
          const newTaxable = Math.max(0, salary - 75000);
          let newTax = 0;
          if (newTaxable > 1500000) newTax = 150000 + (newTaxable - 1500000) * 0.30;
          else if (newTaxable > 1200000) newTax = 90000 + (newTaxable - 1200000) * 0.20;
          else if (newTaxable > 900000) newTax = 45000 + (newTaxable - 900000) * 0.15;
          else if (newTaxable > 600000) newTax = 15000 + (newTaxable - 600000) * 0.10;
          else if (newTaxable > 300000) newTax = (newTaxable - 300000) * 0.05;
          if (newTaxable <= 700000) newTax = 0;
          newTax = newTax * 1.04; // Cess
          
          // Old Regime (Standard deduction ₹50,000 + 80C + Others)
          const oldTaxable = Math.max(0, salary - 50000 - d80c - dOther);
          let oldTax = 0;
          if (oldTaxable > 1000000) oldTax = 112500 + (oldTaxable - 1000000) * 0.30;
          else if (oldTaxable > 500000) oldTax = 12500 + (oldTaxable - 500000) * 0.20;
          else if (oldTaxable > 250000) oldTax = (oldTaxable - 250000) * 0.05;
          if (oldTaxable <= 500000) oldTax = 0;
          oldTax = oldTax * 1.04;
          
          totalInvested = newTax;
          totalGain = oldTax;
          totalValue = Math.abs(oldTax - newTax);
        }}

        // Update UI
        document.getElementById("res-invested").textContent = formatINR(totalInvested);
        document.getElementById("res-returns").textContent = formatINR(totalGain);
        document.getElementById("res-total").textContent = formatINR(totalValue);

        // Update Donut Visual
        const sumForDonut = totalInvested + totalGain;
        let gainPct = sumForDonut > 0 ? Math.round((totalGain / sumForDonut) * 100) : 50;
        gainPct = Math.max(0, Math.min(100, gainPct));
        const seg = document.getElementById("donut-segment");
        if (seg) {{
          seg.setAttribute("stroke-dasharray", `${{gainPct}} ${{100 - gainPct}}`);
        }}
        const legG = document.getElementById("donut-leg-gain");
        const legI = document.getElementById("donut-leg-inv");
        if (legG && legI) {{
          if (type === "swp") {{
            legG.textContent = `Withdrawn: ${{gainPct}}%`;
            legI.textContent = `Corpus: ${{100 - gainPct}}%`;
          }} else if (type === "emi") {{
            legG.textContent = `Saved: ${{gainPct}}%`;
            legI.textContent = `Interest: ${{100 - gainPct}}%`;
          }} else if (type === "budget") {{
            legG.textContent = `Wants: ${{Math.round((totalGain/v1)*100)}}%`;
            legI.textContent = `Needs: ${{Math.round((totalInvested/v1)*100)}}%`;
          }} else {{
            legG.textContent = `Returns: ${{gainPct}}%`;
            legI.textContent = `Principal: ${{100 - gainPct}}%`;
          }}
        }}

        // Populate Table
        const tbody = document.getElementById("schedule-tbody");
        if (tbody) {{
          tbody.innerHTML = scheduleRows.map(r => `
            <tr>
              <td>Year ${{r.yr}}</td>
              <td>${{formatINR(r.open)}}</td>
              <td>${{formatINR(r.dep)}}</td>
              <td style="color:#059669; font-weight:600;">+${{formatINR(r.gain)}}</td>
              <td style="font-weight:700; color:var(--text-primary);">${{formatINR(r.close)}}</td>
            </tr>
          `).join('');
        }}
      }}

      // Initialize
      calculate();
    }})();
  </script>
</body>
</html>"""

        filepath = os.path.join(SITE_DIR, c["slug"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"Generated Calculator: {c['slug']}")

if __name__ == "__main__":
    build_all_calculators()
