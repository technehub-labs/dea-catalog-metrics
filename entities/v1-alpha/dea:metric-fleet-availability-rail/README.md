# dea:metric-fleet-availability-rail

Candidate Performance Metric record for **Fleet Availability (Rail)** (FAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-availability-rail`
- **Name:** Fleet Availability (Rail)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FAR

## 2. Definition

Within Rail Transport, Fleet Availability (Rail) (FAR) is used to gauge the utilization or availability of capacity. It is computed as Serviceable Trains / Total Fleet, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Rail.

## 3. Context

Fleet availability measures the share of trains serviceable at any time, and it is the capacity metric that underlies everything else in rail operations - cancellations and short-formations trace back to insufficient availability, and maintenance programs exist to maximize it. Availability is a maintenance-program quality metric: predictive maintenance (condition monitoring of bearings, doors, traction systems) trades intervention frequency against availability, and the backlog discipline (how much deferred maintenance accumulates) is the honest health indicator. Sub-fleet variation is diagnostic - older stock drags the average while new fleets run hot. Read with availability by unit class, maintenance backlog trend, distance-based reliability (MDBF), and availability-weighted age - a young fleet with poor availability signals a design or maintenance-contract problem rather than asset age.

## Formula

```
Serviceable Trains / Total Fleet
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 992 (batch 3)
