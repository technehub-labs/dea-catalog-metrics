# dea:metric-self-service-analytics-adoption-rate

Candidate Performance Metric record for **Self-Service Analytics Adoption Rate** (SSAAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-analytics-adoption-rate`
- **Name:** Self-Service Analytics Adoption Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSAAR

## 2. Definition

Self-Service Analytics Adoption Rate (SSAAR) addresses capability maturity or development and is a fixture of data science & analytics operations reporting. It is computed as Analyses via Self-Service Tooling / Total Analyses, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of eligible business users actively using governed self-service analytics. Adoption is the return condition on analytics-platform investment: the tools pay off when distributed decisions use them, and adoption rates reveal whether the platform serves the business or a priesthood. Adoption must be measured as meaningful use (queries, dashboards consumed in decisions), not license counts. Read with certified data source utilization (Deep Dive) and decision adoption rates.

## Formula

```
Analyses via Self-Service Tooling / Total Analyses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2585 (batch 7)
