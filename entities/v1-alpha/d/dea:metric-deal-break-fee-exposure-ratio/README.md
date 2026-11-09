# dea:metric-deal-break-fee-exposure-ratio

Candidate Performance Metric record for **Deal Break Fee Exposure Ratio** (DBFE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deal-break-fee-exposure-ratio`
- **Name:** Deal Break Fee Exposure Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DBFE

## 2. Definition

Deal Break Fee Exposure Ratio (DBFE) addresses exposure to adverse outcomes and is a fixture of mergers & acquisitions reporting. Its calculation is Break Fees Payable on Failed Deals / Deal Value, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
DBFE = Break Fees Payable on Failed Deals / Deal Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1700 (batch 6)
