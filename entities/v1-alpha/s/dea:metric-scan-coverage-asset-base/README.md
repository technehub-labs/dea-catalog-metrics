# dea:metric-scan-coverage-asset-base

Candidate Performance Metric record for **Scan Coverage - Asset Base** (SCAB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scan-coverage-asset-base`
- **Name:** Scan Coverage - Asset Base
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCAB

## 2. Definition

Scan Coverage - Asset Base (SCAB) captures capability maturity or development for organizations tracking vulnerability & exposure management. Its calculation is Assets Scanned in Cycle / In-Scope Assets, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of known assets receiving regular vulnerability scans. Unscanned assets are unmanaged risk, and CMDB gaps mean invisible assets are invisible risk. Coverage against an incomplete asset inventory silently overstates protection. Read with open critical vulnerability count and attack surface coverage - external scan.

## Formula

```
SCAB = Assets Scanned in Cycle / In-Scope Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2801 (batch 7)
