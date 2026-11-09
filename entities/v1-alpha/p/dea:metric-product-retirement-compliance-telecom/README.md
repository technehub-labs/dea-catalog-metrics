# dea:metric-product-retirement-compliance-telecom

Candidate Performance Metric record for **Product Retirement Compliance (Telecom)** (PRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-retirement-compliance-telecom`
- **Name:** Product Retirement Compliance (Telecom)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRCT

## 2. Definition

Product Retirement Compliance (Telecom) (PRCT) addresses conformance to standards, plans, or obligations and is a fixture of telecom product & bundle management reporting. The formula is Retirements Completed by Migration Deadline / Retirements Planned - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Telecommunications sector.

## 3. Context

Measures the share of legacy products retired per the portfolio sunset plan. It matters because legacy products carry disproportionate support cost and block simplification. Retirement can slip via indefinite limited-support statuses that never end. Read with Legacy Product Support Cost and Customer Migration completion to confirm sunset plans are real.

## Formula

```
PRCT = Retirements Completed by Migration Deadline / Retirements Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1447 (batch 5)
