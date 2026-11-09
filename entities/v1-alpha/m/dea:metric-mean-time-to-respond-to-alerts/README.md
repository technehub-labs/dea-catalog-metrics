# dea:metric-mean-time-to-respond-to-alerts

Candidate Performance Metric record for **Mean Time to Respond to Alerts** (MTTRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-respond-to-alerts`
- **Name:** Mean Time to Respond to Alerts
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTRA

## 2. Definition

Mean Time to Respond to Alerts (MTTRA) measures how efficiently resources are converted into outputs in the Cybersecurity domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Total Alert Response Time / Alerts; the result is stated in minutes. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MTTRA = Total Alert Response Time / Alerts
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 334 (batch 1)
