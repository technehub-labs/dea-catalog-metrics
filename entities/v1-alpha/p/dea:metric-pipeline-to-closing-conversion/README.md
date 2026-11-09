# dea:metric-pipeline-to-closing-conversion

Candidate Performance Metric record for **Pipeline-to-Closing Conversion** (P2CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pipeline-to-closing-conversion`
- **Name:** Pipeline-to-Closing Conversion
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** P2CC

## 2. Definition

Pipeline-to-Closing Conversion (P2CC) addresses how effectively a process or entity achieves its intended outcome and is a fixture of real estate brokerage reporting. It is defined as Closings / Active Pipeline Opportunities; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Real estate, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of pipeline listings or buyer engagements that close. It matters because conversion efficiency separates productive agents from busy ones. Agents can inflate the denominator by logging low-probability engagements to look busy. Read with Time to Close and Agent Productivity (Transactions) to confirm conversion quality across the funnel.

## Formula

```
P2CC = Closings / Active Pipeline Opportunities
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1015 (batch 3)
