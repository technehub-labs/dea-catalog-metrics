# dea:metric-error-budget-policy-compliance

Candidate Performance Metric record for **Error Budget Policy Compliance** (EBPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-budget-policy-compliance`
- **Name:** Error Budget Policy Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EBPC

## 2. Definition

Within SRE & Observability Standard Measures, Error Budget Policy Compliance (EBPC) is used to gauge conformance to standards, plans, or obligations. It is computed as Enforcement Actions Taken per Policy Breach Windows / Breach Windows, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software.

## 3. Context

Measures whether agreed consequences (reliability sprints, feature freezes) are applied when budgets exhaust. Compliance makes the error budget a real contract rather than a chart. Policies applied to small teams but never to strategic projects are theater. Read with error budget policy enforcement rate and error budget remaining.

## Formula

```
EBPC = Enforcement Actions Taken per Policy Breach Windows / Breach Windows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4390 (batch 11)
