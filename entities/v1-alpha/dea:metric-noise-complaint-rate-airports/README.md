# dea:metric-noise-complaint-rate-airports

Candidate Performance Metric record for **Noise Complaint Rate (Airports)** (NCR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noise-complaint-rate-airports`
- **Name:** Noise Complaint Rate (Airports)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NCR-A

## 2. Definition

Noise Complaint Rate (Airports) (NCR-A) measures the engagement or satisfaction of the people involved in the Airport Operations (Deep Dive) domain. It is computed as Complaints per 1,000 Aircraft Movements, expressed in events per thousand or million (scaled). Its use is concentrated in Aviation. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Complaints per 1,000 Aircraft Movements
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2282 (batch 6)
