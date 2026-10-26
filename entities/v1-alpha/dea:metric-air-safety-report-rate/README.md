# dea:metric-air-safety-report-rate

Candidate Performance Metric record for **Air Safety Report Rate** (ASRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-air-safety-report-rate`
- **Name:** Air Safety Report Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASRR

## 2. Definition

Air Safety Report Rate (ASRR) addresses exposure to adverse outcomes and is a fixture of airline operations (deep dive) reporting. It is defined as Safety Reports per 1,000 Flights; the result is stated in events per thousand or million (scaled). In Airlines, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the frequency of safety reports filed, including near-misses and hazards. Contrary to naive reading, a healthy air safety report rate is high - reporting culture is the precondition of safety management, and falling report rates usually signal fear, not safety. The triage is what matters: report volume read with severity distribution and closure quality. Read with investigation closure aging and just-culture policy adherence.

## Formula

```
Safety Reports per 1,000 Flights
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2264 (batch 6)
