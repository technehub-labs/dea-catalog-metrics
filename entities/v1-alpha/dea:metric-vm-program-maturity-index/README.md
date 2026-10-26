# dea:metric-vm-program-maturity-index

Candidate Performance Metric record for **VM Program Maturity Index** (VMPMI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vm-program-maturity-index`
- **Name:** VM Program Maturity Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VMPMI

## 2. Definition

Within Vulnerability & Exposure Management, VM Program Maturity Index (VMPMI) is used to gauge capability maturity or development. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Composite Program Capability Score; the result is stated in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures progress against a vulnerability-management maturity model spanning discovery, prioritization, remediation, and verification. It shows whether the program is becoming structurally capable rather than just busy. Self-assessed maturity indexes drift toward optimism without external validation. Read with vulnerability remediation SLA attainment and exploitability-weighted risk score trend.

## Formula

```
VMPMI = Composite Program Capability Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2812 (batch 7)
