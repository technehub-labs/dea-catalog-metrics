# dea:metric-privileged-account-ratio

Candidate Performance Metric record for **Privileged Account Ratio** (PAR-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privileged-account-ratio`
- **Name:** Privileged Account Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PAR-IAM

## 2. Definition

A Identity & Access Management Operations indicator, Privileged Account Ratio (PAR-IAM) quantifies exposure to adverse outcomes. The formula is Privileged Accounts / Total Accounts - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures privileged accounts as a share of total accounts. A high ratio signals permission sprawl: more admin accounts than the organization genuinely needs. Re-certification programs that rename accounts without removing privilege do not reduce risk. Read with least privilege compliance ratio and standing privilege reduction rate.

## Formula

```
Privileged Accounts / Total Accounts
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2819 (batch 7)
