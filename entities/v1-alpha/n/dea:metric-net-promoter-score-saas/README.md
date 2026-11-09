# dea:metric-net-promoter-score-saas

Candidate Performance Metric record for **Net Promoter Score (SaaS)** (NPS-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-promoter-score-saas`
- **Name:** Net Promoter Score (SaaS)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPS-S

## 2. Definition

A Customer Success (B2B SaaS) indicator, Net Promoter Score (SaaS) (NPS-S) quantifies the engagement or satisfaction of the people involved. It is computed as % Promoters - % Detractors among SaaS Accounts, expressed in score (points). Its use is concentrated in Software & SaaS. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The recommend metric applied to the SaaS relationship - the loyalty gauge of subscription software, whose strategic significance in this context is the renewal-adjacency: in B2B subscription, the account decision-makers' sentiment is the soft precursor of the renewal decision, and NPS by account is the early-warning layer that customer-success teams prioritize their touches against. The operational value is the segmentation cut: scores by role (end user versus buyer versus economic buyer) diverge sharply, and a product loved by users but unloved by the budget-holder renews on price pressure - the pattern that makes role-split reading essential. The industry convention pairs NPS with churn and expansion in the customer-health stack, and the score earns its place by predicting both, which transactional metrics cannot.

## Formula

```
NPS-S = % Promoters - % Detractors among SaaS Accounts
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
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 580 (batch 2)
