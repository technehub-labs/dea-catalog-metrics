# dea:metric-ground-control-incident-rate

Candidate Performance Metric record for **Ground Control Incident Rate** (GCIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ground-control-incident-rate`
- **Name:** Ground Control Incident Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GCIR

## 2. Definition

Within Metals & Mining Operations (Deep Dive), Ground Control Incident Rate (GCIR) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Ground Failure Incidents / 200,000 Hours, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Metals & Mining.

## 3. Context

Measures events related to ground stability - falls of ground, squeeze events, support failures - in underground mining. Ground control is the dominant fatal hazard in underground operations, making this rate the safety metric that matters most. Reporting culture determines the number: near-miss suppression makes the rate look safe while conditions worsen. Read with seismic monitoring trends and support quality audits.

## Formula

```
GCIR = Ground Failure Incidents / 200,000 Hours
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
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1843 (batch 6)
