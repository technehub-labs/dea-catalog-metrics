# dea:metric-remote-diagnostics-resolution-rate

Candidate Performance Metric record for **Remote Diagnostics Resolution Rate** (RDRR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-remote-diagnostics-resolution-rate`
- **Name:** Remote Diagnostics Resolution Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RDRR-F

## 2. Definition

Remote Diagnostics Resolution Rate (RDRR-F) measures how efficiently resources are converted into outputs in the Field Maintenance & Technical Field Service (Deep Dive) domain. It is computed as Resolutions via Remote Diagnostics / Diagnosable Issues, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of field-service issues resolved without a site visit. Every remote resolution saves a truck roll, which in dispersed geographies can be half the cost base. Resolution quality matters: temporarily cleared symptoms become repeat visits. Read with truck roll resolution rate and first-time fix rate - field.

## Formula

```
RDRR-F = Resolutions via Remote Diagnostics / Diagnosable Issues
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2910 (batch 7)
