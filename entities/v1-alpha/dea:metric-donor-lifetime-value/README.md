# dea:metric-donor-lifetime-value

Candidate Performance Metric record for **Donor Lifetime Value** (DLTV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-donor-lifetime-value`
- **Name:** Donor Lifetime Value
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DLTV

## 2. Definition

A Nonprofit & NGO indicator, Donor Lifetime Value (DLTV) quantifies the economic value created or preserved. It is defined as Average Donation x Average Donor Lifespan x Margin; the result is stated in currency value. In Nonprofit & NGO, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Donor lifetime value projects the total giving of a donor across their relationship, and it is the strategic resource-allocation metric for fundraising - it justifies losing money on first-gift acquisition when the cohort's lifetime value exceeds acquisition cost, which is the math most donor-acquisition decisions hide from. LTV decomposes into gift size, frequency, retention, and relationship duration, and it varies enormously by acquisition channel (major-donor cultivation versus direct response) and by constituency (alumni, patients, faith communities each carry distinct curves). The measurement honesty issue is discounting and attribution of upgrades (planned gifts and bequests arrive at the end, so near-term LTV understates the full arc). Read with acquisition cost by channel, cohort retention curves, and the planned-giving pipeline which is deferred LTV.

## Formula

```
DLTV = Average Donation x Average Donor Lifespan x Margin
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_ngo
- **Sector:** nonprofit_ngo

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1171 (batch 4)
