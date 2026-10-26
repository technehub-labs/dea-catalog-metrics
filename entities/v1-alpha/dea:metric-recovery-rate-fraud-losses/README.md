# dea:metric-recovery-rate-fraud-losses

Candidate Performance Metric record for **Recovery Rate (Fraud Losses)** (RRFL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-rate-fraud-losses`
- **Name:** Recovery Rate (Fraud Losses)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRFL

## 2. Definition

Recovery Rate (Fraud Losses) (RRFL) measures the economic value created or preserved in the Enterprise Fraud & Financial Crime Management domain. Its calculation is Fraud Losses Recovered / Total Fraud Losses, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much of fraud losses are actually recovered. Recovery converts detected fraud from pure loss to partial loss. Recovery rates concentrate in payment-recoverable schemes; others recover near zero. Read with fraud loss ratio and chargeback recovery rate.

## Formula

```
Fraud Losses Recovered / Total Fraud Losses
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3761 (batch 8)
