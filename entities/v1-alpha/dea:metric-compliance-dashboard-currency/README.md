# dea:metric-compliance-dashboard-currency

Candidate Performance Metric record for **Compliance Dashboard Currency** (CDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-dashboard-currency`
- **Name:** Compliance Dashboard Currency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDC

## 2. Definition

Compliance Dashboard Currency (CDC) captures the quality of outputs and outcomes for organizations tracking regulatory affairs & compliance operations. It is computed as Metrics Refreshed within Window / Metrics Tracked, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Metrics Refreshed within Window / Metrics Tracked
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1603 (batch 6)
