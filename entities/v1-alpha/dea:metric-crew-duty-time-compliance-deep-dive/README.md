# dea:metric-crew-duty-time-compliance-deep-dive

Candidate Performance Metric record for **Crew Duty Time Compliance (Deep Dive)** (CDTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crew-duty-time-compliance-deep-dive`
- **Name:** Crew Duty Time Compliance (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDTC

## 2. Definition

Within Airline Operations (Deep Dive), Crew Duty Time Compliance (Deep Dive) (CDTC) is used to gauge conformance to standards, plans, or obligations. It is defined as Duty Periods within FTL Limits / Duty Periods; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Airlines, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures adherence to regulated crew duty and rest requirements. It is the safety-critical compliance metric of airline operations: fatigue rules carry regulatory force, and violations ground flights at minimum, with enforcement and license consequences above that. Compliance stress concentrates on disruption days, so measure disrupted-day compliance, not calendar averages. Read with crew-pairing robustness and fatigue-report review rates.

## Formula

```
Duty Periods within FTL Limits / Duty Periods
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2259 (batch 6)
