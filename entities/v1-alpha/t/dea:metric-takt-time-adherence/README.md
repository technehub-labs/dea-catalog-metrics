# dea:metric-takt-time-adherence

Candidate Performance Metric record for **Takt Time Adherence** (TTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-takt-time-adherence`
- **Name:** Takt Time Adherence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTA

## 2. Definition

Takt Time Adherence (TTA) captures how efficiently resources are converted into outputs for organizations tracking manufacturing. It is defined as Cycle Time / Takt Time; the result is stated in ratio (x:1 or x). In Manufacturing, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Takt adherence measures how well actual production rhythm matches the takt target - the share of cycles completed within the takt window. High adherence means the line runs as a stable pull system; low adherence signals line balancing problems, starvation, or quality interruptions. It is monitored on the floor at each station, and it is the operational companion to takt time itself: setting takt is planning, adhering to it is execution.

## Formula

```
TTA = Cycle Time / Takt Time
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Lean manufacturing (Toyota Production System)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 252 (batch 1)
