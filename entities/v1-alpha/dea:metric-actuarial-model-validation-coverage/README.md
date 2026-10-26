# dea:metric-actuarial-model-validation-coverage

Candidate Performance Metric record for **Actuarial Model Validation Coverage** (AMVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-actuarial-model-validation-coverage`
- **Name:** Actuarial Model Validation Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AMVC

## 2. Definition

Within Actuarial & Reserving, Actuarial Model Validation Coverage (AMVC) is used to gauge conformance to standards, plans, or obligations. It is defined as Models Validated in Period / Models in Use; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of production actuarial models that have current, documented, independent validation. In an era of machine-learning pricing and reserving, validation coverage is the governance floor: unvalidated models embed regulatory risk and silent error. Coverage must include data lineage and implementation checks, not just methodology review. Read with model backtesting pass rate (Actuarial) and findings-remediation aging.

## Formula

```
Models Validated in Period / Models in Use
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1534 (batch 6)
