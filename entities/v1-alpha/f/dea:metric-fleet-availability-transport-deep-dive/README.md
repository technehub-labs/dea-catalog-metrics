# dea:metric-fleet-availability-transport-deep-dive

Candidate Performance Metric record for **Fleet Availability (Transport) (Deep Dive)** (FADD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-availability-transport-deep-dive`
- **Name:** Fleet Availability (Transport) (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FADD

## 2. Definition

A Airline & Transportation Standard Measures (Deep Dive) indicator, Fleet Availability (Transport) (Deep Dive) (FADD) quantifies the utilization or availability of capacity. It is computed as Aircraft Serviceable Days / Fleet Days, expressed in percent (%). Its use is concentrated in Airlines & Aviation. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of the fleet serviceable and available for schedule. Availability is the operational ceiling on utilization and completion. Availability excluding aircraft in planned maintenance overstates. Read with aircraft daily utilization (Deep Dive) and AOG (aircraft on ground) events.

## Formula

```
FADD = Aircraft Serviceable Days / Fleet Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4289 (batch 10)
