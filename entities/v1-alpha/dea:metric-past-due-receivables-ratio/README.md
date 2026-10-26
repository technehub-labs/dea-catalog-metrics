# dea:metric-past-due-receivables-ratio

Candidate Performance Metric record for **Past Due Receivables Ratio** (PDRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-past-due-receivables-ratio`
- **Name:** Past Due Receivables Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDRR

## 2. Definition

A Accounts Payable & Receivable Operations (Deep Dive) indicator, Past Due Receivables Ratio (PDRR) quantifies exposure to adverse outcomes. It is defined as Receivables Past Due / Total Receivables; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Receivables Past Due / Total Receivables
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3809 (batch 8)
