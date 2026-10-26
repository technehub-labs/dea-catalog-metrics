# dea:metric-fleet-downtime-percentage

Candidate Performance Metric record for **Fleet Downtime Percentage** (FDP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-downtime-percentage`
- **Name:** Fleet Downtime Percentage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FDP

## 2. Definition

Fleet Downtime Percentage (FDP) addresses the utilization or availability of capacity and is a fixture of logistics & transportation reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Vehicle Downtime Days / Fleet Available Days, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Logistics practice.

## 3. Context

Measures the share of vehicle time unavailable for service due to breakdowns or maintenance. It matters because every down vehicle shrinks capacity and forces expensive rentals or missed deliveries. Teams can mask it by counting awaiting-parts vehicles as technically available. Read with Preventive Maintenance Compliance and Vehicle Utilization to confirm uptime is earned through maintenance, not deferred into future failures.

## Formula

```
Vehicle Downtime Days / Fleet Available Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 203 (batch 1)
