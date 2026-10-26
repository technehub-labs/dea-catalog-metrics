# dea:metric-assumption-change-frequency

Candidate Performance Metric record for **Assumption Change Frequency** (ACF-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assumption-change-frequency`
- **Name:** Assumption Change Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACF-A

## 2. Definition

Within Actuarial & Reserving, Assumption Change Frequency (ACF-A) is used to gauge exposure to adverse outcomes. Its calculation is Material Assumption Changes per Valuation Cycle, measured in times per period. It originates from and is most used in Insurance practice. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## Formula

```
ACF-A = Material Assumption Changes per Valuation Cycle
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1533 (batch 6)
