# dea:metric-shift-left-security-scan-coverage

Candidate Performance Metric record for **Shift-Left Security Scan Coverage** (SLSSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shift-left-security-scan-coverage`
- **Name:** Shift-Left Security Scan Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLSSC

## 2. Definition

Shift-Left Security Scan Coverage (SLSSC) measures capability maturity or development in the DevSecOps & Application Security Engineering domain. Its calculation is Pipelines with Security Scanning at Build Time / Pipelines, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of code changes scanned for security issues at commit or build time rather than post-deployment. Catching flaws while code is still open halves remediation cost and reduces vulnerable code shipped. Pre-commit scans are shallow by design, so coverage alone says nothing about finding quality. Read with DAST coverage of attack surface and mean time to remediate code vulnerability.

## Formula

```
Pipelines with Security Scanning at Build Time / Pipelines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2748 (batch 7)
