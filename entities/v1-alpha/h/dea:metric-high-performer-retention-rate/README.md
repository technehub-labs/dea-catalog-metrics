# dea:metric-high-performer-retention-rate

Candidate Performance Metric record for **High-Performer Retention Rate** (HPRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-high-performer-retention-rate`
- **Name:** High-Performer Retention Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HPRR

## 2. Definition

High-Performer Retention Rate (HPRR) measures the retention of customers, users, or assets over time in the Employee Engagement & Culture (Deep Dive) domain. The formula is Top Quartile Performers Retained / Top Quartile - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures retention of the top-rated employee population specifically. Losing high performers is a compounding capability loss with market-facing costs. Rating inflation blurs who counts as high-performing. Read with high performer retention rate (Deep Dive) and regretted attrition ratio.

## Formula

```
HPRR = Top Quartile Performers Retained / Top Quartile
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** employee_engagement_culture_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3872 (batch 8)
