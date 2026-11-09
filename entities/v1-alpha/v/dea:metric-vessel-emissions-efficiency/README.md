# dea:metric-vessel-emissions-efficiency

Candidate Performance Metric record for **Vessel Emissions Efficiency** (VEE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vessel-emissions-efficiency`
- **Name:** Vessel Emissions Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VEE

## 2. Definition

Vessel Emissions Efficiency (VEE) measures environmental and social sustainability performance in the Maritime & Shipping domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is CO2e Emitted / Tonne-Nautical Mile - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Maritime & shipping sector.

## 3. Context

Vessel emissions efficiency measures CO2 per tonne-mile (the basis of the IMO's Carbon Intensity Indicator), and it is the metric where shipping's decarbonization is actually being enforced - CII ratings (A through E) now have regulatory teeth, with poorly rated vessels facing commercial pressure and eventual scrutiny. The metric's structure rewards slow steaming (speed reduction improves intensity dramatically) and penalizes low utilization, making it partly controllable through operational choices rather than vessel technology. The honest read distinguishes design efficiency (Energy Efficiency Design Index for newbuilds) from operational efficiency (CII), since the same ship can earn different ratings by trade. Read with CII rating trend by vessel, slow-steaming contribution, utilization effects, and fleet-age renewal plans against phase-in standards.

## Formula

```
VEE = CO2e Emitted / Tonne-Nautical Mile
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 985 (batch 3)
