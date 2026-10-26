# dea:metric-secrets-management-coverage

Candidate Performance Metric record for **Secrets Management Coverage** (SMC-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-secrets-management-coverage`
- **Name:** Secrets Management Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SMC-CS

## 2. Definition

Secrets Management Coverage (SMC-CS) addresses exposure to adverse outcomes and is a fixture of cloud security posture management reporting. It is defined as Secrets in Managed Vault / Secrets in Use; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SMC-CS = Secrets in Managed Vault / Secrets in Use
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3317 (batch 7)
