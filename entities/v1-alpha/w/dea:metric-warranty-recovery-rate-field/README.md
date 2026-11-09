# dea:metric-warranty-recovery-rate-field

Candidate Performance Metric record for **Warranty Recovery Rate (Field)** (WRR-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-recovery-rate-field`
- **Name:** Warranty Recovery Rate (Field)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRR-F

## 2. Definition

Warranty Recovery Rate (Field) (WRR-F) addresses the economic value created or preserved and is a fixture of field service & asset performance reporting. It is computed as Costs Recovered under Warranty / Recoverable Costs, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
WRR-F = Costs Recovered under Warranty / Recoverable Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3387 (batch 7)
