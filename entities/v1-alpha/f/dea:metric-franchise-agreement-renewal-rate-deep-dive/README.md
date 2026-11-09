# dea:metric-franchise-agreement-renewal-rate-deep-dive

Candidate Performance Metric record for **Franchise Agreement Renewal Rate (Deep Dive)** (FARR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-franchise-agreement-renewal-rate-deep-dive`
- **Name:** Franchise Agreement Renewal Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FARR-D

## 2. Definition

Franchise Agreement Renewal Rate (Deep Dive) (FARR-D) addresses the retention of customers, users, or assets over time and is a fixture of franchise operations (deep dive) reporting. It is computed as Renewed Agreements / Expiring Agreements, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of franchisees renewing at term end. It is the ultimate confidence vote in the system: renewals validate the economics, the brand trajectory, and the relationship in one decision, and non-renewal clusters are early warnings of regional or systemic failure. Renewals secured through fee concessions are retention of a kind that erodes the model. Read with franchisee satisfaction index (Deep Dive) and unit economics trends.

## Formula

```
FARR-D = Renewed Agreements / Expiring Agreements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** franchise_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2222 (batch 6)
