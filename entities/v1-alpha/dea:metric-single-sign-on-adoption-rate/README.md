# dea:metric-single-sign-on-adoption-rate

Candidate Performance Metric record for **Single Sign-On Adoption Rate** (SSOAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-sign-on-adoption-rate`
- **Name:** Single Sign-On Adoption Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSOAR

## 2. Definition

Within Identity & Access Management Operations, Single Sign-On Adoption Rate (SSOAR) is used to gauge capability maturity or development. The formula is Applications Integrated with SSO / Applications - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of applications authenticating through the central identity provider. Every app outside SSO is a separate credential store, phishing surface, and offboarding gap. Adoption that exempts legacy and third-party apps preserves the worst offenders. Read with joiner-mover-leaver processing timeliness and MFA coverage.

## Formula

```
Applications Integrated with SSO / Applications
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
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2831 (batch 7)
