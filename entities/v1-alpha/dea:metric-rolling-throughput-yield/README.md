# dea:metric-rolling-throughput-yield

Candidate Performance Metric record for **Rolling Throughput Yield** (RTY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rolling-throughput-yield`
- **Name:** Rolling Throughput Yield
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTY

## 2. Definition

Rolling Throughput Yield (RTY) addresses the quality of outputs and outcomes and is a fixture of manufacturing reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Product of First Pass Yield across All Process Steps, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Manufacturing.

## 3. Context

Measures the probability that a unit passes every process step first time without rework. It matters because it exposes compounding hidden waste that final yield hides. It can be gamed by counting reworked units as first-pass or splitting a process into fewer measured steps. Read with First Pass Yield and Scrap Cost Percentage to verify that yield improvements are genuine, not reclassification.

## Formula

```
Product of First Pass Yield across All Process Steps
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 249 (batch 1)
