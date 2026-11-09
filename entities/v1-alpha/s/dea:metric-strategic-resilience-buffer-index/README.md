# dea:metric-strategic-resilience-buffer-index

Candidate Performance Metric record for **Strategic Resilience Buffer Index** (SRBI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-strategic-resilience-buffer-index`
- **Name:** Strategic Resilience Buffer Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRBI

## 2. Definition

A Emerging Risk & Horizon Scanning indicator, Strategic Resilience Buffer Index (SRBI) quantifies exposure to adverse outcomes. Its calculation is Composite of Financial and Operational Buffers vs Stressed Scenarios, measured in index (0-100 or normalized). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the buffers (cash, capacity, optionality) standing between the organization and disruption. Resilience is purchased in advance and consumed in crisis. Buffers computed under normal assumptions evaporate in correlated stress. Read with cash buffer coverage and disruption readiness confidence score.

## Formula

```
SRBI = Composite of Financial and Operational Buffers vs Stressed Scenarios
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4006 (batch 8)
