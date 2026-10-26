# dea:metric-converting-downtime-rate-paper

Candidate Performance Metric record for **Converting Downtime Rate (Paper)** (CDR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-converting-downtime-rate-paper`
- **Name:** Converting Downtime Rate (Paper)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDR-P

## 2. Definition

Converting Downtime Rate (Paper) (CDR-P) measures the utilization or availability of capacity in the Pulp, Paper & Forest Products domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Converting Downtime / Scheduled Converting Time, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Manufacturing practice.

## Formula

```
CDR-P = Converting Downtime / Scheduled Converting Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pulp_paper_forest_products
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1863 (batch 6)
