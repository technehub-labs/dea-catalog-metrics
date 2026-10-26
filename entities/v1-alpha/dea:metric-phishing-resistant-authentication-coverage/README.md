# dea:metric-phishing-resistant-authentication-coverage

Candidate Performance Metric record for **Phishing-Resistant Authentication Coverage** (PRAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-phishing-resistant-authentication-coverage`
- **Name:** Phishing-Resistant Authentication Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PRAC

## 2. Definition

A Identity & Access Management Operations indicator, Phishing-Resistant Authentication Coverage (PRAC) quantifies exposure to adverse outcomes. It is defined as Identities Using Phishing-Resistant MFA / MFA Identities; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of authentication using phishing-resistant methods (FIDO2/WebAuthn) rather than interceptable OTPs. AI-assisted phishing now defeats SMS and app-based one-time codes at scale. Coverage concentrated on regular users while admins keep OTPs protects the wrong thing. Read with MFA coverage and privileged MFA coverage.

## Formula

```
Identities Using Phishing-Resistant MFA / MFA Identities
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2834 (batch 7)
