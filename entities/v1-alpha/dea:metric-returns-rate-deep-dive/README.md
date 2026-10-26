# dea:metric-returns-rate-deep-dive

Candidate Performance Metric record for **Returns Rate (Deep Dive)** (RETDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-returns-rate-deep-dive`
- **Name:** Returns Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RETDD

## 2. Definition

Returns Rate (Deep Dive) (RETDD) addresses the quality of outputs and outcomes and is a fixture of retail standard measures reporting. It is computed as Returned Value / Gross Sales, expressed in percent (%). Its use is concentrated in Retail & E-commerce. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
RETDD = Returned Value / Gross Sales
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** retail_standard_measures
- **Sector:** retail_e_commerce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4308 (batch 10)
