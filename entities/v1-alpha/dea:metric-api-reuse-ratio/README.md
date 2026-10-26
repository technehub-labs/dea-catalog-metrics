# dea:metric-api-reuse-ratio

Candidate Performance Metric record for **API Reuse Ratio** (APIRU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-reuse-ratio`
- **Name:** API Reuse Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APIRU

## 2. Definition

API Reuse Ratio (APIRU) addresses how efficiently resources are converted into outputs and is a fixture of api lifecycle management reporting. Its calculation is Services Reusing Existing APIs / New Integrations, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## 3. Context

Measures the share of new integrations built on existing, governed APIs versus new point-to-point connections. Reuse compounds: each reuse eliminates duplicate build and future maintenance. Ratios counted by endpoint rather than by consumer hide sprawl. Read with technical debt remediation progress and integration complexity index.

## Formula

```
Services Reusing Existing APIs / New Integrations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3219 (batch 7)
