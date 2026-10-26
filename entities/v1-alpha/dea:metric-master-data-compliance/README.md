# dea:metric-master-data-compliance

Candidate Performance Metric record for **Master Data Compliance** (MDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-compliance`
- **Name:** Master Data Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDC

## 2. Definition

Master Data Compliance (MDC) captures conformance to standards, plans, or obligations for organizations tracking data management & analytics. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Records Meeting Governance Standards / Total Records - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of master records conforming to governance standards for content and structure. It matters because master data errors multiply into every transaction that references them. Compliance can be inflated by widening the standard or auto-correcting records without fixing the source process. Read with Data Accuracy Rate and Data Catalog Coverage to confirm governed data is both correct and discoverable.

## Formula

```
Records Meeting Governance Standards / Total Records
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 339 (batch 1)
