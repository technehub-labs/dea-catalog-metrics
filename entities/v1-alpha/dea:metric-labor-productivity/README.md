# dea:metric-labor-productivity

Candidate Performance Metric record for **Labor Productivity** (LP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-labor-productivity`
- **Name:** Labor Productivity
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LP

## 2. Definition

Labor Productivity (LP) addresses how efficiently resources are converted into outputs and is a fixture of operations reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Output Units / Labor Hour, expressed in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures output per labor hour or per employee. It matters because it is the fundamental unit economics driver for labor-intensive operations. It can be gamed by deferring maintenance or quality checks, which front-loads output and defers cost. Read with Overall Labor Effectiveness and Cost per Unit Produced to ensure productivity gains are not borrowed from quality or assets.

## Formula

```
Output Units / Labor Hour
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 165 (batch 1)
