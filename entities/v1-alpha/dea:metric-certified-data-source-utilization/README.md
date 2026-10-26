# dea:metric-certified-data-source-utilization

Candidate Performance Metric record for **Certified Data Source Utilization** (CDSU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-certified-data-source-utilization`
- **Name:** Certified Data Source Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDSU

## 2. Definition

Within Data Science & Analytics Operations, Certified Data Source Utilization (CDSU) is used to gauge the quality of outputs and outcomes. It is computed as Analyses Using Certified Sources / Analyses, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of analytics work built on certified, governed data sources versus ungoverned extracts. It is the trust-integrity metric of self-service: certified sources carry lineage and quality assurance, while ungoverned extracts quietly reintroduce the conflicting-numbers problem self-service was meant to end. Utilization requires the catalog to be usable, since certification without discoverability is bureaucracy. Read with master data source alignment and dashboard certification coverage.

## Formula

```
Analyses Using Certified Sources / Analyses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2586 (batch 7)
