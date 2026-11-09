# dea:metric-claims-cost-per-file-handled

Candidate Performance Metric record for **Claims Cost per File Handled** (CCPF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-cost-per-file-handled`
- **Name:** Claims Cost per File Handled
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCPF

## 2. Definition

A Claims Operations (Insurance) indicator, Claims Cost per File Handled (CCPF) quantifies how efficiently resources are converted into outputs. Its calculation is Total Claims Handling Cost / Claims Handled, measured in currency per unit. It originates from and is most used in Insurance practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures average cost per claim file including indemnity and expenses. It matters because file economics determine claims operation efficiency. Low cost per file can mean underpaying or under-investigating claims that later reopen or litigate. Read with Claims Reopen Rate and Customer Satisfaction to confirm cheap handling is fair handling.

## Formula

```
CCPF = Total Claims Handling Cost / Claims Handled
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 854 (batch 3)
