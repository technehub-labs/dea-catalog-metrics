# dea:metric-agency-production-per-agent

Candidate Performance Metric record for **Agency Production per Agent** (APA-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agency-production-per-agent`
- **Name:** Agency Production per Agent
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APA-I

## 2. Definition

Agency Production per Agent (APA-I) captures how efficiently resources are converted into outputs for organizations tracking insurance distribution & agency management. It is computed as Written Premium / Active Agents, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Insurance.

## Formula

```
APA-I = Written Premium / Active Agents
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1724 (batch 6)
