# dea:metric-self-service-resolution-rate-it

Candidate Performance Metric record for **Self-Service Resolution Rate - IT** (SSRR-IT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-resolution-rate-it`
- **Name:** Self-Service Resolution Rate - IT
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSRR-IT

## 2. Definition

Self-Service Resolution Rate - IT (SSRR-IT) captures how efficiently resources are converted into outputs for organizations tracking it incident & major problem management. It is computed as Resolutions via Self-Service / Resolutions, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of user issues resolved via self-service channels without agent involvement. Deflection scales support and satisfies users who prefer instant answers. Deflection that pushes users into abandoned searches before ticketing degrades experience while flattering the metric. Read with contact center self-service containment rate and incident volume per period.

## Formula

```
SSRR-IT = Resolutions via Self-Service / Resolutions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2897 (batch 7)
