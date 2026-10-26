# dea:metric-financial-statement-close-cycle-time

Candidate Performance Metric record for **Financial Statement Close Cycle Time** (FSCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-financial-statement-close-cycle-time`
- **Name:** Financial Statement Close Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FSCCT

## 2. Definition

Financial Statement Close Cycle Time (FSCCT) captures how efficiently resources are converted into outputs for organizations tracking internal controls & financial reporting integrity. The formula is Days from Period End to Signed Financials - reported in days. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures elapsed time from period end to published financial statements. Fast, high-quality closes signal strong process and control health. Speed bought by waiving reconciliations converts cycle time into restatement risk. Read with financial restatement count and financial statement audit adjustments.

## Formula

```
Days from Period End to Signed Financials
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3584 (batch 8)
