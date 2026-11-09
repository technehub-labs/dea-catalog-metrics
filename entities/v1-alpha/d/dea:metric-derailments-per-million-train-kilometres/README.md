# dea:metric-derailments-per-million-train-kilometres

Candidate Performance Metric record for **Derailments per Million Train Kilometres** (DPMT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-derailments-per-million-train-kilometres`
- **Name:** Derailments per Million Train Kilometres
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPMT

## 2. Definition

A Rail Transport indicator, Derailments per Million Train Kilometres (DPMT) quantifies exposure to adverse outcomes. It is computed as Derailments / Train Kilometres x 1,000,000, expressed in events per thousand or million (scaled). Its use is concentrated in Rail. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Derailments per million train kilometres measures the catastrophic-risk metric of rail safety, and it is where the industry's engineering rigor concentrates - the FRA and European safety agencies track it obsessively because derailments are the mechanism for the worst rail outcomes (hazardous material releases, passenger casualties). The good news is decades-long improvement, driven by improved track inspection technology, better bogie design, and wayside detection systems - but the tail events dominate risk: hazmat derailments like East Palestine show that a single low-probability event carries massive consequence. Track-related causes dominate the distribution, so the metric is largely an infrastructure-quality measure. Read with cause-category distribution (track versus equipment versus human factors), broken-rail detection coverage, wayside detector network density, and traffic-weighted risk exposure.

## Formula

```
DPMT = Derailments / Train Kilometres x 1,000,000
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
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 997 (batch 3)
