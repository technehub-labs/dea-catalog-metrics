# dea:metric-managed-spend-under-contract

Candidate Performance Metric record for **Managed Spend under Contract** (MSUC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-managed-spend-under-contract`
- **Name:** Managed Spend under Contract
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSUC

## 2. Definition

Managed Spend under Contract (MSUC) captures conformance to standards, plans, or obligations for organizations tracking strategic sourcing & supplier performance (deep dive). Its calculation is Contracted Spend / Addressable Spend, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of addressable spend flowing through negotiated contracts. Contracted spend is governed spend: pricing, terms, and risk all improve. Spend classified as managed while buying off-contract is self-deception. Read with addressable spend coverage and contract compliance rate (Procurement).

## Formula

```
MSUC = Contracted Spend / Addressable Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** strategic_sourcing_supplier_performance_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3736 (batch 8)
