# dea:metric-data-center-uptime-deep-dive

Candidate Performance Metric record for **Data Center Uptime (Deep Dive)** (DCU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-center-uptime-deep-dive`
- **Name:** Data Center Uptime (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DCU-D

## 2. Definition

Data Center Uptime (Deep Dive) (DCU-D) measures the utilization or availability of capacity in the Data Centers & Cloud Infrastructure domain. It is computed as Available Hours / Total Hours, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Technology.

## 3. Context

Measures facility availability against tier commitments. Uptime is the contractual product of data centers: SLA credits, churn, and reputation all hang on it, and outage events are industry news. Tier certification should be validated by concurrent-maintainability testing, since design uptime without demonstrated maintenance paths is a claim, not a capability. Read with incident root-cause patterns and redundancy-topology stress tests.

## Formula

```
Available Hours / Total Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2139 (batch 6)
