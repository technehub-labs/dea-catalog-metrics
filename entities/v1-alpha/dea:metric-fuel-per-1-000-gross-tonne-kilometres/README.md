# dea:metric-fuel-per-1-000-gross-tonne-kilometres

Candidate Performance Metric record for **Fuel per 1,000 Gross Tonne Kilometres** (FGTK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-per-1-000-gross-tonne-kilometres`
- **Name:** Fuel per 1,000 Gross Tonne Kilometres
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FGTK

## 2. Definition

Fuel per 1,000 Gross Tonne Kilometres (FGTK) addresses how efficiently resources are converted into outputs and is a fixture of rail freight (deep dive) reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Fuel / 1,000 GTK - reported in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Rail sector.

## Formula

```
FGTK = Fuel / 1,000 GTK
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2428 (batch 6)
