# dea:metric-security-gate-enforcement-rate

Candidate Performance Metric record for **Security Gate Enforcement Rate** (SGER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-gate-enforcement-rate`
- **Name:** Security Gate Enforcement Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SGER

## 2. Definition

Within DevSecOps & Application Security Engineering, Security Gate Enforcement Rate (SGER) is used to gauge conformance to standards, plans, or obligations. Its calculation is Releases Blocked by Security Gate when Threshold Exceeded / Threshold Events, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of deployments that passed mandatory security gates without override. Gates only work if failing them actually stops the release. High override rates convert a security program into an approval theater. Read with emergency release ratio and security test debt closure rate.

## Formula

```
Releases Blocked by Security Gate when Threshold Exceeded / Threshold Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2764 (batch 7)
