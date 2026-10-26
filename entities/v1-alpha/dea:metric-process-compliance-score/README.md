# dea:metric-process-compliance-score

Candidate Performance Metric record for **Process Compliance Score** (PCS-BSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-compliance-score`
- **Name:** Process Compliance Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCS-BSC

## 2. Definition

Process Compliance Score (PCS-BSC) measures conformance to standards, plans, or obligations in the Balanced Scorecard - Internal Process Perspective domain. It is computed as Control Tests Passed / Control Tests, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures adherence to defined process standards across executions. Compliance is what makes process performance predictable rather than heroic. Inspection-based scoring samples only observed executions. Read with regulatory process compliance rate and process standardization ratio.

## Formula

```
Control Tests Passed / Control Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3087 (batch 7)
