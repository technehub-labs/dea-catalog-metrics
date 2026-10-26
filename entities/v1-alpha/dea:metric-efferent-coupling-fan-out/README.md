# dea:metric-efferent-coupling-fan-out

Candidate Performance Metric record for **Efferent Coupling (Fan-Out)** (EFFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-efferent-coupling-fan-out`
- **Name:** Efferent Coupling (Fan-Out)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EFFC

## 2. Definition

Efferent Coupling (Fan-Out) (EFFC) measures the quality of outputs and outcomes in the Code Quality & Static Analysis domain. Its calculation is Outbound Dependencies per Module, measured in count (items per period). It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Outbound Dependencies per Module
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4181 (batch 9)
