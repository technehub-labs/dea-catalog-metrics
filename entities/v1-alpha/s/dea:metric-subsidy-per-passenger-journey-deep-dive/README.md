# dea:metric-subsidy-per-passenger-journey-deep-dive

Candidate Performance Metric record for **Subsidy per Passenger Journey (Deep Dive)** (SPR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-subsidy-per-passenger-journey-deep-dive`
- **Name:** Subsidy per Passenger Journey (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPR-D

## 2. Definition

Subsidy per Passenger Journey (Deep Dive) (SPR-D) measures how efficiently resources are converted into outputs in the Public Transit (Deep Dive) domain. The formula is Net Subsidy / Journeys - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Public Transit sector.

## 3. Context

Measures public funding per rider carried. It is the value-for-money metric transit agencies answer to treasuries with, and it must be read against mission: coverage routes serving carless populations carry high per-journey subsidy by design, and penalizing them blindly is policy failure dressed as efficiency. Comparisons across agencies need fare-structure and service-type normalization. Read with farebox recovery ratio (Deep Dive) and ridership trends by route class.

## Formula

```
SPR-D = Net Subsidy / Journeys
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2413 (batch 6)
