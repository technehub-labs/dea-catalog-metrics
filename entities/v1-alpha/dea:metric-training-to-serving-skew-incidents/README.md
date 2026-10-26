# dea:metric-training-to-serving-skew-incidents

Candidate Performance Metric record for **Training-to-Serving Skew Incidents** (TSSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-training-to-serving-skew-incidents`
- **Name:** Training-to-Serving Skew Incidents
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TSSI

## 2. Definition

Training-to-Serving Skew Incidents (TSSI) captures the quality of outputs and outcomes for organizations tracking mlops & model lifecycle operations. It is computed as Skew Incidents Requiring Rollback per Quarter, expressed in count (items per period). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures occurrences where production inference behaves differently from training due to pipeline discrepancies. Skew is the most preventable class of production ML failure, and incident frequency is a direct read on pipeline engineering discipline - the same computation should run in both contexts. Each incident deserves root-cause classification (feature logic, preprocessing, latency effects). Read with feature store coverage ratio (Deep Dive) and skew-detection test cadence.

## Formula

```
Skew Incidents Requiring Rollback per Quarter
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2527 (batch 7)
