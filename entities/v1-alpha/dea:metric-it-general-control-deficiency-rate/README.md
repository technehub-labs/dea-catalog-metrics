# dea:metric-it-general-control-deficiency-rate

Candidate Performance Metric record for **IT General Control Deficiency Rate** (ITGCDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-it-general-control-deficiency-rate`
- **Name:** IT General Control Deficiency Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITGCDR

## 2. Definition

IT General Control Deficiency Rate (ITGCDR) addresses exposure to adverse outcomes and is a fixture of internal controls & financial reporting integrity reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is ITGC Tests with Deficiencies / ITGC Tests - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the rate of deficiencies in ITGCs (access, change, operations) that underpin application controls. ITGC failures silently disable every automated control above them. Deficiency counting that aggregates high and low severity obscures the ones that matter. Read with automated control coverage and identity and access governance maturity.

## Formula

```
ITGC Tests with Deficiencies / ITGC Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_controls_financial_reporting_integrity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3592 (batch 8)
