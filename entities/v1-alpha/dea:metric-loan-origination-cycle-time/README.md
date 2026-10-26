# dea:metric-loan-origination-cycle-time

Candidate Performance Metric record for **Loan Origination Cycle Time** (LOCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-origination-cycle-time`
- **Name:** Loan Origination Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LOCT

## 2. Definition

Within Retail Banking & Lending, Loan Origination Cycle Time (LOCT) is used to gauge how efficiently resources are converted into outputs. It is defined as Days from Complete Application to Disbursement; the result is stated in days. Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Banking, it is a recognized element of the standard performance toolkit.

## 3. Context

Loan origination cycle time measures elapsed time from application to funding decision, and it is where customer experience and credit discipline collide - fintech challengers compress mortgage closing from the traditional 45 days toward two weeks, and each day of lag raises abandonment as borrowers shop multiple lenders simultaneously. The decomposition matters because total time is a sum of distinct queues: document collection (usually the largest), appraisal, underwriting, and compliance review, and improvement programs succeed by attacking the true bottleneck, not the average. Cycle time also embeds market conditions: appraisal capacity and volume surges create external delays. Read with fulfillment rate (fast approvals mean nothing if loans die at funding), pull-through by stage, and time-at-each-stage distributions rather than means.

## Formula

```
Days from Complete Application to Disbursement
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 835 (batch 3)
