# dea:metric-organizational-layers

Candidate Performance Metric record for **Organizational Layers** (ORGL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-organizational-layers`
- **Name:** Organizational Layers
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ORGL

## 2. Definition

A Operating Model & Decision Effectiveness indicator, Organizational Layers (ORGL) quantifies how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Layers from Frontline to CEO; the result is stated in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Counts the number of reporting levels from front line to CEO. Every additional layer adds translation loss to strategy, delay to decisions, and cost to management overhead. It matters because it is a hard structural constraint on agility that no amount of culture work can offset. Be skeptical of re-orgs that cut layers in title while preserving shadow hierarchies through dotted-line roles and committees. Read with span of control and decision cycle time to see whether flattening actually changed behavior.

## Formula

```
ORGL = Layers from Frontline to CEO
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1307 (batch 5)
