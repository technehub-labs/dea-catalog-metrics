# dea:metric-complaints-per-100-000-boardings

Candidate Performance Metric record for **Complaints per 100,000 Boardings** (CPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaints-per-100-000-boardings`
- **Name:** Complaints per 100,000 Boardings
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPB

## 2. Definition

A Public Transit indicator, Complaints per 100,000 Boardings (CPB) quantifies the quality of outputs and outcomes. Its calculation is Complaints / Boardings x 100,000, measured in events per thousand or million (scaled). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Public transit practice.

## 3. Context

Measures complaint frequency normalized by passenger volume in transit. It matters because it is the public-facing service quality read regulators and media use. Complaint channels that are hard to access suppress the numerator. Read with On-Time Performance and Customer Satisfaction surveys to confirm fewer complaints mean better service, not dimmer signaling.

## Formula

```
Complaints / Boardings x 100,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1005 (batch 3)
