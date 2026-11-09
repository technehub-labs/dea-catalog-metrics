# dea:metric-quota-attainment

Candidate Performance Metric record for **Quota Attainment** (QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quota-attainment`
- **Name:** Quota Attainment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** QA

## 2. Definition

A Sales indicator, Quota Attainment (QA) quantifies conformance to standards, plans, or obligations. The formula is Actual Sales / Quota - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the percentage of assigned sales quota each rep or team achieves. It matters as the basic execution signal for whether capacity and targets are calibrated to market reality. Gaming risk includes sandbagged quotas, end-of-quarter discount blowouts to hit thresholds, and deal timing pulled between periods. Read with Win Rate and Sales Cycle Length to judge whether attainment reflects healthy selling or forced closes.

## Formula

```
QA = Actual Sales / Quota
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 87 (batch 1)
