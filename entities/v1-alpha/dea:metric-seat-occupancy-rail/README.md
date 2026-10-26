# dea:metric-seat-occupancy-rail

Candidate Performance Metric record for **Seat Occupancy (Rail)** (SO-R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-seat-occupancy-rail`
- **Name:** Seat Occupancy (Rail)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SO-R

## 2. Definition

Seat Occupancy (Rail) (SO-R) addresses the utilization or availability of capacity and is a fixture of rail transport reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Passenger Kilometres Travelled / Seat Kilometres Offered, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Rail practice.

## 3. Context

Seat occupancy measures passengers against seat capacity, and it is the yield metric of passenger rail - the load factor that determines whether a service covers its marginal cost and contributes to fixed infrastructure charges. The metric needs crowding context: occupancy above 100 percent of seats is common at peak (standing passengers) and signals capacity shortage rather than commercial success, while low off-peak occupancy signals scheduling or pricing problems. Peak versus off-peak occupancy split is the strategic number - peak-constrained services can't grow revenue without more trains while off-peak capacity is available. Read with passenger-km per train-km, peak standing-load frequency, yield management adoption (advance-purchase pricing changes the revenue-per-seat calculus), and station-pair demand matrices for service-design insight.

## Formula

```
Passenger Kilometres Travelled / Seat Kilometres Offered
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 993 (batch 3)
