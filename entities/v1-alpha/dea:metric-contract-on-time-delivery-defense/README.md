# dea:metric-contract-on-time-delivery-defense

Candidate Performance Metric record for **Contract On-Time Delivery (Defense)** (COTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-on-time-delivery-defense`
- **Name:** Contract On-Time Delivery (Defense)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** COTD

## 2. Definition

Contract On-Time Delivery (Defense) (COTD) addresses conformance to standards, plans, or obligations and is a fixture of defense & aerospace reporting. It is defined as Deliveries on Contract Schedule / Deliveries Due; the result is stated in percent (%). In Defense & aerospace, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Contract on-time delivery measures prime and subcontractor adherence to delivery schedules, and it is the industrial-base metric of defense readiness - weapons systems availability depends on a defense-industrial ecosystem where delivery delays cascade through sustainment and modernization programs. The distinctive measurement issue is the baseline negotiation: defense contracts set delivery dates through negotiation between primes and suppliers under incentive structures that reward optimistic promises, so on-time percentages reflect both performance and realism of commitments. Second- and third-tier suppliers are the opacity zone - primes often lack visibility into sub-tier schedule risk until delays surface. Read with first-pass quality acceptance rates (rejections cause rework delays), sub-tier supply chain visibility, raw material lead-time trends, and the delivery-delay root-cause distribution.

## Formula

```
COTD = Deliveries on Contract Schedule / Deliveries Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 972 (batch 3)
