# dea:metric-automation-assisted-change-rate

Candidate Performance Metric record for **Automation-Assisted Change Rate** (AACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-assisted-change-rate`
- **Name:** Automation-Assisted Change Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AACR

## 2. Definition

Automation-Assisted Change Rate (AACR) addresses how efficiently resources are converted into outputs and is a fixture of network change & configuration management reporting. It is computed as Changes Executed via Automation / Changes, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of network changes executed through automated, validated workflows. Automated changes are more repeatable and less error-prone than CLI heroics. Automation without pre/post validation automates mistakes faster. Read with change failure rate - network and automation ratio.

## Formula

```
Changes Executed via Automation / Changes
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3370 (batch 7)
