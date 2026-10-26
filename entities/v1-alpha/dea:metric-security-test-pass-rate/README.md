# dea:metric-security-test-pass-rate

Candidate Performance Metric record for **Security Test Pass Rate** (STPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-test-pass-rate`
- **Name:** Security Test Pass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STPR

## 2. Definition

Security Test Pass Rate (STPR) addresses conformance to standards, plans, or obligations and is a fixture of application security (appsec) reporting. Its calculation is Pipeline Runs Passing Security Gates / Runs, measured in percent (%). It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Pipeline Runs Passing Security Gates / Runs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3330 (batch 7)
