# dea:metric-safety-incident-rate-field

Candidate Performance Metric record for **Safety Incident Rate (Field)** (SIR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-safety-incident-rate-field`
- **Name:** Safety Incident Rate (Field)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SIR-F

## 2. Definition

Safety Incident Rate (Field) (SIR-F) captures exposure to adverse outcomes for organizations tracking field service & asset performance. The formula is Recordable Field Incidents per 200,000 Hours - reported in events per thousand or million (scaled). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures recordable safety incidents per hours worked in field operations. Field work concentrates physical risk in driving, electrical, and site conditions. Bonus-linked reporting suppresses the number rather than the incidents. Read with field work safety incident rate and workers compensation cost trend.

## Formula

```
Recordable Field Incidents per 200,000 Hours
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** operations
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3392 (batch 7)
