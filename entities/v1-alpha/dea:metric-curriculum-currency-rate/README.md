# dea:metric-curriculum-currency-rate

Candidate Performance Metric record for **Curriculum Currency Rate** (CURR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-curriculum-currency-rate`
- **Name:** Curriculum Currency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CURR

## 2. Definition

Curriculum Currency Rate (CURR) captures the quality of outputs and outcomes for organizations tracking education & training outcome standard measures. It is computed as Courses Reviewed within Update Cycle / Courses, expressed in percent (%). Its use is concentrated in Education. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how recently each program's curriculum was reviewed against current practice. Stale curriculum sells yesterday's skills at today's prices. Currency measured as review date rather than substantive content change is nominal. Read with program accreditation standard compliance and employer satisfaction with graduates.

## Formula

```
CURR = Courses Reviewed within Update Cycle / Courses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** education_training_outcome_standard_measures
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4404 (batch 11)
