# dea:metric-producer-productivity

Candidate Performance Metric record for **Producer Productivity** (PRP-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-producer-productivity`
- **Name:** Producer Productivity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRP-I

## 2. Definition

Producer Productivity (PRP-I) measures how efficiently resources are converted into outputs in the Insurance Distribution & Brokerage domain. It is defined as Premium Written per Producer per Period; the result is stated in currency value. Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance distribution, it is a recognized element of the standard performance toolkit.

## 3. Context

Producer productivity measures revenue per insurance producer or broker, and it is the unit-economics metric of distribution - commissions are the largest cost of insurance distribution, so revenue per producer determines whether the distribution model funds itself. Productivity decomposes into sales activity (policies written), average premium per policy (segment and product mix), and persistency of the book written (a producer whose business lapses early is not productive despite volume). The measurement trap is the deferred-cost structure: commission advances paid on business that later lapses create negative productivity invisible in point-in-time figures. Read with persistency by producer, product mix written, commission-schedule effectiveness, and the tenure curve since new producers ramp slowly and mature producers can plateau.

## Formula

```
PRP-I = Premium Written per Producer per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1156 (batch 4)
