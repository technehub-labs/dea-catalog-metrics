# dea:metric-unused-table-ratio

Candidate Performance Metric record for **Unused Table Ratio** (UTR-DB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unused-table-ratio`
- **Name:** Unused Table Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UTR-DB

## 2. Definition

Within Database & Data Platform Operations, Unused Table Ratio (UTR-DB) is used to gauge how efficiently resources are converted into outputs. The formula is Tables with No Access in 90 Days / Tables - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Software sector.

## Formula

```
Tables with No Access in 90 Days / Tables
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3245 (batch 7)
