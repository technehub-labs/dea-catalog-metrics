# dea:metric-data-accuracy-rate

Candidate Performance Metric record for **Data Accuracy Rate** (DAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-accuracy-rate`
- **Name:** Data Accuracy Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DAR

## 2. Definition

Data Accuracy Rate (DAR) captures the quality of outputs and outcomes for organizations tracking data management & analytics. Its calculation is Records Matching Verified Source / Records Sampled, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of data values verified correct against a source of truth. It matters because accurate-but-late or complete-but-wrong data still poisons decisions. It can be gamed by sampling easy fields or defining truth as whatever the system currently says. Read with Data Completeness and downstream Model Prediction Accuracy to see whether quality issues surface where data is consumed.

## Formula

```
Records Matching Verified Source / Records Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 336 (batch 1)
