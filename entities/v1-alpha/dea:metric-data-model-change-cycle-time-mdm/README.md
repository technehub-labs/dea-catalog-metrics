# dea:metric-data-model-change-cycle-time-mdm

Candidate Performance Metric record for **Data Model Change Cycle Time (MDM)** (DMCCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-model-change-cycle-time-mdm`
- **Name:** Data Model Change Cycle Time (MDM)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DMCCT

## 2. Definition

Data Model Change Cycle Time (MDM) (DMCCT) captures how efficiently resources are converted into outputs for organizations tracking master data management. Its calculation is Days from Model Change Request to Production, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Days from Model Change Request to Production
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3651 (batch 8)
