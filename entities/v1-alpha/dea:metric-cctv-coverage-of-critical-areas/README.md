# dea:metric-cctv-coverage-of-critical-areas

Candidate Performance Metric record for **CCTV Coverage of Critical Areas** (CCVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cctv-coverage-of-critical-areas`
- **Name:** CCTV Coverage of Critical Areas
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCVC

## 2. Definition

A Physical Security Operations indicator, CCTV Coverage of Critical Areas (CCVC) quantifies conformance to standards, plans, or obligations. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Critical Areas under Surveillance / Critical Areas Identified; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of designated critical areas under functional camera coverage. It matters because coverage gaps are discovered only at incident time. Coverage can be counted by camera presence rather than working, useful footage. Read with Camera Uptime and incident review findings to confirm coverage delivers usable evidence.

## Formula

```
Critical Areas under Surveillance / Critical Areas Identified
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1210 (batch 4)
