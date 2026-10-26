# dea:metric-cash-conversion-cycle

Candidate Performance Metric record for **Cash Conversion Cycle** (CCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-conversion-cycle`
- **Name:** Cash Conversion Cycle
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCC

## 2. Definition

Cash Conversion Cycle (CCC) captures how efficiently resources are converted into outputs for organizations tracking finance & accounting. Its calculation is DSO + DIO - DPO, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the number of days between paying for inputs and collecting cash from customers. It matters because every day removed frees working capital that funds growth without new debt. Gaming risk includes stretching suppliers or booking sales early to compress the cycle artificially. Read with Days Inventory Outstanding and Days Sales Outstanding to see which component is actually moving.

## Formula

```
DSO + DIO - DPO
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 22 (batch 1)
