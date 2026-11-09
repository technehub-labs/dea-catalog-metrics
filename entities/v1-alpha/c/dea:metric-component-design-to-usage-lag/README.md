# dea:metric-component-design-to-usage-lag

Candidate Performance Metric record for **Component Design-to-Usage Lag** (CDUL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-component-design-to-usage-lag`
- **Name:** Component Design-to-Usage Lag
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDUL

## 2. Definition

Component Design-to-Usage Lag (CDUL) measures how efficiently resources are converted into outputs in the UX & Design Systems domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Median Days from Component Design to First Production Use, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CDUL = Median Days from Component Design to First Production Use
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3274 (batch 7)
