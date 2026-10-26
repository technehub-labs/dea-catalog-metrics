# dea:metric-cold-chain-excursion-rate-logistics

Candidate Performance Metric record for **Cold Chain Excursion Rate (Logistics)** (CCER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cold-chain-excursion-rate-logistics`
- **Name:** Cold Chain Excursion Rate (Logistics)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCER

## 2. Definition

Cold Chain Excursion Rate (Logistics) (CCER) addresses exposure to adverse outcomes and is a fixture of supply chain standard measures (deep dive) reporting. The formula is Shipments with Temperature Excursion / Monitored Shipments - reported in events per thousand or million (scaled). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Shipments with Temperature Excursion / Monitored Shipments
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4274 (batch 10)
