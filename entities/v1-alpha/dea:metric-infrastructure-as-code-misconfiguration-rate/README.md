# dea:metric-infrastructure-as-code-misconfiguration-rate

Candidate Performance Metric record for **Infrastructure-as-Code Misconfiguration Rate** (IaCMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-infrastructure-as-code-misconfiguration-rate`
- **Name:** Infrastructure-as-Code Misconfiguration Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IaCMR

## 2. Definition

Within DevSecOps & Application Security Engineering, Infrastructure-as-Code Misconfiguration Rate (IaCMR) is used to gauge exposure to adverse outcomes. The formula is Misconfigurations Found per 1,000 IaC Lines - reported in events per thousand or million (scaled). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Misconfigurations Found per 1,000 IaC Lines
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2754 (batch 7)
