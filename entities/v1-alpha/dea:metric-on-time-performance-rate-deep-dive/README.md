# dea:metric-on-time-performance-rate-deep-dive

Candidate Performance Metric record for **On-Time Performance Rate (Deep Dive)** (OTPDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-performance-rate-deep-dive`
- **Name:** On-Time Performance Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTPDD

## 2. Definition

On-Time Performance Rate (Deep Dive) (OTPDD) captures the quality of outputs and outcomes for organizations tracking airline & transportation standard measures (deep dive). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Flights within 15 Minutes of Schedule / Flights, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Airlines & Aviation.

## 3. Context

Measures the share of flights departing/arriving within threshold windows. OTP is the most consumer-visible airline reliability metric and contractually significant in some markets. Schedule padding is the classic way to improve OTP without improving operations. Read with flight completion factor and customer satisfaction - airline.

## Formula

```
Flights within 15 Minutes of Schedule / Flights
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4279 (batch 10)
