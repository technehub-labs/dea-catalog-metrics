# dea:metric-client-referral-rate

Candidate Performance Metric record for **Client Referral Rate** (CRR-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-referral-rate`
- **Name:** Client Referral Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRR-RE

## 2. Definition

Client Referral Rate (CRR-RE) addresses growth over time and is a fixture of real estate brokerage reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Clients from Referrals / New Clients, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Real estate.

## 3. Context

Client referral rate measures the share of new business arriving from client recommendations, and it is the quality-of-service metric that no marketing budget can fake - a referral is a client putting their own reputation behind your service, which happens only when experience genuinely exceeded expectations. In real estate brokerage specifically, referrals are the dominant growth channel for high-performing agents because transaction frequency is low (clients move every 7-10 years) but referral networks compound. The measurement discipline is attribution honesty: agents frequently claim referral status loosely (someone who heard about you through any channel), so the honest version tracks confirmed source. Read with client satisfaction and post-close communication consistency (referrals trace to post-transaction service), repeat-client rate, and lifetime-value-by-source comparisons.

## Formula

```
Clients from Referrals / New Clients
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1018 (batch 3)
