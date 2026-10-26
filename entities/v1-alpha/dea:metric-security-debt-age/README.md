# dea:metric-security-debt-age

Candidate Performance Metric record for **Security Debt Age** (SDA-AS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-debt-age`
- **Name:** Security Debt Age
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SDA-AS

## 2. Definition

Within Application Security (AppSec), Security Debt Age (SDA-AS) is used to gauge exposure to adverse outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Average Age of Open Security Backlog Items, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Software.

## Formula

```
Average Age of Open Security Backlog Items
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3333 (batch 7)
