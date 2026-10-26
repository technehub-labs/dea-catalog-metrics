# dea:metric-rule-of-40

Candidate Performance Metric record for **Rule of 40** (R40) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rule-of-40`
- **Name:** Rule of 40
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** R40

## 2. Definition

Within Startup & Venture-Backed Business, Rule of 40 (R40) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Revenue Growth Percent + Profit Margin Percent, measured in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The Rule of 40, popularized in venture practice (often credited to Brad Feld), says a healthy SaaS company's revenue growth rate percentage plus profit margin percentage should exceed 40. A company growing 30% needs roughly 10% margin; a company growing 50% can lose 10% and still qualify. It is a screening heuristic, not a valuation formula - it deliberately trades off growth and profitability so investors can compare capital-efficient growers with profitable slow-coaches. Note the gaming risks: the choice of growth (new vs total ARR) and profit (EBITDA vs FCF) definitions materially moves the number, so compare like definitions.

## Formula

```
Revenue Growth Percent + Profit Margin Percent
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** Venture capital practice (popularized by Brad Feld)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2444 (batch 6)
