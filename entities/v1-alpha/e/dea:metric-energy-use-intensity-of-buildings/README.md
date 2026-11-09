# dea:metric-energy-use-intensity-of-buildings

Candidate Performance Metric record for **Energy Use Intensity of Buildings** (EUI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-use-intensity-of-buildings`
- **Name:** Energy Use Intensity of Buildings
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EUI

## 2. Definition

Energy Use Intensity of Buildings (EUI) captures environmental and social sustainability performance for organizations tracking facilities & real estate. It is defined as Building Energy / Floor Area; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Energy consumed per unit of floor area, conventionally kilowatt-hours per square meter per year - the normalization that made building energy performance comparable, and the metric that building codes, benchmarking ordinances, and asset-rating schemes all speak in. Its strategic significance is regulatory and asset-value simultaneously: an expanding set of jurisdictions requires disclosure and sets performance floors, and assets below threshold face fines, required upgrades, or shrinking buyer and lender pools as the floors tighten - energy performance has become a pricing factor in real assets, transmitted through ratings. The honest comparisons are occupancy- and use-adjusted: an intensively used building legitimately runs higher than an empty one, and climate normalization is required before comparing across geographies. Read with on-site measurement: intensity computed from utility bills mixes building performance with tenant behavior, which is why audits meter the building separately.

## Formula

```
EUI = Building Energy / Floor Area
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
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 450 (batch 1)
