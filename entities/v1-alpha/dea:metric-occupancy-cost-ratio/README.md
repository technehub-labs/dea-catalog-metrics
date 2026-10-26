# dea:metric-occupancy-cost-ratio

Candidate Performance Metric record for **Occupancy Cost Ratio** (OCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-occupancy-cost-ratio`
- **Name:** Occupancy Cost Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCR

## 2. Definition

Occupancy Cost Ratio (OCR) captures how efficiently resources are converted into outputs for organizations tracking facilities & real estate. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Total Occupancy Cost / Revenue - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Total occupancy cost as a share of revenue - the gauge that expresses real estate as a business cost rather than a real-estate number, which is the form management actually needs: cost per square meter describes the space, this ratio describes what the space does to the operating model. Its strategic use is threshold diagnosis: retail businesses watch it obsessively (occupancy cost above a certain share of store revenue is the classic unprofitable-store signature), and for offices it measures how much of each revenue dollar is consumed by housing the people who earn it. Read with the fixed-cost lens: occupancy costs are contractual and sticky, rising automatically with indexation, which makes this ratio deteriorate in flat-revenue years without any real-estate decision being taken - and that automatic deterioration is the signal to renegotiate or exit.

## Formula

```
Total Occupancy Cost / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 454 (batch 1)
