# dea:metric-settlement-window-compliance-rate

Candidate Performance Metric record for **Settlement Window Compliance Rate** (SWCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-settlement-window-compliance-rate`
- **Name:** Settlement Window Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SWCR

## 2. Definition

Settlement Window Compliance Rate (SWCR) addresses conformance to standards, plans, or obligations and is a fixture of payments & cards (deep dive) reporting. It is defined as Settlement Batches within Window / Batches; the result is stated in percent (%). In Payments, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SWCR = Settlement Batches within Window / Batches
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2096 (batch 6)
