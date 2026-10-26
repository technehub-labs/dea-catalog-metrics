# dea:metric-cloud-network-segmentation-conformance

Candidate Performance Metric record for **Cloud Network Segmentation Conformance** (CNSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-network-segmentation-conformance`
- **Name:** Cloud Network Segmentation Conformance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CNSC

## 2. Definition

A Cloud Security Posture Management indicator, Cloud Network Segmentation Conformance (CNSC) quantifies exposure to adverse outcomes. It is defined as Environments Matching Segmentation Standard / Environments; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether cloud network architecture conforms to segmentation standards. Flat cloud networks let a compromised workload reach everything. Conformance measured by design documents rather than runtime flow analysis is theoretical. Read with network segment compliance and cloud compliance framework coverage.

## Formula

```
CNSC = Environments Matching Segmentation Standard / Environments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3318 (batch 7)
