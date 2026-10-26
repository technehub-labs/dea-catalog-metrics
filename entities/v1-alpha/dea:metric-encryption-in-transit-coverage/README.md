# dea:metric-encryption-in-transit-coverage

Candidate Performance Metric record for **Encryption in Transit Coverage** (EITC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-encryption-in-transit-coverage`
- **Name:** Encryption in Transit Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EITC

## 2. Definition

Encryption in Transit Coverage (EITC) captures exposure to adverse outcomes for organizations tracking cloud security posture management. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Services Enforcing TLS / Network-Exposed Services - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Services Enforcing TLS / Network-Exposed Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3307 (batch 7)
