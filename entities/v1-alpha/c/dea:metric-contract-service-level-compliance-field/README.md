# dea:metric-contract-service-level-compliance-field

Candidate Performance Metric record for **Contract Service Level Compliance (Field)** (CSLCF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-service-level-compliance-field`
- **Name:** Contract Service Level Compliance (Field)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSLCF

## 2. Definition

Contract Service Level Compliance (Field) (CSLCF) captures conformance to standards, plans, or obligations for organizations tracking field service & asset performance. The formula is SLAs Met under Service Contracts / SLAs - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
CSLCF = SLAs Met under Service Contracts / SLAs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3398 (batch 7)
