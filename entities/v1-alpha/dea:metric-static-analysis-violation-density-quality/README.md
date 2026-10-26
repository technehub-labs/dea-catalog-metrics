# dea:metric-static-analysis-violation-density-quality

Candidate Performance Metric record for **Static Analysis Violation Density (Quality)** (SAVD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-static-analysis-violation-density-quality`
- **Name:** Static Analysis Violation Density (Quality)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SAVD

## 2. Definition

A Code Quality & Static Analysis indicator, Static Analysis Violation Density (Quality) (SAVD) quantifies the quality of outputs and outcomes. Its calculation is Violations per 1,000 Lines of Code, measured in events per thousand or million (scaled). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Software practice.

## Formula

```
Violations per 1,000 Lines of Code
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4183 (batch 9)
