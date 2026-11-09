# dea:metric-sca-vulnerable-dependency-detection-rate

Candidate Performance Metric record for **SCA - Vulnerable Dependency Detection Rate** (SCAVDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sca-vulnerable-dependency-detection-rate`
- **Name:** SCA - Vulnerable Dependency Detection Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCAVDR

## 2. Definition

SCA - Vulnerable Dependency Detection Rate (SCAVDR) measures exposure to adverse outcomes in the DevSecOps & Application Security Engineering domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Known Vulnerable Dependencies Detected before Release / Total Found, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how completely software composition analysis identifies known-vulnerable libraries across the codebase. Most modern applications are mostly open source, so unscanned dependencies are unmanaged risk. Detection depends on accurate inventories and transitive-dependency resolution, which lagging tooling quietly misses. Read with SBOM coverage and open critical vulnerability count.

## Formula

```
SCAVDR = Known Vulnerable Dependencies Detected before Release / Total Found
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2751 (batch 7)
