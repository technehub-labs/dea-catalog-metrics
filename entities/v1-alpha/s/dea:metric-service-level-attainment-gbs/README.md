# dea:metric-service-level-attainment-gbs

Candidate Performance Metric record for **Service Level Attainment (GBS)** (SLA-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-attainment-gbs`
- **Name:** Service Level Attainment (GBS)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLA-G

## 2. Definition

Service Level Attainment (GBS) (SLA-G) measures conformance to standards, plans, or obligations in the Shared Services & Global Business Services domain. The formula is Requests Met within Agreed Service Level / Requests - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of shared-service requests meeting committed SLAs. It matters because GBS functions live or die on credible service commitments. SLA definitions can be loosened until attainment looks healthy. Read with Internal Customer Satisfaction (GBS) and Catalog Adoption Rate to confirm SLAs reflect customer expectations, not negotiated-down targets.

## Formula

```
SLA-G = Requests Met within Agreed Service Level / Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1057 (batch 4)
