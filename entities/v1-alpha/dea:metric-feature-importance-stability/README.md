# dea:metric-feature-importance-stability

Candidate Performance Metric record for **Feature Importance Stability** (FIIMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-importance-stability`
- **Name:** Feature Importance Stability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FIIMP

## 2. Definition

Within Statistical Model Performance Diagnostics, Feature Importance Stability (FIIMP) is used to gauge the quality of outputs and outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Rank Correlation of Feature Importances across Retrains - reported in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
Rank Correlation of Feature Importances across Retrains
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4074 (batch 9)
