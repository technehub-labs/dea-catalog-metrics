# dea:metric-horizon-scan-coverage-ratio

Candidate Performance Metric record for **Horizon Scan Coverage Ratio** (HSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-horizon-scan-coverage-ratio`
- **Name:** Horizon Scan Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HSCR

## 2. Definition

Within Emerging Risk & Horizon Scanning, Horizon Scan Coverage Ratio (HSCR) is used to gauge exposure to adverse outcomes. Its calculation is Scanned Risk Categories per Framework / Categories, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how systematically the organization scans defined horizon (emerging) risk domains. Unscanned horizons are blind spots by definition. Coverage counted as reports received rather than risks assessed is collection, not scanning. Read with emerging risk scanning coverage and regulatory horizon anticipation rate.

## Formula

```
Scanned Risk Categories per Framework / Categories
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3995 (batch 8)
