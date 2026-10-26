# dea:metric-farebox-recovery-ratio

Candidate Performance Metric record for **Farebox Recovery Ratio** (FBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-farebox-recovery-ratio`
- **Name:** Farebox Recovery Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FBR

## 2. Definition

Farebox Recovery Ratio (FBR) addresses the economic value created or preserved and is a fixture of public transit reporting. The formula is Fare Revenue / Operating Costs - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Public transit sector.

## 3. Context

Farebox recovery ratio measures fare revenue against operating cost, and it is the subsidy metric of public transit - the number that frames political debates about transit funding, with systems in dense Asian cities exceeding 100 percent while US bus systems often recover under 20 percent. The metric is frequently misused: farebox recovery is a funding-policy variable, not a performance verdict, since fares are a policy choice (equity objectives cap them), service mandates require coverage routes regardless of demand, and operating cost structures vary enormously. Optimizing recovery by raising fares can backfire through ridership elasticity, suppressing revenue while burdening riders. Read with fare elasticity evidence, cost per trip by mode, subsidy per trip against policy objectives, and ridership trend to test whether recovery gains are real or self-defeating.

## Formula

```
Fare Revenue / Operating Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1002 (batch 3)
