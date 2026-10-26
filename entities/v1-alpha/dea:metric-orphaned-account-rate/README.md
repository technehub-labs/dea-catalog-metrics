# dea:metric-orphaned-account-rate

Candidate Performance Metric record for **Orphaned Account Rate** (OAR-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-orphaned-account-rate`
- **Name:** Orphaned Account Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OAR-IAM

## 2. Definition

Within Identity & Access Management Operations, Orphaned Account Rate (OAR-IAM) is used to gauge exposure to adverse outcomes. It is defined as Accounts without Active Owner / Accounts; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures active accounts not linked to any current employee or owner. Orphans are unmonitored doors that outlive audits and attackers love. Rate against a directory full of stale service and shared accounts understates the problem. Read with joiner-mover-leaver processing timeliness and service account governance compliance.

## Formula

```
Accounts without Active Owner / Accounts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2822 (batch 7)
