# dea:metric-reliability-at-time-t-r-t

Candidate Performance Metric record for **Reliability at Time t (R(t))** (RTT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reliability-at-time-t-r-t`
- **Name:** Reliability at Time t (R(t))
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTT

## 2. Definition

Reliability at Time t (R(t)) (RTT) addresses exposure to adverse outcomes and is a fixture of reliability & maintainability engineering (deep dive) reporting. It is computed as exp(-Integral of Hazard Function to t), expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the probability an asset survives failure-free to a specified time. R(t) is the fundamental reliability function behind warranty, maintenance, and design decisions. Field data censored by early replacement biases estimates. Read with mean life (MTTF Deep Dive) and reliability growth rate.

## Formula

```
exp(-Integral of Hazard Function to t)
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4095 (batch 9)
