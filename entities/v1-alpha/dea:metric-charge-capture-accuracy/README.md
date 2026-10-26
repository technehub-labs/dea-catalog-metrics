# dea:metric-charge-capture-accuracy

Candidate Performance Metric record for **Charge Capture Accuracy** (CCA-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-charge-capture-accuracy`
- **Name:** Charge Capture Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCA-H

## 2. Definition

Charge Capture Accuracy (CCA-H) addresses the economic value created or preserved and is a fixture of healthcare revenue cycle reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Charges Captured for Billable Services / Billable Services - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Healthcare sector.

## 3. Context

Measures how completely billable services are captured and coded in patient records. It matters because missed charges are revenue leakage, while coding errors drive compliance risk. Accuracy can be gamed by avoiding complex coding cases rather than mastering them. Read with Claim Denial Rate and Coding Audit findings to confirm capture is both complete and compliant.

## Formula

```
Charges Captured for Billable Services / Billable Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 876 (batch 3)
