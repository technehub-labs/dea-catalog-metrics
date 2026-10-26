# dea:metric-cost-per-originated-loan

Candidate Performance Metric record for **Cost per Originated Loan** (CPOL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-originated-loan`
- **Name:** Cost per Originated Loan
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPOL

## 2. Definition

Cost per Originated Loan (CPOL) captures how efficiently resources are converted into outputs for organizations tracking banking retail lending (deep dive). It is computed as Origination Costs / Loans Originated, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Banking.

## 3. Context

Measures fully loaded acquisition cost per funded loan - marketing, origination, underwriting, personnel. It is the efficiency summary of the lending front book, and it is the dial that channel investment, automation, and partner economics move. Cost per loan without quality (EPD, early delinquency) is a false metric, since cheap origination of bad loans is expensive. Read with first payment default rate and approval-rate throughput.

## Formula

```
Origination Costs / Loans Originated
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2087 (batch 6)
