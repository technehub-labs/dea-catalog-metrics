# dea:metric-gini-coefficient-model-discrimination

Candidate Performance Metric record for **Gini Coefficient (Model Discrimination)** (GINIM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gini-coefficient-model-discrimination`
- **Name:** Gini Coefficient (Model Discrimination)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GINIM

## 2. Definition

Within Statistical Model Performance Diagnostics, Gini Coefficient (Model Discrimination) (GINIM) is used to gauge the quality of outputs and outcomes. Its calculation is 2 x AUC - 1 (Rank Discrimination Power), measured in index (0-100 or normalized). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## 3. Context

The Gini coefficient, from Corrado Gini (1912) and long used for income inequality, is the standard discrimination measure for credit and fraud scoring: the area between the cumulative good/bad distributions relative to chance. In credit it is conventionally computed as 2 x AUC - 1, so 40-60% is typical for scorecards, and values below 30% suggest a weak or degraded model. Its practical uses are model comparison and monitoring: a Gini that decays over time on new originations is the classic sign of population drift or stale development data.

## Formula

```
2 x AUC - 1 (Rank Discrimination Power)
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Corrado Gini, 1912

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4067 (batch 9)
