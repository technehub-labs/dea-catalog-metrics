# dea:metric-monthly-active-users

Candidate Performance Metric record for **Monthly Active Users** (MAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monthly-active-users`
- **Name:** Monthly Active Users
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MAU

## 2. Definition

Monthly Active Users (MAU) captures the engagement or satisfaction of the people involved for organizations tracking product management. Its calculation is Unique Active Users per Month, measured in count (items per period). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Unique users engaging in a month - the reach metric that trades DAU's habit-resolution for category-defining scale, and the number that market-size narratives, network-effect arguments, and top-of-funnel valuations actually quote. Its strategic significance is comparability: monthly windows smooth the periodicity of utility products (tax software is active seasonally, travel apps episodically) into a single comparable reach figure, which is why it anchors cross-category benchmarking. The known inflation risks are definitional: passive opens, push-triggered sessions, and multi-device de-duplication conventions all move the count materially, and the honest MAU states its activity definition. Read as DAU/MAU companion rather than alone - a large MAU with a tiny DAU is an audience, not a habit, and the two numbers together say what neither says separately.

## Formula

```
Unique Active Users per Month
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 551 (batch 1)
