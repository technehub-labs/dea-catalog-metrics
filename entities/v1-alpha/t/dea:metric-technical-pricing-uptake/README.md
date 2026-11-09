# dea:metric-technical-pricing-uptake

Candidate Performance Metric record for **Technical Pricing Uptake** (TPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-pricing-uptake`
- **Name:** Technical Pricing Uptake
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TPU

## 2. Definition

Technical Pricing Uptake (TPU) captures capability maturity or development for organizations tracking insurance underwriting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Policies Priced with Technical Model / Policies Priced - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Insurance sector.

## 3. Context

Measures the share of quotes or written premium that follows technically indicated pricing, versus pricing overridden for market reasons. It quantifies the gap between the actuarial view and commercial reality, which is where underwriting margin quietly leaks. Full uptake is not the goal - commercial judgment has a role - but systematic divergence in one segment signals strategy inconsistency. Read with rate adequacy index (Underwriting) and underwriting loss ratio by uptake cohort.

## Formula

```
TPU = Policies Priced with Technical Model / Policies Priced
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1521 (batch 6)
