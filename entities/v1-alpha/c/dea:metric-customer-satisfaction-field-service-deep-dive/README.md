# dea:metric-customer-satisfaction-field-service-deep-dive

Candidate Performance Metric record for **Customer Satisfaction - Field Service (Deep Dive)** (CSFS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-satisfaction-field-service-deep-dive`
- **Name:** Customer Satisfaction - Field Service (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSFS-D

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Customer Satisfaction - Field Service (Deep Dive) (CSFS-D) quantifies the engagement or satisfaction of the people involved. The formula is Average Field Visit CSAT - reported in score (points). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures user-rated satisfaction with field service interactions. Field techs are the human face of the company for many customers, often at their most frustrated moments. Scores influenced by survey timing and by resolution outcome rather than service quality. Read with first-time fix rate - field and CSAT - operational.

## Formula

```
CSFS-D = Average Field Visit CSAT
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** engagement
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2915 (batch 7)
