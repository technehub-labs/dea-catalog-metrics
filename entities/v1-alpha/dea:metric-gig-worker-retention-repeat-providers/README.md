# dea:metric-gig-worker-retention-repeat-providers

Candidate Performance Metric record for **Gig Worker Retention (Repeat Providers)** (GWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gig-worker-retention-repeat-providers`
- **Name:** Gig Worker Retention (Repeat Providers)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GWR

## 2. Definition

Within Gig & Contingent Workforce, Gig Worker Retention (Repeat Providers) (GWR) is used to gauge the retention of customers, users, or assets over time. Its calculation is Workers Completing Repeat Tasks / Workers Onboarded, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of gig workers who continue providing on the platform. It matters because churned gig workers leave capacity gaps and raise acquisition cost. Retention can be bought with temporary incentive spikes that reverse. Read with Earnings per Provider trend and platform supply-demand balance to confirm retention is economic.

## Formula

```
Workers Completing Repeat Tasks / Workers Onboarded
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** gig_contingent_workforce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1464 (batch 5)
