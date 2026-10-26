# dea:metric-mean-time-to-contain-security

Candidate Performance Metric record for **Mean Time to Contain - Security** (MTTC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-contain-security`
- **Name:** Mean Time to Contain - Security
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTC-S

## 2. Definition

Within SecOps & Security Operations Center, Mean Time to Contain - Security (MTTC-S) is used to gauge how efficiently resources are converted into outputs. It is defined as Hours from Response to Containment; the result is stated in hours. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average time from detection to an incident being contained and attacker access cut off. Containment stops the bleeding: every hour extends data loss and lateral movement. Declaring containment without verifying persistence mechanisms (backdoors, tokens) produces premature closure. Read with mean time to recover - security incident and security incident recurrence rate.

## Formula

```
Hours from Response to Containment
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2774 (batch 7)
