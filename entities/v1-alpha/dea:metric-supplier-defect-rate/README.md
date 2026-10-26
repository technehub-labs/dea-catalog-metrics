# dea:metric-supplier-defect-rate

Candidate Performance Metric record for **Supplier Defect Rate** (SDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-defect-rate`
- **Name:** Supplier Defect Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SDR

## 2. Definition

Within Supply Chain, Supplier Defect Rate (SDR) is used to gauge the quality of outputs and outcomes. The formula is Defective Units from Supplier / Units Received - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures defective parts per million (or percentage) received from a supplier. It matters because incoming defects propagate into production downtime, rework, and field failures. Suppliers can massage it by replacing defective lots before inspection counts them, or by disputing defect classifications. Read with Supplier Quality Rating and Incoming Inspection findings to confirm defect accounting survives audit.

## Formula

```
Defective Units from Supplier / Units Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 181 (batch 1)
