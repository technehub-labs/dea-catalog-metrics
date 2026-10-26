# dea:metric-network-availability-deep-dive

Candidate Performance Metric record for **Network Availability (Deep Dive)** (NA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-availability-deep-dive`
- **Name:** Network Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NA-D

## 2. Definition

Network Availability (Deep Dive) (NA-D) measures the utilization or availability of capacity in the Telecom Network Operations (Deep Dive) domain. It is computed as Available Time / Total Time, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Telecommunications.

## 3. Context

Measures the accessibility of telecom services - cell sites, RAN availability, core network uptime. Availability is the license-to-exist metric of telecom: customers tolerate nothing, regulators measure it, and enterprise SLAs attach penalties. Averaging across the network hides the market-level outages that drive churn and regulatory attention, so read market-level and incident-duration distributions. Read with service-quality regulator reporting and proactive fault detection ratio.

## Formula

```
Available Time / Total Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2125 (batch 6)
