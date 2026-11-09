# dea:metric-rate-adequacy-index-underwriting

Candidate Performance Metric record for **Rate Adequacy Index (Underwriting)** (RAIU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rate-adequacy-index-underwriting`
- **Name:** Rate Adequacy Index (Underwriting)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RAIU

## 2. Definition

Rate Adequacy Index (Underwriting) (RAIU) addresses the economic value created or preserved and is a fixture of insurance underwriting reporting. It is computed as Adequately Priced Renewals / Renewals, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Compares actual rates charged against technically indicated rates for the risks written. It quantifies the gap between pricing discipline and market reality, exposing where growth buys underpriced risk. The index inherits every assumption of the technical pricing model, and adequacy deterioration is often hidden by rate changes that lag loss trend. Read with technical pricing uptake and underwriting loss ratio by segment.

## Formula

```
RAIU = Adequately Priced Renewals / Renewals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1505 (batch 6)
