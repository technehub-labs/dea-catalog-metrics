# dea:metric-prime-cost-percentage

Candidate Performance Metric record for **Prime Cost Percentage** (PCP-R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-prime-cost-percentage`
- **Name:** Prime Cost Percentage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCP-R

## 2. Definition

Prime Cost Percentage (PCP-R) measures the economic value created or preserved in the Restaurants domain. It is defined as (Food Cost + Labor Cost) / Revenue; the result is stated in percent (%). In Restaurants, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Prime cost - food plus beverage cost plus labor cost, as a percentage of sales - is the restaurant metric that captures most of the controllable P&L, and operators track it as the single composite number that determines whether a restaurant can be profitable at all: the industry rule of thumb holds that prime cost around 60-65 percent leaves enough margin for occupancy and overhead, while higher prime costs are structurally very difficult to overcome. The composite's value is exactly its aggregation: any operator can optimize one component at the expense of another (cheaper ingredients requiring more skilled labor, or vice versa), and prime cost closes that loophole. Read with component trend decomposition to locate the driver, margin versus prime cost scatter across units (revealing operator capability differences), and mix effects when average check changes.

## Formula

```
(Food Cost + Labor Cost) / Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurants
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 937 (batch 3)
