# dea:metric-access-recertification-completion-rate

Candidate Performance Metric record for **Access Recertification Completion Rate** (ARCR-IAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-access-recertification-completion-rate`
- **Name:** Access Recertification Completion Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ARCR-IAM

## 2. Definition

Access Recertification Completion Rate (ARCR-IAM) addresses conformance to standards, plans, or obligations and is a fixture of identity & access management operations reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Reviews Completed by Deadline / Reviews Due - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of required access reviews completed on schedule with decisions recorded. Recertification is the periodic backstop against accumulated entitlement drift. Rubber-stamp approvals (99% confirm rates) indicate review theater. Read with segregation of duties violation rate and least privilege compliance ratio.

## Formula

```
Reviews Completed by Deadline / Reviews Due
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2824 (batch 7)
