# dea:metric-application-overlap-index

Candidate Performance Metric record for **Application Overlap Index** (AOI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-application-overlap-index`
- **Name:** Application Overlap Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AOI

## 2. Definition

Within Enterprise Architecture, Application Overlap Index (AOI) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Applications with Duplicated Functionality / Total Applications, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Quantifies functional redundancy across the application portfolio - how many systems perform the same job (and at what cost each). Overlap drives duplicate data entry, conflicting master records, and licensing waste. The index is only as honest as its capability mapping, which vendors and system owners tend to shape in self-serving ways. Read with application portfolio rationalization and integration cost trends.

## Formula

```
AOI = Applications with Duplicated Functionality / Total Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1345 (batch 5)
