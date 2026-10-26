# dea:metric-occupational-exposure-limit-compliance

Candidate Performance Metric record for **Occupational Exposure Limit Compliance** (OELC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-occupational-exposure-limit-compliance`
- **Name:** Occupational Exposure Limit Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OELC

## 2. Definition

A Chemicals & Specialty Materials indicator, Occupational Exposure Limit Compliance (OELC) quantifies exposure to adverse outcomes. The formula is Monitoring Results below OEL / Results - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Chemicals sector.

## 3. Context

Measures workplace exposure to hazardous substances against regulatory limits. It is the quantitative core of industrial hygiene in chemical operations, protecting against both acute and chronic health harm. Sampling coverage and representativeness determine credibility, and excursions at the limit demand control investment rather than re-sampling. Read with exposure surveillance trends and control technology investment.

## Formula

```
OELC = Monitoring Results below OEL / Results
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals_specialty_materials
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1823 (batch 6)
