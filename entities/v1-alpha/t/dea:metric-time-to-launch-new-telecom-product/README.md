# dea:metric-time-to-launch-new-telecom-product

Candidate Performance Metric record for **Time to Launch New Telecom Product** (TTLN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-launch-new-telecom-product`
- **Name:** Time to Launch New Telecom Product
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTLN

## 2. Definition

A Telecom Product & Bundle Management indicator, Time to Launch New Telecom Product (TTLN) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Concept Approval to Commercial Launch - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Telecommunications sector.

## 3. Context

Measures elapsed time from product approval to commercial launch - catalogue, pricing, provisioning, billing, channel readiness. Telecom launch speed is throttled less by market planning than by OSS/BSS configuration, making this a de facto systems-capability metric. Counting to soft launch versus full national availability changes the number materially, so fix the definition. Read with digital initiative value realization and feature parity time to competitor.

## Formula

```
TTLN = Days from Concept Approval to Commercial Launch
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1442 (batch 5)
