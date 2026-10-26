# dea:metric-fairness-metric-demographic-parity-gap

Candidate Performance Metric record for **Fairness Metric - Demographic Parity Gap** (FMDPG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fairness-metric-demographic-parity-gap`
- **Name:** Fairness Metric - Demographic Parity Gap
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FMDPG

## 2. Definition

A AI Ethics, Fairness & Responsible AI indicator, Fairness Metric - Demographic Parity Gap (FMDPG) quantifies the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Max Difference in Positive Outcome Rate across Groups; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the difference in positive-outcome rates across demographic groups. Demographic parity is the bluntest fairness lens, and it is informative precisely because it is blunt: it exposes outcome distribution without pretending the causes are known. Parity is not always the appropriate fairness definition (equal outcomes can be unfair to qualified individuals in some contexts), so read it alongside other fairness metrics. Read with disparate impact ratio (Deep Dive) and adverse impact analysis currency (Deep Dive).

## Formula

```
Max Difference in Positive Outcome Rate across Groups
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2562 (batch 7)
