# dea:metric-fraud-savings-ratio

Candidate Performance Metric record for **Fraud Savings Ratio** (FSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-savings-ratio`
- **Name:** Fraud Savings Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FSR

## 2. Definition

Within Insurance Claims Deep Dive, Fraud Savings Ratio (FSR) is used to gauge the economic value created or preserved. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Fraud-Related Savings / Claims Spend; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures fraud detection and avoidance savings against claims paid or fraud program cost. It justifies SIU investment, but savings figures are notoriously soft: avoided losses are counterfactual, and attribution rules decide the number more than the fraud team does. Set conservative detection attribution and validate a sample of savings against actual declines-to-pay upheld on appeal. Read with referral quality from adjusters and false positive rates.

## Formula

```
Fraud-Related Savings / Claims Spend
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1546 (batch 6)
