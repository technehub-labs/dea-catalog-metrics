# dea:metric-storage-cost-per-unit

Candidate Performance Metric record for **Storage Cost per Unit** (SCPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-storage-cost-per-unit`
- **Name:** Storage Cost per Unit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCPU

## 2. Definition

Storage Cost per Unit (SCPU) captures how efficiently resources are converted into outputs for organizations tracking warehousing. Its calculation is Total Storage Cost / Units Stored, measured in currency per unit. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average warehousing cost per unit stored or handled. It matters because it isolates the real cost of holding inventory beyond purchase price. It can be gamed by allocating fixed warehouse overhead across more units while service degrades. Read with Warehouse Capacity Utilization and Inventory Days of Supply to check unit costs fall for the right reasons.

## Formula

```
Total Storage Cost / Units Stored
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 212 (batch 1)
