# dea:metric-passenger-trip-cost-ratio

Candidate Performance Metric record for **Passenger Trip Cost Ratio** (PTCR-AT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passenger-trip-cost-ratio`
- **Name:** Passenger Trip Cost Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PTCR-AT

## 2. Definition

Within Airline & Transportation Standard Measures (Deep Dive), Passenger Trip Cost Ratio (PTCR-AT) is used to gauge how efficiently resources are converted into outputs. Its calculation is Total Operating Cost / Passengers Carried, measured in currency per unit. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Airlines & Aviation practice.

## 3. Context

Measures the share of a passenger's ticket price consumed by trip cost. It frames unit economics from the passenger's perspective. Ratio improved by unbundling charges while keeping headline fares is definitional arbitrage. Read with cost per available seat kilometer and ancillary revenue per passenger.

## Formula

```
Total Operating Cost / Passengers Carried
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** airline_transportation_standard_measures_deep_dive
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4287 (batch 10)
