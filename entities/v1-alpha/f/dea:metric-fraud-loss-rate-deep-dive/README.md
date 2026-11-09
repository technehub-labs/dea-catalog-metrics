# dea:metric-fraud-loss-rate-deep-dive

Candidate Performance Metric record for **Fraud Loss Rate (Deep Dive)** (FLR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-loss-rate-deep-dive`
- **Name:** Fraud Loss Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FLR-D

## 2. Definition

Fraud Loss Rate (Deep Dive) (FLR-D) captures exposure to adverse outcomes for organizations tracking insurance fraud & financial crime. It is computed as Fraud Losses / Transaction or Premium Base, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Financial Services.

## 3. Context

Measures fraud losses against premium or exposure volume. It is the exposure metric of insurance financial crime, and its honesty depends on detection: reported fraud loss rates rise with better detection while undetected fraud (application, opportunistic) silently inflates loss ratios attributed to genuine claims. Segment by fraud type, since application, claims, and organized fraud need entirely different controls. Read with detection-rate trends and claims leakage analysis.

## Formula

```
FLR-D = Fraud Losses / Transaction or Premium Base
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2464 (batch 6)
