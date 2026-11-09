# dea:metric-promotional-roi

Candidate Performance Metric record for **Promotional ROI** (PRoi) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-promotional-roi`
- **Name:** Promotional ROI
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRoi

## 2. Definition

Promotional ROI (PRoi) addresses the economic value created or preserved and is a fixture of pricing & revenue management reporting. It is computed as (Incremental Promotion Revenue - Promotion Cost) / Promotion Cost, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures incremental margin generated per unit of promotional investment. It matters because promotions that do not lift incremental sales simply subsidize purchases that would happen anyway. Baseline manipulation (understating pre-promotion sales) inflates the measured lift. Read with Post-Promotion Dips and Trade Spend effectiveness to confirm lift is incremental, not borrowed.

## Formula

```
PRoi = (Incremental Promotion Revenue - Promotion Cost) / Promotion Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1069 (batch 4)
