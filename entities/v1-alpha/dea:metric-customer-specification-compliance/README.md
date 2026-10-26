# dea:metric-customer-specification-compliance

Candidate Performance Metric record for **Customer Specification Compliance** (CSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-specification-compliance`
- **Name:** Customer Specification Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CSC

## 2. Definition

Within Chemicals, Customer Specification Compliance (CSC) is used to gauge the quality of outputs and outcomes. It is computed as Batches Meeting Customer Specification / Batches Tested, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Chemicals.

## Formula

```
Batches Meeting Customer Specification / Batches Tested
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 903 (batch 3)
