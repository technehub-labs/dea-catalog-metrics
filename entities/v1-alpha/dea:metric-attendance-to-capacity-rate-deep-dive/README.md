# dea:metric-attendance-to-capacity-rate-deep-dive

Candidate Performance Metric record for **Attendance-to-Capacity Rate (Deep Dive)** (ATC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attendance-to-capacity-rate-deep-dive`
- **Name:** Attendance-to-Capacity Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ATC-D

## 2. Definition

Attendance-to-Capacity Rate (Deep Dive) (ATC-D) captures the utilization or availability of capacity for organizations tracking sports clubs & leagues (deep dive). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Tickets Sold / Stadium Capacity, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Sports practice.

## 3. Context

Measures stadium or arena fill against available capacity, by competition and event type. It is the demand thermometer of a club: broadcast revenue may dominate the P&L, but attendance drives matchday revenue and the atmosphere that sustains season-ticket demand. No-shows count differently than unsold seats, so distinguish sold from attended. Read with season ticket renewal rate (Deep Dive) and average ticket yield per seat (Deep Dive).

## Formula

```
Tickets Sold / Stadium Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sports_clubs_leagues_deep_dive
- **Sector:** sports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1994 (batch 6)
