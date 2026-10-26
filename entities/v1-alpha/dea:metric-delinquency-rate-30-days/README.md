# dea:metric-delinquency-rate-30-days

Candidate Performance Metric record for **Delinquency Rate (30+ Days)** (DEL30) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delinquency-rate-30-days`
- **Name:** Delinquency Rate (30+ Days)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DEL30

## 2. Definition

Delinquency Rate (30+ Days) (DEL30) measures exposure to adverse outcomes in the Retail Banking & Lending domain. The formula is Loans 30+ Days Past Due / Gross Loans - reported in percent (%). It is a standard measure in the Banking sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The 30+ day delinquency rate measures the share of loans with payments past due beyond a month, and it is the earliest reliable leading indicator of credit losses - charge-offs lag delinquency by months, so the roll-rate model (30-to-60-to-90-to-loss) is how lenders forecast future losses from current delinquency. The metric is also a sensitive economic indicator, moving with unemployment, inflation-driven household stress, and regional shocks. Reading it well requires cohort discipline: vintage analysis separates deteriorating underwriting from a deteriorating economy, since both raise delinquency but demand opposite responses. Read with roll rates by vintage and channel, cure rates (how many delinquent loans recover), and payment-to-income stress indicators for the current book.

## Formula

```
Loans 30+ Days Past Due / Gross Loans
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 837 (batch 3)
