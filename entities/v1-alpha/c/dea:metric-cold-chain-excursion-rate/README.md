# dea:metric-cold-chain-excursion-rate

Candidate Performance Metric record for **Cold Chain Excursion Rate** (CCER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cold-chain-excursion-rate`
- **Name:** Cold Chain Excursion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCER

## 2. Definition

Cold Chain Excursion Rate (CCER) captures exposure to adverse outcomes for organizations tracking pharmacy retail. Its calculation is Refrigerated Items with Temperature Excursion / Items, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Healthcare practice.

## Formula

```
CCER = Refrigerated Items with Temperature Excursion / Items
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmacy_retail
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2292 (batch 6)
