# dea:metric-fairness-metric-equal-opportunity-gap

Candidate Performance Metric record for **Fairness Metric - Equal Opportunity Gap** (FMEOG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fairness-metric-equal-opportunity-gap`
- **Name:** Fairness Metric - Equal Opportunity Gap
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FMEOG

## 2. Definition

Fairness Metric - Equal Opportunity Gap (FMEOG) measures the quality of outputs and outcomes in the AI Ethics, Fairness & Responsible AI domain. The formula is Difference in True Positive Rates across Groups - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the difference in true-positive rates across groups - whether qualified individuals are equally likely to receive the positive outcome. Equal opportunity is the qualified-candidate fairness standard for decisions like hiring and lending, and the gap exposes whether a model's errors distribute unevenly, which harms groups even when aggregate accuracy looks fine. Gap measurement requires ground-truth labels, which are themselves biased in many domains. Read with demographic parity gap (Deep Dive) and human review coverage of automated decisions (Deep Dive).

## Formula

```
Difference in True Positive Rates across Groups
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2563 (batch 7)
