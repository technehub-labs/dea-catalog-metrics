# dea:metric-roll-rate-30-to-60-days

Candidate Performance Metric record for **Roll Rate (30 to 60 Days)** (RR3060) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-roll-rate-30-to-60-days`
- **Name:** Roll Rate (30 to 60 Days)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RR3060

## 2. Definition

Roll Rate (30 to 60 Days) (RR3060) measures exposure to adverse outcomes in the Credit & Collections Risk (Enterprise) domain. Its calculation is Accounts Rolling from 30DPD to 60DPD / Accounts at 30DPD, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
RR3060 = Accounts Rolling from 30DPD to 60DPD / Accounts at 30DPD
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4200 (batch 9)
