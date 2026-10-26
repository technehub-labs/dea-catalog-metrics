# dea:metric-average-client-relationship-value

Candidate Performance Metric record for **Average Client Relationship Value** (ACRV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-client-relationship-value`
- **Name:** Average Client Relationship Value
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACRV

## 2. Definition

A Wealth Management indicator, Average Client Relationship Value (ACRV) quantifies the economic value created or preserved. The formula is Assets under Management / Client Relationships - reported in currency value. It is a standard measure in the Wealth management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Average client relationship value measures total revenue (or assets) per client relationship, and it is the segmentation-insight metric of wealth management: the business is bimodal - most relationships are subscale while a small tail carries the economics - so the average is really a statement about client mix. Its trend is the strategic signal: a rising average usually means segment discipline (shedding subscale clients, or the minimum account size creeping upward), while a falling one can mean growth diluting down-market. The measurement must be relationship-based rather than account-based, since clients hold multiple accounts and account-level averaging undercounts the true relationship. Read with client-profitability distribution (the tail analysis), segment migration flows, and service-cost-to-serve per relationship since value without margin coverage is not sustainable.

## Formula

```
Assets under Management / Client Relationships
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1140 (batch 4)
