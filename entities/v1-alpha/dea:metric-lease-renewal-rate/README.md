# dea:metric-lease-renewal-rate

Candidate Performance Metric record for **Lease Renewal Rate** (LRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lease-renewal-rate`
- **Name:** Lease Renewal Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LRR

## 2. Definition

Lease Renewal Rate (LRR) measures the retention of customers, users, or assets over time in the Facilities & Real Estate domain. It is computed as Leases Renewed / Leases Expiring, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of expiring leases that renew rather than leave - the retention metric of the landlord-tenant relationship, and strategically the cheapest growth available: renewing a tenant costs a fraction of acquiring one (no vacancy, no fit-out, no commission), so renewal-rate movements swing net operating income more than equivalent rent movements. Its diagnostic content is reason-coded: departures driven by business contraction or relocation are market facts, while departures driven by condition, service, or price competitiveness are management failures, and the reason split tells the landlord which lever to pull. Read with the rent-achieved dimension: a renewal rate bought with deep concessions is worse economics than a lower rate at full rent, which is why mature reporting pairs renewal rate with renewal rent versus expiring rent - the releasing spread that is the honest economics of the renewal decision.

## Formula

```
Leases Renewed / Leases Expiring
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 456 (batch 1)
