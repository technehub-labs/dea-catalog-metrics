# dea:metric-days-sales-outstanding-deep-dive

Candidate Performance Metric record for **Days Sales Outstanding (Deep Dive)** (DSODD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-sales-outstanding-deep-dive`
- **Name:** Days Sales Outstanding (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSODD

## 2. Definition

Days Sales Outstanding (Deep Dive) (DSODD) captures how efficiently resources are converted into outputs for organizations tracking accounts payable & receivable operations (deep dive). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Average Days from Invoice to Collection, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the average time to collect revenue after billing. DSO is where booked revenue becomes actual cash. Averages hide the aging tail where write-offs are born. Read with best possible DSO gap and collections effectiveness index.

## Formula

```
Average Days from Invoice to Collection
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3802 (batch 8)
