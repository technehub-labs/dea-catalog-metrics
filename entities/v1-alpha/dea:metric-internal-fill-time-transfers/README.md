# dea:metric-internal-fill-time-transfers

Candidate Performance Metric record for **Internal Fill Time (Transfers)** (IFT-WF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-fill-time-transfers`
- **Name:** Internal Fill Time (Transfers)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IFT-WF

## 2. Definition

Within Workforce Planning & Productivity, Internal Fill Time (Transfers) (IFT-WF) is used to gauge how efficiently resources are converted into outputs. It is a working-level control: thresholds trigger immediate operational response. It is defined as Days to Fill Role via Internal Move; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
IFT-WF = Days to Fill Role via Internal Move
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3905 (batch 8)
