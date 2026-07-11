(function () {
  "use strict";

  /* ============ Helpers ============ */
  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => Array.from((ctx || document).querySelectorAll(sel));

  const inrFormat = (num, decimals = 0) => {
    const n = Math.round(num * Math.pow(10, decimals)) / Math.pow(10, decimals);
    return "₹" + n.toLocaleString("en-IN", { maximumFractionDigits: decimals, minimumFractionDigits: decimals });
  };

  const parseNum = (str) => {
    const n = parseFloat(String(str).replace(/[^0-9.]/g, ""));
    return isNaN(n) ? 0 : n;
  };

  const clampVal = (v, min, max) => Math.min(max, Math.max(min, v));

  /* ============ Number Counter Animation ============ */
  const animatedValues = {};
  
  function animateValue(elementId, endVal, prefix = "₹", isInteger = true) {
    const el = $(`#${elementId}`);
    if (!el) return;

    const startVal = animatedValues[elementId] || 0;
    animatedValues[elementId] = endVal;

    if (startVal === endVal) {
      el.textContent = prefix + endVal.toLocaleString("en-IN", { maximumFractionDigits: isInteger ? 0 : 2 });
      return;
    }

    const duration = 250; // ms
    const startTime = performance.now();

    function update(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out quad
      const easeProgress = progress * (2 - progress);
      const current = startVal + (endVal - startVal) * easeProgress;

      el.textContent = prefix + Math.round(current).toLocaleString("en-IN", { maximumFractionDigits: isInteger ? 0 : 2 });

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = prefix + endVal.toLocaleString("en-IN", { maximumFractionDigits: isInteger ? 0 : 2 });
      }
    }
    requestAnimationFrame(update);
  }

  /* ============ Platform State ============ */
  let activeCalc = null; // 'sip', 'lumpsum', 'step-up', 'goal'
  const state = {
    sip: { monthly: 10000, rate: 12, years: 10 },
    lumpsum: { amount: 100000, rate: 12, years: 10 },
    stepup: { monthly: 10000, stepupPct: 10, rate: 12, years: 10 },
    goal: { target: 1000000, rate: 12, years: 10 }
  };

  let yearlyData = [];
  let monthlyData = [];

  // Determine active calculator from page elements
  if ($("#calc-type-sip")) activeCalc = "sip";
  else if ($("#calc-type-lumpsum")) activeCalc = "lumpsum";
  else if ($("#calc-type-stepup")) activeCalc = "stepup";
  else if ($("#calc-type-goal")) activeCalc = "goal";

  if (!activeCalc) return; // Exit if no calculator on current page

  const els = {
    // Range sliders
    monthlyRange: $("#monthlyInvestmentRange"),
    amountRange: $("#lumpsumAmountRange"),
    stepupRange: $("#stepupPctRange"),
    rateRange: $("#expectedReturnRange"),
    yearsRange: $("#investmentPeriodRange"),
    targetRange: $("#targetWealthRange"),

    // Text inputs
    monthlyInput: $("#monthlyInvestment"),
    amountInput: $("#lumpsumAmount"),
    stepupInput: $("#stepupPct"),
    rateInput: $("#expectedReturn"),
    yearsInput: $("#investmentPeriod"),
    targetInput: $("#targetWealth"),

    // Display outputs
    totalInvestment: $("#totalInvestment"),
    estimatedReturns: $("#estimatedReturns"),
    totalWealth: $("#totalWealth"),
    reqMonthlySip: $("#reqMonthlySip"), // Goal calculator only
    
    // UI elements
    canvas: $("#growthChart"),
    yearlyTable: $("#yearlyTable tbody"),
    monthlyTable: $("#monthlyTable tbody"),
    yearSelect: $("#monthlyYearSelect"),
    copyBtn: $("#btn-copy"),
    shareBtn: $("#btn-share"),
    printBtn: $("#btn-print")
  };

  /* ============ Mathematical Projections ============ */
  
  // Standard SIP Future Value
  function calculateSipFutureValue(P, annualRate, months) {
    const i = annualRate / 1200;
    if (i === 0) return P * months;
    return P * ((Math.pow(1 + i, months) - 1) / i) * (1 + i);
  }

  // Standard Lumpsum Future Value (compounded annually)
  function calculateLumpsumFutureValue(P, annualRate, years) {
    return P * Math.pow(1 + annualRate / 100, years);
  }

  // Monthly breakdown calculator for Lumpsum
  function calculateLumpsumValueAtMonth(P, annualRate, months) {
    const i = annualRate / 1200;
    return P * Math.pow(1 + i, months);
  }

  function computeSIPSchedule() {
    const P = state.sip.monthly;
    const rate = state.sip.rate;
    const years = state.sip.years;
    const totalMonths = years * 12;

    monthlyData = [];
    let cumulativeInvested = 0;
    for (let m = 1; m <= totalMonths; m++) {
      cumulativeInvested += P;
      const val = calculateSipFutureValue(P, rate, m);
      monthlyData.push({ month: m, instalment: P, cumulativeInvested, value: val });
    }

    yearlyData = [];
    for (let y = 1; y <= years; y++) {
      const monthsElapsed = y * 12;
      const totalInvested = P * monthsElapsed;
      const val = calculateSipFutureValue(P, rate, monthsElapsed);
      yearlyData.push({
        year: y,
        investedThisYear: P * 12,
        totalInvested,
        yearEndValue: val,
        wealthGained: val - totalInvested
      });
    }
  }

  function computeLumpsumSchedule() {
    const P = state.lumpsum.amount;
    const rate = state.lumpsum.rate;
    const years = state.lumpsum.years;
    const totalMonths = years * 12;

    monthlyData = [];
    for (let m = 1; m <= totalMonths; m++) {
      const val = calculateLumpsumValueAtMonth(P, rate, m);
      monthlyData.push({ month: m, instalment: m === 1 ? P : 0, cumulativeInvested: P, value: val });
    }

    yearlyData = [];
    for (let y = 1; y <= years; y++) {
      const totalInvested = P;
      const val = calculateLumpsumFutureValue(P, rate, y);
      yearlyData.push({
        year: y,
        investedThisYear: y === 1 ? P : 0,
        totalInvested,
        yearEndValue: val,
        wealthGained: val - totalInvested
      });
    }
  }

  function computeStepupSchedule() {
    const P = state.stepup.monthly;
    const stepPct = state.stepup.stepupPct;
    const rate = state.stepup.rate;
    const years = state.stepup.years;
    const totalMonths = years * 12;
    const i = rate / 1200;

    monthlyData = [];
    yearlyData = [];

    let currentMonthlyInvest = P;
    let cumulativeInvested = 0;
    let cumulativeValue = 0;
    let yearInvestedAccumulator = 0;

    for (let m = 1; m <= totalMonths; m++) {
      cumulativeInvested += currentMonthlyInvest;
      yearInvestedAccumulator += currentMonthlyInvest;

      // Compound step
      cumulativeValue = (cumulativeValue + currentMonthlyInvest) * (1 + i);
      
      monthlyData.push({
        month: m,
        instalment: currentMonthlyInvest,
        cumulativeInvested,
        value: cumulativeValue
      });

      // Year boundary
      if (m % 12 === 0) {
        const yearNum = m / 12;
        yearlyData.push({
          year: yearNum,
          investedThisYear: yearInvestedAccumulator,
          totalInvested: cumulativeInvested,
          yearEndValue: cumulativeValue,
          wealthGained: cumulativeValue - cumulativeInvested
        });

        // Step up monthly instalment for next year
        currentMonthlyInvest = currentMonthlyInvest * (1 + stepPct / 100);
        yearInvestedAccumulator = 0;
      }
    }
  }

  function computeGoalSchedule() {
    const target = state.goal.target;
    const rate = state.goal.rate;
    const years = state.goal.years;
    const totalMonths = years * 12;

    // Work backwards for required monthly SIP (compounded monthly)
    const i = rate / 1200;
    let reqSip = 0;
    if (i === 0) {
      reqSip = target / totalMonths;
    } else {
      reqSip = target / (((Math.pow(1 + i, totalMonths) - 1) / i) * (1 + i));
    }

    // Keep state values sync
    state.goal.calculatedSip = reqSip;

    monthlyData = [];
    let cumulativeInvested = 0;
    for (let m = 1; m <= totalMonths; m++) {
      cumulativeInvested += reqSip;
      const val = calculateSipFutureValue(reqSip, rate, m);
      monthlyData.push({ month: m, instalment: reqSip, cumulativeInvested, value: val });
    }

    yearlyData = [];
    for (let y = 1; y <= years; y++) {
      const monthsElapsed = y * 12;
      const totalInvested = reqSip * monthsElapsed;
      const val = calculateSipFutureValue(reqSip, rate, monthsElapsed);
      yearlyData.push({
        year: y,
        investedThisYear: reqSip * 12,
        totalInvested,
        yearEndValue: val,
        wealthGained: val - totalInvested
      });
    }
  }

  function recalculateData() {
    if (activeCalc === "sip") computeSIPSchedule();
    else if (activeCalc === "lumpsum") computeLumpsumSchedule();
    else if (activeCalc === "stepup") computeStepupSchedule();
    else if (activeCalc === "goal") computeGoalSchedule();
  }

  /* ============ Summary Section Update ============ */
  function updateSummaryBox() {
    let investedVal = 0;
    let finalWealthVal = 0;

    if (activeCalc === "sip") {
      investedVal = state.sip.monthly * state.sip.years * 12;
      finalWealthVal = calculateSipFutureValue(state.sip.monthly, state.sip.rate, state.sip.years * 12);
    } else if (activeCalc === "lumpsum") {
      investedVal = state.lumpsum.amount;
      finalWealthVal = calculateLumpsumFutureValue(state.lumpsum.amount, state.lumpsum.rate, state.lumpsum.years);
    } else if (activeCalc === "stepup") {
      // Pull from pre-computed yearly schedule
      const finalYear = yearlyData[yearlyData.length - 1];
      investedVal = finalYear ? finalYear.totalInvested : 0;
      finalWealthVal = finalYear ? finalYear.yearEndValue : 0;
    } else if (activeCalc === "goal") {
      finalWealthVal = state.goal.target;
      const reqSip = state.goal.calculatedSip || 0;
      investedVal = reqSip * state.goal.years * 12;

      // Animate the required Monthly SIP
      animateValue("reqMonthlySip", Math.round(reqSip));
    }

    const returnsVal = Math.max(0, finalWealthVal - investedVal);

    animateValue("totalInvestment", Math.round(investedVal));
    animateValue("estimatedReturns", Math.round(returnsVal));
    animateValue("totalWealth", Math.round(finalWealthVal));
  }

  /* ============ High-DPI Canvas Chart Drawing ============ */
  function drawGrowthChart() {
    const canvas = els.canvas;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    const w = Math.max(rect.width, 280);
    const h = 220;

    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.height = h + "px";
    
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    if (yearlyData.length === 0) return;

    // Theme responsive colors
    const isDark = document.documentElement.getAttribute("data-theme") !== "light";
    const gridColor = isDark ? "rgba(155, 176, 167, 0.08)" : "rgba(15, 40, 30, 0.06)";
    const textColor = isDark ? "#5D7269" : "#728A80";

    const padL = 10, padR = 10, padT = 16, padB = 22;
    const chartW = w - padL - padR;
    const chartH = h - padT - padB;
    
    const maxVal = Math.max(...yearlyData.map(r => r.yearEndValue));
    const count = yearlyData.length;

    const xPos = (idx) => padL + (count === 1 ? chartW / 2 : (idx / (count - 1)) * chartW);
    const yPos = (val) => padT + chartH - (val / (maxVal || 1)) * chartH;

    // Gridlines drawing
    ctx.strokeStyle = gridColor;
    ctx.lineWidth = 1;
    for (let g = 0; g <= 4; g++) {
      const gy = padT + (chartH / 4) * g;
      ctx.beginPath();
      ctx.moveTo(padL, gy);
      ctx.lineTo(w - padR, gy);
      ctx.stroke();
    }

    // Wealth gained filled area gradient
    const emeraldGrad = ctx.createLinearGradient(0, padT, 0, padT + chartH);
    if (isDark) {
      emeraldGrad.addColorStop(0, "rgba(52, 211, 153, 0.38)");
      emeraldGrad.addColorStop(1, "rgba(16, 185, 129, 0.01)");
    } else {
      emeraldGrad.addColorStop(0, "rgba(16, 185, 129, 0.25)");
      emeraldGrad.addColorStop(1, "rgba(5, 150, 105, 0.01)");
    }

    ctx.beginPath();
    yearlyData.forEach((r, idx) => {
      const x = xPos(idx);
      const y = yPos(r.yearEndValue);
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.lineTo(xPos(count - 1), padT + chartH);
    ctx.lineTo(xPos(0), padT + chartH);
    ctx.closePath();
    ctx.fillStyle = emeraldGrad;
    ctx.fill();

    // Invested principal filled area gradient
    const steelGrad = ctx.createLinearGradient(0, padT, 0, padT + chartH);
    if (isDark) {
      steelGrad.addColorStop(0, "rgba(96, 165, 250, 0.28)");
      steelGrad.addColorStop(1, "rgba(96, 165, 250, 0.01)");
    } else {
      steelGrad.addColorStop(0, "rgba(37, 99, 235, 0.18)");
      steelGrad.addColorStop(1, "rgba(37, 99, 235, 0.01)");
    }

    ctx.beginPath();
    yearlyData.forEach((r, idx) => {
      const x = xPos(idx);
      const y = yPos(r.totalInvested);
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.lineTo(xPos(count - 1), padT + chartH);
    ctx.lineTo(xPos(0), padT + chartH);
    ctx.closePath();
    ctx.fillStyle = steelGrad;
    ctx.fill();

    // Wealth outer curve stroke line
    ctx.beginPath();
    yearlyData.forEach((r, idx) => {
      const x = xPos(idx);
      const y = yPos(r.yearEndValue);
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.strokeStyle = isDark ? "#34D399" : "#059669";
    ctx.lineWidth = 2.5;
    ctx.lineJoin = "round";
    ctx.stroke();

    // Invested outer curve stroke line
    ctx.beginPath();
    yearlyData.forEach((r, idx) => {
      const x = xPos(idx);
      const y = yPos(r.totalInvested);
      if (idx === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.strokeStyle = isDark ? "#60A5FA" : "#2563EB";
    ctx.lineWidth = 1.8;
    ctx.setLineDash([4, 3]);
    ctx.stroke();
    ctx.setLineDash([]); // clear dash

    // Endpoint golden dot highlighter
    const lastIdx = count - 1;
    const dotX = xPos(lastIdx);
    const dotY = yPos(yearlyData[lastIdx].yearEndValue);
    ctx.beginPath();
    ctx.arc(dotX, dotY, 5, 0, Math.PI * 2);
    ctx.fillStyle = isDark ? "#FBBF24" : "#D97706";
    ctx.fill();
    ctx.strokeStyle = isDark ? "#050B09" : "#FFFFFF";
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  /* ============ Tabular Schedule Binding ============ */
  function renderYearlyBreakdownTable() {
    if (!els.yearlyTable) return;
    
    els.yearlyTable.innerHTML = yearlyData.map(r => `
      <tr>
        <td>Year ${r.year}</td>
        <td>${inrFormat(r.investedThisYear)}</td>
        <td>${inrFormat(r.totalInvested)}</td>
        <td>${inrFormat(r.yearEndValue)}</td>
        <td>${inrFormat(r.wealthGained)}</td>
      </tr>
    `).join("");
  }

  function populateYearSelectOptions() {
    if (!els.yearSelect) return;
    
    const prevSelectVal = els.yearSelect.value ? parseInt(els.yearSelect.value, 10) : 1;
    const currentYearsCount = activeCalc === "sip" ? state.sip.years :
                             activeCalc === "lumpsum" ? state.lumpsum.years :
                             activeCalc === "stepup" ? state.stepup.years :
                             state.goal.years;

    els.yearSelect.innerHTML = yearlyData.map(r => `
      <option value="${r.year}">Year ${r.year}</option>
    `).join("");

    els.yearSelect.value = Math.min(prevSelectVal, currentYearsCount) || 1;
  }

  function renderMonthlyBreakdownTable() {
    if (!els.monthlyTable || !els.yearSelect) return;

    const selectYear = parseInt(els.yearSelect.value, 10) || 1;
    const startM = (selectYear - 1) * 12 + 1;
    const endM = selectYear * 12;

    const targetRows = monthlyData.filter(r => r.month >= startM && r.month <= endM);

    els.monthlyTable.innerHTML = targetRows.map(r => {
      const displayMonthIdx = ((r.month - 1) % 12) + 1;
      return `
        <tr>
          <td>Month ${displayMonthIdx}</td>
          <td>${inrFormat(r.instalment)}</td>
          <td>${inrFormat(r.cumulativeInvested)}</td>
          <td>${inrFormat(r.value)}</td>
        </tr>
      `;
    }).join("");
  }

  /* ============ Execution & Sync Engine ============ */
  function runUpdateCycle() {
    recalculateData();
    updateSummaryBox();
    drawGrowthChart();
    renderYearlyBreakdownTable();
    populateYearSelectOptions();
    renderMonthlyBreakdownTable();
  }

  function syncInputs(slider, text, min, max, parser, formatter) {
    if (!slider || !text) return;

    // Slide updates text field
    slider.addEventListener("input", () => {
      text.value = formatter ? formatter(slider.value) : slider.value;
      readInputsFromDOM();
      runUpdateCycle();
    });

    // Manual typing validation
    text.addEventListener("input", () => {
      const value = parser(text.value);
      const clamp = clampVal(value, min, max);
      slider.value = clamp;
    });

    // Blur formatting
    text.addEventListener("blur", () => {
      const value = parser(text.value);
      const clamp = clampVal(value, min, max);
      text.value = formatter ? formatter(clamp) : clamp;
      slider.value = clamp;
      readInputsFromDOM();
      runUpdateCycle();
    });

    // Submit on enter key
    text.addEventListener("keydown", (e) => {
      if (e.key === "Enter") text.blur();
    });
  }

  function readInputsFromDOM() {
    if (activeCalc === "sip") {
      state.sip.monthly = clampVal(parseNum(els.monthlyInput.value), 500, 200000);
      state.sip.rate = clampVal(parseNum(els.rateInput.value), 1, 30);
      state.sip.years = clampVal(parseInt(els.yearsInput.value, 10) || 1, 1, 40);
    } else if (activeCalc === "lumpsum") {
      state.lumpsum.amount = clampVal(parseNum(els.amountInput.value), 1000, 10000000);
      state.lumpsum.rate = clampVal(parseNum(els.rateInput.value), 1, 30);
      state.lumpsum.years = clampVal(parseInt(els.yearsInput.value, 10) || 1, 1, 40);
    } else if (activeCalc === "stepup") {
      state.stepup.monthly = clampVal(parseNum(els.monthlyInput.value), 500, 200000);
      state.stepup.stepupPct = clampVal(parseNum(els.stepupInput.value), 1, 100);
      state.stepup.rate = clampVal(parseNum(els.rateInput.value), 1, 30);
      state.stepup.years = clampVal(parseInt(els.yearsInput.value, 10) || 1, 1, 40);
    } else if (activeCalc === "goal") {
      state.goal.target = clampVal(parseNum(els.targetInput.value), 10000, 100000000);
      state.goal.rate = clampVal(parseNum(els.rateInput.value), 1, 30);
      state.goal.years = clampVal(parseInt(els.yearsInput.value, 10) || 1, 1, 40);
    }
  }

  // Setup input listeners per active page
  if (activeCalc === "sip") {
    syncInputs(els.monthlyRange, els.monthlyInput, 500, 200000, parseNum, (v) => parseInt(v, 10).toLocaleString("en-IN"));
    syncInputs(els.rateRange, els.rateInput, 1, 30, parseNum, (v) => v);
    syncInputs(els.yearsRange, els.yearsInput, 1, 40, (v) => parseInt(v, 10) || 1, (v) => v);
  } else if (activeCalc === "lumpsum") {
    syncInputs(els.amountRange, els.amountInput, 1000, 10000000, parseNum, (v) => parseInt(v, 10).toLocaleString("en-IN"));
    syncInputs(els.rateRange, els.rateInput, 1, 30, parseNum, (v) => v);
    syncInputs(els.yearsRange, els.yearsInput, 1, 40, (v) => parseInt(v, 10) || 1, (v) => v);
  } else if (activeCalc === "stepup") {
    syncInputs(els.monthlyRange, els.monthlyInput, 500, 200000, parseNum, (v) => parseInt(v, 10).toLocaleString("en-IN"));
    syncInputs(els.stepupRange, els.stepupInput, 1, 100, parseNum, (v) => v);
    syncInputs(els.rateRange, els.rateInput, 1, 30, parseNum, (v) => v);
    syncInputs(els.yearsRange, els.yearsInput, 1, 40, (v) => parseInt(v, 10) || 1, (v) => v);
  } else if (activeCalc === "goal") {
    syncInputs(els.targetRange, els.targetInput, 10000, 100000000, parseNum, (v) => parseInt(v, 10).toLocaleString("en-IN"));
    syncInputs(els.rateRange, els.rateInput, 1, 30, parseNum, (v) => v);
    syncInputs(els.yearsRange, els.yearsInput, 1, 40, (v) => parseInt(v, 10) || 1, (v) => v);
  }

  // Monthly table selection dropdown trigger
  if (els.yearSelect) {
    els.yearSelect.addEventListener("change", renderMonthlyBreakdownTable);
  }

  // Progressive Slider Fill (Chrome/Safari — no native ::-moz-range-progress)
  function updateSliderFill(slider) {
    if (!slider) return;
    const min = parseFloat(slider.min) || 0;
    const max = parseFloat(slider.max) || 100;
    const val = parseFloat(slider.value) || 0;
    const pct = ((val - min) / (max - min)) * 100;

    let trackColor;
    if (slider.classList.contains("slider-emerald")) {
      trackColor = getComputedStyle(document.documentElement).getPropertyValue("--emerald").trim() || "#10B981";
    } else if (slider.classList.contains("slider-gold")) {
      trackColor = getComputedStyle(document.documentElement).getPropertyValue("--gold").trim() || "#F59E0B";
    } else if (slider.classList.contains("slider-steel")) {
      trackColor = getComputedStyle(document.documentElement).getPropertyValue("--steel").trim() || "#60A5FA";
    } else {
      trackColor = getComputedStyle(document.documentElement).getPropertyValue("--emerald").trim() || "#10B981";
    }

    slider.style.background = `linear-gradient(to right, ${trackColor} 0%, ${trackColor} ${pct}%, var(--bg-elevated) ${pct}%, var(--bg-elevated) 100%)`;
  }

  // Initialize fill on all sliders
  $$(".slider").forEach(function (s) {
    updateSliderFill(s);
    s.addEventListener("input", function () { updateSliderFill(s); });
  });

  // Re-fill on theme change
  window.addEventListener("themechange", function () {
    $$(".slider").forEach(updateSliderFill);
  });

  // Responsive redraw on resize
  window.addEventListener("resize", (() => {
    let timeoutId;
    return () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(drawGrowthChart, 120);
    };
  })());

  // Listen to custom theme switch event
  window.addEventListener("themechange", () => {
    drawGrowthChart();
  });

  /* ============ Copy Results Share and Printing ============ */
  function constructCopyShareString() {
    const formattedDate = new Date().toLocaleDateString("en-IN", { year: "numeric", month: "short", day: "numeric" });
    
    let summaryText = `-----------------------------------------\n` +
                      `CALCULATORSHIP REPORT (${formattedDate})\n` +
                      `-----------------------------------------\n`;

    if (activeCalc === "sip") {
      summaryText += `Systematic Investment Plan (SIP) Projection\n\n` +
                     `Monthly instalment: ${inrFormat(state.sip.monthly)}\n` +
                     `Expected annual return: ${state.sip.rate}%\n` +
                     `Investment duration: ${state.sip.years} years\n`;
    } else if (activeCalc === "lumpsum") {
      summaryText += `Lumpsum Investment Projection\n\n` +
                     `One-time investment: ${inrFormat(state.lumpsum.amount)}\n` +
                     `Expected annual return: ${state.lumpsum.rate}%\n` +
                     `Investment duration: ${state.lumpsum.years} years\n`;
    } else if (activeCalc === "stepup") {
      summaryText += `Step-Up SIP Projection\n\n` +
                     `Initial monthly instalment: ${inrFormat(state.stepup.monthly)}\n` +
                     `Annual step-up increment: ${state.stepup.stepupPct}%\n` +
                     `Expected annual return: ${state.stepup.rate}%\n` +
                     `Investment duration: ${state.stepup.years} years\n`;
    } else if (activeCalc === "goal") {
      summaryText += `SIP Goal Planner\n\n` +
                     `Target financial goal: ${inrFormat(state.goal.target)}\n` +
                     `Expected annual return: ${state.goal.rate}%\n` +
                     `Investment duration: ${state.goal.years} years\n` +
                     `Required monthly SIP: ${inrFormat(state.goal.calculatedSip || 0)}\n`;
    }

    const totalInvested = parseNum(els.totalInvestment.textContent);
    const estReturns = parseNum(els.estimatedReturns.textContent);
    const finalWealth = parseNum(els.totalWealth.textContent);

    summaryText += `-----------------------------------------\n` +
                   `Total Investment  : ${inrFormat(totalInvested)}\n` +
                   `Estimated Returns : ${inrFormat(estReturns)}\n` +
                   `Total Wealth      : ${inrFormat(finalWealth)}\n` +
                   `-----------------------------------------\n` +
                   `Calculate yours at: ${window.location.origin + window.location.pathname}\n`;

    return summaryText;
  }

  function displayFeedbackMessage(msg) {
    const toast = $("#copy-toast");
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add("is-visible");
    clearTimeout(displayFeedbackMessage._t);
    displayFeedbackMessage._t = setTimeout(() => toast.classList.remove("is-visible"), 2500);
  }

  if (els.copyBtn) {
    els.copyBtn.addEventListener("click", async () => {
      const summaryString = constructCopyShareString();
      try {
        await navigator.clipboard.writeText(summaryString);
        displayFeedbackMessage("Calculations copied to clipboard.");
      } catch (err) {
        displayFeedbackMessage("Clipboard write blocked. Select values manually.");
      }
    });
  }

  if (els.shareBtn) {
    els.shareBtn.addEventListener("click", async () => {
      const summaryString = constructCopyShareString();
      if (navigator.share) {
        try {
          await navigator.share({
            title: "Calculatorship Calculation Report",
            text: summaryString,
            url: window.location.href
          });
        } catch (err) {
          // Cancelled
        }
      } else {
        try {
          await navigator.clipboard.writeText(summaryString);
          displayFeedbackMessage("Sharing not supported. Copied to clipboard instead.");
        } catch (err) {
          displayFeedbackMessage("Sharing interface is unavailable.");
        }
      }
    });
  }

  if (els.printBtn) {
    els.printBtn.addEventListener("click", () => {
      window.print();
    });
  }

  /* ============ Yearly/Monthly Table Tabs ============ */
  (function initBreakdownTabs() {
    const yearlyTabBtn = $("#tab-yearly");
    const monthlyTabBtn = $("#tab-monthly");
    const yearlyPanel = $("#panel-yearly");
    const monthlyPanel = $("#panel-monthly");

    if (!yearlyTabBtn || !monthlyTabBtn) return;

    function activateTab(tab) {
      const isYearly = tab === "yearly";
      
      yearlyTabBtn.classList.toggle("is-active", isYearly);
      monthlyTabBtn.classList.toggle("is-active", !isYearly);
      
      yearlyTabBtn.setAttribute("aria-selected", isYearly ? "true" : "false");
      monthlyTabBtn.setAttribute("aria-selected", !isYearly ? "true" : "false");
      
      if (yearlyPanel) yearlyPanel.hidden = !isYearly;
      if (monthlyPanel) monthlyPanel.hidden = isYearly;
    }

    yearlyTabBtn.addEventListener("click", () => activateTab("yearly"));
    monthlyTabBtn.addEventListener("click", () => activateTab("monthly"));
  })();

  /* ============ Initialization ============ */
  readInputsFromDOM();
  runUpdateCycle();

})();
