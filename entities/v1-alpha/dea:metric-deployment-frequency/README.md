# dea:metric-deployment-frequency

Candidate Performance Metric record for **Deployment Frequency** (DF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-frequency`
- **Name:** Deployment Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DF

## 2. Definition

Deployment Frequency (DF) addresses how efficiently resources are converted into outputs and is a fixture of software engineering reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Production Deployments per Period, measured in times per period. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Deployment frequency, a DORA metric, counts how often changes reach production. Elite teams deploy on demand - often many times a day; low performers deploy monthly or less. Frequency matters because it is a proxy for batch size and risk appetite: small, frequent deployments are individually safer and give faster feedback than big-bang releases. Measure deployments per developer per day and resist gaming through definitional drift - a deployment means a change to production, not a build to a staging environment.

## Formula

```
DF = Production Deployments per Period
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** DORA research program (DevOps Research and Assessment)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 277 (batch 1)
