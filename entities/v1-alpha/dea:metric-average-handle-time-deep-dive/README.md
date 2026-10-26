# dea:metric-average-handle-time-deep-dive

Candidate Performance Metric record for **Average Handle Time (Deep Dive)** (AHT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-handle-time-deep-dive`
- **Name:** Average Handle Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AHT-D

## 2. Definition

Average Handle Time (Deep Dive) (AHT-D) addresses how efficiently resources are converted into outputs and is a fixture of contact center operations (deep dive) reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Talk Time + Hold + After-Call Work per Contact - reported in minutes. The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Talk Time + Hold + After-Call Work per Contact
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2482 (batch 6)
