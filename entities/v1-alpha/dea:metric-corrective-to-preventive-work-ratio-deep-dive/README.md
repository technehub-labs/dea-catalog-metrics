# dea:metric-corrective-to-preventive-work-ratio-deep-dive

Candidate Performance Metric record for **Corrective-to-Preventive Work Ratio (Deep Dive)** (CPPW-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-corrective-to-preventive-work-ratio-deep-dive`
- **Name:** Corrective-to-Preventive Work Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPPW-D

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Corrective-to-Preventive Work Ratio (Deep Dive) (CPPW-D) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Corrective Hours / Preventive Hours, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the balance of reactive repairs versus scheduled preventive work in field operations. A corrective-heavy ratio signals firefighting economics and predictable future downtime. Moving the ratio requires customer cooperation with access windows, not just internal will. Read with preventive maintenance compliance - field and MTBF - field assets.

## Formula

```
Corrective Hours / Preventive Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2928 (batch 7)
