# dea:metric-reserving-cycle-time

Candidate Performance Metric record for **Reserving Cycle Time** (RCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserving-cycle-time`
- **Name:** Reserving Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RCT

## 2. Definition

Reserving Cycle Time (RCT) captures how efficiently resources are converted into outputs for organizations tracking actuarial & reserving. It is computed as Days to Complete Reserving Valuation, expressed in days. Its use is concentrated in Insurance. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days to Complete Reserving Valuation
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1527 (batch 6)
