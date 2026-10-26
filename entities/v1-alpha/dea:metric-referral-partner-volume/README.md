# dea:metric-referral-partner-volume

Candidate Performance Metric record for **Referral Partner Volume** (RPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-referral-partner-volume`
- **Name:** Referral Partner Volume
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPV

## 2. Definition

Referral Partner Volume (RPV) captures growth over time for organizations tracking insurance distribution & brokerage. Its calculation is New Business from Referral Partners per Period, measured in count (items per period). It originates from and is most used in Insurance distribution practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures business referred through partner channels in insurance distribution. It matters because partner channels scale distribution without linear cost. Volume can be bought with referral commissions that exceed channel value. Read with Quote Conversion Rate (Insurance) and persistency of partner-referred policies to confirm partner flow is profitable.

## Formula

```
New Business from Referral Partners per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1161 (batch 4)
