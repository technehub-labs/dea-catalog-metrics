# dea:metric-change-saturation-index

Candidate Performance Metric record for **Change Saturation Index** (CSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-saturation-index`
- **Name:** Change Saturation Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CSI

## 2. Definition

A Change Management indicator, Change Saturation Index (CSI) quantifies exposure to adverse outcomes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Active Initiatives Impacting Same Population vs Capacity Threshold; the result is stated in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the degree to which employees are overloaded with concurrent change. It matters because saturated audiences stop absorbing change, dooming every initiative at once. Index construction can be tuned to show capacity that interviews contradict. Read with Change-Driven Productivity Dip Duration and engagement trends to confirm saturation readings are honest.

## Formula

```
Active Initiatives Impacting Same Population vs Capacity Threshold
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** change_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1378 (batch 5)
