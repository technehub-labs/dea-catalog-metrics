# dea:metric-master-data-coverage-rate

Candidate Performance Metric record for **Master Data Coverage Rate** (MDCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-coverage-rate`
- **Name:** Master Data Coverage Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDCR

## 2. Definition

A Master Data Management indicator, Master Data Coverage Rate (MDCR) quantifies capability maturity or development. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Entities Managed under MDM / Identified Master Entities; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of master data domains and records brought under managed MDM. Unmanaged master data means conflicting truths across systems. Coverage measured against a stale data landscape overstates control. Read with golden record confidence score and master data completeness index.

## Formula

```
MDCR = Entities Managed under MDM / Identified Master Entities
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3635 (batch 8)
