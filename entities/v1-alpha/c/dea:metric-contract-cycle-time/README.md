# dea:metric-contract-cycle-time

Candidate Performance Metric record for **Contract Cycle Time** (CnCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-cycle-time`
- **Name:** Contract Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CnCT

## 2. Definition

Within Legal, Contract Cycle Time (CnCT) is used to gauge how efficiently resources are converted into outputs. Its calculation is Days from Request to Fully Executed Contract, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures elapsed time from contract request to fully executed agreement. It matters because slow legal cycles delay revenue, procurement, and partner momentum. It can be gamed by starting the clock at first lawyer touch rather than the business request. Read with Standard Clause Adoption Rate and legal backlog trends to confirm speed comes from standardization, not corner-cutting.

## Formula

```
CnCT = Days from Request to Fully Executed Contract
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 388 (batch 1)
