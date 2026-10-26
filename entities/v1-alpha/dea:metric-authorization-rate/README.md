# dea:metric-authorization-rate

Candidate Performance Metric record for **Authorization Rate** (AUTH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-authorization-rate`
- **Name:** Authorization Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AUTH

## 2. Definition

Authorization Rate (AUTH) measures the quality of outputs and outcomes in the Payments & Fintech domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Approved Transactions / Authorization Attempts - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Payments & fintech sector.

## 3. Context

Authorization rate is the share of transaction attempts approved by issuers, and in payments it is the quiet battleground between revenue and risk: every declined legitimate transaction is lost revenue plus customer erosion, while every approved fraudulent one is a loss. The industry treats the difference between theoretical maximum (issuer-decline-only) and actual auth rate as recoverable revenue, and optimization here - retry logic, network tokenization, issuer-specific routing - is a genuine margin lever at scale. The metric's blind side is composition: auth rate varies enormously by geography, card type, and merchant category, so a blended number hides where the problem concentrates. Read with false decline rate and fraud rate together, since pushing auth rate up moves fraud up too.

## Formula

```
Approved Transactions / Authorization Attempts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 774 (batch 2)
