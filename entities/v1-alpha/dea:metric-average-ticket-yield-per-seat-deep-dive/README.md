# dea:metric-average-ticket-yield-per-seat-deep-dive

Candidate Performance Metric record for **Average Ticket Yield per Seat (Deep Dive)** (ATYS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-ticket-yield-per-seat-deep-dive`
- **Name:** Average Ticket Yield per Seat (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATYS-D

## 2. Definition

Within Sports Clubs & Leagues (Deep Dive), Average Ticket Yield per Seat (Deep Dive) (ATYS-D) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Ticket Revenue / Available Seats, measured in currency per unit. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Sports practice.

## 3. Context

Measures ticket revenue per seat available, blending price, occupancy, and category mix. It is the yield-management metric of sports venues, and it exposes the classic trade: filling seats with discounting versus protecting average yield. Dynamic pricing performance lives in this number. Read with attendance-to-capacity rate (Deep Dive) and secondary-market price premiums as demand evidence.

## Formula

```
ATYS-D = Ticket Revenue / Available Seats
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1996 (batch 6)
