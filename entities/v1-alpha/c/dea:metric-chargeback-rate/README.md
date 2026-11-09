# dea:metric-chargeback-rate

Candidate Performance Metric record for **Chargeback Rate** (CBKR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-chargeback-rate`
- **Name:** Chargeback Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CBKR

## 2. Definition

Chargeback Rate (CBKR) addresses exposure to adverse outcomes and is a fixture of payments & fintech reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Chargebacks / Total Transactions, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Payments & fintech practice.

## 3. Context

Chargeback rate is disputed transactions as a share of total count, and it is the payments industry's disciplinary mechanism - exceed network thresholds (typically around 0.9 percent for Visa) and the merchant enters monitoring programs with fees, remediation requirements, and eventual termination risk. Chargebacks are a three-faced metric: genuine fraud (criminal), friendly fraud (customers disputing legitimate charges), and service disputes (product quality issues), and treating them as one problem guarantees miscalibrated response. Pre-arbitration and representment win rates determine how much of the measured rate is actually a loss. Read with dispute reason-code distribution, refund policy flexibility (generous refunds often reduce chargebacks), and fraud rate to decompose cause.

## Formula

```
CBKR = Chargebacks / Total Transactions
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 777 (batch 2)
