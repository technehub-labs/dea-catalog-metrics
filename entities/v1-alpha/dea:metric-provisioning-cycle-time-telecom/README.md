# dea:metric-provisioning-cycle-time-telecom

Candidate Performance Metric record for **Provisioning Cycle Time (Telecom)** (PCT-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-provisioning-cycle-time-telecom`
- **Name:** Provisioning Cycle Time (Telecom)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCT-T

## 2. Definition

Within Telecom Field & Installation, Provisioning Cycle Time (Telecom) (PCT-T) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Days from Order to Active Service; the result is stated in days. It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures elapsed time from order capture to service activation, the interval where telecom customer goodwill most often dies. Long provisioning windows drive order cancellations and support calls before the revenue has even started. Honest reads distinguish cleanly-ordered installs from data-quality rescues, and separate field-availability constraints from process constraints, since they need different fixes. Read with order fallout rate, first-attempt install success, and contract end churn risk conversion.

## Formula

```
Days from Order to Active Service
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1279 (batch 5)
