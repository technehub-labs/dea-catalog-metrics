# dea:metric-robot-utilization-rate

Candidate Performance Metric record for **Robot Utilization Rate** (RUR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-robot-utilization-rate`
- **Name:** Robot Utilization Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RUR-I

## 2. Definition

Robot Utilization Rate (RUR-I) captures the utilization or availability of capacity for organizations tracking industrial automation & robotics. It is defined as Robot Productive Hours / Robot Available Hours; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Manufacturing, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of industrial robot capacity used for productive work. It matters because robot cells are large capital items whose payback depends on utilization. Utilization can be inflated by running cycles that feed overproduction. Read with Overall Equipment Effectiveness for the line and takt alignment to confirm utilization is productive.

## Formula

```
Robot Productive Hours / Robot Available Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1334 (batch 5)
