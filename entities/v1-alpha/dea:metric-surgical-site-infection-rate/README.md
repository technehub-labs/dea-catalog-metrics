# dea:metric-surgical-site-infection-rate

Candidate Performance Metric record for **Surgical Site Infection Rate** (SSIR-HC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-surgical-site-infection-rate`
- **Name:** Surgical Site Infection Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSIR-HC

## 2. Definition

Surgical Site Infection Rate (SSIR-HC) measures exposure to adverse outcomes in the Healthcare Quality & Patient Safety Standard Measures domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as SSI Events / Surgical Procedures, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Healthcare.

## 3. Context

Measures infections following surgical procedures, risk-adjusted. SSI reflects surgical discipline, environment, and post-op care together. Post-discharge surveillance that misses patient-managed infections undercounts. Read with surgical volume outcomes and antibiotic prophylaxis compliance.

## Formula

```
SSI Events / Surgical Procedures
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4241 (batch 10)
