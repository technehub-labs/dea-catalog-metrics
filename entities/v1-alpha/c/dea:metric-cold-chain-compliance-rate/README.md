# dea:metric-cold-chain-compliance-rate

Candidate Performance Metric record for **Cold Chain Compliance Rate** (CCCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cold-chain-compliance-rate`
- **Name:** Cold Chain Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCCR

## 2. Definition

Within Food & Beverage Manufacturing, Cold Chain Compliance Rate (CCCR) is used to gauge conformance to standards, plans, or obligations. It is computed as Temperature-Compliant Shipments / Shipments, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Food & Beverage.

## Formula

```
CCCR = Temperature-Compliant Shipments / Shipments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1798 (batch 6)
