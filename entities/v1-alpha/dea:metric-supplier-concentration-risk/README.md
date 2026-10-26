# dea:metric-supplier-concentration-risk

Candidate Performance Metric record for **Supplier Concentration Risk** (SCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-concentration-risk`
- **Name:** Supplier Concentration Risk
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCR

## 2. Definition

A Supply Chain indicator, Supplier Concentration Risk (SCR) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Spend with Top Supplier / Total Supplier Spend, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of spend or volume dependent on the top suppliers - classically measured through the concentration of the top-N, and formally through the Herfindahl-type index that the antitrust tradition lends to procurement. The 2020-2022 disruption era made it a board metric: single-source dependencies that looked efficient proved fragile when geography, logistics, or a single plant failure removed a whole input at once. Strategic use is a portfolio question - concentration is acceptable when the supplier is stable and switching is cheap, and unacceptable when the dependency is engineering-embedded with years to qualify an alternative, which the metric alone does not reveal. Read with the substitution analysis: concentration with a qualified second source is risk managed; concentration with none is exposure, whatever the spend share.

## Formula

```
Spend with Top Supplier / Total Supplier Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 188 (batch 1)
