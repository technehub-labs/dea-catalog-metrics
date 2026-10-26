# dea:metric-predictive-maintenance-coverage

Candidate Performance Metric record for **Predictive Maintenance Coverage** (PDMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-predictive-maintenance-coverage`
- **Name:** Predictive Maintenance Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PDMC

## 2. Definition

Predictive Maintenance Coverage (PDMC) captures capability maturity or development for organizations tracking reliability & maintainability engineering (deep dive). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Critical Assets with Condition Monitoring / Critical Assets, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of the asset base with condition monitoring driving maintenance decisions. Predictive approaches replace calendar-based guesswork with failure-precursor detection. Coverage with sensors installed but models unused is monitoring theater. Read with remaining useful life prediction accuracy and preventive maintenance compliance - Field (Deep Dive).

## Formula

```
PDMC = Critical Assets with Condition Monitoring / Critical Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4106 (batch 9)
