# dea:metric-usability-defect-escape-rate

Candidate Performance Metric record for **Usability Defect Escape Rate** (UDER-UX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-usability-defect-escape-rate`
- **Name:** Usability Defect Escape Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UDER-UX

## 2. Definition

Usability Defect Escape Rate (UDER-UX) captures the quality of outputs and outcomes for organizations tracking ux & design systems. It is a working-level control: thresholds trigger immediate operational response. It is defined as Usability Issues Found Post-Release / All Usability Issues; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
UDER-UX = Usability Issues Found Post-Release / All Usability Issues
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3270 (batch 7)
