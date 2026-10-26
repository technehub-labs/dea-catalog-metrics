# dea:metric-truck-roll-resolution-rate

Candidate Performance Metric record for **Truck Roll Resolution Rate** (TRRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-truck-roll-resolution-rate`
- **Name:** Truck Roll Resolution Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TRRR

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Truck Roll Resolution Rate (TRRR) quantifies how efficiently resources are converted into outputs. It is computed as Issues Resolved without Truck Roll via Remote Support / Issues, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of issues resolved on-site after a technician dispatch. Truck rolls are the most expensive resolution channel, so their necessity and success rate drive field economics. High resolution on unnecessary rolls (solvable remotely) still wastes money. Read with remote diagnostics resolution rate and first-time fix rate - field.

## Formula

```
Issues Resolved without Truck Roll via Remote Support / Issues
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2909 (batch 7)
