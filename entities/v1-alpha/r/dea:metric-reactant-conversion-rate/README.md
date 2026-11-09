# dea:metric-reactant-conversion-rate

Candidate Performance Metric record for **Reactant Conversion Rate** (RCTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reactant-conversion-rate`
- **Name:** Reactant Conversion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCTR

## 2. Definition

Reactant Conversion Rate (RCTR) measures how efficiently resources are converted into outputs in the Chemicals domain. It is computed as Reactant Converted to Product / Reactant Fed, expressed in percent (%). Its use is concentrated in Chemicals. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
RCTR = Reactant Converted to Product / Reactant Fed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 894 (batch 3)
