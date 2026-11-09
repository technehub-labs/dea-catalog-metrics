# dea:metric-store-staffing-ratio

Candidate Performance Metric record for **Store Staffing Ratio** (SSR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-store-staffing-ratio`
- **Name:** Store Staffing Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSR2

## 2. Definition

Within Retail & E-commerce, Store Staffing Ratio (SSR2) is used to gauge the utilization or availability of capacity. It is a working-level control: thresholds trigger immediate operational response. It is defined as Labor Hours / Store Operating Hours; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. In Retail, it is a recognized element of the standard performance toolkit.

## Formula

```
SSR2 = Labor Hours / Store Operating Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 501 (batch 1)
