# dea:metric-recovery-rate-fraud-recoveries-deep-dive

Candidate Performance Metric record for **Recovery Rate - Fraud Recoveries (Deep Dive)** (RFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-rate-fraud-recoveries-deep-dive`
- **Name:** Recovery Rate - Fraud Recoveries (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RFR-D

## 2. Definition

Recovery Rate - Fraud Recoveries (Deep Dive) (RFR-D) captures the economic value created or preserved for organizations tracking insurance fraud & financial crime. It is defined as Fraud Amounts Recovered / Fraud Losses; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of identified fraud losses actually recovered through restitution, subrogation, or legal action. It is the economic-completion metric of fraud programs: detection alone is cost, recovery closes the loop, and low recovery rates signal either weak civil-recovery strategy or cases built for headlines rather than restitution. Recovery timelines run years, so track realization curves. Read with fraud loss rate (Deep Dive) and case-cost economics.

## Formula

```
Fraud Amounts Recovered / Fraud Losses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2468 (batch 6)
