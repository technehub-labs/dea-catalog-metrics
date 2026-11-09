# dea:metric-land-use-per-megawatt

Candidate Performance Metric record for **Land Use per Megawatt** (LUMW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-land-use-per-megawatt`
- **Name:** Land Use per Megawatt
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LUMW

## 2. Definition

Land Use per Megawatt (LUMW) addresses environmental and social sustainability performance and is a fixture of energy transition & renewables reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Land Area Occupied / Installed Capacity, measured in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Renewable energy practice.

## 3. Context

Measures land footprint per unit of renewable capacity. It matters because siting and permitting risk scale with land intensity and community acceptance. Land calculations can exclude roads and substations to flatter the ratio. Read with Permitting Cycle Time and community engagement metrics to confirm land metrics reflect real project footprint.

## Formula

```
LUMW = Land Area Occupied / Installed Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1108 (batch 4)
