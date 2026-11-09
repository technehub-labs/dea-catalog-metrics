# dea:metric-decision-grade-data-readiness-rate

Candidate Performance Metric record for **Decision-Grade Data Readiness Rate** (DGDRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-grade-data-readiness-rate`
- **Name:** Decision-Grade Data Readiness Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DGDRA

## 2. Definition

Decision-Grade Data Readiness Rate (DGDRA) addresses the quality of outputs and outcomes and is a fixture of data governance & stewardship reporting. It is computed as Enterprise Reports Sourced from Governed Data / Reports, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether the data feeding major decision processes meets the quality bar for those decisions. This is where governance pays: decisions on unfit data are confident mistakes. Readiness declared by data producers rather than consumers overstates. Read with critical data element quality index and management information freshness score.

## Formula

```
DGDRA = Enterprise Reports Sourced from Governed Data / Reports
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3613 (batch 8)
