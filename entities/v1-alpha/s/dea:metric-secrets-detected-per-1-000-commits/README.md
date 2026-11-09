# dea:metric-secrets-detected-per-1-000-commits

Candidate Performance Metric record for **Secrets Detected per 1,000 Commits** (SD1KC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-secrets-detected-per-1-000-commits`
- **Name:** Secrets Detected per 1,000 Commits
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SD1KC

## 2. Definition

Secrets Detected per 1,000 Commits (SD1KC) captures exposure to adverse outcomes for organizations tracking devsecops & application security engineering. It provides the day-to-day signal that a process is running as designed. Its calculation is Hardcoded Secrets Detected / 1,000 Commits, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SD1KC = Hardcoded Secrets Detected / 1,000 Commits
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2755 (batch 7)
