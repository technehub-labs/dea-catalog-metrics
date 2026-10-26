# dea:metric-secret-scanning-coverage

Candidate Performance Metric record for **Secret Scanning Coverage** (SSC-AS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-secret-scanning-coverage`
- **Name:** Secret Scanning Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSC-AS

## 2. Definition

Secret Scanning Coverage (SSC-AS) captures exposure to adverse outcomes for organizations tracking application security (appsec). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Repositories with Secret Scanning / Repositories - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
Repositories with Secret Scanning / Repositories
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3325 (batch 7)
