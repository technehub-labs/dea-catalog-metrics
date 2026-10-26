# dea:metric-customer-segment-nps-delta

Candidate Performance Metric record for **Customer Segment NPS Delta** (CSND) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-segment-nps-delta`
- **Name:** Customer Segment NPS Delta
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CSND

## 2. Definition

Customer Segment NPS Delta (CSND) addresses the engagement or satisfaction of the people involved and is a fixture of customer journey & experience reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as NPS of Target Segment - NPS of Baseline Segment, expressed in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Compares Net Promoter Score across customer segments, converting a blunt satisfaction average into a diagnostic of which audiences the experience actually works for. Strategic because resource allocation follows the delta: segments with high scores and low growth usually reveal monetization gaps, not loyalty surpluses. Caveats are sample size at segment level (NPS is noisy below a few hundred responses) and priming effects from recent interactions. Read with segment revenue growth and churn by segment, never alone.

## Formula

```
NPS of Target Segment - NPS of Baseline Segment
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1254 (batch 4)
