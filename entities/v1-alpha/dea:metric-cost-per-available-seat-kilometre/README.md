# dea:metric-cost-per-available-seat-kilometre

Candidate Performance Metric record for **Cost per Available Seat Kilometre** (CASK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-available-seat-kilometre`
- **Name:** Cost per Available Seat Kilometre
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CASK

## 2. Definition

Cost per Available Seat Kilometre (CASK) addresses how efficiently resources are converted into outputs and is a fixture of airlines & aviation reporting. It is defined as Total Operating Cost / Available Seat Kilometres; the result is stated in currency per unit. In Airlines & aviation, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Operating cost divided by available seat-kilometres - the unit-cost metric of aviation, and the universal efficiency currency of the industry: it makes a regional operator with 50-seat aircraft comparable to a widebody intercontinental carrier, because both are cost per unit of the same product - a seat flown a kilometre. Its strategic significance is the cost-structure separation it enables: fuel, crew, maintenance, ownership, and distribution are all expressed per ASK, and the decomposition shows where an airline is structurally efficient versus where cost advantage actually comes from (the low-cost-carrier model is essentially a CASK playbook - single fleet type, secondary airports, direct distribution, dense seating). The honest comparison is stage-length adjusted, since short-haul and long-haul CASK differ systematically on physics and stage mix alone. Read with RASK: an airline can lose money at excellent CASK if revenue is worse, which is why unit cost is only half of any competitiveness argument.

## Formula

```
Total Operating Cost / Available Seat Kilometres
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 650 (batch 2)
