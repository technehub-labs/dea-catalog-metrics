# dea:metric-decision-rights-clarity-index

Candidate Performance Metric record for **Decision Rights Clarity Index** (DRCI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-rights-clarity-index`
- **Name:** Decision Rights Clarity Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRCI

## 2. Definition

Decision Rights Clarity Index (DRCI) addresses governance and is a fixture of operating model & process health deep dive reporting. Its calculation is Survey Score on Decision Authority Clarity, measured in index (0-100 or normalized). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how unambiguously decision authority is assigned across the organization. Unclear rights produce slow, escalated, and contested decisions. Index scores from policy documents diverge from lived reality. Read with decision rights clarity score and delegation of authority compliance.

## Formula

```
DRCI = Survey Score on Decision Authority Clarity
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** governance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operating_model_process_health_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3499 (batch 7)
