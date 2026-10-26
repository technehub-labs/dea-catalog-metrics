# dea:metric-missed-collection-rate

Candidate Performance Metric record for **Missed Collection Rate** (MCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-missed-collection-rate`
- **Name:** Missed Collection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCR

## 2. Definition

Missed Collection Rate (MCR) measures the quality of outputs and outcomes in the Waste & Environmental Services domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Missed Collections / Scheduled Collections, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Environmental services practice.

## Formula

```
MCR = Missed Collections / Scheduled Collections
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 815 (batch 2)
