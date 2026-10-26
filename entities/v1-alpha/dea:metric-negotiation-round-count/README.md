# dea:metric-negotiation-round-count

Candidate Performance Metric record for **Negotiation Round Count** (NRC-CL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-negotiation-round-count`
- **Name:** Negotiation Round Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NRC-CL

## 2. Definition

Negotiation Round Count (NRC-CL) addresses how efficiently resources are converted into outputs and is a fixture of contract lifecycle management reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Average Redline Cycles before Execution, expressed in times per period. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
NRC-CL = Average Redline Cycles before Execution
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3697 (batch 8)
