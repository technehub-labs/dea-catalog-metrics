# dea:metric-hcahps-patient-experience-score

Candidate Performance Metric record for **HCAHPS Patient Experience Score** (HCAHPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hcahps-patient-experience-score`
- **Name:** HCAHPS Patient Experience Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HCAHPS

## 2. Definition

HCAHPS Patient Experience Score (HCAHPS) captures the engagement or satisfaction of the people involved for organizations tracking healthcare quality & patient safety standard measures. It is computed as Composite Patient Experience Survey Rating, expressed in score (points). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Healthcare.

## 3. Context

Measures standardized patient-reported experience across US hospital stays. It is publicly reported and payment-linked. Survey response rates skew toward the healthiest and most engaged patients. Read with patient experience (non-HCAHPS) post-discharge follow-up and 30-day readmission rate (Deep Dive).

## Formula

```
Composite Patient Experience Survey Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4237 (batch 10)
