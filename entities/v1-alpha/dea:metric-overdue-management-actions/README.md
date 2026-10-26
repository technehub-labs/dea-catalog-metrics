# dea:metric-overdue-management-actions

Candidate Performance Metric record for **Overdue Management Actions** (OMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overdue-management-actions`
- **Name:** Overdue Management Actions
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OMA

## 2. Definition

Overdue Management Actions (OMA) captures exposure to adverse outcomes for organizations tracking internal audit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Actions Past Due Date; the result is stated in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the count and age of management actions past their agreed due dates. It matters because overdue actions reveal whether audit commitments are honored or performative. Owners can reset due dates to clear the overdue list without remediating anything. Read with Management Action Closure Rate and Audit Finding Acceptance Rate to detect date-shuffling versus real progress.

## Formula

```
Actions Past Due Date
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 616 (batch 2)
