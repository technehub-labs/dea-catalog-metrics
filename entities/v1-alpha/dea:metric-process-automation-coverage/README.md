# dea:metric-process-automation-coverage

Candidate Performance Metric record for **Process Automation Coverage** (PAC-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-automation-coverage`
- **Name:** Process Automation Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PAC-A

## 2. Definition

Process Automation Coverage (PAC-A) measures capability maturity or development in the Automation & Robotic Process Automation domain. It is defined as Automated Process Steps / Total Process Steps in Scope; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of process steps or volume eligible for automation that is actually automated, by process family. It converts automation ambition into a mapped, measurable reality and identifies where human effort still concentrates. The gaming risk is trivial-step inflation: automating lookups and formatting inflates coverage while the expensive judgment steps remain manual. Read with straight-through processing rate (Automation) and cost avoidance from automation for the economic mirror.

## Formula

```
Automated Process Steps / Total Process Steps in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1322 (batch 5)
