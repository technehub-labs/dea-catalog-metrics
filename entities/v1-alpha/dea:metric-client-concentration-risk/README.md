# dea:metric-client-concentration-risk

Candidate Performance Metric record for **Client Concentration Risk** (CCR-PS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-concentration-risk`
- **Name:** Client Concentration Risk
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCR-PS

## 2. Definition

Within Professional Services, Client Concentration Risk (CCR-PS) is used to gauge exposure to adverse outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Largest Client Fee Revenue / Total Fee Revenue - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Professional services sector.

## 3. Context

The share of revenue from the largest clients - the dependency metric of the professional-services model, where the chronic failure mode is the firm that is healthy by every operating measure but is one client-relationship change away from crisis: procurement turnover, a champion's departure, or a strategic shift at the client can remove a fifth of the revenue in a quarter. Its strategic significance is the valuation discount it imposes: advisory businesses with heavy concentration trade below the multiple of diversified peers, because the acquirer is buying a relationship risk, not a revenue line. The honest measurement tracks both share and relationship-depth (number of engaged partners, practice lines, and years - depth diversifies within the account) since a client spanning five practice lines is stickier than one at five times the revenue in a single line. Read with the contract-renewal calendar: concentration is only actionable ahead of the renewal dates, which is why the metric is always published with the renewal timeline.

## Formula

```
Largest Client Fee Revenue / Total Fee Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 686 (batch 2)
