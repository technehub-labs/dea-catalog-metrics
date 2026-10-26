# dea:metric-ready-backlog-coverage-ratio

Candidate Performance Metric record for **Ready Backlog Coverage Ratio** (RBCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ready-backlog-coverage-ratio`
- **Name:** Ready Backlog Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RBCR

## 2. Definition

Ready Backlog Coverage Ratio (RBCR) captures the utilization or availability of capacity for organizations tracking requirements engineering & product discovery. The formula is Sprint-Ready Backlog Items / Planned Sprint Demand - reported in ratio (x:1 or x). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Sprint-Ready Backlog Items / Planned Sprint Demand
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2608 (batch 7)
