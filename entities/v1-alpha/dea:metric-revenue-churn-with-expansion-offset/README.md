# dea:metric-revenue-churn-with-expansion-offset

Candidate Performance Metric record for **Revenue Churn with Expansion Offset** (RCWEO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-churn-with-expansion-offset`
- **Name:** Revenue Churn with Expansion Offset
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCWEO

## 2. Definition

Revenue Churn with Expansion Offset (RCWEO) captures the retention of customers, users, or assets over time for organizations tracking unit economics & growth (deep dive). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Net Revenue Lost after Expansion / Starting MRR, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## 3. Context

Measures net revenue churn after expansion offsets. The net view can flatter: heavy expansion hiding heavy churn is unstable. Both gross and net numbers are needed for an honest read. Read with gross dollar retention (Deep Dive) and net dollar retention (Deep Dive).

## Formula

```
RCWEO = Net Revenue Lost after Expansion / Starting MRR
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4170 (batch 9)
