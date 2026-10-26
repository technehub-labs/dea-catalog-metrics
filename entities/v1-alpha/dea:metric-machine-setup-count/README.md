# dea:metric-machine-setup-count

Candidate Performance Metric record for **Machine Setup Count** (MSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-machine-setup-count`
- **Name:** Machine Setup Count
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSC

## 2. Definition

Machine Setup Count (MSC) captures how efficiently resources are converted into outputs for organizations tracking manufacturing. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Number of Setups per Period - reported in count (items per period). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Manufacturing sector.

## Formula

```
Number of Setups per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 262 (batch 1)
