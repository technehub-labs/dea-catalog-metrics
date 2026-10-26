# dea:metric-match-rule-precision

Candidate Performance Metric record for **Match Rule Precision** (MRP-MD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-match-rule-precision`
- **Name:** Match Rule Precision
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRP-MD

## 2. Definition

Within Master Data Management, Match Rule Precision (MRP-MD) is used to gauge the quality of outputs and outcomes. Its calculation is True Matches / Total Auto-Matches, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
True Matches / Total Auto-Matches
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** master_data_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3636 (batch 8)
