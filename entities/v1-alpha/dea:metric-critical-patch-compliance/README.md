# dea:metric-critical-patch-compliance

Candidate Performance Metric record for **Critical Patch Compliance** (CPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-patch-compliance`
- **Name:** Critical Patch Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPC

## 2. Definition

A Cybersecurity indicator, Critical Patch Compliance (CPC) quantifies conformance to standards, plans, or obligations. It is defined as Critical Patches Applied within SLA / Critical Patches Released; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of systems patched within policy windows for critical vulnerabilities. It matters because unpatched criticals are the cheapest attack path for adversaries. Teams can hit compliance by granting risk exceptions or excluding end-of-life systems from scope. Read with Attack Surface Exposure and Vulnerability Remediation Time to confirm compliance reflects genuine risk reduction.

## Formula

```
Critical Patches Applied within SLA / Critical Patches Released
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 322 (batch 1)
