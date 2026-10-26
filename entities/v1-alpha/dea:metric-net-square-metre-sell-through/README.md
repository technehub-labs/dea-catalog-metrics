# dea:metric-net-square-metre-sell-through

Candidate Performance Metric record for **Net Square Metre Sell-Through** (NSMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-square-metre-sell-through`
- **Name:** Net Square Metre Sell-Through
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NSMS

## 2. Definition

Net Square Metre Sell-Through (NSMS) measures the economic value created or preserved in the Events & Exhibitions domain. The formula is Sold Exhibition Area / Sellable Area - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Media & Entertainment sector.

## 3. Context

Measures sold exhibition space against available space. It is the capacity utilization of events, and its rate integrity decides both revenue and attendee experience (dense but navigable floors sell better next cycle). Late-cycle discounting to fill space erodes the rate that full-price exhibitors paid. Read with exhibitor rebook rate and attendance-quality feedback.

## Formula

```
Sold Exhibition Area / Sellable Area
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** events_exhibitions
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1934 (batch 6)
