# dea:metric-incident-response-time-security-deep-dive

Candidate Performance Metric record for **Incident Response Time (Security Deep Dive)** (IRT-SD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-response-time-security-deep-dive`
- **Name:** Incident Response Time (Security Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IRT-SD

## 2. Definition

Incident Response Time (Security Deep Dive) (IRT-SD) captures how efficiently resources are converted into outputs for organizations tracking security services & guarding. The formula is Minutes from Alert to Guard on Scene - reported in minutes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Security sector.

## Formula

```
Minutes from Alert to Guard on Scene
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2052 (batch 6)
