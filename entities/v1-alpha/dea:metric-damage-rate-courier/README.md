# dea:metric-damage-rate-courier

Candidate Performance Metric record for **Damage Rate (Courier)** (DMG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-damage-rate-courier`
- **Name:** Damage Rate (Courier)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DMG

## 2. Definition

Within Postal & Courier, Damage Rate (Courier) (DMG) is used to gauge the quality of outputs and outcomes. Its calculation is Damaged Items / Items Handled, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Postal & courier practice.

## Formula

```
DMG = Damaged Items / Items Handled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 828 (batch 2)
