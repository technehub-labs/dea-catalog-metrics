# dea:metric-invoice-processing-cycle-time

Candidate Performance Metric record for **Invoice Processing Cycle Time** (IPCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-invoice-processing-cycle-time`
- **Name:** Invoice Processing Cycle Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IPCT

## 2. Definition

Invoice Processing Cycle Time (IPCT) measures how efficiently resources are converted into outputs in the Accounts Payable & Receivable Operations (Deep Dive) domain. Its calculation is Days from Receipt to Posted, measured in days. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Days from Receipt to Posted
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3796 (batch 8)
