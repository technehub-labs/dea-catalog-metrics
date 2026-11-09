# dea:metric-noc-ticket-resolution-within-sla

Candidate Performance Metric record for **NOC Ticket Resolution within SLA** (NCTRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-ticket-resolution-within-sla`
- **Name:** NOC Ticket Resolution within SLA
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NCTRS

## 2. Definition

A Network Operations Center (Deep Dive) indicator, NOC Ticket Resolution within SLA (NCTRS) quantifies conformance to standards, plans, or obligations. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Tickets Resolved within SLA / Tickets, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of network tickets resolved within committed time windows. SLA attainment is the contract-level promise of the NOC to the business. Averages can be met by neglecting rare but severe long-tail tickets. Read with NOC mean time to resolve and unmonitored critical device count.

## Formula

```
NCTRS = Tickets Resolved within SLA / Tickets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2837 (batch 7)
