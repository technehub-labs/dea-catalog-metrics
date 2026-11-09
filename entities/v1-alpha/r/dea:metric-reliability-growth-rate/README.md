# dea:metric-reliability-growth-rate

Candidate Performance Metric record for **Reliability Growth Rate** (RGR-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reliability-growth-rate`
- **Name:** Reliability Growth Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RGR-RM

## 2. Definition

Within Reliability & Maintainability Engineering (Deep Dive), Reliability Growth Rate (RGR-RM) is used to gauge the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Change in MTBF across Test-Fix-Test Cycles - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how quickly product or asset reliability improves across design iterations. Growth is the learning curve of reliability engineering. Growth claimed without field-failure feedback is curve-fitting. Read with mean life (MTTF Deep Dive) and failure prediction lead time.

## Formula

```
RGR-RM = Change in MTBF across Test-Fix-Test Cycles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4113 (batch 9)
