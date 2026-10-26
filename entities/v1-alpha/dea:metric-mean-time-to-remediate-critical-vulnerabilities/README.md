# dea:metric-mean-time-to-remediate-critical-vulnerabilities

Candidate Performance Metric record for **Mean Time to Remediate - Critical Vulnerabilities** (MTTRCV2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-remediate-critical-vulnerabilities`
- **Name:** Mean Time to Remediate - Critical Vulnerabilities
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTRCV2

## 2. Definition

Mean Time to Remediate - Critical Vulnerabilities (MTTRCV2) captures how efficiently resources are converted into outputs for organizations tracking vulnerability & exposure management. The formula is Days to Patch Critical Vulnerabilities - reported in days. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average time to fix critical-severity vulnerabilities in production. Criticals are the ones attackers actually exploit, often within days of disclosure. The mean conceals stragglers; percentiles and aging reports matter more. Read with internet-facing critical exposure time and vulnerability remediation SLA attainment.

## Formula

```
Days to Patch Critical Vulnerabilities
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2798 (batch 7)
