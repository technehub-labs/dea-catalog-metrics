# dea:metric-maritime-safety-inspection-pass-rate

Candidate Performance Metric record for **Maritime Safety Inspection Pass Rate** (MSIP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maritime-safety-inspection-pass-rate`
- **Name:** Maritime Safety Inspection Pass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MSIP

## 2. Definition

A Cruise & Passenger Shipping indicator, Maritime Safety Inspection Pass Rate (MSIP) quantifies conformance to standards, plans, or obligations. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Inspections Passed without Major Finding / Inspections, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Hospitality practice.

## 3. Context

Measures outcomes of port state and flag state inspections (deficiencies, detentions). Detentions halt itineraries, generate headlines, and concentrate regulator attention on operators with repeat findings, so pass rates are commercial risk management. Root-cause corrective action quality determines whether the rate stays healthy. Read with detention history and classification society survey findings.

## Formula

```
Inspections Passed without Major Finding / Inspections
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1922 (batch 6)
