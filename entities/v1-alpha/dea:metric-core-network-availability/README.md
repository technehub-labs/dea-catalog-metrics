# dea:metric-core-network-availability

Candidate Performance Metric record for **Core Network Availability** (CNA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-core-network-availability`
- **Name:** Core Network Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CNA

## 2. Definition

A Telecom Network Operations indicator, Core Network Availability (CNA) quantifies the quality of outputs and outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Core Network Uptime / Total Time, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## 3. Context

Core network availability measures the uptime of the primary service infrastructure - the switches, databases, and routing layers that must be up for anything else to work - and it is deliberately separated from total service availability because many degradations occur in edge systems while the core stays green. In regulated industries like telecom, availability carries contractual service-level commitments with penalties, and measurement methodology (which minutes count, maintenance-window treatment, per- versus per-user availability) determines reported figures as much as actual reliability. Redundant architectures are designed so that component failures never reach the availability metric, which is the point. Read with mean time between failures and repair times for components, service-level-credit payouts as the honest cost signal, and affected-customer-weighted availability rather than simple uptime.

## Formula

```
Core Network Uptime / Total Time
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 867 (batch 3)
