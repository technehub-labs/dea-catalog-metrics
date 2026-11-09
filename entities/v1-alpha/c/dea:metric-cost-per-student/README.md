# dea:metric-cost-per-student

Candidate Performance Metric record for **Cost per Student** (CPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-student`
- **Name:** Cost per Student
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPS

## 2. Definition

A Education indicator, Cost per Student (CPS) quantifies how efficiently resources are converted into outputs. Its calculation is Total Institution Cost / Enrolled Students, measured in currency per unit. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Education practice.

## 3. Context

Total expenditure divided by enrolled students - the unit-economics metric of the education model, and the number that exposes whether tuition covers delivery: institutions where tuition is below cost per student are subsidized or eroding, and the gap is the fiscal truth that headline budgets blur. Its strategic significance is the mix that composes it - instruction, administration, facilities, and student services each compete for share, and the trend of the shares is the real strategy conversation, since administrative cost creep at the expense of instruction is the sector's most-cited pathology. Read with the revenue counterpart (net tuition per student, actual not sticker) to get the margin picture, and with outcome data to get the value picture - cost per student alone says nothing about quality of what the spend buys.

## Formula

```
CPS = Total Institution Cost / Enrolled Students
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** education
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 520 (batch 1)
