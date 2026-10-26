# dea:metric-cost-per-invoice-processed-ap

Candidate Performance Metric record for **Cost per Invoice Processed (AP)** (CPIP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-invoice-processed-ap`
- **Name:** Cost per Invoice Processed (AP)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPIP

## 2. Definition

Cost per Invoice Processed (AP) (CPIP) addresses how efficiently resources are converted into outputs and is a fixture of accounts payable & receivable operations (deep dive) reporting. Its calculation is AP Cost / Invoices Processed, measured in currency per unit. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
AP Cost / Invoices Processed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3814 (batch 8)
