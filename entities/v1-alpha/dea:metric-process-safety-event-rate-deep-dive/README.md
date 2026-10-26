# dea:metric-process-safety-event-rate-deep-dive

Candidate Performance Metric record for **Process Safety Event Rate (Deep Dive)** (PSER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-safety-event-rate-deep-dive`
- **Name:** Process Safety Event Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSER-D

## 2. Definition

Process Safety Event Rate (Deep Dive) (PSER-D) captures exposure to adverse outcomes for organizations tracking chemicals & specialty materials. It is defined as Tier 1 and 2 Process Safety Events per 200,000 Hours; the result is stated in events per thousand or million (scaled). In Chemicals, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures loss-of-containment and process safety events against exposure hours in chemical operations. PSE rates are the honest top of the safety pyramid in an industry where catastrophic potential, not injury frequency, defines risk. Event classification determines the number, so guard against down-tiering of near-misses. Read with layers-of-protection audit findings and asset integrity completion rate (Chemicals).

## Formula

```
Tier 1 and 2 Process Safety Events per 200,000 Hours
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals_specialty_materials
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1811 (batch 6)
