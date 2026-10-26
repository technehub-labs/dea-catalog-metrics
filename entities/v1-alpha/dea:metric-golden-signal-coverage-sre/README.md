# dea:metric-golden-signal-coverage-sre

Candidate Performance Metric record for **Golden Signal Coverage (SRE)** (GSCOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-golden-signal-coverage-sre`
- **Name:** Golden Signal Coverage (SRE)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GSCOV

## 2. Definition

Golden Signal Coverage (SRE) (GSCOV) addresses capability maturity or development and is a fixture of sre & observability standard measures reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Services Instrumented for Latency, Traffic, Errors, Saturation / Services; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures how completely the four golden signals (latency, traffic, errors, saturation) are monitored for critical services. Golden signals are the minimum viable observability for any production service. Coverage without alerting on the signals is instrumentation, not monitoring. Read with SLI coverage rate and service dependency mapping currency.

## Formula

```
Services Instrumented for Latency, Traffic, Errors, Saturation / Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4382 (batch 11)
