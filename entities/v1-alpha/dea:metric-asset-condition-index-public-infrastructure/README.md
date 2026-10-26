# dea:metric-asset-condition-index-public-infrastructure

Candidate Performance Metric record for **Asset Condition Index (Public Infrastructure)** (ACI-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-condition-index-public-infrastructure`
- **Name:** Asset Condition Index (Public Infrastructure)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACI-P

## 2. Definition

Asset Condition Index (Public Infrastructure) (ACI-P) captures the utilization or availability of capacity for organizations tracking government & public administration. It is defined as Weighted Infrastructure Condition Score; the result is stated in index (0-100 or normalized). In Public Sector, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the physical condition of public assets - roads, bridges, buildings, water systems - against maintenance and renewal standards. It converts deferred maintenance into a quantified liability, which is essential because infrastructure decay is invisible in annual budgets until it becomes dangerous. Index weights and inspection sampling determine credibility, and condition data ages quickly. Read with renewal funding gap and asset failure incident trends.

## Formula

```
ACI-P = Weighted Infrastructure Condition Score
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** government_public_administration
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1586 (batch 6)
