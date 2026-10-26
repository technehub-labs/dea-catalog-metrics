# dea:metric-mean-time-to-respond-security

Candidate Performance Metric record for **Mean Time to Respond - Security** (MTTR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-respond-security`
- **Name:** Mean Time to Respond - Security
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTR-S

## 2. Definition

Within SecOps & Security Operations Center, Mean Time to Respond - Security (MTTR-S) is used to gauge how efficiently resources are converted into outputs. The formula is Minutes from Confirmed Alert to Response Initiated - reported in minutes. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average time from alert to an analyst actively working the incident. Response delay lets attackers deepen access while the clock runs. Response measured as ticket assignment rather than substantive action is easy to game. Read with MTTD - security and SOC cost per investigated incident.

## Formula

```
MTTR-S = Minutes from Confirmed Alert to Response Initiated
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2773 (batch 7)
