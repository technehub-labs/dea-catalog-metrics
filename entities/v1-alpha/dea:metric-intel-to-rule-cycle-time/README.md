# dea:metric-intel-to-rule-cycle-time

Candidate Performance Metric record for **Intel-to-Rule Cycle Time** (ITRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-intel-to-rule-cycle-time`
- **Name:** Intel-to-Rule Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITRCT

## 2. Definition

Intel-to-Rule Cycle Time (ITRCT) addresses how efficiently resources are converted into outputs and is a fixture of threat intelligence & red team reporting. It is defined as Days from Threat Intel Received to Detection Rule Deployed; the result is stated in days. It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days from Threat Intel Received to Detection Rule Deployed
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3289 (batch 7)
