# dea:metric-trade-secret-protection-coverage

Candidate Performance Metric record for **Trade Secret Protection Coverage** (TSPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-secret-protection-coverage`
- **Name:** Trade Secret Protection Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TSPC

## 2. Definition

Trade Secret Protection Coverage (TSPC) captures exposure to adverse outcomes for organizations tracking intellectual property & licensing. The formula is Trade Secrets under Documented Controls / Identified Trade Secrets - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely trade-secret assets are identified and protected by reasonable measures. Trade secrets depend entirely on protection discipline: one careless disclosure ends them. Coverage that classifies everything as secret protects nothing. Read with IP audit trail completeness and data classification coverage.

## Formula

```
Trade Secrets under Documented Controls / Identified Trade Secrets
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** intellectual_property_licensing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3949 (batch 8)
