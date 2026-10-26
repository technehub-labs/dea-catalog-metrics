# dea:metric-network-availability

Candidate Performance Metric record for **Network Availability** (NAV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-availability`
- **Name:** Network Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NAV

## 2. Definition

Network Availability (NAV) addresses the quality of outputs and outcomes and is a fixture of telecommunications reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Uptime of Network Services / Total Time, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Telecommunications practice.

## 3. Context

The share of time the network performs within its service commitments - the foundational quality metric of connectivity, conventionally measured against call, data, and coverage standards rather than a simple up-or-down binary, since a network can be up and still failing. Its strategic significance is the regulatory and market double exposure: quality regimes in many markets mandate measurement and publication (with spectrum and roaming consequences), and customers experience outages as brand events regardless of what the SLA said. Read with the availability-versus-experience distinction: cell-level availability and per-user experience diverge as networks load, which is why experience metrics (throughput, latency, drop rates) sit alongside availability in any honest quality picture. The nines arithmetic is unforgiving at scale: minutes of downtime times millions of users is hours of aggregate outage.

## Formula

```
Uptime of Network Services / Total Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 526 (batch 1)
