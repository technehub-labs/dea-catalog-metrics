# dea:metric-process-cost-per-transaction-deep-dive

Candidate Performance Metric record for **Process Cost per Transaction (Deep Dive)** (PCPT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-cost-per-transaction-deep-dive`
- **Name:** Process Cost per Transaction (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCPT-D

## 2. Definition

Process Cost per Transaction (Deep Dive) (PCPT-D) captures how efficiently resources are converted into outputs for organizations tracking balanced scorecard - internal process perspective. It is computed as Operating Cost / Process Transactions, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the unit economics of standard transactions. Unit cost trends reveal whether scale and automation are delivering. Allocating fixed costs across shrinking volumes can mask efficiency gains. Read with process automation ratio and cost-to-serve.

## Formula

```
Operating Cost / Process Transactions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3084 (batch 7)
