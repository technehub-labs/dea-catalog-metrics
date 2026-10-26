# dea:metric-feature-parity-time-to-competitor

Candidate Performance Metric record for **Feature Parity Time to Competitor** (FPTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-parity-time-to-competitor`
- **Name:** Feature Parity Time to Competitor
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FPTC

## 2. Definition

Within Telecom Product & Bundle Management, Feature Parity Time to Competitor (FPTC) is used to gauge capability maturity or development. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days between Competitor Launch and Parity Feature Launch - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Telecommunications sector.

## 3. Context

Measures how long after a competitor launches a market-relevant feature before the company matches it. It is the competitive-clock metric for product strategy, quantifying catch-up drag. Some parity gaps are deliberate and fine (gimmick features), so weight by features that show adoption or churn-relevance evidence. Read with time to launch new telecom product and feature usage rates before responding.

## Formula

```
Days between Competitor Launch and Parity Feature Launch
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1449 (batch 5)
