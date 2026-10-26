# dea:metric-season-ticket-renewal-rate-deep-dive

Candidate Performance Metric record for **Season Ticket Renewal Rate (Deep Dive)** (STRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-season-ticket-renewal-rate-deep-dive`
- **Name:** Season Ticket Renewal Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** STRR-D

## 2. Definition

A Sports Clubs & Leagues (Deep Dive) indicator, Season Ticket Renewal Rate (Deep Dive) (STRR-D) quantifies the retention of customers, users, or assets over time. It is defined as Renewed Season Seats / Eligible Season Seats; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Sports, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of season-ticket holders renewing. It is the recurring-revenue anchor of matchday economics and the purest loyalty signal a club owns, since season-ticket base renewal predicts sellout stability through on-field cycles. Renewal protected by lock-in pricing may conceal weakening affinity, so read satisfaction alongside. Read with attendance-to-capacity rate (Deep Dive) and waitlist depth.

## Formula

```
STRR-D = Renewed Season Seats / Eligible Season Seats
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1995 (batch 6)
