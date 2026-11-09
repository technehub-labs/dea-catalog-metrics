# dea:metric-policy-issuance-turnaround

Candidate Performance Metric record for **Policy Issuance Turnaround** (PIT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-policy-issuance-turnaround`
- **Name:** Policy Issuance Turnaround
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PIT

## 2. Definition

Policy Issuance Turnaround (PIT) addresses how efficiently resources are converted into outputs and is a fixture of insurance distribution & brokerage reporting. Its calculation is Hours from Application to Policy Issued, measured in hours. It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Insurance distribution practice.

## Formula

```
PIT = Hours from Application to Policy Issued
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1154 (batch 4)
