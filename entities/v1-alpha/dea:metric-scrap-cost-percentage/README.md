# dea:metric-scrap-cost-percentage

Candidate Performance Metric record for **Scrap Cost Percentage** (SCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scrap-cost-percentage`
- **Name:** Scrap Cost Percentage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCP

## 2. Definition

Scrap Cost Percentage (SCP) captures the economic value created or preserved for organizations tracking manufacturing. It is computed as Scrap Cost / Total Production Cost, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Manufacturing.

## 3. Context

Measures scrapped material cost as a share of production cost. It matters because scrap is pure waste that flows straight to margin erosion. Gaming risk includes reclassifying scrap as rework or selling scrap with its cost written into overhead. Read with First Pass Yield and Direct Material Usage Variance to confirm scrap reduction reflects process improvement, not accounting moves.

## Formula

```
Scrap Cost / Total Production Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 255 (batch 1)
