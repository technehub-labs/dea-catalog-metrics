# dea:metric-net-promoter-score

Candidate Performance Metric record for **Net Promoter Score** (NPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-promoter-score`
- **Name:** Net Promoter Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPS

## 2. Definition

A Customer indicator, Net Promoter Score (NPS) quantifies the engagement or satisfaction of the people involved. The formula is % Promoters - % Detractors - reported in score (points). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Net Promoter Score asks customers one question - how likely are you to recommend us (0-10) - and subtracts the share of detractors (0-6) from promoters (9-10). Introduced by Fred Reichheld (Bain & Company, 2003), it became the de facto loyalty standard because it correlates with referral-driven growth and is cheap enough to run continuously. A positive score means promoters outnumber detractors; leading B2B software firms typically exceed +40, while consumer services often hover near 0. Its blind spot is the why - always pair it with a follow-up open-text question, and read it quarterly: single-month swings are usually sampling noise.

## Formula

```
NPS = % Promoters - % Detractors
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Fred Reichheld (Bain & Company), 2003

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 66 (batch 1)
