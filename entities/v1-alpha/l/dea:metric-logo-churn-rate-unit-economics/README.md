# dea:metric-logo-churn-rate-unit-economics

Candidate Performance Metric record for **Logo Churn Rate (Unit Economics)** (LCRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-logo-churn-rate-unit-economics`
- **Name:** Logo Churn Rate (Unit Economics)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCRDD

## 2. Definition

Logo Churn Rate (Unit Economics) (LCRDD) addresses the retention of customers, users, or assets over time and is a fixture of unit economics & growth (deep dive) reporting. It is computed as Customers Lost / Customers at Start, expressed in percent (%). Its use is concentrated in Software. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of customers lost per period. Logo churn is the bluntest honesty metric: customers voting with exits. Churn concentrated in small logos can hide the loss of anchor accounts. Read with gross dollar retention (Deep Dive) and churn rate.

## Formula

```
LCRDD = Customers Lost / Customers at Start
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4169 (batch 9)
