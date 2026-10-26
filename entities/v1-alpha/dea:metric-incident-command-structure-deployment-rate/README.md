# dea:metric-incident-command-structure-deployment-rate

Candidate Performance Metric record for **Incident Command Structure Deployment Rate** (ICSDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-command-structure-deployment-rate`
- **Name:** Incident Command Structure Deployment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ICSDR

## 2. Definition

Incident Command Structure Deployment Rate (ICSDR) measures conformance to standards, plans, or obligations in the Crisis Management & Emergency Response domain. The formula is Events Managed under Formal Command Structure / Events - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how consistently a defined command structure is actually used in crisis events. Structures that exist on paper but are bypassed in real events produce chaotic command. Deployment without trained role-fillers is an org chart, not capability. Read with crisis response team activation time and tabletop exercise completion rate.

## Formula

```
Events Managed under Formal Command Structure / Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3542 (batch 8)
