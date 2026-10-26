# dea:metric-exposure-at-default-deep-dive

Candidate Performance Metric record for **Exposure at Default (Deep Dive)** (EADDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exposure-at-default-deep-dive`
- **Name:** Exposure at Default (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EADDD

## 2. Definition

Exposure at Default (Deep Dive) (EADDD) measures exposure to adverse outcomes in the Credit & Collections Risk (Enterprise) domain. It is computed as Outstanding Balance plus Undrawn Commitment at Default, expressed in currency value. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the expected exposure at the moment of default, including future drawdowns. EAD is what converts likelihood into money at risk. Revolving facilities' EAD spikes precisely when distress begins. Read with expected loss rate (Deep Dive) and credit utilization trend.

## Formula

```
Outstanding Balance plus Undrawn Commitment at Default
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4197 (batch 9)
