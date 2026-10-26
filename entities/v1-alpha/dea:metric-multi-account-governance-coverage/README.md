# dea:metric-multi-account-governance-coverage

Candidate Performance Metric record for **Multi-Account Governance Coverage** (MAGC-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-multi-account-governance-coverage`
- **Name:** Multi-Account Governance Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MAGC-CS

## 2. Definition

Multi-Account Governance Coverage (MAGC-CS) measures governance in the Cloud Security Posture Management domain. The formula is Accounts under Central Landing Zone Policy / Accounts - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of cloud accounts under central guardrails, logging, and account-vending standards. Ungoverned accounts are untracked risk with a URL. Coverage excluding sandbox and experiment accounts preserves a common breach origin. Read with CSPM policy coverage and log source coverage rate.

## Formula

```
Accounts under Central Landing Zone Policy / Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** governance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3316 (batch 7)
