# dea:metric-fraud-rate-transaction-value

Candidate Performance Metric record for **Fraud Rate (Transaction Value)** (FRTV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-rate-transaction-value`
- **Name:** Fraud Rate (Transaction Value)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FRTV

## 2. Definition

Fraud Rate (Transaction Value) (FRTV) captures exposure to adverse outcomes for organizations tracking payments & fintech. It is computed as Fraudulent Transaction Value / Total Transaction Value, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Payments & fintech.

## 3. Context

Fraud rate by transaction value measures fraud losses as a share of total processed volume, and it is the primary risk-metric in card network rules - Visa and Mastercard monitor it against program thresholds (like 0.9 percent for standard programs) where breaches trigger fines or mandatory remediation, even termination. Value-based measurement weights large-ticket fraud more than count-based, aligning the metric with economic harm. The operational subtlety is allocation: fraud can be measured at authorization, at settlement, or at charge-off, each giving materially different numbers, and networks measure issuers and acquirers differently. Read with chargeback rate, false decline rate, and fraud-loss-per-attempt economics for the full risk-cost picture.

## Formula

```
FRTV = Fraudulent Transaction Value / Total Transaction Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 776 (batch 2)
