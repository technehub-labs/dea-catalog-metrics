# dea:metric-cargo-load-factor

Candidate Performance Metric record for **Cargo Load Factor** (CLF-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cargo-load-factor`
- **Name:** Cargo Load Factor
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CLF-AT

## 2. Definition

Within Airline & Transportation Standard Measures (Deep Dive), Cargo Load Factor (CLF-AT) is used to gauge how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Cargo Tonne-Kilometers Carried / Available Tonne-Kilometers, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Airlines & Aviation practice.

## 3. Context

Measures the utilization of available cargo capacity. Cargo contribution is the quiet margin cushion on passenger networks. Load counted on booked rather than uplifted weight inflates. Read with freight yield per ton-kilometer and cargo capacity utilization trend.

## Formula

```
CLF-AT = Cargo Tonne-Kilometers Carried / Available Tonne-Kilometers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4291 (batch 10)
