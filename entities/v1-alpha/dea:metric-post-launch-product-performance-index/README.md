# dea:metric-post-launch-product-performance-index

Candidate Performance Metric record for **Post-Launch Product Performance Index** (PPPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-launch-product-performance-index`
- **Name:** Post-Launch Product Performance Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPPI

## 2. Definition

A R&D and Innovation indicator, Post-Launch Product Performance Index (PPPI) quantifies the economic value created or preserved. Its calculation is Weighted Index of Sales, Quality, Margin vs Targets, measured in index (0-100 or normalized). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

A composite of how launched products perform against their business-case expectations - revenue, margin, adoption, and quality dimensions combined - the metric that closes the loop between the promises in the stage-gate document and the reality in the P&L. Its strategic weight is the estimate-integrity effect: when launch performance is never audited, business cases become advocacy documents calibrated to pass gates, and the entire portfolio process inherits the optimism. Organizations that publish this index create an uncomfortable but valuable feedback loop - the teams whose past cases were wildly optimistic get discounted, and gate reviewers accumulate the calibration data to make better next decisions. Read with the persistence dimension: product performance against case peaks early or late in the launch curve depending on category, so the index should compare products at comparable maturity points rather than blended.

## Formula

```
Weighted Index of Sales, Quality, Margin vs Targets
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 549 (batch 1)
