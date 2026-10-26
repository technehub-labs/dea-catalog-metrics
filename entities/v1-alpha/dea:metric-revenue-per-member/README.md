# dea:metric-revenue-per-member

Candidate Performance Metric record for **Revenue per Member** (RPM-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-member`
- **Name:** Revenue per Member
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RPM-F

## 2. Definition

Revenue per Member (RPM-F) captures the economic value created or preserved for organizations tracking fitness & wellness. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total Revenue / Average Members, measured in currency per unit. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Fitness & wellness practice.

## 3. Context

Revenue per member measures average monthly revenue across the membership base, and it is the monetization-depth metric that sits beside membership-count growth - a gym can grow revenue without adding members (price increases, tier upgrades, personal training attach) or add members while revenue per member falls (discount-driven growth). The metric's decomposition is the management information: dues revenue versus ancillary (personal training, classes, retail, supplements) reveal different strategic positions - boutique studios monetize ancillary at multiples of big-box gyms. The pricing-model effect is structural: budget models with no-contract pricing trade revenue per member for volume. Read with membership growth (the pair that must be read together), ancillary attach rates by member cohort, and lifetime value per member which combines revenue per month with retention.

## Formula

```
Total Revenue / Average Members
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** fitness_wellness
- **Sector:** fitness_wellness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1033 (batch 3)
