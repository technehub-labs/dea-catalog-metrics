# dea:metric-tool-sprawl-index

Candidate Performance Metric record for **Tool Sprawl Index** (TSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tool-sprawl-index`
- **Name:** Tool Sprawl Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TSI

## 2. Definition

Within Digital Workplace & Collaboration, Tool Sprawl Index (TSI) is used to gauge how efficiently resources are converted into outputs. The formula is Distinct Collaboration Apps per Team / Target App Count - reported in ratio (x:1 or x). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
TSI = Distinct Collaboration Apps per Team / Target App Count
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_workplace_collaboration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1479 (batch 5)
