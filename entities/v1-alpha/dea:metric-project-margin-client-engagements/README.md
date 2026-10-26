# dea:metric-project-margin-client-engagements

Candidate Performance Metric record for **Project Margin (Client Engagements)** (PM-PS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-margin-client-engagements`
- **Name:** Project Margin (Client Engagements)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PM-PS

## 2. Definition

Project Margin (Client Engagements) (PM-PS) addresses the economic value created or preserved and is a fixture of professional services reporting. Its calculation is (Fees - Delivery Costs) / Fees, measured in percent (%). It originates from and is most used in Professional services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Engagement revenue minus direct delivery cost - the profitability metric at the unit the firm actually operates in: the engagement, and the one that corrects the practice-level averages that hide everything - the client mix, the scope-creep pattern, and the leverage quality of the staffing pyramid. Its strategic significance is the portfolio truth it forces: firms routinely discover that a minority of engagements carry most of the profit while respected flagship clients sit at negative margin, a finding that only engagement-level arithmetic can surface. The honest version includes all delivery cost - the rework, the internal reviews, and the partners' unbillable time on the account - since margins that exclude partner attention are comfortable fictions. Read with the trend-by-phase: engagement margins by lifecycle stage reveal the classic pattern of first-phase over-servicing to win the next phase, and the margin at renewal versus the margin at signature is the client-relationship economics in one comparison.

## Formula

```
PM-PS = (Fees - Delivery Costs) / Fees
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 683 (batch 2)
