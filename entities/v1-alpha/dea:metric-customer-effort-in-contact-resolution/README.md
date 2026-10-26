# dea:metric-customer-effort-in-contact-resolution

Candidate Performance Metric record for **Customer Effort in Contact Resolution** (CECR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-effort-in-contact-resolution`
- **Name:** Customer Effort in Contact Resolution
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CECR

## 2. Definition

Customer Effort in Contact Resolution (CECR) addresses the engagement or satisfaction of the people involved and is a fixture of contact center reporting. Its calculation is Average Contact Effort Rating on Survey, measured in score (points). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much work customers invest to get an issue resolved through support contacts. It matters because effort is the disloyalty driver in service; low-effort resolutions build trust. It can be gamed by scripted effort questions or resolving only the easy ticket classes. Read with Repeat Contact Rate and Customer Effort Score to confirm measured effort matches the real journey.

## Formula

```
CECR = Average Contact Effort Rating on Survey
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 576 (batch 2)
