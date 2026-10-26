# dea:metric-transit-security-incident-rate

Candidate Performance Metric record for **Transit Security Incident Rate** (TSIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transit-security-incident-rate`
- **Name:** Transit Security Incident Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TSIR

## 2. Definition

Transit Security Incident Rate (TSIR) captures exposure to adverse outcomes for organizations tracking public transit (deep dive). The formula is Incidents per 100,000 Journeys - reported in events per thousand or million (scaled). It is a standard measure in the Public Transit sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Incidents per 100,000 Journeys
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2416 (batch 6)
