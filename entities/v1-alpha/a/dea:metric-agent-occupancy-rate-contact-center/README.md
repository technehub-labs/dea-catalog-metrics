# dea:metric-agent-occupancy-rate-contact-center

Candidate Performance Metric record for **Agent Occupancy Rate (Contact Center)** (AOR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agent-occupancy-rate-contact-center`
- **Name:** Agent Occupancy Rate (Contact Center)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AOR-CC

## 2. Definition

A Contact Center Standard Measures (Deep Dive) indicator, Agent Occupancy Rate (Contact Center) (AOR-CC) quantifies the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Handle Time / Scheduled Time, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
AOR-CC = Handle Time / Scheduled Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4319 (batch 10)
