# dea:metric-haccp-compliance-rate

Candidate Performance Metric record for **HACCP Compliance Rate** (HCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-haccp-compliance-rate`
- **Name:** HACCP Compliance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HCR

## 2. Definition

Within Food & Beverage Manufacturing, HACCP Compliance Rate (HCR) is used to gauge conformance to standards, plans, or obligations. It is defined as HACCP Checks Passed / Checks Performed; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Food & Beverage, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures adherence to critical control points and monitoring requirements under HACCP food safety systems. CCP compliance is where food safety is actually managed - everything else is documentation - and failures here are direct contamination risk. Audit the monitoring records for perfection patterns (identical readings are a falsification signature), not just presence. Read with food safety audit score (GFSI) and environmental monitoring results.

## Formula

```
HCR = HACCP Checks Passed / Checks Performed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1793 (batch 6)
