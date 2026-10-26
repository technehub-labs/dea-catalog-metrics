# dea:metric-capital-allocation-fulfilment-rate

Candidate Performance Metric record for **Capital Allocation Fulfilment Rate** (CAFR-BSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capital-allocation-fulfilment-rate`
- **Name:** Capital Allocation Fulfilment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAFR-BSC

## 2. Definition

Capital Allocation Fulfilment Rate (CAFR-BSC) captures conformance to standards, plans, or obligations for organizations tracking balanced scorecard - financial perspective. It is computed as Strategic Capital Deployed per Plan / Planned, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether approved capital allocations were actually deployed as intended. Quiet reallocation away from strategy-starved investments is a common governance failure. Fulfilment measured at commitment rather than spend reveals little. Read with capital allocation ROI variance and strategic initiative funding fulfilment.

## Formula

```
CAFR-BSC = Strategic Capital Deployed per Plan / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3059 (batch 7)
