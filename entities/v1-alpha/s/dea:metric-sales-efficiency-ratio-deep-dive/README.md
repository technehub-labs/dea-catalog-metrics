# dea:metric-sales-efficiency-ratio-deep-dive

Candidate Performance Metric record for **Sales Efficiency Ratio (Deep Dive)** (SERD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sales-efficiency-ratio-deep-dive`
- **Name:** Sales Efficiency Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SERD

## 2. Definition

Sales Efficiency Ratio (Deep Dive) (SERD) addresses how efficiently resources are converted into outputs and is a fixture of unit economics & growth (deep dive) reporting. Its calculation is New ARR / Total Sales and Marketing Cost, measured in ratio (x:1 or x). It originates from and is most used in Software practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures new revenue generated per unit of sales and marketing spend. It is the capital-efficiency check on go-to-market investment. Efficiency on bookings rather than realized revenue front-loads hope. Read with CAC payback period (Unit Economics) and net new ARR per sales rep.

## Formula

```
SERD = New ARR / Total Sales and Marketing Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4174 (batch 9)
