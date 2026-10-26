# dea:metric-pay-equity-ratio

Candidate Performance Metric record for **Pay Equity Ratio** (PEQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pay-equity-ratio`
- **Name:** Pay Equity Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PEQ

## 2. Definition

Pay Equity Ratio (PEQ) captures conformance to standards, plans, or obligations for organizations tracking diversity, equity & inclusion. It is defined as Median Pay of Comparison Group / Median Pay of Reference Group; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Compares compensation across demographic groups in like-for-like roles, typically expressed as the ratio of underrepresented group median pay to majority group median. It is the core quantitative anchor of fair-pay commitments and increasingly a disclosure expectation. The honesty hinges on the like-for-like job architecture: narrow job matching can hide inequity, and regression-adjusted ratios can obscure unexplained gaps. Read with promotion parity ratio and hiring diversity rate.

## Formula

```
Median Pay of Comparison Group / Median Pay of Reference Group
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** diversity_equity_inclusion

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1368 (batch 5)
