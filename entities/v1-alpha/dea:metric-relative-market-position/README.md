# dea:metric-relative-market-position

Candidate Performance Metric record for **Relative Market Position** (RMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-relative-market-position`
- **Name:** Relative Market Position
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RMP

## 2. Definition

A Strategy & Portfolio indicator, Relative Market Position (RMP) quantifies growth over time. Its calculation is Organization Market Share / Largest Competitor Market Share, measured in ratio (x:1 or x). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The firm's market position expressed against its leading competitor - conventionally as a ratio of market shares, which is the arithmetic behind the strategic rules of thumb (market leaders versus followers) that competitive strategy runs on. Its strategic significance is that position, not absolute size, determines the options available: the number-two player can choose confrontation, flanking, or specialization against the leader, while the leader's problem is defending a position everyone aims at, and the same industry looks different from each seat. The ratio form also encodes the stability insight that share gaps are harder to close as they widen, since scale advantages compound - which is why challengers attack segments rather than the whole market. Read with position-versus-relative-cost, since share bought with price concessions and share earned with structural advantage have opposite durability.

## Formula

```
Organization Market Share / Largest Competitor Market Share
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 371 (batch 1)
