# dea:metric-kyc-remediation-backlog-ratio

Candidate Performance Metric record for **KYC Remediation Backlog Ratio** (KRB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-kyc-remediation-backlog-ratio`
- **Name:** KYC Remediation Backlog Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** KRB

## 2. Definition

A Insurance Fraud & Financial Crime indicator, KYC Remediation Backlog Ratio (KRB) quantifies conformance to standards, plans, or obligations. It is computed as Files Requiring Update / Total Customer Files, expressed in percent (%). Its use is concentrated in Financial Services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the volume of customer files needing KYC refresh or remediation against processing capacity. Aged remediation backlogs are the regulatory-audit scarlet letter of financial crime compliance, and they indicate either process under-capacity or risk appetite misalignment. Backlog composition matters most - high-risk files aging in queue is the finding that becomes enforcement. Read with remediation aging distribution and risk-tier throughput.

## Formula

```
KRB = Files Requiring Update / Total Customer Files
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2470 (batch 6)
