# dea:metric-loan-loss-provision-ratio

Candidate Performance Metric record for **Loan Loss Provision Ratio** (LLPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-loss-provision-ratio`
- **Name:** Loan Loss Provision Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LLPR

## 2. Definition

Loan Loss Provision Ratio (LLPR) measures exposure to adverse outcomes in the Banking & Financial Services domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Loan Loss Provisions / Gross Loans - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Financial services sector.

## 3. Context

Measures loan loss provisions relative to the gross loan portfolio. It matters as the forward-looking cushion for expected credit losses and a signal of portfolio quality. Banks can under-provision in good times to flatter earnings, only to take painful catch-up charges later. Read with Non-Performing Loan Ratio and Net Charge-Off Rate to test whether provisioning keeps pace with actual credit deterioration.

## Formula

```
Loan Loss Provisions / Gross Loans
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 43 (batch 1)
