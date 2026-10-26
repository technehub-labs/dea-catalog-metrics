# dea:metric-bot-utilization-rate

Candidate Performance Metric record for **Bot Utilization Rate** (BUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bot-utilization-rate`
- **Name:** Bot Utilization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BUR

## 2. Definition

Bot Utilization Rate (BUR) measures the utilization or availability of capacity in the Automation & Robotic Process Automation domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Bot Productive Hours / Bot Licensed Hours - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of deployed software robots actively running at expected volumes. It matters because unattended bots are sunk build cost with zero return. Utilization can be protected by keeping low-value make-work in bot queues. Read with Human-in-the-Loop Intervention Rate and bot benefit realization to confirm utilization is valuable.

## Formula

```
BUR = Bot Productive Hours / Bot Licensed Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1323 (batch 5)
