# dea:metric-overhead-ratio

Candidate Performance Metric record for **Overhead Ratio** (OHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overhead-ratio`
- **Name:** Overhead Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OHR

## 2. Definition

Overhead Ratio (OHR) captures how efficiently resources are converted into outputs for organizations tracking banking & financial services. The formula is Non-Interest Expense / Average Assets - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Financial services sector.

## 3. Context

Non-interest expense over average assets - the banking cost gauge that scales the cost base to balance-sheet size rather than to income, making it insensitive to the rate cycle in a way cost-to-income is not. That independence is its virtue: in a falling-rate year, cost-to-income deteriorates mechanically while overhead ratio isolates whether costs themselves are disciplined. A bank with a heavy branch network and legacy technology will run structurally high; digitization shows up here first, years before it shows in profit. The strategic use is productivity benchmarking across institutions and across time, since the numerator can be decomposed into people, premises, and technology to show exactly where the cost weight sits.

## Formula

```
Non-Interest Expense / Average Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 48 (batch 1)
