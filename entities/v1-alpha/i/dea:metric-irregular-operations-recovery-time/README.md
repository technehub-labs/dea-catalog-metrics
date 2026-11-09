# dea:metric-irregular-operations-recovery-time

Candidate Performance Metric record for **Irregular Operations Recovery Time** (IROPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-irregular-operations-recovery-time`
- **Name:** Irregular Operations Recovery Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IROPR

## 2. Definition

Irregular Operations Recovery Time (IROPR) captures how efficiently resources are converted into outputs for organizations tracking airline operations (deep dive). Its calculation is Minutes to Restore Schedule after Disruption, measured in minutes. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Airlines practice.

## Formula

```
IROPR = Minutes to Restore Schedule after Disruption
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2261 (batch 6)
