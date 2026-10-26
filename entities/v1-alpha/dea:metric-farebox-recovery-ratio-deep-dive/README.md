# dea:metric-farebox-recovery-ratio-deep-dive

Candidate Performance Metric record for **Farebox Recovery Ratio (Deep Dive)** (FRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-farebox-recovery-ratio-deep-dive`
- **Name:** Farebox Recovery Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FRR-D

## 2. Definition

Farebox Recovery Ratio (Deep Dive) (FRR-D) captures the economic value created or preserved for organizations tracking public transit (deep dive). It is defined as Fare Revenue / Operating Cost; the result is stated in percent (%). In Public Transit, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures fare revenue against operating cost. It is the fiscal-dependency metric of public transit, and it frames the policy conversation honestly: most systems require subsidy by design, and the ratio measures how much policy is choosing, not how well the agency performs. Recovery-driven fare increases can suppress ridership and cost more subsidy than they recover. Read with subsidy per passenger journey (Deep Dive) and ridership elasticity evidence.

## Formula

```
Fare Revenue / Operating Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2411 (batch 6)
