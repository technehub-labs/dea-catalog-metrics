# dea:metric-adverse-event-reporting-timeliness-devices

Candidate Performance Metric record for **Adverse Event Reporting Timeliness (Devices)** (AERT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-adverse-event-reporting-timeliness-devices`
- **Name:** Adverse Event Reporting Timeliness (Devices)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AERT-D

## 2. Definition

Within Medical Devices, Adverse Event Reporting Timeliness (Devices) (AERT-D) is used to gauge conformance to standards, plans, or obligations. The formula is Reports Filed within Deadline / Reports Required - reported in percent (%). It is a standard measure in the Medical devices sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Adverse event reporting timeliness measures how quickly a manufacturer files legally required reports of device-related deaths, serious injuries, or malfunctions - 30 days under FDA MDR rules, 10 for public-health-threat events. Timeliness is a compliance metric with teeth: late MDR filing is among the most common FDA warning-letter findings, and enforcement has cost manufacturers tens of millions. The deeper signal is organizational: a lagging timeliness rate often reflects unclear escalation paths rather than slow paperwork. Read with complaint-to-report conversion rate and timeliness trend by severity class, since the most dangerous pattern is timeliness degrading precisely on the most serious event types.

## Formula

```
Reports Filed within Deadline / Reports Required
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 753 (batch 2)
