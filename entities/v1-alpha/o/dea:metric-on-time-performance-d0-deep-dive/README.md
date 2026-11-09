# dea:metric-on-time-performance-d0-deep-dive

Candidate Performance Metric record for **On-Time Performance - D0 (Deep Dive)** (OTP-D0) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-performance-d0-deep-dive`
- **Name:** On-Time Performance - D0 (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OTP-D0

## 2. Definition

Within Airline Operations (Deep Dive), On-Time Performance - D0 (Deep Dive) (OTP-D0) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Departures within 0 Minutes of Schedule / Departures, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Airlines practice.

## 3. Context

Measures flights departing at or within zero minutes of schedule. D0 is the operational-discipline metric of airlines: on-time departures cascade into on-time arrivals across the network, and the push-back moment is where controllable factors (boarding, turnaround, fuelling) are decided. D0 success from padded schedules is schedule honesty theater. Read with schedule padding analysis and turnaround process compliance.

## Formula

```
OTP-D0 = Departures within 0 Minutes of Schedule / Departures
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2249 (batch 6)
