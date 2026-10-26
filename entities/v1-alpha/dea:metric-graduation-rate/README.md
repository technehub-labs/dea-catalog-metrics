# dea:metric-graduation-rate

Candidate Performance Metric record for **Graduation Rate** (GR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-graduation-rate`
- **Name:** Graduation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GR

## 2. Definition

Graduation Rate (GR) captures the quality of outputs and outcomes for organizations tracking education. It is computed as Students Graduating On Time / Students in Cohort, expressed in percent (%). Its use is concentrated in Education. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of a cohort completing their program within a defined window - the outcome metric that accreditation, ranking systems, and funding formulas all track, and the one that converts retention from process to promise. Its strategic significance is completion economics: retention without graduation is merely slower attrition, and the national policy concern about completion rates has attached funding and reputational consequence to exactly this number. The honest measurement is cohort-honest: graduation rates computed on first-time, full-time cohorts (the conventional definition) systematically exclude transfer and part-time students, whose outcomes are far worse - so an institution's headline rate can flatter while the true completion problem hides in the excluded populations. Read with time-to-degree, since graduating a year late is a cost to student and institution that the binary rate ignores.

## Formula

```
Students Graduating On Time / Students in Cohort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** education
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 515 (batch 1)
