# dea:metric-free-cash-flow

Candidate Performance Metric record for **Free Cash Flow** (FCF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-free-cash-flow`
- **Name:** Free Cash Flow
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCF

## 2. Definition

Free Cash Flow (FCF) captures the economic value created or preserved for organizations tracking finance & accounting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Operating Cash Flow - Capital Expenditure - reported in currency value. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Operating cash flow minus capital expenditure - the cash actually available to investors after the business has maintained and grown itself. It is the ground truth of valuation: profits are an opinion, this is cash, and every DCF is at heart a projection of this line. Strategic readers compare it against net income, where a persistent gap signals accruals-driven earnings quality, and against the capital-expenditure split between maintenance and growth, since cutting growth capex can manufacture FCF for a few quarters while quietly starving the future. Its weakness is volatility - working capital swings and lumpy projects make single years unrepresentative, so annual averages and normalized capex are the honest way to read it.

## Formula

```
FCF = Operating Cash Flow - Capital Expenditure
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 21 (batch 1)
