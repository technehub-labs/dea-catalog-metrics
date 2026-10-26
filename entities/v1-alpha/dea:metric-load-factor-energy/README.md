# dea:metric-load-factor-energy

Candidate Performance Metric record for **Load Factor (Energy)** (LFE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-load-factor-energy`
- **Name:** Load Factor (Energy)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LFE

## 2. Definition

Load Factor (Energy) (LFE) captures how efficiently resources are converted into outputs for organizations tracking operations energy management. It is defined as Average Load / Peak Load; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures average demand as a share of peak demand. It matters because a higher load factor spreads fixed energy cost over more useful consumption. Load factor can be inflated by raising off-peak baseload wastefully. Read with Energy Cost per Unit and Peak Demand Ratio to confirm improvements are efficient.

## Formula

```
Average Load / Peak Load
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1432 (batch 5)
