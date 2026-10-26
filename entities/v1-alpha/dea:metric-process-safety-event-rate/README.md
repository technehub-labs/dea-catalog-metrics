# dea:metric-process-safety-event-rate

Candidate Performance Metric record for **Process Safety Event Rate** (PSER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-safety-event-rate`
- **Name:** Process Safety Event Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSER

## 2. Definition

A Oil & Gas indicator, Process Safety Event Rate (PSER) quantifies exposure to adverse outcomes. The formula is Process Safety Events / Total Hours Worked x 1,000,000 - reported in events per thousand or million (scaled). It is a standard measure in the Oil & gas sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Process safety event rate measures releases of hazardous substances, fires, explosions, and near-loss-of-containment events - the low-frequency, high-consequence failures that personal safety metrics miss. The distinction is fundamental: injury rates can trend to zero while process safety degrades (the Texas City refinery explosion happened at a site with celebrated personal safety performance), which is why the industry separates Tier 1 and Tier 2 process safety events from personnel safety. The deep lesson from decades of investigation reports is that PSEs come from degraded management systems - deferred maintenance, alarm floods, procedure drift - visible in leading indicators long before events. Read with mechanical integrity backlog, safety-critical equipment outage rates, alarm system health, and management-of-change discipline.

## Formula

```
Process Safety Events / Total Hours Worked x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 889 (batch 3)
