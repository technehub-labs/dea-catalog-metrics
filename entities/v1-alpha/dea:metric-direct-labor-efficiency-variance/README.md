# dea:metric-direct-labor-efficiency-variance

Candidate Performance Metric record for **Direct Labor Efficiency Variance** (DLEV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-direct-labor-efficiency-variance`
- **Name:** Direct Labor Efficiency Variance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DLEV

## 2. Definition

Direct Labor Efficiency Variance (DLEV) addresses the economic value created or preserved and is a fixture of manufacturing reporting. Its calculation is (Actual Labor Hours - Standard Hours) x Standard Rate, measured in currency value. It originates from and is most used in Manufacturing practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the gap between standard and actual labor hours for output achieved. It matters because it isolates labor performance from rate and mix changes. Gaming risk includes revising standards upward after the fact or absorbing idle time into overhead. Read with Labor Productivity and Overtime Hours to confirm efficiency gains are not cost-shifting in disguise.

## Formula

```
(Actual Labor Hours - Standard Hours) x Standard Rate
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 257 (batch 1)
