# dea:metric-mdm-cost-per-million-records

Candidate Performance Metric record for **MDM Cost per Million Records** (MDMCPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mdm-cost-per-million-records`
- **Name:** MDM Cost per Million Records
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDMCPR

## 2. Definition

MDM Cost per Million Records (MDMCPR) measures how efficiently resources are converted into outputs in the Master Data Management domain. It is computed as Annual MDM Spend / Records in Millions, expressed in currency per unit. It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Annual MDM Spend / Records in Millions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3654 (batch 8)
