# dea:metric-infrastructure-as-code-coverage

Candidate Performance Metric record for **Infrastructure-as-Code Coverage** (IaCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-infrastructure-as-code-coverage`
- **Name:** Infrastructure-as-Code Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IaCC

## 2. Definition

A Continuous Delivery & Deployment indicator, Infrastructure-as-Code Coverage (IaCC) quantifies capability maturity or development. It is computed as Infrastructure Managed as Code / Total Infrastructure, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the proportion of infrastructure provisioned and managed through declarative code rather than console clicks or scripts. IaC converts environments into reviewable, versioned, reproducible assets, eliminating snowflake servers and configuration drift. Coverage that excludes network or data layers leaves the riskiest manual work untouched. Read with environment-drift findings and deployment automation rate.

## Formula

```
Infrastructure Managed as Code / Total Infrastructure
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2693 (batch 7)
