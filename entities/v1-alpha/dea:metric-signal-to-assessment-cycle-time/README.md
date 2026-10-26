# dea:metric-signal-to-assessment-cycle-time

Candidate Performance Metric record for **Signal-to-Assessment Cycle Time** (SACT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-signal-to-assessment-cycle-time`
- **Name:** Signal-to-Assessment Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SACT

## 2. Definition

A Emerging Risk & Horizon Scanning indicator, Signal-to-Assessment Cycle Time (SACT) quantifies how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Days from External Signal to Formal Risk Assessment; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how long it takes from a detected weak signal to a completed assessment with a decision. The gap is where organizations lose response time to emerging risks. Cycle time measured from formal risk-acceptance rather than first signal hides the delay. Read with emerging risk escalation timeliness and signal-to-assessment cycle time.

## Formula

```
SACT = Days from External Signal to Formal Risk Assessment
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3997 (batch 8)
