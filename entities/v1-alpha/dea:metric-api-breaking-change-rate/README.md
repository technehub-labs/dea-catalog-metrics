# dea:metric-api-breaking-change-rate

Candidate Performance Metric record for **API Breaking Change Rate** (APBCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-breaking-change-rate`
- **Name:** API Breaking Change Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APBCR

## 2. Definition

API Breaking Change Rate (APBCR) captures exposure to adverse outcomes for organizations tracking software architecture & technical design. Its calculation is Breaking Changes per API Version, measured in count (items per period). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Breaking Changes per API Version
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2627 (batch 7)
