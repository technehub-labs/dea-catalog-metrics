# dea:metric-loan-application-approval-rate

Candidate Performance Metric record for **Loan Application Approval Rate** (LAAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-application-approval-rate`
- **Name:** Loan Application Approval Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LAAR

## 2. Definition

Loan Application Approval Rate (LAAR) captures how effectively a process or entity achieves its intended outcome for organizations tracking retail banking & lending. Its calculation is Approved Applications / Applications Received, measured in percent (%). It originates from and is most used in Banking practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of loan applications approved. It matters because it balances access to credit against portfolio quality, and sudden swings signal credit-cycle risk. Chasing approval volume by lowering credit standards books future defaults. Read with Early Payment Delinquency Rate and Non-Performing Loan Ratio for new vintages to confirm approvals are sound.

## Formula

```
Approved Applications / Applications Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 834 (batch 3)
