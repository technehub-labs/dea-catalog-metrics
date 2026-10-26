# dea:metric-noc-ticket-volume-per-operator-per-shift

Candidate Performance Metric record for **NOC Ticket Volume per Operator per Shift** (NOC-TVS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-ticket-volume-per-operator-per-shift`
- **Name:** NOC Ticket Volume per Operator per Shift
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NOC-TVS

## 2. Definition

A Network Operations Center (Deep Dive) indicator, NOC Ticket Volume per Operator per Shift (NOC-TVS) quantifies the utilization or availability of capacity. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Tickets Handled / Operator Shift, expressed in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Tickets Handled / Operator Shift
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2858 (batch 7)
