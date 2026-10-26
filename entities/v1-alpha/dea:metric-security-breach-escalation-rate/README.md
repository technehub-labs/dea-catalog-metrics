# dea:metric-security-breach-escalation-rate

Candidate Performance Metric record for **Security Breach Escalation Rate** (SBER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-breach-escalation-rate`
- **Name:** Security Breach Escalation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SBER

## 2. Definition

Security Breach Escalation Rate (SBER) addresses exposure to adverse outcomes and is a fixture of security services & guarding reporting. It is defined as Breaches Escalated / Breaches Detected; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Security, it is a recognized element of the standard performance toolkit.

## Formula

```
SBER = Breaches Escalated / Breaches Detected
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** security_services_guarding
- **Sector:** security

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2059 (batch 6)
