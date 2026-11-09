# dea:metric-claims-leakage-rate-deep-dive

Candidate Performance Metric record for **Claims Leakage Rate (Deep Dive)** (CLR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-leakage-rate-deep-dive`
- **Name:** Claims Leakage Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CLR-D

## 2. Definition

A Insurance Claims Deep Dive indicator, Claims Leakage Rate (Deep Dive) (CLR-D) quantifies the economic value created or preserved. It is computed as Avoidable Claim Costs / Total Claim Costs, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures amounts paid in excess of what proper adjudication would have required - missed subrogation, duplicate payment, unwarranted allocations, over-valuation. Leakage is invisible in the loss ratio without file-level audits, and estimates that are never audit-grounded are folklore. Recovery-focused programs can overpay in the other direction: leakage includes underpayment that triggers litigation and regulatory findings. Read with audit coverage of paid files and claims cycle time (Deep Dive).

## Formula

```
CLR-D = Avoidable Claim Costs / Total Claim Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1543 (batch 6)
