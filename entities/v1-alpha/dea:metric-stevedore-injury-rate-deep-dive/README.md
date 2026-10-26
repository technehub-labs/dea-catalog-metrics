# dea:metric-stevedore-injury-rate-deep-dive

Candidate Performance Metric record for **Stevedore Injury Rate (Deep Dive)** (SIR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stevedore-injury-rate-deep-dive`
- **Name:** Stevedore Injury Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIR-D

## 2. Definition

A Maritime Shipping (Deep Dive) indicator, Stevedore Injury Rate (Deep Dive) (SIR-D) quantifies exposure to adverse outcomes. The formula is Injuries per 200,000 Hours - reported in events per thousand or million (scaled). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Maritime sector.

## 3. Context

Measures dockworker injuries against exposure hours. Port operations combine heavy loads, suspended cargo, vehicle movement, and shift work into one of the most hazardous industrial environments, making injury performance both a moral and operational continuity metric. Lashing and driving operations dominate injury patterns, so targeted programs beat general safety campaigns. Read with near-miss reporting rates and equipment-maintenance interactions.

## Formula

```
SIR-D = Injuries per 200,000 Hours
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2440 (batch 6)
