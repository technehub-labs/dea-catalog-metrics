# dea:metric-product-margin-per-bundle

Candidate Performance Metric record for **Product Margin per Bundle** (PMPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-margin-per-bundle`
- **Name:** Product Margin per Bundle
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMPB

## 2. Definition

A Telecom Product & Bundle Management indicator, Product Margin per Bundle (PMPB) quantifies the economic value created or preserved. It is computed as (Bundle Revenue - Bundle Direct Cost) / Bundle Revenue, expressed in percent (%). Its use is concentrated in Telecommunications. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures blended margin across the components of a bundle, the honesty check on bundling strategy. Bundles can hide cross-subsidies where one loss-leading component drags the economics while headline ARPU grows. Compute with fully loaded component costs including content rights and device subsidies, and re-test as component prices change. Read with bundle attach rate (Telecom) and promotional discount depth.

## Formula

```
PMPB = (Bundle Revenue - Bundle Direct Cost) / Bundle Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1441 (batch 5)
