# dea:metric-instability-ratio-architecture

Candidate Performance Metric record for **Instability Ratio (Architecture)** (INSTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-instability-ratio-architecture`
- **Name:** Instability Ratio (Architecture)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** INSTA

## 2. Definition

Instability Ratio (Architecture) (INSTA) measures the quality of outputs and outcomes in the Code Quality & Static Analysis domain. The formula is Efferent / (Efferent + Afferent Coupling) - reported in ratio (x:1 or x). It is a standard measure in the Software sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Efferent / (Efferent + Afferent Coupling)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4182 (batch 9)
