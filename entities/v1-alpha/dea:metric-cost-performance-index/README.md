# dea:metric-cost-performance-index

Candidate Performance Metric record for **Cost Performance Index** (CPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-performance-index`
- **Name:** Cost Performance Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPI

## 2. Definition

A Project Management indicator, Cost Performance Index (CPI) quantifies conformance to standards, plans, or obligations. The formula is Earned Value / Actual Cost - reported in ratio (x:1 or x). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

CPI, Earned Value Management's cost gauge, is earned value divided by actual cost - budgeted worth of work performed per dollar actually spent. At 1.0 you get a dollar of scope per dollar spent; at 0.8 you are paying 1.25 dollars per dollar of progress, and EVM's standard forecasting uses cumulative CPI as the efficiency the remainder will likely sustain. CPI is remarkably stable late in projects, which is why it anchors the classic over-run forecasts; it says nothing about schedule, so pair it with SPI.

## Formula

```
Earned Value / Actual Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Earned Value Management (DoD/NASA tradition)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 349 (batch 1)
