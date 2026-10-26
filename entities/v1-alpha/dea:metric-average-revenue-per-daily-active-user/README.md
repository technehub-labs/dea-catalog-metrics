# dea:metric-average-revenue-per-daily-active-user

Candidate Performance Metric record for **Average Revenue per Daily Active User** (ARPDAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-daily-active-user`
- **Name:** Average Revenue per Daily Active User
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ARPDAU

## 2. Definition

A Gaming indicator, Average Revenue per Daily Active User (ARPDAU) quantifies the economic value created or preserved. It is defined as Daily Revenue / Daily Active Users; the result is stated in currency per unit. In Gaming, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Revenue divided by daily active users, typically per day - the monetization-efficiency metric of live gaming, expressing what a day of engagement is worth across the whole player base. Its strategic significance is the separation of the two levers that produce it: ARPDAU is average revenue per paying user times payer share, and the decomposition is the diagnosis - a high ARPDAU on thin payer share is a whale-dependent economy, while a lower ARPDAU on broad payer share is a healthier distribution of monetization - and the design interventions differ entirely. The benchmark context is genre-bound: casual, mid-core, and casino-genre ARPDAU norms differ by an order of magnitude, so cross-genre comparison is meaningless. Read with the content-event calendar: ARPDAU moves with the update and event cycle, so the trend is read around the cadence - a title whose ARPDAU decays between events is monetizing its content rather than its player relationships.

## Formula

```
Daily Revenue / Daily Active Users
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 703 (batch 2)
