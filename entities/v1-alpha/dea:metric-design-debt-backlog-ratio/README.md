# dea:metric-design-debt-backlog-ratio

Candidate Performance Metric record for **Design Debt Backlog Ratio** (DDBR-UX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-debt-backlog-ratio`
- **Name:** Design Debt Backlog Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDBR-UX

## 2. Definition

Design Debt Backlog Ratio (DDBR-UX) captures the quality of outputs and outcomes for organizations tracking ux & design systems. Its calculation is Design Debt Items / Total Design Backlog Items, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
DDBR-UX = Design Debt Items / Total Design Backlog Items
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3273 (batch 7)
