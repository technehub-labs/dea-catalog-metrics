# dea:metric-it-cost-as-percentage-of-revenue

Candidate Performance Metric record for **IT Cost as Percentage of Revenue** (ITCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-it-cost-as-percentage-of-revenue`
- **Name:** IT Cost as Percentage of Revenue
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ITCR

## 2. Definition

A IT Service Management indicator, IT Cost as Percentage of Revenue (ITCR) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total IT Cost / Revenue, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Total IT spend over revenue - the headline ratio of technology economics that boards use to ask the simplest question: are we spending too much on IT. The answer is always relative: the level varies several-fold across industries by digital intensity, and even within industries by business model (an insurer with a direct channel and one with brokers have different technology needs at the same revenue). Strategic use is decomposition rather than the total: run-versus-change spend (keeping lights on versus building new capability) is the ratio that carries strategy content, since a run share above 70 percent means technology consumes its budget standing still. Trend against digital ambition matters most - rising spend without rising digital revenue share is the pattern that deserves interrogation.

## Formula

```
ITCR = Total IT Cost / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 314 (batch 1)
