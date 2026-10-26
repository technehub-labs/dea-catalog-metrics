# dea:metric-audit-nonconformance-closure-rate

Candidate Performance Metric record for **Audit Nonconformance Closure Rate** (ANCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-nonconformance-closure-rate`
- **Name:** Audit Nonconformance Closure Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ANCR

## 2. Definition

Audit Nonconformance Closure Rate (ANCR) captures conformance to standards, plans, or obligations for organizations tracking quality management. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Closed Nonconformances / Identified Nonconformances; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of audit-identified nonconformances closed within target time. It matters because unclosed findings are compounding risk and audit scrutiny. Teams can game it by closing findings on paper with weak evidence or downgrading severity to lower the bar. Read with Corrective Action Effectiveness and repeat-finding rates to confirm closures are real fixes, not paperwork.

## Formula

```
Closed Nonconformances / Identified Nonconformances
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 238 (batch 1)
