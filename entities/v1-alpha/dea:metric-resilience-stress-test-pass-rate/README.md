# dea:metric-resilience-stress-test-pass-rate

Candidate Performance Metric record for **Resilience Stress Test Pass Rate** (RSTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-resilience-stress-test-pass-rate`
- **Name:** Resilience Stress Test Pass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RSTP

## 2. Definition

A Business Resilience & Continuity indicator, Resilience Stress Test Pass Rate (RSTP) quantifies exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Stress Scenarios Passed / Scenarios Executed, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of stress scenarios - cyber, supply, demand shock, key-site loss - in which the organization demonstrated acceptable response within set thresholds. Pass rates move resilience from documentation to demonstrated capability, mirroring the credibility bank stress testing brought to financial risk. Be skeptical of scenarios scoped around known strengths and thresholds set for passage rather than safety. Read with recovery time objective attainment and crisis response activation time.

## Formula

```
Stress Scenarios Passed / Scenarios Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1415 (batch 5)
