# dea:metric-dast-coverage-of-attack-surface

Candidate Performance Metric record for **DAST Coverage of Attack Surface** (DASC-DV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dast-coverage-of-attack-surface`
- **Name:** DAST Coverage of Attack Surface
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DASC-DV

## 2. Definition

A DevSecOps & Application Security Engineering indicator, DAST Coverage of Attack Surface (DASC-DV) quantifies exposure to adverse outcomes. It is defined as Applications Scanned Dynamically / Applications in Production; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the proportion of externally reachable endpoints and applications exercised by dynamic security testing. DAST sees runtime behavior that static tools miss, including misconfigurations and injection paths. Coverage counted by URL count can hide the deepest, most transaction-heavy flows. Read with attack surface reduction rate and penetration test finding recurrence rate.

## Formula

```
Applications Scanned Dynamically / Applications in Production
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2750 (batch 7)
