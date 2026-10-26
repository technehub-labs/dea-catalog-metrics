# dea:metric-cost-per-transaction-processed

Candidate Performance Metric record for **Cost per Transaction Processed** (CPT-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-transaction-processed`
- **Name:** Cost per Transaction Processed
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPT-P

## 2. Definition

Cost per Transaction Processed (CPT-P) addresses how efficiently resources are converted into outputs and is a fixture of payments & fintech reporting. It is computed as Total Processing Cost / Transactions, expressed in currency per unit. It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Payments & fintech.

## 3. Context

Measures total processing cost per payment or transaction. It matters because payment economics are scale-and-cost games where basis points decide winners. It can be cut by deferring fraud-loss costs into a separate ledger or under-investing in reliability that later breaches. Read with Transaction Success Rate and Fraud Loss Rate to confirm unit cost is not bought with quality.

## Formula

```
Total Processing Cost / Transactions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 782 (batch 2)
