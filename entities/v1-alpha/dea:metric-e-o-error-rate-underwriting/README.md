# dea:metric-e-o-error-rate-underwriting

Candidate Performance Metric record for **E&O Error Rate (Underwriting)** (EOR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-e-o-error-rate-underwriting`
- **Name:** E&O Error Rate (Underwriting)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EOR-U

## 2. Definition

A Insurance Underwriting indicator, E&O Error Rate (Underwriting) (EOR-U) quantifies exposure to adverse outcomes. The formula is Errors and Omissions Incidents / Policies Processed - reported in events per thousand or million (scaled). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Insurance sector.

## Formula

```
Errors and Omissions Incidents / Policies Processed
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1518 (batch 6)
