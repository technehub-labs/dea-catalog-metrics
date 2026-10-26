# dea:metric-multi-factor-authentication-coverage

Candidate Performance Metric record for **Multi-Factor Authentication Coverage** (MFAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-multi-factor-authentication-coverage`
- **Name:** Multi-Factor Authentication Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MFAC

## 2. Definition

A Identity & Access Management Operations indicator, Multi-Factor Authentication Coverage (MFAC) quantifies exposure to adverse outcomes. The formula is Identities Enrolled in MFA / Eligible Identities - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of user accounts protected by MFA. MFA blocks the dominant initial access vector: credential theft and phishing. Coverage excluding service accounts, VPN, and legacy apps leaves the side doors open. Read with privileged MFA coverage and phishing-resistant authentication coverage.

## Formula

```
Identities Enrolled in MFA / Eligible Identities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2817 (batch 7)
