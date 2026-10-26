# dea:metric-days-past-due-30-rate

Candidate Performance Metric record for **Days Past Due 30+ Rate** (DPD30) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-past-due-30-rate`
- **Name:** Days Past Due 30+ Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DPD30

## 2. Definition

Days Past Due 30+ Rate (DPD30) captures exposure to adverse outcomes for organizations tracking credit & collections risk (enterprise). The formula is Accounts 30+ Days Past Due / Active Accounts - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Accounts 30+ Days Past Due / Active Accounts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4199 (batch 9)
