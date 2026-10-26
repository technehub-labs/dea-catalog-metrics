# dea:metric-days-cash-on-hand

Candidate Performance Metric record for **Days Cash on Hand** (DCOH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-cash-on-hand`
- **Name:** Days Cash on Hand
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DCOH

## 2. Definition

Days Cash on Hand (DCOH) captures exposure to adverse outcomes for organizations tracking treasury & cash management. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Cash and Equivalents / Average Daily Operating Expenses; the result is stated in days. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Operating liquidity divided by average daily operating expense - the specific-days version of liquidity adequacy, favored in healthcare and non-profit sectors where revenue is receivable-heavy and a cash squeeze can arrive while the accrual accounts look healthy. Its strategic significance is the operating-continuity guarantee: it prices how long payroll and suppliers can be met if revenue stops, and in receivable-heavy models the metric is the truth that the income statement hides - profit is an accrual and payroll is a bank debit. The expense-basis choice matters: the honest version uses cash-basis operating expenses including debt service that cannot be deferred, since the point is survivability, and including discretionary spending that would be cut first understates the survivable days. Read with the receivables conversion cycle: days cash rising while days-receivable lengthen indicates liquidity being built by stretching collections, which is a different and less durable source of buffer.

## Formula

```
Cash and Equivalents / Average Daily Operating Expenses
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 599 (batch 2)
