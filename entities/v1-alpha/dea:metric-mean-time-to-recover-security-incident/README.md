# dea:metric-mean-time-to-recover-security-incident

Candidate Performance Metric record for **Mean Time to Recover - Security Incident** (MTTRSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-recover-security-incident`
- **Name:** Mean Time to Recover - Security Incident
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTRSI

## 2. Definition

Mean Time to Recover - Security Incident (MTTRSI) captures how efficiently resources are converted into outputs for organizations tracking secops & security operations center. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Hours from Containment to Full Recovery, expressed in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the average time from incident to full restoration of trusted, normal operations. Recovery includes eradication and hardening, not just service restoration. Rushed recoveries that skip eradication feed recurrence. Read with mean time to contain - security and post-mortem action item closure rate.

## Formula

```
Hours from Containment to Full Recovery
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2775 (batch 7)
