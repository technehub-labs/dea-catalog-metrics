# dea:metric-time-to-competency-compression

Candidate Performance Metric record for **Time-to-Competency Compression** (TTCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-competency-compression`
- **Name:** Time-to-Competency Compression
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTCC

## 2. Definition

Time-to-Competency Compression (TTCC) measures how efficiently resources are converted into outputs in the Learning & Development Effectiveness (Deep Dive) domain. Its calculation is Reduction in Ramp Days vs Baseline / Baseline, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how much faster new hires or new-role holders reach full productivity versus the baseline. Compression is the productivity payoff of onboarding and enablement design. Self-assessed competency arrival is optimistic. Read with time to productivity and onboarding completion rate.

## Formula

```
TTCC = Reduction in Ramp Days vs Baseline / Baseline
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** learning_development_effectiveness_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3883 (batch 8)
