# dea:metric-service-level-80-20-deep-dive

Candidate Performance Metric record for **Service Level - 80/20 (Deep Dive)** (SL8020-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-80-20-deep-dive`
- **Name:** Service Level - 80/20 (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SL8020-D

## 2. Definition

Service Level - 80/20 (Deep Dive) (SL8020-D) addresses the quality of outputs and outcomes and is a fixture of contact center operations (deep dive) reporting. It is defined as Calls Answered within 20 Seconds / Calls Offered; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether 80 percent of contacts are answered within 20 seconds. It is the classic access commitment of contact centers, balancing caller abandon cost against staffing cost, and it remains the contract currency with enterprise customers. Service-level design must match channel economics - 80/20 on voice trades against digital response expectations - and met levels with long handle times can still fail customers. Read with abandonment rates and first call resolution (Deep Dive).

## Formula

```
Calls Answered within 20 Seconds / Calls Offered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2475 (batch 6)
