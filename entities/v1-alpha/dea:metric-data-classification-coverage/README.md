# dea:metric-data-classification-coverage

Candidate Performance Metric record for **Data Classification Coverage** (DCC-DG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-classification-coverage`
- **Name:** Data Classification Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCC-DG

## 2. Definition

A Data Governance & Stewardship indicator, Data Classification Coverage (DCC-DG) quantifies exposure to adverse outcomes. It is defined as Data Assets Classified per Policy / Data Assets; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of data assets classified per the governance scheme. Classification is the control trigger: privacy, retention, and security controls all key off it. Coverage counted at the repository level while contents remain mixed is coarse. Read with personal data inventory coverage and security policy coverage (data).

## Formula

```
DCC-DG = Data Assets Classified per Policy / Data Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3601 (batch 8)
