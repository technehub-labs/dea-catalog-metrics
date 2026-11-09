# dea:metric-reconciliation-completion-rate-financial

Candidate Performance Metric record for **Reconciliation Completion Rate (Financial)** (RCRF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reconciliation-completion-rate-financial`
- **Name:** Reconciliation Completion Rate (Financial)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCRF

## 2. Definition

Reconciliation Completion Rate (Financial) (RCRF) measures conformance to standards, plans, or obligations in the Internal Controls & Financial Reporting Integrity domain. The formula is Reconciliations Completed by Deadline / Reconciliations - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
RCRF = Reconciliations Completed by Deadline / Reconciliations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3587 (batch 8)
