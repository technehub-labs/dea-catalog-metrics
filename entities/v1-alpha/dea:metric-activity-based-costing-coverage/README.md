# dea:metric-activity-based-costing-coverage

Candidate Performance Metric record for **Activity-Based Costing Coverage** (ABCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-activity-based-costing-coverage`
- **Name:** Activity-Based Costing Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ABCC

## 2. Definition

A Product Costing & Margin Management indicator, Activity-Based Costing Coverage (ABCC) quantifies capability maturity or development. It is computed as Products Costed via ABC Model / Products Costed, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of cost base allocated through activity-based models. It matters because poor allocation distorts product and customer profitability decisions. Coverage can be broad but shallow, with key activities still spread on volume. Read with Segment Profitability Coverage and allocation accuracy reviews to confirm ABC depth matches claimed coverage.

## Formula

```
ABCC = Products Costed via ABC Model / Products Costed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1241 (batch 4)
