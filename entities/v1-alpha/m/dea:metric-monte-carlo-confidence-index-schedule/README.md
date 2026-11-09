# dea:metric-monte-carlo-confidence-index-schedule

Candidate Performance Metric record for **Monte Carlo Confidence Index (Schedule)** (MCCIS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monte-carlo-confidence-index-schedule`
- **Name:** Monte Carlo Confidence Index (Schedule)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCCIS

## 2. Definition

Monte Carlo Confidence Index (Schedule) (MCCIS) captures exposure to adverse outcomes for organizations tracking project risk & issue management. It is computed as Probability of Achieving Committed Date per Simulation, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
MCCIS = Probability of Achieving Committed Date per Simulation
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** project_risk_issue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3431 (batch 7)
