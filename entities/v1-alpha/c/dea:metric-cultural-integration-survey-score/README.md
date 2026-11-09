# dea:metric-cultural-integration-survey-score

Candidate Performance Metric record for **Cultural Integration Survey Score** (CISS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cultural-integration-survey-score`
- **Name:** Cultural Integration Survey Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CISS

## 2. Definition

Cultural Integration Survey Score (CISS) measures the engagement or satisfaction of the people involved in the Mergers & Acquisitions domain. It is computed as Post-Merger Employee Culture Survey Score, expressed in score (points). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures employee sentiment about the merged organization's culture, identity, and decision climate. Culture is the standard post-merger failure narrative, and this metric tests it early enough to intervene, before attrition does the talking. Survey response rates matter - fear-driven silence is itself a signal - so read participation alongside scores. Read with regretted attrition and decision cycle time in the combined entity.

## Formula

```
CISS = Post-Merger Employee Culture Survey Score
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1697 (batch 6)
