# dea:metric-train-punctuality

Candidate Performance Metric record for **Train Punctuality** (TRP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-train-punctuality`
- **Name:** Train Punctuality
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TRP

## 2. Definition

Train Punctuality (TRP) addresses the quality of outputs and outcomes and is a fixture of rail transport reporting. It is defined as Trains Arriving within Tolerance of Schedule / Trains Run; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Rail, it is a recognized element of the standard performance toolkit.

## 3. Context

Train punctuality measures the share of trains arriving within a tolerance (commonly 5-15 minutes) of schedule, and it is the public-facing performance metric of rail - the number regulators publish, passengers experience, and franchise or concession contracts monetize through penalties and bonuses. The tolerance definition is the game: 5 minutes for intercity is honest, 15 for commuter is forgiving, and measures can count arrival at final destination only (hiding en-route lateness) or origin departure (hiding en-route delay). Punctuality is a network property: single-track bottlenecks, junction congestion, and cascading delays mean the system is only as strong as its constrained nodes. Read with delay-minute attribution by cause (infrastructure, rolling stock, external, operator), right-time-versus-recovery punctuality, and cancellation rate alongside since a high-punctuality operation can cancel its way to the number.

## Formula

```
Trains Arriving within Tolerance of Schedule / Trains Run
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 990 (batch 3)
