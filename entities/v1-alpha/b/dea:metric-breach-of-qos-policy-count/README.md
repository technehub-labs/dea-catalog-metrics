# dea:metric-breach-of-qos-policy-count

Candidate Performance Metric record for **Breach of QoS Policy Count** (BQPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-breach-of-qos-policy-count`
- **Name:** Breach of QoS Policy Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BQPC

## 2. Definition

Breach of QoS Policy Count (BQPC) addresses the quality of outputs and outcomes and is a fixture of network performance & capacity reporting. It is computed as QoS Policy Violations in Period, expressed in count (items per period). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
BQPC = QoS Policy Violations in Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3349 (batch 7)
