# dea:metric-subsidy-per-passenger-trip

Candidate Performance Metric record for **Subsidy per Passenger Trip** (SPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-subsidy-per-passenger-trip`
- **Name:** Subsidy per Passenger Trip
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPT

## 2. Definition

Subsidy per Passenger Trip (SPT) measures the economic value created or preserved in the Public Transit domain. The formula is (Operating Cost - Fare Revenue) / Trips - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Public transit sector.

## 3. Context

Subsidy per passenger trip measures the public funding required per rider after fares, and it is the transit metric that most directly frames the public-funding debate - the question of what society pays so an individual can ride. Its honesty problem is allocation depth: fully loaded subsidy includes not just operating shortfall but capital amortization, debt service, and paratransit costs (which run multiples of fixed-route cost per trip), so headline figures quoted without those layers understate reality. Mode comparison is where the metric gets political - per-trip subsidy for rail versus bus versus demand-responsive service differ by an order of magnitude in some systems. Read with farebox recovery ratio as its companion, mobility outcomes per subsidy dollar, and distributional analysis - a subsidy concentrated on low-income riders is policy success, not inefficiency.

## Formula

```
(Operating Cost - Fare Revenue) / Trips
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1008 (batch 3)
