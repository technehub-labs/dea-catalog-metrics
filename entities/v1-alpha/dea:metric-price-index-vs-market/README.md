# dea:metric-price-index-vs-market

Candidate Performance Metric record for **Price Index vs Market** (PIM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-price-index-vs-market`
- **Name:** Price Index vs Market
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PIM

## 2. Definition

Price Index vs Market (PIM) addresses the economic value created or preserved and is a fixture of retail & e-commerce reporting. It is computed as Average Selling Price / Market Average Price, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Retail.

## 3. Context

Measures the firm's price position relative to a market basket of competitors. It matters because pricing power relative to market determines margin sustainability without volume loss. Index construction is easy to game via basket selection that favors cheaper comparable items. Read with Price Realization and Market Share trends to confirm position translates into actual sales outcomes.

## Formula

```
Average Selling Price / Market Average Price
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 500 (batch 1)
