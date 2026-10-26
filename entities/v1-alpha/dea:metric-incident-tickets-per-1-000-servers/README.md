# dea:metric-incident-tickets-per-1-000-servers

Candidate Performance Metric record for **Incident Tickets per 1,000 Servers** (ITPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-tickets-per-1-000-servers`
- **Name:** Incident Tickets per 1,000 Servers
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ITPS

## 2. Definition

A Data Center & Cloud Operations indicator, Incident Tickets per 1,000 Servers (ITPS) quantifies the quality of outputs and outcomes. The formula is Incident Tickets / Servers x 1,000 - reported in events per thousand or million (scaled). It is a standard measure in the Technology & data centers sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Incident Tickets / Servers x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1098 (batch 4)
