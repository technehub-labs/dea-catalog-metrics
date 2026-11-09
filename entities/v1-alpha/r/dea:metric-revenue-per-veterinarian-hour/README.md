# dea:metric-revenue-per-veterinarian-hour

Candidate Performance Metric record for **Revenue per Veterinarian Hour** (RPVH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-veterinarian-hour`
- **Name:** Revenue per Veterinarian Hour
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPVH

## 2. Definition

Revenue per Veterinarian Hour (RPVH) addresses how efficiently resources are converted into outputs and is a fixture of veterinary & animal health reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Revenue / Veterinarian Hours - reported in currency per unit. Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Healthcare sector.

## 3. Context

Measures revenue generated per clinical hour. It is the productivity core of veterinary economics, a labor-constrained profession with rising demand and fixed clinical capacity - so yield per hour, not volume, drives growth. Revenue mix (wellness versus procedure) shifts the number materially, and burnout-driven schedule reduction hides in the trend. Read with appointment length and utilization versus demand backlog.

## Formula

```
RPVH = Revenue / Veterinarian Hours
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** veterinary_animal_health
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2034 (batch 6)
