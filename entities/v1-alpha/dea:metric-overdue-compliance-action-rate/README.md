# dea:metric-overdue-compliance-action-rate

Candidate Performance Metric record for **Overdue Compliance Action Rate** (OCAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overdue-compliance-action-rate`
- **Name:** Overdue Compliance Action Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OCAR

## 2. Definition

Overdue Compliance Action Rate (OCAR) captures conformance to standards, plans, or obligations for organizations tracking compliance monitoring & testing. It provides the day-to-day signal that a process is running as designed. Its calculation is Remediation Actions Past Due / Actions, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
OCAR = Remediation Actions Past Due / Actions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3561 (batch 8)
