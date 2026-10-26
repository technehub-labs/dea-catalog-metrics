# dea:metric-gross-renewal-rate

Candidate Performance Metric record for **Gross Renewal Rate** (GRR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-renewal-rate`
- **Name:** Gross Renewal Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GRR-S

## 2. Definition

Within Customer Success (B2B SaaS), Gross Renewal Rate (GRR-S) is used to gauge the retention of customers, users, or assets over time. It is defined as Renewed Contracts / Contracts Up for Renewal; the result is stated in percent (%). In Software & SaaS, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of up-for-renewal recurring revenue that renewed, excluding expansion - the base-retention metric of the subscription renewal motion, and the honest one: it counts what the renewal process kept, not what upsell added, so it cannot hide decay behind growth. Its strategic significance is the ceiling it reveals: existing-customer revenue can only compound if this rate runs high, and each point of renewal is worth several points of new business on acquisition-cost economics. The measurement convention matters: renewal measured by contract count versus by revenue weight diverge when big and small accounts renew differently, and the revenue-weighted figure is the one that carries financial meaning. Read with the reason-coded losses: losses at renewal driven by price, product gaps, budget, or champion departure each demand different countermeasures - and the reason distribution is the renewal program's actual agenda.

## Formula

```
Renewed Contracts / Contracts Up for Renewal
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 582 (batch 2)
