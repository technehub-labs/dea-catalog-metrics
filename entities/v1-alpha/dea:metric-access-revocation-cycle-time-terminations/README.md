# dea:metric-access-revocation-cycle-time-terminations

Candidate Performance Metric record for **Access Revocation Cycle Time - Terminations** (ARCTT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-access-revocation-cycle-time-terminations`
- **Name:** Access Revocation Cycle Time - Terminations
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARCTT

## 2. Definition

Within Identity & Access Management Operations, Access Revocation Cycle Time - Terminations (ARCTT) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Hours from Termination to Access Revoked, measured in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the time from employment end to full access removal. Each hour of post-termination access is unbounded insider risk. Manual, ticket-driven revocation cannot match automated deprovisioning speed. Read with orphaned account rate and joiner-mover-leaver processing timeliness.

## Formula

```
Hours from Termination to Access Revoked
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2825 (batch 7)
