# dea:metric-sanctions-screening-coverage

Candidate Performance Metric record for **Sanctions Screening Coverage** (SSC-FC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sanctions-screening-coverage`
- **Name:** Sanctions Screening Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSC-FC

## 2. Definition

Sanctions Screening Coverage (SSC-FC) addresses conformance to standards, plans, or obligations and is a fixture of insurance fraud & financial crime reporting. It is computed as Transactions Screened / In-Scope Transactions, expressed in percent (%). Its use is concentrated in Financial Services. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of customers, transactions, and counterparties screened against sanctions lists. Sanctions exposure carries strict-liability consequences - regulators penalize even undetected accidental breaches - and coverage gaps are the failure mode that turns routine business into enforcement events. Coverage must include beneficial owners and payment chains, not just named parties. Read with false-positive management quality and list-update timeliness.

## Formula

```
Transactions Screened / In-Scope Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2469 (batch 6)
