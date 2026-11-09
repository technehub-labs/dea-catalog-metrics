# dea:metric-sales-cycle-length

Candidate Performance Metric record for **Sales Cycle Length** (SCL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sales-cycle-length`
- **Name:** Sales Cycle Length
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCL

## 2. Definition

Sales Cycle Length (SCL) addresses how efficiently resources are converted into outputs and is a fixture of sales reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Days from First Contact to Close, Averaged; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the average time from qualified opportunity to closed deal. It matters because shorter cycles free capacity and improve forecast reliability. Teams can shrink it cosmetically by creating opportunities late, after the deal is already decided. Read with Pipeline Coverage Ratio and Average Deal Size to check cycle time against deal complexity rather than pipeline hygiene tricks.

## Formula

```
SCL = Days from First Contact to Close, Averaged
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 92 (batch 1)
