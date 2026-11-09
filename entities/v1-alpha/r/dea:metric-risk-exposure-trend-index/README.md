# dea:metric-risk-exposure-trend-index

Candidate Performance Metric record for **Risk Exposure Trend Index** (RETI-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-exposure-trend-index`
- **Name:** Risk Exposure Trend Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RETI-PM

## 2. Definition

Risk Exposure Trend Index (RETI-PM) captures exposure to adverse outcomes for organizations tracking project management (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Change in Aggregated Risk Score per Reporting Cycle - reported in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether aggregated project risk exposure is rising or falling over time. A rising trend with a green status report is the classic pre-failure signature. Index construction embeds severity judgments that need consistent calibration. Read with risk response plan completion rate and project portfolio health distribution.

## Formula

```
RETI-PM = Change in Aggregated Risk Score per Reporting Cycle
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2939 (batch 7)
