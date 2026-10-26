# dea:metric-rework-rate

Candidate Performance Metric record for **Rework Rate** (RWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rework-rate`
- **Name:** Rework Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RWR

## 2. Definition

Rework Rate (RWR) addresses the quality of outputs and outcomes and is a fixture of operations reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as Units Requiring Rework / Units Produced; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Units Requiring Rework / Units Produced
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 163 (batch 1)
