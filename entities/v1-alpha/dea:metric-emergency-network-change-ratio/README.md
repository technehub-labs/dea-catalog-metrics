# dea:metric-emergency-network-change-ratio

Candidate Performance Metric record for **Emergency Network Change Ratio** (ENCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-network-change-ratio`
- **Name:** Emergency Network Change Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ENCR

## 2. Definition

Emergency Network Change Ratio (ENCR) captures exposure to adverse outcomes for organizations tracking network change & configuration management. It is defined as Emergency Changes / Total Network Changes; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Emergency Changes / Total Network Changes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3361 (batch 7)
