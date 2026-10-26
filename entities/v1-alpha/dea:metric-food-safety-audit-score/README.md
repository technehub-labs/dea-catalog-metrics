# dea:metric-food-safety-audit-score

Candidate Performance Metric record for **Food Safety Audit Score** (FSAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-food-safety-audit-score`
- **Name:** Food Safety Audit Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FSAS

## 2. Definition

Within Agriculture & Food Processing, Food Safety Audit Score (FSAS) is used to gauge conformance to standards, plans, or obligations. Its calculation is Weighted Score of Food Safety Compliance Audits, measured in score (points). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Agriculture & food practice.

## 3. Context

A food safety audit score summarizes compliance against standards such as BRCGS, FSSC 22000, or SQF, and it is the market's entry ticket - major retailers will not stock a supplier without a recent acceptable rating. Treat scores as a hygiene factor, not a performance measure: audits sample, and the days of preparation before an auditor arrives can mask everyday drift. What matters more is the gap analysis between audit cycles: are repeat non-conformances recurring on the same clauses? Read with recall events, environmental swab results, and pest-control records, which reflect steady-state conditions rather than audit-week performance.

## Formula

```
Weighted Score of Food Safety Compliance Audits
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 730 (batch 2)
