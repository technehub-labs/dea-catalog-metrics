# dea:metric-access-control-compliance

Candidate Performance Metric record for **Access Control Compliance** (ACC-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-access-control-compliance`
- **Name:** Access Control Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACC-P

## 2. Definition

Access Control Compliance (ACC-P) captures conformance to standards, plans, or obligations for organizations tracking physical security operations. It is computed as Access Events per Policy / Access Events Audited, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
ACC-P = Access Events per Policy / Access Events Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** physical_security_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1206 (batch 4)
