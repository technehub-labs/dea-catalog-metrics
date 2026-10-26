# dea:metric-metal-recovery-rate-deep-dive

Candidate Performance Metric record for **Metal Recovery Rate (Deep Dive)** (MRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-metal-recovery-rate-deep-dive`
- **Name:** Metal Recovery Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRR-D

## 2. Definition

A Metals & Mining Operations (Deep Dive) indicator, Metal Recovery Rate (Deep Dive) (MRR-D) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Recovered Metal / Contained Metal - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Metals & Mining sector.

## 3. Context

Measures the share of metal content recovered from ore through processing. It converts geology into payable metal, and small recovery percentage changes are worth more than most cost programs at typical margins. Recovery improvements claimed against softer feed (lower grades and easier mineralogy) flatter the process. Read with ore grade variance (Deep Dive) for feed quality and reagent and energy consumption per tonne.

## Formula

```
Recovered Metal / Contained Metal
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1840 (batch 6)
