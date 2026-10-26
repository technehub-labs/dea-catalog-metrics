# dea:metric-donor-lifetime-value-deep-dive

Candidate Performance Metric record for **Donor Lifetime Value (Deep Dive)** (DLTV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-donor-lifetime-value-deep-dive`
- **Name:** Donor Lifetime Value (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DLTV-D

## 2. Definition

Donor Lifetime Value (Deep Dive) (DLTV-D) measures the economic value created or preserved in the Nonprofit & Donor Operations (Deep Dive) domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Average Lifetime Donations per Donor, measured in currency value. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Nonprofit practice.

## 3. Context

Measures total expected giving per donor relationship. It is the strategic ceiling on acquisition spending: sustainable fundraising acquires donors up to their lifetime value with margin, and organizations acquiring above LTV are burning reserves for donor counts. LTV estimates from young cohorts are fragile, so mature-cohort data should anchor the modeling. Read with cost to raise a dollar (Deep Dive) and mid-level and major-donor upgrade rates.

## Formula

```
DLTV-D = Average Lifetime Donations per Donor
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** governance
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_donor_operations_deep_dive
- **Sector:** nonprofit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2463 (batch 6)
