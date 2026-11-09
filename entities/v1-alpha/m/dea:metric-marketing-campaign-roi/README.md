# dea:metric-marketing-campaign-roi

Candidate Performance Metric record for **Marketing Campaign ROI** (MROI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-campaign-roi`
- **Name:** Marketing Campaign ROI
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MROI

## 2. Definition

Marketing Campaign ROI (MROI) captures the economic value created or preserved for organizations tracking marketing. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as (Campaign Revenue - Campaign Cost) / Campaign Cost, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures incremental profit generated per unit of campaign spend. It matters because it is the ultimate test of whether marketing creates more value than it costs. Gaming risk includes attribution models that credit the last click, or counting branded search that would convert anyway. Read with Cost per Acquisition and Marketing Mix Modeling results to test whether attributed lift survives incrementality testing.

## Formula

```
MROI = (Campaign Revenue - Campaign Cost) / Campaign Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 125 (batch 1)
