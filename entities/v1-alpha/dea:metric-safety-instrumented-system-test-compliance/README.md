# dea:metric-safety-instrumented-system-test-compliance

Candidate Performance Metric record for **Safety Instrumented System Test Compliance** (SISTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-safety-instrumented-system-test-compliance`
- **Name:** Safety Instrumented System Test Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SISTC

## 2. Definition

Safety Instrumented System Test Compliance (SISTC) addresses conformance to standards, plans, or obligations and is a fixture of oil & gas downstream & refining reporting. It is defined as SIS Function Tests on Schedule / Required; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Oil & Gas, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures completion of scheduled proof tests for safety instrumented functions. SIS testing is the mechanical guarantee that shutdown protection works when demanded, and test deferral is quiet risk accumulation: untested safety functions have untested reliability. Proof-test quality (full function verification, not partial) matters as much as completion. Read with demand-rate and fail-dangerous findings from testing.

## Formula

```
SIS Function Tests on Schedule / Required
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2305 (batch 6)
