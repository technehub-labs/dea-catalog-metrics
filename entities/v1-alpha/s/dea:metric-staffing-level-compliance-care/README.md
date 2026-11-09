# dea:metric-staffing-level-compliance-care

Candidate Performance Metric record for **Staffing Level Compliance (Care)** (SLCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-staffing-level-compliance-care`
- **Name:** Staffing Level Compliance (Care)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLCC

## 2. Definition

Staffing Level Compliance (Care) (SLCC) captures conformance to standards, plans, or obligations for organizations tracking elder & social care. The formula is Shifts Meeting Minimum Staffing / Shifts - reported in percent (%). It is a standard measure in the Social care sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Staffing level compliance measures adherence to required staffing ratios and skill mix (registered nurse coverage, aide hours per resident day), and it is the capacity metric that underlies nearly every other care-quality outcome - the evidence base links understaffing to pressure ulcers, falls, weight loss, and infection outbreaks, which is why regulators increasingly mandate and publish staffing levels. The measurement is exposure-based: hours per resident day, not bodies per shift, since acuity varies - and self-reported compliance versus payroll-verified staffing can diverge (the gap being the real signal). Compliance is a floor: minimum ratios are set low enough that full compliance still leaves some units stretched. Read with agency-temporary staffing share (continuity-of-care cost), turnover-adjusted productivity (high-turnover units need more hours for the same output), and outcome trends by staffing quartile rather than binary compliance.

## Formula

```
SLCC = Shifts Meeting Minimum Staffing / Shifts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1197 (batch 4)
