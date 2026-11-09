# dea:metric-alert-triage-cycle-time

Candidate Performance Metric record for **Alert Triage Cycle Time** (ATCT-EF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-triage-cycle-time`
- **Name:** Alert Triage Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATCT-EF

## 2. Definition

Alert Triage Cycle Time (ATCT-EF) measures how efficiently resources are converted into outputs in the Enterprise Fraud & Financial Crime Management domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Hours from Alert to Triage Decision - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ATCT-EF = Hours from Alert to Triage Decision
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3759 (batch 8)
