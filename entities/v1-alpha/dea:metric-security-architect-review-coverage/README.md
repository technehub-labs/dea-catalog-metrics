# dea:metric-security-architect-review-coverage

Candidate Performance Metric record for **Security Architect Review Coverage** (SARC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-architect-review-coverage`
- **Name:** Security Architect Review Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SARC

## 2. Definition

Within Application Security (AppSec), Security Architect Review Coverage (SARC) is used to gauge exposure to adverse outcomes. Its calculation is Material Changes with Security Review / Material Changes, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## 3. Context

Measures the share of significant changes receiving architectural security review. Architect review catches systemic design risks tools cannot see. Reviews without authority to block launch are advisory decoration. Read with security gate enforcement rate and threat modeling coverage (Applications).

## Formula

```
Material Changes with Security Review / Material Changes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3335 (batch 7)
