# dea:metric-baggage-handling-system-availability

Candidate Performance Metric record for **Baggage Handling System Availability** (BHSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baggage-handling-system-availability`
- **Name:** Baggage Handling System Availability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BHSA

## 2. Definition

Baggage Handling System Availability (BHSA) addresses the quality of outputs and outcomes and is a fixture of airport operations reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is System Uptime / Scheduled Operating Time, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Airports practice.

## Formula

```
System Uptime / Scheduled Operating Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1175 (batch 4)
