# dea:metric-compliance-risk-assessment-coverage-deep-dive

Candidate Performance Metric record for **Compliance Risk Assessment Coverage (Deep Dive)** (CRAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-risk-assessment-coverage-deep-dive`
- **Name:** Compliance Risk Assessment Coverage (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRAC

## 2. Definition

A Compliance Monitoring & Testing indicator, Compliance Risk Assessment Coverage (Deep Dive) (CRAC) quantifies exposure to adverse outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Entities with Current Compliance Risk Assessment / Entities - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how completely compliance risks across the business are periodically assessed. Unassessed compliance risk is managed by luck. Coverage with shallow generic assessments is inventory, not assessment. Read with compliance obligation register coverage and assurance map coverage.

## Formula

```
CRAC = Entities with Current Compliance Risk Assessment / Entities
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3567 (batch 8)
