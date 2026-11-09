# dea:metric-standing-privilege-reduction-rate

Candidate Performance Metric record for **Standing Privilege Reduction Rate** (SPRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-standing-privilege-reduction-rate`
- **Name:** Standing Privilege Reduction Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPRR

## 2. Definition

Within Identity & Access Management Operations, Standing Privilege Reduction Rate (SPRR) is used to gauge exposure to adverse outcomes. It is defined as Just-in-Time Access Grants / Privileged Access Grants; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures progress in converting permanent admin rights to just-in-time, time-boxed elevation. Standing privilege turns any admin compromise into total compromise; JIT shrinks the window to minutes. Reduction programs often stall on executives and legacy system owners. Read with privileged account ratio and least privilege compliance ratio.

## Formula

```
SPRR = Just-in-Time Access Grants / Privileged Access Grants
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2820 (batch 7)
