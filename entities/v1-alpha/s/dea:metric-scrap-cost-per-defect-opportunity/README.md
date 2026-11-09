# dea:metric-scrap-cost-per-defect-opportunity

Candidate Performance Metric record for **Scrap Cost per Defect Opportunity** (SCPDO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scrap-cost-per-defect-opportunity`
- **Name:** Scrap Cost per Defect Opportunity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCPDO

## 2. Definition

Within Process Capability & Six Sigma (Deep Dive), Scrap Cost per Defect Opportunity (SCPDO) is used to gauge the economic value created or preserved. The formula is Scrap Cost / Defect Opportunities - reported in currency per unit. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Manufacturing sector.

## Formula

```
SCPDO = Scrap Cost / Defect Opportunities
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** capability
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4092 (batch 9)
