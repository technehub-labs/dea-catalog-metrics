# dea:metric-hedge-documentation-compliance-rate

Candidate Performance Metric record for **Hedge Documentation Compliance Rate** (HDCR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hedge-documentation-compliance-rate`
- **Name:** Hedge Documentation Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HDCR-T

## 2. Definition

Within Corporate Treasury (Deep Dive), Hedge Documentation Compliance Rate (HDCR-T) is used to gauge conformance to standards, plans, or obligations. It is defined as Hedges Meeting Documentation Requirements / Hedges; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether derivative hedges carry complete, timely documentation as accounting standards require. Undocumented hedges lose hedge accounting treatment, converting intended protection into P&L volatility - a compliance failure that is purely administrative but financially material. Documentation timing is the failure mode, since hedges documented after the fact fail the test. Read with hedge effectiveness ratios and external audit findings.

## Formula

```
HDCR-T = Hedges Meeting Documentation Requirements / Hedges
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2184 (batch 6)
