# dea:metric-bundle-attach-rate-telecom

Candidate Performance Metric record for **Bundle Attach Rate (Telecom)** (BART-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bundle-attach-rate-telecom`
- **Name:** Bundle Attach Rate (Telecom)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BART-T

## 2. Definition

Bundle Attach Rate (Telecom) (BART-T) addresses growth over time and is a fixture of telecom product & bundle management reporting. The formula is Customers with Multi-Product Bundle / Customers - reported in percent (%). It is a standard measure in the Telecommunications sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of customers taking multiple products - broadband, mobile, TV, streaming add-ons - together. Bundling is telecom's core retention and ARPU lever: multi-product customers churn far less and cost less to serve. Watch for attach driven by discount stacking that erodes margin without loyalty, and for counting gimmick add-ons as bundle components. Read with product margin per bundle and contract end churn risk conversion.

## Formula

```
Customers with Multi-Product Bundle / Customers
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1440 (batch 5)
