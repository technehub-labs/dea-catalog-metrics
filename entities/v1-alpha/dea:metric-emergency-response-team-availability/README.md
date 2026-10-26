# dea:metric-emergency-response-team-availability

Candidate Performance Metric record for **Emergency Response Team Availability** (ERTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-response-team-availability`
- **Name:** Emergency Response Team Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERTA

## 2. Definition

Emergency Response Team Availability (ERTA) addresses the utilization or availability of capacity and is a fixture of crisis management & emergency response reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as ERT Shifts Fully Staffed / Shifts in Period, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ERTA = ERT Shifts Fully Staffed / Shifts in Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3541 (batch 8)
