# dea:metric-maximum-drawdown-duration

Candidate Performance Metric record for **Maximum Drawdown Duration** (MDDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maximum-drawdown-duration`
- **Name:** Maximum Drawdown Duration
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDDD

## 2. Definition

A Investment Performance Measurement indicator, Maximum Drawdown Duration (MDDD) quantifies exposure to adverse outcomes. It is computed as Days from Peak to Recovery of Prior High, expressed in days. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Investment management.

## 3. Context

Measures how long the portfolio took to recover from its worst peak-to-trough decline. Duration is what clients experience as pain. Long durations trigger redemptions that lock in losses. Read with maximum drawdown (Deep Dive) and redemption rate.

## Formula

```
Days from Peak to Recovery of Prior High
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3444 (batch 7)
