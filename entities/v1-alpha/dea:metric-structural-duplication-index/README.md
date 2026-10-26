# dea:metric-structural-duplication-index

Candidate Performance Metric record for **Structural Duplication Index** (SDI-OM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-structural-duplication-index`
- **Name:** Structural Duplication Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SDI-OM

## 2. Definition

Structural Duplication Index (SDI-OM) measures how efficiently resources are converted into outputs in the Operating Model Monitoring & Design Effectiveness domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Duplicated Functions across Units / Functions, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the extent of duplicated capabilities, roles, and structures across the organization. Duplication is silent cost and inconsistent customer experience. Indexes built on org charts miss duplication embedded in processes and systems. Read with process standardization ratio and cost of governance ratio.

## Formula

```
Duplicated Functions across Units / Functions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_monitoring_design_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3119 (batch 7)
