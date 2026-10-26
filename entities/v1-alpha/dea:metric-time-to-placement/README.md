# dea:metric-time-to-placement

Candidate Performance Metric record for **Time to Placement** (TTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-placement`
- **Name:** Time to Placement
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTP

## 2. Definition

Time to Placement (TTP) addresses how efficiently resources are converted into outputs and is a fixture of staffing & recruiting reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days from Mandate Opening to Accepted Offer - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Staffing & recruiting sector.

## 3. Context

Measures days from candidate sourcing start to accepted placement in staffing. It matters because placement speed drives client satisfaction and requisition win rates. Speed can be bought by submitting poorly matched candidates to look active. Read with Placement Retention at 90 Days and Offer Decline Rate (Staffing) to confirm fast placements stick.

## Formula

```
TTP = Days from Mandate Opening to Accepted Offer
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** staffing_recruiting
- **Sector:** staffing_recruiting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1022 (batch 3)
