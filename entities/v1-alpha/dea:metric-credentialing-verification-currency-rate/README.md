# dea:metric-credentialing-verification-currency-rate

Candidate Performance Metric record for **Credentialing Verification Currency Rate** (CVCR-HC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-credentialing-verification-currency-rate`
- **Name:** Credentialing Verification Currency Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CVCR-HC

## 2. Definition

Credentialing Verification Currency Rate (CVCR-HC) measures conformance to standards, plans, or obligations in the Healthcare Quality & Patient Safety Standard Measures domain. The formula is Practitioners with Current Primary Source Verification / Practitioners - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Healthcare sector.

## 3. Context

Measures whether practitioner credentials and privileges are verified within required cycles. Credentialing failures are a direct patient-safety and liability exposure. Currency measured as file date rather than primary-source verification is thin. Read with practitioner data quality score and medical staff office cycle time.

## Formula

```
Practitioners with Current Primary Source Verification / Practitioners
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4254 (batch 10)
