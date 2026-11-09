# dea:metric-average-time-to-issue-audit-report

Candidate Performance Metric record for **Average Time to Issue Audit Report** (TIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-time-to-issue-audit-report`
- **Name:** Average Time to Issue Audit Report
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TIR

## 2. Definition

A Internal Audit indicator, Average Time to Issue Audit Report (TIR) quantifies how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Days from Fieldwork End to Report Issued, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
TIR = Days from Fieldwork End to Report Issued
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 614 (batch 2)
