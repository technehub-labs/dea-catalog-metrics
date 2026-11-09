# dea:metric-content-completion-rate

Candidate Performance Metric record for **Content Completion Rate** (CCR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-content-completion-rate`
- **Name:** Content Completion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCR-M

## 2. Definition

Content Completion Rate (CCR-M) measures the engagement or satisfaction of the people involved in the Media & Entertainment domain. Its calculation is Titles Completed by Viewers / Titles Started, measured in percent (%). It originates from and is most used in Media & entertainment practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of started media content finished by viewers. It matters because completion is the core engagement signal that drives recommendations and ad pricing. Completion can be inflated by counting brief trailing views or padding content with recaps. Read with Average Watch Time and Subscriber Churn to confirm completion reflects genuine engagement.

## Formula

```
CCR-M = Titles Completed by Viewers / Titles Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 695 (batch 2)
