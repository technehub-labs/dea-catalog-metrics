# dea:metric-days-in-accounts-receivable

Candidate Performance Metric record for **Days in Accounts Receivable** (DAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-in-accounts-receivable`
- **Name:** Days in Accounts Receivable
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DAR

## 2. Definition

Within Healthcare Revenue Cycle, Days in Accounts Receivable (DAR) is used to gauge how efficiently resources are converted into outputs. It is defined as Total Accounts Receivable / Average Daily Revenue; the result is stated in days. In Healthcare, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Days in accounts receivable measures the average age of unpaid claims - how long revenue sits between service delivery and cash collection, and in healthcare revenue cycle management it is the cash-flow master metric, with high-performing organizations running below 40 days while laggards exceed 60. The metric blends clinical, coding, payer, and process quality: documentation gaps at the point of care become claim rejections weeks later, making AR days a lagging composite of upstream workflow. Its decomposition is where management lives: AR days by payer, by claim type, and by aging bucket (>90 day claims that will likely never be paid should be worked differently than fresh ones). Read with clean claim rate (the leading driver), denial rate by reason code, and percentage of AR older than 90 days.

## Formula

```
Total Accounts Receivable / Average Daily Revenue
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
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 871 (batch 3)
