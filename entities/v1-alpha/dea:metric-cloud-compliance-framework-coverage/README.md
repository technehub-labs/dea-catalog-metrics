# dea:metric-cloud-compliance-framework-coverage

Candidate Performance Metric record for **Cloud Compliance Framework Coverage** (CCFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-compliance-framework-coverage`
- **Name:** Cloud Compliance Framework Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCFC

## 2. Definition

Cloud Compliance Framework Coverage (CCFC) measures conformance to standards, plans, or obligations in the Cloud Security Posture Management domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Framework Controls Monitored / Applicable Controls; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how completely cloud environments are assessed against required frameworks (e.g., CIS, SOC 2, PCI). Framework coverage converts diffuse cloud risk into a manageable checklist. Coverage on sampled accounts extrapolates poorly in large estates. Read with CSPM policy coverage and regulatory process compliance rate.

## Formula

```
Framework Controls Monitored / Applicable Controls
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3313 (batch 7)
