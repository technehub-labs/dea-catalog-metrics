# dea:metric-security-test-debt-closure-rate

Candidate Performance Metric record for **Security Test Debt Closure Rate** (STDCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-test-debt-closure-rate`
- **Name:** Security Test Debt Closure Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STDCR

## 2. Definition

Within DevSecOps & Application Security Engineering, Security Test Debt Closure Rate (STDCR) is used to gauge conformance to standards, plans, or obligations. It is defined as Security Findings Remediated per SLA / Findings; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the pace at which known, accepted security test exceptions are remediated relative to their agreed timelines. Debt accrues when deadlines slip while new vulnerabilities keep arriving. High closure rates can hide aggressive risk-acceptance of findings rather than genuine reduction. Read with security gate enforcement rate and mean time to remediate code vulnerability.

## Formula

```
Security Findings Remediated per SLA / Findings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2756 (batch 7)
