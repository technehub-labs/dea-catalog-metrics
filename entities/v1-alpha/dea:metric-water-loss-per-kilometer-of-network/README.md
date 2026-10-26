# dea:metric-water-loss-per-kilometer-of-network

Candidate Performance Metric record for **Water Loss per Kilometer of Network** (WLK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-water-loss-per-kilometer-of-network`
- **Name:** Water Loss per Kilometer of Network
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WLK

## 2. Definition

Water Loss per Kilometer of Network (WLK) addresses how efficiently resources are converted into outputs and is a fixture of energy & utilities reporting. It is defined as Volume of Water Lost / Network Length; the result is stated in ratio (x:1 or x). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Energy & utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures non-revenue water lost per unit of distribution network. It matters because leakage wastes treated water, pumping energy, and capital, and pressures scarce resources. Losses can be understated by estimating consumption rather than metering it. Read with Metering Coverage and Water Recycling Rate to distinguish real losses from measurement gaps.

## Formula

```
Volume of Water Lost / Network Length
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 446 (batch 1)
