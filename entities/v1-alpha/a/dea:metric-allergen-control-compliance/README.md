# dea:metric-allergen-control-compliance

Candidate Performance Metric record for **Allergen Control Compliance** (ACC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-allergen-control-compliance`
- **Name:** Allergen Control Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACC

## 2. Definition

Allergen Control Compliance (ACC) measures exposure to adverse outcomes in the Food & Beverage Manufacturing domain. It is defined as Allergen Control Checks Passed / Checks; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Food & Beverage, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures adherence to allergen management controls - segregation, changeover cleaning, label verification. Allergens are the leading cause of food recalls, and control failures are process failures with severe consumer consequences. Swab-based verification of changeover cleaning is the objective test, and label reconciliation belongs in scope. Read with consumer complaint rate (Deep Dive) allergen themes and audit findings.

## Formula

```
ACC = Allergen Control Checks Passed / Checks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1799 (batch 6)
