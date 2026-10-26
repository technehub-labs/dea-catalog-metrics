# dea:metric-encryption-at-rest-coverage

Candidate Performance Metric record for **Encryption at Rest Coverage** (EARC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-encryption-at-rest-coverage`
- **Name:** Encryption at Rest Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EARC

## 2. Definition

Encryption at Rest Coverage (EARC) addresses exposure to adverse outcomes and is a fixture of cloud security posture management reporting. It is defined as Storage Services Encrypted at Rest / Storage Services; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Storage Services Encrypted at Rest / Storage Services
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3306 (batch 7)
