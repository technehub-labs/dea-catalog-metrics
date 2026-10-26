# dea:metric-analyst-attrition-rate-soc

Candidate Performance Metric record for **Analyst Attrition Rate - SOC** (AAR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-analyst-attrition-rate-soc`
- **Name:** Analyst Attrition Rate - SOC
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AAR-SOC

## 2. Definition

Within SecOps & Security Operations Center, Analyst Attrition Rate - SOC (AAR-SOC) is used to gauge the retention of customers, users, or assets over time. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Analysts Leaving / Analysts Employed, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures annual turnover among security analysts. SOC work is high-stress and market-demanding; attrition destroys detection continuity and institutional memory of your environment. A stable attrition number can hide the loss of exactly your most senior people. Read with SOC cost per investigated incident and mean time to respond - security.

## Formula

```
Analysts Leaving / Analysts Employed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2790 (batch 7)
