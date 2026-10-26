# dea:metric-renewal-rate-with-expansion-deep-dive

Candidate Performance Metric record for **Renewal Rate with Expansion (Deep Dive)** (RREWED) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-renewal-rate-with-expansion-deep-dive`
- **Name:** Renewal Rate with Expansion (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RREWED

## 2. Definition

Renewal Rate with Expansion (Deep Dive) (RREWED) addresses the retention of customers, users, or assets over time and is a fixture of unit economics & growth (deep dive) reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Renewed including Uplift / Contract Value Up for Renewal, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Software.

## 3. Context

Measures the share of up-for-renewal revenue retained including expansion. Renewals are the moment of truth for delivered value. Rates boosted by pre-renewal discounting trade margin for the metric. Read with net dollar retention (Deep Dive) and gross dollar retention (Deep Dive).

## Formula

```
RREWED = Renewed including Uplift / Contract Value Up for Renewal
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4172 (batch 9)
