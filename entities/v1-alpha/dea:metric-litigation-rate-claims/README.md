# dea:metric-litigation-rate-claims

Candidate Performance Metric record for **Litigation Rate (Claims)** (LRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-litigation-rate-claims`
- **Name:** Litigation Rate (Claims)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LRC

## 2. Definition

A Claims Operations (Insurance) indicator, Litigation Rate (Claims) (LRC) quantifies exposure to adverse outcomes. It is computed as Claims Going to Litigation / Claims Settled, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Litigation rate measures the share of claims escalating to lawsuits, and it is the cost-amplification metric of claims handling - a litigated claim costs multiples of a settled one, in legal spend, indemnity inflation, and cycle time measured in years instead of weeks. Rising litigation rate signals either deteriorating claims-handling quality (claimants escalate when they feel mishandled) or a hardening legal environment (attorney representation rates in bodily injury have climbed steadily for years). The metric responds to handling quality in measurable ways: early engagement, empathy in communication, and fair first offers demonstrably reduce escalation. Read with attorney-representation rate by claim type (a leading indicator), first-offer acceptance rates, and litigation cost per claim versus settlement cost.

## Formula

```
LRC = Claims Going to Litigation / Claims Settled
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
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 851 (batch 3)
