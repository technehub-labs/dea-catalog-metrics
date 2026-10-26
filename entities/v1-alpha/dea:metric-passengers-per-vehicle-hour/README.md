# dea:metric-passengers-per-vehicle-hour

Candidate Performance Metric record for **Passengers per Vehicle Hour** (PPVH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passengers-per-vehicle-hour`
- **Name:** Passengers per Vehicle Hour
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPVH

## 2. Definition

Passengers per Vehicle Hour (PPVH) measures how efficiently resources are converted into outputs in the Public Transit domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Boardings / Vehicle Revenue Hours, expressed in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Public transit.

## 3. Context

Passengers per vehicle hour measures transit productivity - ridership relative to the operating resource consumed - and it is the efficiency metric that determines service sustainability: high-productivity routes can justify frequency while low ones are candidates for restructuring or alternative modes (demand-responsive, feeder). The metric's strategic use is route-network optimization - transit agencies use it to allocate service hours where they generate the most mobility. But it embeds an equity tension: low-ridership routes often serve transit-dependent populations, so pure productivity optimization can strand the riders with the fewest alternatives. Read with productivity by route and time-of-day, cost per passenger trip, subsidy per passenger by route, and coverage-versus-productivity service balance per the agency's policy goals.

## Formula

```
Boardings / Vehicle Revenue Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1001 (batch 3)
