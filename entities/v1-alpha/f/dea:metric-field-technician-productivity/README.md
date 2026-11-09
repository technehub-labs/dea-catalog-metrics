# dea:metric-field-technician-productivity

Candidate Performance Metric record for **Field Technician Productivity** (FTP-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-technician-productivity`
- **Name:** Field Technician Productivity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FTP-T

## 2. Definition

Field Technician Productivity (FTP-T) captures how efficiently resources are converted into outputs for organizations tracking telecom field & installation. It is defined as Completed Jobs / Technician Day; the result is stated in ratio (x:1 or x). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
FTP-T = Completed Jobs / Technician Day
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1280 (batch 5)
