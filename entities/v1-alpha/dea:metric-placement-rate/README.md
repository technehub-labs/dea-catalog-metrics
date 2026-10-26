# dea:metric-placement-rate

Candidate Performance Metric record for **Placement Rate** (PLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-placement-rate`
- **Name:** Placement Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PLR

## 2. Definition

Placement Rate (PLR) measures how effectively a process or entity achieves its intended outcome in the Staffing & Recruiting domain. The formula is Placements / Open Mandates - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Staffing & recruiting sector.

## 3. Context

Placement rate measures the share of candidates or job orders successfully filled, and it is the throughput metric of staffing and recruiting - the business model only earns revenue on completed placements, so the ratio between effort expended and placements closed determines profitability. The measurement distinction is denominator clarity: placements per job order (fill rate) and placements per candidate (candidate conversion) are different metrics with different drivers, and conflating them hides whether the problem is candidate supply or client demand quality. Fill rates vary systematically by role type - high-volume clerical fills far above executive search, so blended rates mislead. Read with time-to-fill (its speed companion), submittal-to-interview and interview-to-offer conversion rates (the funnel), and order-cancellation rates which can flatter fill metrics by removing hard orders from the pool.

## Formula

```
Placements / Open Mandates
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** staffing_recruiting
- **Sector:** staffing_recruiting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1021 (batch 3)
