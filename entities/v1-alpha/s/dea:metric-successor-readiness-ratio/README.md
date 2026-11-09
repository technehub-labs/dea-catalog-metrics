# dea:metric-successor-readiness-ratio

Candidate Performance Metric record for **Successor Readiness Ratio** (SRR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-successor-readiness-ratio`
- **Name:** Successor Readiness Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRR-W

## 2. Definition

Successor Readiness Ratio (SRR-W) captures exposure to adverse outcomes for organizations tracking workforce planning & analytics. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Ready-Now Successors / Critical Roles - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of critical roles with ready-now (or ready-soon) identified successors. It is the quantified buffer against key-person risk and the leading indicator of leadership pipeline health. Ready ratings drift optimistic when assessed by the incumbent's sponsor, so validate with actual placements and success rates of successors appointed. Read with key-person dependency ratio and internal promotion fill rates.

## Formula

```
SRR-W = Ready-Now Successors / Critical Roles
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1455 (batch 5)
