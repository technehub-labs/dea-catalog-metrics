# dea:metric-financial-restatement-count

Candidate Performance Metric record for **Financial Restatement Count** (FRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-financial-restatement-count`
- **Name:** Financial Restatement Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FRC

## 2. Definition

A Internal Controls & Financial Reporting Integrity indicator, Financial Restatement Count (FRC) quantifies exposure to adverse outcomes. It is defined as Restatements Issued in Period; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the frequency of restated financial statements. Restatements are the most public and costly control failure in financial reporting. Near-miss restatements (fixed in review) reveal the same underlying weakness. Read with material weakness count and financial data quality score.

## Formula

```
Restatements Issued in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3585 (batch 8)
