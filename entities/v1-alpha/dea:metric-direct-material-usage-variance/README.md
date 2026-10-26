# dea:metric-direct-material-usage-variance

Candidate Performance Metric record for **Direct Material Usage Variance** (DMUV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-direct-material-usage-variance`
- **Name:** Direct Material Usage Variance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DMUV

## 2. Definition

A Manufacturing indicator, Direct Material Usage Variance (DMUV) quantifies the economic value created or preserved. It is computed as (Actual Material Used - Standard Material) x Standard Price, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Manufacturing.

## 3. Context

Measures the gap between standard and actual material consumed per unit of output. It matters because it catches yield loss, substitution, and BOM drift early. It can be gamed by updating standards to match whatever is actually being used, laundering waste into the baseline. Read with Scrap Cost Percentage and Purchase Price Variance to see whether usage and price effects are being honestly separated.

## Formula

```
(Actual Material Used - Standard Material) x Standard Price
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 256 (batch 1)
