# dea:metric-farm-cost-per-tonne-produced-deep-dive

Candidate Performance Metric record for **Farm Cost per Tonne Produced (Deep Dive)** (FCPT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-farm-cost-per-tonne-produced-deep-dive`
- **Name:** Farm Cost per Tonne Produced (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FCPT-D

## 2. Definition

A Agriculture & Agronomy (Deep Dive) indicator, Farm Cost per Tonne Produced (Deep Dive) (FCPT-D) quantifies how efficiently resources are converted into outputs. The formula is Total Cost / Production Tonnes - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Agriculture sector.

## 3. Context

Measures fully loaded production cost per output unit. It is the survival metric of commodity farming: producers are price-takers, so cost per tonne against the market price curve decides everything, and the lowest-cost quartile is who survives the down cycles. Cost allocation between enterprises on mixed farms determines comparability. Read with yield trends and input-price exposure hedging.

## Formula

```
Total Cost / Production Tonnes
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2326 (batch 6)
