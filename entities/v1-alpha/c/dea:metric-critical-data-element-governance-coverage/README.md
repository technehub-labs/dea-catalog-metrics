# dea:metric-critical-data-element-governance-coverage

Candidate Performance Metric record for **Critical Data Element Governance Coverage** (CDEGC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-data-element-governance-coverage`
- **Name:** Critical Data Element Governance Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDEGC

## 2. Definition

Within Data Governance & Stewardship, Critical Data Element Governance Coverage (CDEGC) is used to gauge the quality of outputs and outcomes. Its calculation is Critical Data Elements with Defined Standard / CDEs, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely the elements that decisions and reporting depend on are under governance. Governing all data is unaffordable; governing the critical few is the point. Criticality set once and never revisited decays as usage shifts. Read with critical data element quality index and decision-grade data readiness rate.

## Formula

```
CDEGC = Critical Data Elements with Defined Standard / CDEs
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3598 (batch 8)
