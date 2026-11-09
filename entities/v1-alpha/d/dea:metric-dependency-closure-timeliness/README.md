# dea:metric-dependency-closure-timeliness

Candidate Performance Metric record for **Dependency Closure Timeliness** (DCT-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dependency-closure-timeliness`
- **Name:** Dependency Closure Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCT-PM

## 2. Definition

A Project Management (Deep Dive) indicator, Dependency Closure Timeliness (DCT-PM) quantifies exposure to adverse outcomes. The formula is Cross-Project Dependencies Resolved by Date / Dependencies - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether cross-project and cross-team dependencies resolve by their committed dates. Late dependencies cascade: one slippage becomes several project delays. Timeliness on declared dependencies misses the undeclared ones discovered mid-flight. Read with critical path adherence and portfolio dependency visibility coverage.

## Formula

```
DCT-PM = Cross-Project Dependencies Resolved by Date / Dependencies
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2951 (batch 7)
