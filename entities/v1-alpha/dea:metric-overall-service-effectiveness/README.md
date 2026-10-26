# dea:metric-overall-service-effectiveness

Candidate Performance Metric record for **Overall Service Effectiveness** (OSE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overall-service-effectiveness`
- **Name:** Overall Service Effectiveness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OSE

## 2. Definition

Overall Service Effectiveness (OSE) captures how effectively a process or entity achieves its intended outcome for organizations tracking operations. It is defined as Service Level Attainment x First Pass Resolution x Quality Score; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the compound of service staff availability, engagement, and first-pass quality in service operations. It matters because paid service hours only create value when they resolve customer needs. It can be gamed by lowering the resolution bar counted as effective service. Read with First Contact Resolution and Customer Effort Score to tie effectiveness scores to customer-felt outcomes.

## Formula

```
Service Level Attainment x First Pass Resolution x Quality Score
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** effectiveness
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 172 (batch 1)
