# dea:metric-estimate-accuracy-cost

Candidate Performance Metric record for **Estimate Accuracy - Cost** (EAC-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-estimate-accuracy-cost`
- **Name:** Estimate Accuracy - Cost
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EAC-PM

## 2. Definition

A Project Management (Deep Dive) indicator, Estimate Accuracy - Cost (EAC-PM) quantifies the quality of outputs and outcomes. The formula is Actual Cost / Estimated Cost at Completion - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the historical reliability of project cost estimates. Systematic under-estimation is the quiet source of portfolio-level cost blowouts. Accuracy computed only on completed projects lags reality by years. Read with cost variance percent and estimation bias calibration index.

## Formula

```
EAC-PM = Actual Cost / Estimated Cost at Completion
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2932 (batch 7)
