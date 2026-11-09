# dea:metric-supply-chain-attestation-coverage

Candidate Performance Metric record for **Supply Chain Attestation Coverage** (SCATC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-chain-attestation-coverage`
- **Name:** Supply Chain Attestation Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCATC

## 2. Definition

Within Application Security (AppSec), Supply Chain Attestation Coverage (SCATC) is used to gauge exposure to adverse outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Builds with Signed Provenance / Production Builds; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of build artifacts and dependencies carrying verified provenance attestations. Attestations make software provenance checkable rather than trusted. Attestations not verified at deploy time are collector's items. Read with supply chain integrity verification rate and SBOM coverage.

## Formula

```
SCATC = Builds with Signed Provenance / Production Builds
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
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3339 (batch 7)
