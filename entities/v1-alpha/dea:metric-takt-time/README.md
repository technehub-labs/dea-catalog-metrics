# dea:metric-takt-time

Candidate Performance Metric record for **Takt Time** (TAKT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-takt-time`
- **Name:** Takt Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TAKT

## 2. Definition

Within Process Excellence (Lean Six Sigma), Takt Time (TAKT) is used to gauge the utilization or availability of capacity. The formula is Available Production Time / Customer Demand Units - reported in seconds. It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Takt time is the drumbeat of lean production: available production time divided by customer demand. It is not a measure of how fast you work but of how fast you must work to meet demand without overproduction - the core of Toyota Production System pull logic. If cycle time exceeds takt, the line cannot keep up; if it is far shorter, you are over-staffed or over-producing. Because demand shifts, takt must be recalculated regularly and used to size staffing, line balance, and work cells.

## Formula

```
Available Production Time / Customer Demand Units
```

## Unit

- **Unit reference:** `dea:unit-seconds`
- **Unit:** seconds
- **Unit label (as published):** seconds

## Classification

- **Subject classification:** capability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Lean manufacturing (Toyota Production System)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1113 (batch 4)
