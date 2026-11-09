# dea:metric-netting-center-settlement-efficiency

Candidate Performance Metric record for **Netting Center Settlement Efficiency** (NCSE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-netting-center-settlement-efficiency`
- **Name:** Netting Center Settlement Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NCSE

## 2. Definition

A Corporate Treasury (Deep Dive) indicator, Netting Center Settlement Efficiency (NCSE) quantifies how efficiently resources are converted into outputs. It is computed as Netted Intercompany Flows / Gross Flows, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
NCSE = Netted Intercompany Flows / Gross Flows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2191 (batch 6)
