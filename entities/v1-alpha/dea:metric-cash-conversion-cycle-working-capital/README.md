# dea:metric-cash-conversion-cycle-working-capital

Candidate Performance Metric record for **Cash Conversion Cycle (Working Capital)** (CCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-conversion-cycle-working-capital`
- **Name:** Cash Conversion Cycle (Working Capital)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCC

## 2. Definition

Cash Conversion Cycle (Working Capital) (CCC) measures how efficiently resources are converted into outputs in the Financial Statement Analysis Ratios (Deep Dive) domain. Its calculation is Days Inventory + Days Receivable - Days Payable, measured in days. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the days between paying for inputs and collecting from customers. It is the single best summary of working capital efficiency. Each day removed is a day of financing freed. Negative cycles (collect before paying) are the retailer's structural advantage. Read with days sales outstanding (Deep Dive) and days payable outstanding (Deep Dive).

## Formula

```
Days Inventory + Days Receivable - Days Payable
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4019 (batch 9)
