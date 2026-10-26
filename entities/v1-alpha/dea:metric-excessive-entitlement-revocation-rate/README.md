# dea:metric-excessive-entitlement-revocation-rate

Candidate Performance Metric record for **Excessive Entitlement Revocation Rate** (EERR-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-excessive-entitlement-revocation-rate`
- **Name:** Excessive Entitlement Revocation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EERR-IAM

## 2. Definition

A Identity & Access Management Operations indicator, Excessive Entitlement Revocation Rate (EERR-IAM) quantifies exposure to adverse outcomes. It is computed as Entitlements Revoked after Recertification Flag / Flagged, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Entitlements Revoked after Recertification Flag / Flagged
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2836 (batch 7)
