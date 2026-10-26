# dea:metric-sli-coverage-rate

Candidate Performance Metric record for **SLI Coverage Rate** (SLIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sli-coverage-rate`
- **Name:** SLI Coverage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SLIC

## 2. Definition

SLI Coverage Rate (SLIC) captures conformance to standards, plans, or obligations for organizations tracking sre & observability standard measures. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Critical Services with Defined SLIs / Critical Services; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures how completely services have defined, measured service level indicators. SLIs are the atoms of reliability management. Coverage weighted by service count rather than traffic-weighted misses the services users actually touch. Read with service level indicator coverage and golden signal coverage (SRE).

## Formula

```
Critical Services with Defined SLIs / Critical Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4378 (batch 11)
