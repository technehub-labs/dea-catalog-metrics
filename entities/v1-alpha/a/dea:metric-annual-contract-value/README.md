# dea:metric-annual-contract-value

Candidate Performance Metric record for **Annual Contract Value** (ACV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-annual-contract-value`
- **Name:** Annual Contract Value
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACV

## 2. Definition

Annual Contract Value (ACV) measures the economic value created or preserved in the Sales domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Contract Value / Contract Years; the result is stated in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The annualized value of a customer contract - the standard unit of B2B sales economics, because it normalizes deals of different lengths onto a yearly footing and lets bookings, backlog, and backlog-to-revenue conversion be compared like for like. Strategic use is multi-layered: ACV by segment reveals whether the sales motion targets elephants or long-tail, average ACV trend shows whether pricing power is real, and new-ACV versus churned-ACV is the cleanest one-line growth decomposition a subscription company can produce. The definitional wedge is what gets annualized - multi-year ramp deals, usage floors, and professional services all have house conventions, so cross-company ACV comparisons need the fine print before the comparison means anything.

## Formula

```
ACV = Total Contract Value / Contract Years
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 98 (batch 1)
