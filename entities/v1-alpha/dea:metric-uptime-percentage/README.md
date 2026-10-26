# dea:metric-uptime-percentage

Candidate Performance Metric record for **Uptime Percentage** (UP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-uptime-percentage`
- **Name:** Uptime Percentage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UP

## 2. Definition

Uptime Percentage (UP) captures the quality of outputs and outcomes for organizations tracking it service management. It is computed as Available Time / Total Time, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of time an asset or service is available for use - the twin of availability expressed as a proportion, tracked wherever continuous operation carries value: production lines, networks, platforms, and increasingly whole business models. The nines scale gives it strategic texture, because the step from 99 to 99.9 percent is not a rounding improvement but an order-of-magnitude reduction in allowed failure time, and each further nine demands architecturally different investment - redundancy, failover, geographic distribution - not just better operations. Read with duration-of-outage data: the percentage is indifferent between frequent brief interruptions and rare long ones, but customers are not. For assets rather than services, uptime measured against scheduled time (excluding planned maintenance) is the honest utilization-adjacent form, since planned downtime is a choice, not a failure.

## Formula

```
UP = Available Time / Total Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 318 (batch 1)
