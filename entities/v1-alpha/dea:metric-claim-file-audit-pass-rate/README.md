# dea:metric-claim-file-audit-pass-rate

Candidate Performance Metric record for **Claim File Audit Pass Rate** (CFAP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-file-audit-pass-rate`
- **Name:** Claim File Audit Pass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFAP

## 2. Definition

Claim File Audit Pass Rate (CFAP) addresses conformance to standards, plans, or obligations and is a fixture of insurance claims deep dive reporting. It is computed as Files Meeting Documentation Standards / Files Audited, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Insurance.

## Formula

```
Files Meeting Documentation Standards / Files Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1559 (batch 6)
