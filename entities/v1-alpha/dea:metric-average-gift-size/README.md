# dea:metric-average-gift-size

Candidate Performance Metric record for **Average Gift Size** (AGS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-gift-size`
- **Name:** Average Gift Size
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AGS

## 2. Definition

Average Gift Size (AGS) measures the economic value created or preserved in the Nonprofit & NGO domain. It is computed as Total Donations / Number of Gifts, expressed in currency value. Its use is concentrated in Nonprofit & NGO. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures mean donation value per donor or gift in nonprofit fundraising. It matters because gift economics determine fundraising cost coverage. Gaming risk includes counting pledged but unfulfilled amounts. Read with Donor Retention Rate and Fundraising Cost per Dollar Raised to confirm gift growth is real and efficient.

## Formula

```
Total Donations / Number of Gifts
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_ngo
- **Sector:** nonprofit_ngo

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1170 (batch 4)
