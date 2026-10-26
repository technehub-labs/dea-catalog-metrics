# dea:metric-privileged-mfa-coverage

Candidate Performance Metric record for **Privileged MFA Coverage** (PMFAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privileged-mfa-coverage`
- **Name:** Privileged MFA Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMFAC

## 2. Definition

A Identity & Access Management Operations indicator, Privileged MFA Coverage (PMFAC) quantifies exposure to adverse outcomes. Its calculation is Privileged Accounts Enrolled in MFA / Privileged Accounts, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of privileged and administrative accounts protected by MFA. Admin credentials are the keys to the kingdom; a single unprotected one can undo everything else. Coverage that excludes emergency (break-glass) accounts creates a permanent weak point. Read with standing privilege reduction rate and privileged account ratio.

## Formula

```
Privileged Accounts Enrolled in MFA / Privileged Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2818 (batch 7)
