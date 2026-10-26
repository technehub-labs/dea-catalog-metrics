# dea:metric-preventive-screening-compliance-hedis-style

Candidate Performance Metric record for **Preventive Screening Compliance (HEDIS-Style)** (PSCH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preventive-screening-compliance-hedis-style`
- **Name:** Preventive Screening Compliance (HEDIS-Style)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSCH

## 2. Definition

Within Healthcare Quality & Patient Safety Standard Measures, Preventive Screening Compliance (HEDIS-Style) (PSCH) is used to gauge the quality of outputs and outcomes. Its calculation is Members Receiving Age-Risk Appropriate Screenings / Eligible Members, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Healthcare practice.

## 3. Context

Measures completion of age- and risk-appropriate preventive screenings. Screenings are the highest-leverage preventive care activity in population health. Compliance computed on enrolled populations without closing care gaps rewards measurement. Read with care gap closure rate and wellness program participation rate.

## Formula

```
Members Receiving Age-Risk Appropriate Screenings / Eligible Members
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4248 (batch 10)
