# dea:metric-master-data-source-alignment

Candidate Performance Metric record for **Master Data Source Alignment** (MDSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-source-alignment`
- **Name:** Master Data Source Alignment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDSA

## 2. Definition

Master Data Source Alignment (MDSA) addresses conformance to standards, plans, or obligations and is a fixture of enterprise architecture reporting. It is computed as Domains with Single Authoritative Source / Data Domains, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of critical master data entities (customer, product, supplier, employee) governed by the designated golden source rather than divergent local copies. Misalignment quietly corrupts every downstream metric and integration. Watch for declared alignment versus observed use - shadow copies persist long after golden sources are announced. Read with data quality scores and reconciliation breakage rates.

## Formula

```
MDSA = Domains with Single Authoritative Source / Data Domains
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1351 (batch 5)
