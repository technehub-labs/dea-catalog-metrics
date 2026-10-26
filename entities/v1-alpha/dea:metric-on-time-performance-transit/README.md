# dea:metric-on-time-performance-transit

Candidate Performance Metric record for **On-Time Performance (Transit)** (OTP-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-performance-transit`
- **Name:** On-Time Performance (Transit)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OTP-T

## 2. Definition

On-Time Performance (Transit) (OTP-T) addresses the quality of outputs and outcomes and is a fixture of public transit reporting. Its calculation is Trips Departing Key Stops within Threshold / Trips, measured in percent (%). It originates from and is most used in Public transit practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

On-time performance measures the share of transit trips within schedule tolerance, and for public transit it carries a distinctive equity dimension - riders who depend on transit (shift workers, those without cars) experience lateness as employment risk, not inconvenience, which is why transit OTP is a social-outcome metric in a way airline OTP is not. Headway-based measurement is the honest approach for high-frequency service: passengers at a stop care about wait time, not whether a specific run matched its timetable, so scheduled-headway adherence beats run-based punctuality. Bunching (buses arriving in pairs after gaps) is the system-failure mode OTP must capture. Read with headway-adherence distribution, bunching incidence, travel-time variability by time-of-day, and stop-level wait-time experience rather than terminal-only measurement.

## Formula

```
OTP-T = Trips Departing Key Stops within Threshold / Trips
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1000 (batch 3)
