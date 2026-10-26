# dea:metric-first-in-human-success-rate

Candidate Performance Metric record for **First-in-Human Success Rate** (FIHS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-in-human-success-rate`
- **Name:** First-in-Human Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FIHS

## 2. Definition

First-in-Human Success Rate (FIHS) captures how effectively a process or entity achieves its intended outcome for organizations tracking pharma r&d & clinical trials. The formula is Compounds Progressing past First-in-Human / Compounds Entering - reported in percent (%). It is a standard measure in the Pharmaceuticals sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of candidates entering first-in-human studies that proceed safely through planned dosing and study objectives. It is the first translational filter between preclinical promise and human reality, and the checkpoint where safety design quality is tested. Small sample noise dominates at candidate level, so read program-level trends rather than single events. Read with Phase transition success rate and preclinical model reproducibility evidence.

## Formula

```
Compounds Progressing past First-in-Human / Compounds Entering
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1613 (batch 6)
