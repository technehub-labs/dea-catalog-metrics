# dea:metric-generic-substitution-rate-deep-dive

Candidate Performance Metric record for **Generic Substitution Rate (Deep Dive)** (GSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-generic-substitution-rate-deep-dive`
- **Name:** Generic Substitution Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GSR-D

## 2. Definition

Within Pharmacy Retail, Generic Substitution Rate (Deep Dive) (GSR-D) is used to gauge the economic value created or preserved. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Generic Fills / Fillable Prescriptions - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Healthcare sector.

## 3. Context

Measures the share of prescriptions dispensed as generics where clinically appropriate. It is the affordability engine of pharmaceutical spending for payers, patients, and pharmacy margins alike, and substitution barriers (brand perception, availability) are the target of policy and counseling practice. Substitution outside clinical appropriateness is a quality failure in the other direction. Read with out-of-stock rates by molecule and patient counseling quality.

## Formula

```
GSR-D = Generic Fills / Fillable Prescriptions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmacy_retail
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2287 (batch 6)
