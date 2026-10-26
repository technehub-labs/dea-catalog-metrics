# dea:metric-capacity-utilization-venues

Candidate Performance Metric record for **Capacity Utilization (Venues)** (CUV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-utilization-venues`
- **Name:** Capacity Utilization (Venues)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CUV

## 2. Definition

Capacity Utilization (Venues) (CUV) addresses the utilization or availability of capacity and is a fixture of entertainment venues & attractions reporting. Its calculation is Tickets Sold / Ticketable Capacity, measured in percent (%). It originates from and is most used in Media & Entertainment practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures attendance or use against available capacity. It is the revenue-efficiency floor of venues: fixed costs dominate, so utilization swings profit directly, but chronic saturation degrades experience and caps per-capita spend. Peak versus off-peak utilization tells the pricing story. Read with per capita spend (Venues) and event-mix yield analysis.

## Formula

```
Tickets Sold / Ticketable Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** entertainment_venues_attractions
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1947 (batch 6)
