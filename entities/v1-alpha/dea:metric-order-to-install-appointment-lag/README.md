# dea:metric-order-to-install-appointment-lag

Candidate Performance Metric record for **Order-to-Install Appointment Lag** (OIAL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-to-install-appointment-lag`
- **Name:** Order-to-Install Appointment Lag
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OIAL

## 2. Definition

Order-to-Install Appointment Lag (OIAL) measures how efficiently resources are converted into outputs in the Telecom Field & Installation domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Days between Order and First Available Appointment Slot, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Telecommunications practice.

## 3. Context

Measures the gap between order and first available installation appointment. It matters because appointment availability, not technician speed, is often the true customer wait. Lag can be hidden by quoting install dates customers did not ask for. Read with On-Time Appointment Attainment and Service Activation Time to confirm the lag is honest.

## Formula

```
Days between Order and First Available Appointment Slot
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1287 (batch 5)
