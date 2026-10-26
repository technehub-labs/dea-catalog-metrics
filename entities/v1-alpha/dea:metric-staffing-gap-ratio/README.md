# dea:metric-staffing-gap-ratio

Candidate Performance Metric record for **Staffing Gap Ratio** (SGR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-staffing-gap-ratio`
- **Name:** Staffing Gap Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SGR-W

## 2. Definition

Staffing Gap Ratio (SGR-W) addresses the utilization or availability of capacity and is a fixture of workforce planning & analytics reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is (Required Staff - Actual Staff) / Required Staff - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures unfilled positions or capability gaps against workforce demand at current plan. It converts workforce planning from headcount accounting into capacity risk, and it directly predicts service degradation and overtime spend. Gaps need quality cuts - critical roles, revenue-critical units - since a blended ratio hides the units that matter. Read with time-to-fill and overtime or contractor spend as the compensating-cost evidence.

## Formula

```
(Required Staff - Actual Staff) / Required Staff
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1451 (batch 5)
