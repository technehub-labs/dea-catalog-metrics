# dea:metric-disaster-recovery-test-frequency-compliance

Candidate Performance Metric record for **Disaster Recovery Test Frequency Compliance** (DRTF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-disaster-recovery-test-frequency-compliance`
- **Name:** Disaster Recovery Test Frequency Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRTF

## 2. Definition

A Business Resilience & Continuity indicator, Disaster Recovery Test Frequency Compliance (DRTF) quantifies conformance to standards, plans, or obligations. Its calculation is DR Tests per Standard / DR Tests Required, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether DR tests occur at the frequency policy requires for each criticality tier. Untested recovery is theoretical, and test failure rates reliably surprise organizations that have drifted into nominal compliance. Watch for table-top exercises counted as full failover tests and for scope exclusions that remove the genuinely hard systems. Read with recovery time objective attainment and resilience stress test pass rate.

## Formula

```
DR Tests per Standard / DR Tests Required
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1411 (batch 5)
