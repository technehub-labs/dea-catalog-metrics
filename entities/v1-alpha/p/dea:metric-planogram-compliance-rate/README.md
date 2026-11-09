# dea:metric-planogram-compliance-rate

Candidate Performance Metric record for **Planogram Compliance Rate** (PGCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-planogram-compliance-rate`
- **Name:** Planogram Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PGCR

## 2. Definition

Planogram Compliance Rate (PGCR) measures conformance to standards, plans, or obligations in the Retail Standard Measures domain. It is computed as Shelves Matching Planogram on Audit / Audited, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Retail & E-commerce.

## Formula

```
PGCR = Shelves Matching Planogram on Audit / Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** retail_standard_measures
- **Sector:** retail_e_commerce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4305 (batch 10)
