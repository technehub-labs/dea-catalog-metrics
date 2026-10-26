# dea:metric-product-discovery-to-delivery-ratio

Candidate Performance Metric record for **Product Discovery-to-Delivery Ratio** (PDDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-discovery-to-delivery-ratio`
- **Name:** Product Discovery-to-Delivery Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PDDR

## 2. Definition

Product Discovery-to-Delivery Ratio (PDDR) measures capability maturity or development in the Requirements Engineering & Product Discovery domain. The formula is Discovery Time / Delivery Time - reported in ratio (x:1 or x). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the balance of investment between discovery (learning what to build) and delivery (building it). Teams that under-invest in discovery ship more features that fail outcome tests, and the ratio is the structural indicator of that pattern. The right ratio varies by context, so benchmark within product maturity stage. Read with experiment win rate - business experiments (Deep Dive) and shipped-feature outcome attainment.

## Formula

```
Discovery Time / Delivery Time
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2617 (batch 7)
