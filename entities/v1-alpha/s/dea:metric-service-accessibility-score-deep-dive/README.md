# dea:metric-service-accessibility-score-deep-dive

Candidate Performance Metric record for **Service Accessibility Score (Deep Dive)** (SAS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-accessibility-score-deep-dive`
- **Name:** Service Accessibility Score (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAS-D

## 2. Definition

Within Balanced Scorecard - Customer Perspective, Service Accessibility Score (Deep Dive) (SAS-D) is used to gauge the quality of outputs and outcomes. It is computed as Composite Channel Accessibility Score, expressed in index (0-100 or normalized). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how easily customers can reach and use support and service channels across their situations. Accessibility is a retention lever often invisible to digital-first metrics. Survey instruments that sample only successful users bias scores. Read with omnichannel consistency score and customer effort score.

## Formula

```
SAS-D = Composite Channel Accessibility Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_customer_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3078 (batch 7)
