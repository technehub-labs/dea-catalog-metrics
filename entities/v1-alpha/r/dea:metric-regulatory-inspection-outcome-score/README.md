# dea:metric-regulatory-inspection-outcome-score

Candidate Performance Metric record for **Regulatory Inspection Outcome Score** (RIOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-inspection-outcome-score`
- **Name:** Regulatory Inspection Outcome Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RIOS

## 2. Definition

Regulatory Inspection Outcome Score (RIOS) captures conformance to standards, plans, or obligations for organizations tracking elder & social care. It is defined as Weighted Score from Care Regulator Inspection; the result is stated in score (points). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Social care, it is a recognized element of the standard performance toolkit.

## 3. Context

Regulatory inspection outcome scores measure the findings from government care inspections, and in elder care they are the public-trust metric: scores publish to consumer directories, drive census through family choice, and determine enforcement consequences (denied payment for new admissions, civil penalties, and decertification in escalation). The inspection-sampling honesty issue applies: inspections sample a few days and a subset of records, so scores blend steady-state quality with inspection-window performance - though the well-documented pre-notification dynamics in some regimes do let facilities prepare. The findings taxonomy is the management information: actual harm citations versus standard noncompliance are different problems. Read with repeat-citation analysis (the same finding recurring signals systemic failure), complaint-driven versus routine inspection outcomes, and the correlation of self-reported quality metrics with inspection findings - divergence there reveals reporting honesty.

## Formula

```
RIOS = Weighted Score from Care Regulator Inspection
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1203 (batch 4)
