# dea:metric-invoice-touchless-processing-rate

Candidate Performance Metric record for **Invoice Touchless Processing Rate** (ITPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-invoice-touchless-processing-rate`
- **Name:** Invoice Touchless Processing Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITPR

## 2. Definition

Invoice Touchless Processing Rate (ITPR) captures how efficiently resources are converted into outputs for organizations tracking accounts payable & receivable operations (deep dive). It is computed as Invoices Processed without Manual Intervention / Invoices, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Invoices Processed without Manual Intervention / Invoices
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3795 (batch 8)
