# dea:metric-test-maintenance-cost-ratio

Candidate Performance Metric record for **Test Maintenance Cost Ratio** (TMCR-QA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-maintenance-cost-ratio`
- **Name:** Test Maintenance Cost Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TMCR-QA

## 2. Definition

Test Maintenance Cost Ratio (TMCR-QA) addresses how efficiently resources are converted into outputs and is a fixture of software testing & quality engineering reporting. The formula is Test Maintenance Effort / Total Test Effort - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
TMCR-QA = Test Maintenance Effort / Total Test Effort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2721 (batch 7)
