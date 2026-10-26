# dea:metric-patch-compliance-rate

Candidate Performance Metric record for **Patch Compliance Rate** (PCR-VM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patch-compliance-rate`
- **Name:** Patch Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCR-VM

## 2. Definition

Patch Compliance Rate (PCR-VM) measures conformance to standards, plans, or obligations in the Vulnerability & Exposure Management domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Assets Fully Patched per Policy / Assets, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of systems current on required patches within policy windows. Patching remains the highest-volume risk-reduction activity in most estates. Compliance measured against optional baselines or with unmapped systems excluded is illusory. Read with scan coverage - asset base and mean time to remediate - critical vulnerabilities.

## Formula

```
PCR-VM = Assets Fully Patched per Policy / Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2804 (batch 7)
