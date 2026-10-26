# dea:metric-information-ratio-deep-dive

Candidate Performance Metric record for **Information Ratio (Deep Dive)** (IR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-information-ratio-deep-dive`
- **Name:** Information Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IR-D

## 2. Definition

Within Asset & Wealth Management (Deep Dive), Information Ratio (Deep Dive) (IR-D) is used to gauge how effectively a process or entity achieves its intended outcome. It is defined as Active Return / Tracking Error; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures excess return per unit of tracking error - the efficiency of active management. It is the industry's standard quality metric for active risk-taking: two managers with identical excess returns differ enormously if one took twice the active risk. IR is unstable over short windows, so read multi-year, and beware in-sample computation against stale benchmarks. Read with tracking error and active share for the risk budget's composition.

## Formula

```
Active Return / Tracking Error
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** asset_wealth_management_deep_dive
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2104 (batch 6)
