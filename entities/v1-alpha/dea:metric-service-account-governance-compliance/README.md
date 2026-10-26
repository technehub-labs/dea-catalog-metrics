# dea:metric-service-account-governance-compliance

Candidate Performance Metric record for **Service Account Governance Compliance** (SAGC-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-account-governance-compliance`
- **Name:** Service Account Governance Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAGC-IAM

## 2. Definition

Service Account Governance Compliance (SAGC-IAM) addresses conformance to standards, plans, or obligations and is a fixture of identity & access management operations reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Service Accounts with Owner and Review / Service Accounts - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of non-human accounts meeting ownership, rotation, and least-privilege requirements. Service accounts outnumber people accounts in modern estates and often hold their highest privileges. Unowned, never-rotated credentials are the classic pivot point in breaches. Read with orphaned account rate and privileged MFA coverage.

## Formula

```
SAGC-IAM = Service Accounts with Owner and Review / Service Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2829 (batch 7)
