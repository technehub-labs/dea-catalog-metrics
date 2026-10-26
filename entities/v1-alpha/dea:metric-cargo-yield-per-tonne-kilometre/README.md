# dea:metric-cargo-yield-per-tonne-kilometre

Candidate Performance Metric record for **Cargo Yield per Tonne-Kilometre** (CYTK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cargo-yield-per-tonne-kilometre`
- **Name:** Cargo Yield per Tonne-Kilometre
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CYTK

## 2. Definition

Cargo Yield per Tonne-Kilometre (CYTK) addresses the economic value created or preserved and is a fixture of airline operations (deep dive) reporting. Its calculation is Cargo Revenue / Cargo Tonne-Kilometres, measured in currency per unit. It originates from and is most used in Airlines practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
CYTK = Cargo Revenue / Cargo Tonne-Kilometres
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2268 (batch 6)
