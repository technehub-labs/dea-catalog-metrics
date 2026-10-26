# dea:metric-security-incident-recurrence-rate

Candidate Performance Metric record for **Security Incident Recurrence Rate** (SIRR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-incident-recurrence-rate`
- **Name:** Security Incident Recurrence Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIRR-SOC

## 2. Definition

Security Incident Recurrence Rate (SIRR-SOC) captures the quality of outputs and outcomes for organizations tracking secops & security operations center. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Incidents Repeating Same Root Cause / Incidents, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the frequency of incidents sharing root causes with prior incidents. Recurrence is the ultimate scoreboard on whether learning actually happened. Classifying repeat incidents under new categories launders the number. Read with post-mortem action item closure rate and mean time to contain - security.

## Formula

```
SIRR-SOC = Incidents Repeating Same Root Cause / Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2793 (batch 7)
