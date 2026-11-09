# dea:metric-recycling-recovery-rate

Candidate Performance Metric record for **Recycling Recovery Rate** (RCR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recycling-recovery-rate`
- **Name:** Recycling Recovery Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCR-E

## 2. Definition

Recycling Recovery Rate (RCR-E) addresses environmental and social sustainability performance and is a fixture of waste & environmental services reporting. The formula is Materials Recovered for Recycling / Recyclable Materials Received - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Environmental services sector.

## 3. Context

Recycling recovery rate measures the share of a specific material that is captured for recycling relative to what enters the waste stream, and it differs from diversion rate by focusing on material-level efficiency rather than overall tonnage - the question is not just whether material was separated, but whether the system recovers it. Recovery rates expose the gap between collection infrastructure and actual capture: many programs collect a material officially but recover single-digit percentages of what is sold into the market. It is the metric that connects to circular-economy commitments and recycled-content sourcing. Read with end-market demand for the recovered grade (recovery without buyers is landfill), contamination levels, and collection-method capture differentials.

## Formula

```
RCR-E = Materials Recovered for Recycling / Recyclable Materials Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 817 (batch 2)
