# dea:metric-capital-adequacy-ratio

Candidate Performance Metric record for **Capital Adequacy Ratio** (CAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capital-adequacy-ratio`
- **Name:** Capital Adequacy Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAR

## 2. Definition

Capital Adequacy Ratio (CAR) captures exposure to adverse outcomes for organizations tracking banking & financial services. It is defined as Regulatory Capital / Risk-Weighted Assets; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Financial services, it is a recognized element of the standard performance toolkit.

## 3. Context

Regulatory capital as a percentage of risk-weighted assets - the solvency backbone of modern banking, institutionalized by the 1988 Basel Accord and its successors. The ratio exists to absorb unexpected losses without touching depositors, which is why it sits at the center of every supervisory conversation, SREP process, and stress test. A bank operating close to the requirement has no buffer for growth or shocks; one far above it is either conservatively managed or unable to deploy capital profitably - the market increasingly distinguishes these. The denominator is the game: risk weights turn a static capital stack into a moving target, and every Basel renegotiation redistributes the arithmetic across asset classes.

## Formula

```
CAR = Regulatory Capital / Risk-Weighted Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 39 (batch 1)
