# dea:metric-board-decision-implementation-rate

Candidate Performance Metric record for **Board Decision Implementation Rate** (BDIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-board-decision-implementation-rate`
- **Name:** Board Decision Implementation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BDIR

## 2. Definition

Board Decision Implementation Rate (BDIR) addresses conformance to standards, plans, or obligations and is a fixture of enterprise decision effectiveness & governance monitoring reporting. It is defined as Board Decisions Implemented Fully / Board Decisions; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely board decisions are executed as taken. Implementation is the last mile of governance credibility. Rates can be gamed by declaring decisions advisory after the fact. Read with board meeting effectiveness score and delegation of authority compliance.

## Formula

```
BDIR = Board Decisions Implemented Fully / Board Decisions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3138 (batch 7)
