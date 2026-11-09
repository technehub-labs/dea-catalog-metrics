# dea:metric-vintage-default-emergence-curve

Candidate Performance Metric record for **Vintage Default Emergence Curve** (VDEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vintage-default-emergence-curve`
- **Name:** Vintage Default Emergence Curve
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VDEC

## 2. Definition

Vintage Default Emergence Curve (VDEC) measures exposure to adverse outcomes in the Credit & Collections Risk (Enterprise) domain. The formula is Cumulative Default Rate by Loan Age Cohort - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how defaults emerge over the life of loans by origination cohort. Vintage curves expose underwriting quality shifts season by season. Early-performance curves flatten misleadingly before later-stage defaults arrive. Read with probability of default (Deep Dive) and cohort delinquency transition rates.

## Formula

```
VDEC = Cumulative Default Rate by Loan Age Cohort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** credit_collections_risk_enterprise

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4202 (batch 9)
