# dea:metric-least-privilege-compliance-ratio

Candidate Performance Metric record for **Least Privilege Compliance Ratio** (LPCR-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-least-privilege-compliance-ratio`
- **Name:** Least Privilege Compliance Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LPCR-IAM

## 2. Definition

Least Privilege Compliance Ratio (LPCR-IAM) captures exposure to adverse outcomes for organizations tracking identity & access management operations. It is defined as Accounts with Only Required Entitlements / Sampled; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of access grants conforming to least-privilege policy. Excess privilege multiplies both breach impact and accidental-outage blast radius. Compliance scored against permissive policy baselines is self-congratulation. Read with privileged account ratio and access recertification completion rate.

## Formula

```
Accounts with Only Required Entitlements / Sampled
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
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2826 (batch 7)
