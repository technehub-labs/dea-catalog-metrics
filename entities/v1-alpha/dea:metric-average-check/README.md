# dea:metric-average-check

Candidate Performance Metric record for **Average Check** (AC-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-check`
- **Name:** Average Check
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AC-H

## 2. Definition

Average Check (AC-H) measures the economic value created or preserved in the Hospitality & Food Service domain. Its calculation is Revenue / Number of Guests or Checks, measured in currency value. It originates from and is most used in Hospitality practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures mean spend per guest visit. It matters because growing check size is the primary revenue lever once traffic is fixed. Upselling can drift into pressure that degrades satisfaction and repeat visits. Read with Guest Satisfaction and Repeat Visit Rate to confirm check growth is welcome, not coercive.

## Formula

```
Revenue / Number of Guests or Checks
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 512 (batch 1)
