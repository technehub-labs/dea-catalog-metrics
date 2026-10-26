# dea:metric-system-availability

Candidate Performance Metric record for **System Availability** (SYS-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-availability`
- **Name:** System Availability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SYS-A

## 2. Definition

System Availability (SYS-A) addresses the quality of outputs and outcomes and is a fixture of it service management reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Uptime / Scheduled Availability; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of time a system is operational and accessible to users - the foundational service metric of IT, conventionally expressed in the nines shorthand where each additional nine is a tenfold improvement: three nines tolerates about 9 hours of downtime per year, five nines about 5 minutes. The strategic significance is asymmetry of arithmetic: availability targets compound across dependencies - a service built on ten dependent systems each at 99.9 percent has a raw composite below 99 percent without redundancy - which is why architecture, not operations heroics, determines what availability is achievable. Read with the cost of downtime: the right target is set by business impact per minute, and engineering beyond the point where marginal reliability cost exceeds downtime cost is gold-plating.

## Formula

```
Uptime / Scheduled Availability
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 311 (batch 1)
