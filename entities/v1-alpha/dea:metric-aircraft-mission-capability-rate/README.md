# dea:metric-aircraft-mission-capability-rate

Candidate Performance Metric record for **Aircraft Mission Capability Rate** (MCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-mission-capability-rate`
- **Name:** Aircraft Mission Capability Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MCR

## 2. Definition

A Defense & Aerospace indicator, Aircraft Mission Capability Rate (MCR) quantifies the utilization or availability of capacity. It is computed as Aircraft Available for Tasking / Aircraft Assigned, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Defense & aerospace.

## 3. Context

Aircraft mission capability rate measures the share of aircraft able to perform at least one mission - not fully mission capable, but flyable for something - and it is the defense readiness metric that Congress and GAO audit relentlessly. The DoD goal for decades was 80 percent while actual rates across major fleets have often run in the 50-70 percent range, with GAO reports documenting the gap year after year. MC rate blends maintenance capacity, parts availability, and airframe age - an aging fleet's MC rate declines mechanically, so the metric is a fleet-age indicator as much as a maintenance-performance one. Read with full-mission-capable versus partially-capable decomposition, cannibalization rate (a maintenance-debt signal), parts backorder days, and maintainability trends by airframe hours.

## Formula

```
Aircraft Available for Tasking / Aircraft Assigned
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 967 (batch 3)
