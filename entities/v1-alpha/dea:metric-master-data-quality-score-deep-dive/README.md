# dea:metric-master-data-quality-score-deep-dive

Candidate Performance Metric record for **Master Data Quality Score (Deep Dive)** (MDQ-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-master-data-quality-score-deep-dive`
- **Name:** Master Data Quality Score (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDQ-D

## 2. Definition

Within ERP & Enterprise Application Operations, Master Data Quality Score (Deep Dive) (MDQ-D) is used to gauge the quality of outputs and outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Composite Master Data Quality Score, expressed in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures completeness, accuracy, and consistency of core master data - customer, vendor, material - against defined standards. Master data quality is the upstream determinant of every downstream metric, integration, and AI initiative, and the score makes it a managed asset. Score composition should weight by business impact, since a missing phone number and a wrong bank account are not equal defects. Read with data-process defect rates and root-cause aging.

## Formula

```
Composite Master Data Quality Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** erp_enterprise_application_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2171 (batch 6)
