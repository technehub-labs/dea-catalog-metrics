# dea:metric-incident-rate-environmental

Candidate Performance Metric record for **Incident Rate (Environmental)** (IRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-rate-environmental`
- **Name:** Incident Rate (Environmental)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IRE

## 2. Definition

A Waste & Environmental Services indicator, Incident Rate (Environmental) (IRE) quantifies exposure to adverse outcomes. Its calculation is Reportable Environmental Incidents / Sites per Period, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Environmental services practice.

## 3. Context

Environmental incident rate measures the frequency of reportable spills, exceedances, and unpermitted releases, and it is the compliance-and-license metric for industrial operations - regulators track it, insurers price it, and communities watch it. The measurement challenge is classification consistency: a small spill contained on-site and a release reaching a waterway are categorically different events that a raw count treats equally. Reportability itself varies by jurisdiction and substance thresholds, so cross-site comparisons need normalization. The deeper signal is in near-misses and leading indicators: overflow events, alarm activations, and control-device bypasses predict escalation. Read with severity-weighted incident trends, corrective-action closure rates, and inspection findings that recur - repeat findings reveal systemic control failure rather than bad luck.

## Formula

```
Reportable Environmental Incidents / Sites per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 823 (batch 2)
