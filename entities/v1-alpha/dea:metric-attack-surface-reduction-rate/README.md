# dea:metric-attack-surface-reduction-rate

Candidate Performance Metric record for **Attack Surface Reduction Rate** (ASRR-DSO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attack-surface-reduction-rate`
- **Name:** Attack Surface Reduction Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ASRR-DSO

## 2. Definition

A DevSecOps & Application Security Engineering indicator, Attack Surface Reduction Rate (ASRR-DSO) quantifies exposure to adverse outcomes. It is defined as Deprecated or Exposed Endpoints Removed per Quarter; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the pace at which external-facing services, ports, and endpoints are retired or consolidated. Shrinking surface is the only vulnerability class you can eliminate outright. Reduction programs often stall at legacy endpoints nobody will decommission. Read with internet-facing critical exposure time and external scan coverage.

## Formula

```
Deprecated or Exposed Endpoints Removed per Quarter
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2771 (batch 7)
