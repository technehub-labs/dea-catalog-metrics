# dea:metric-contingency-income-per-agency

Candidate Performance Metric record for **Contingency Income per Agency** (CIPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contingency-income-per-agency`
- **Name:** Contingency Income per Agency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CIPA

## 2. Definition

A Insurance Distribution & Agency Management indicator, Contingency Income per Agency (CIPA) quantifies the economic value created or preserved. It is computed as Profit-Sharing Earned / Appointed Agencies, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Insurance.

## Formula

```
CIPA = Profit-Sharing Earned / Appointed Agencies
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1731 (batch 6)
