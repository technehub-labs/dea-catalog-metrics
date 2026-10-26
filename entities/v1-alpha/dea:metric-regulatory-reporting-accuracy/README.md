# dea:metric-regulatory-reporting-accuracy

Candidate Performance Metric record for **Regulatory Reporting Accuracy** (RRA-R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-reporting-accuracy`
- **Name:** Regulatory Reporting Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRA-R

## 2. Definition

Within Regulatory Affairs & Compliance Operations, Regulatory Reporting Accuracy (RRA-R) is used to gauge the quality of outputs and outcomes. The formula is Reports Accepted without Amendment / Reports Filed - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures error rates in regulatory filings - data quality, restatements, corrections. Regulators weight reporting reliability heavily when calibrating supervision intensity, and chronic small errors erode credibility faster than occasional large ones. Errors born of data lineage defects need fixing upstream, not in the reporting spreadsheet. Read with master data source alignment and submission rejection and query rates.

## Formula

```
RRA-R = Reports Accepted without Amendment / Reports Filed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1594 (batch 6)
