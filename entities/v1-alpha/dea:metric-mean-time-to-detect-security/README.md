# dea:metric-mean-time-to-detect-security

Candidate Performance Metric record for **Mean Time to Detect - Security** (MTTD-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-detect-security`
- **Name:** Mean Time to Detect - Security
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTTD-S

## 2. Definition

Within SecOps & Security Operations Center, Mean Time to Detect - Security (MTTD-S) is used to gauge how efficiently resources are converted into outputs. The formula is Minutes from Alert Generation to Triage - reported in minutes. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average time from security incident start to SOC detection. Dwell time is the single biggest driver of breach cost: attackers inside the network for months exfiltrate everything. MTTD measured from the tool alert rather than true compromise understates reality substantially. Read with detection rule coverage against MITRE ATT&CK and mean time to respond - security.

## Formula

```
Minutes from Alert Generation to Triage
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2772 (batch 7)
