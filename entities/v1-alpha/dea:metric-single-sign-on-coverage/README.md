# dea:metric-single-sign-on-coverage

Candidate Performance Metric record for **Single Sign-On Coverage** (SSOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-sign-on-coverage`
- **Name:** Single Sign-On Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSOC

## 2. Definition

Single Sign-On Coverage (SSOC) measures exposure to adverse outcomes in the Digital Workplace & Collaboration domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Applications behind SSO / Applications, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of applications accessible through the SSO identity platform rather than local credentials. It is simultaneously a security metric (orphaned credentials are attack surface), a productivity metric (password friction), and an offboarding hygiene metric. Count apps behind the SSO proxy, not those merely federated on paper, and include shadow SaaS in the denominator. Read with orphaned account findings and access review pass rates.

## Formula

```
SSOC = Applications behind SSO / Applications
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_workplace_collaboration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1476 (batch 5)
