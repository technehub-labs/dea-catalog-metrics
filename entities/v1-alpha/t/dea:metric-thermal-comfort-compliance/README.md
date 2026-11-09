# dea:metric-thermal-comfort-compliance

Candidate Performance Metric record for **Thermal Comfort Compliance** (TCC-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-thermal-comfort-compliance`
- **Name:** Thermal Comfort Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TCC-E

## 2. Definition

Thermal Comfort Compliance (TCC-E) measures the quality of outputs and outcomes in the Operations Energy Management domain. It is defined as Working Hours within Comfort Band / Total Working Hours; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
TCC-E = Working Hours within Comfort Band / Total Working Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1439 (batch 5)
