# dea:metric-attrition-rate-agents-deep-dive

Candidate Performance Metric record for **Attrition Rate - Agents (Deep Dive)** (ARR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attrition-rate-agents-deep-dive`
- **Name:** Attrition Rate - Agents (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARR-D

## 2. Definition

A Contact Center Operations (Deep Dive) indicator, Attrition Rate - Agents (Deep Dive) (ARR-D) quantifies the retention of customers, users, or assets over time. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Agents Leaving / Agents Employed, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures contact center agent turnover. Agent churn is the dominant capability destroyer of contact centers: every departure resets institutional knowledge, quality, and schedule adherence, and the recruiting-training ramp consumes the margin that volume flexibility was supposed to create. Pay-market positioning and schedule-quality (split shifts, forced overtime) predict attrition better than engagement programs. Read with 90-day attrition and quality scores by agent tenure.

## Formula

```
Agents Leaving / Agents Employed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2485 (batch 6)
