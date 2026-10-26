# dea:metric-refactoring-frequency

Candidate Performance Metric record for **Refactoring Frequency** (REFF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-refactoring-frequency`
- **Name:** Refactoring Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** REFF

## 2. Definition

Refactoring Frequency (REFF) addresses the quality of outputs and outcomes and is a fixture of software development - coding & engineering practices reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Refactoring Commits per 100 Commits; the result is stated in events per thousand or million (scaled). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
REFF = Refactoring Commits per 100 Commits
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_development_coding_engineering_practices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2658 (batch 7)
