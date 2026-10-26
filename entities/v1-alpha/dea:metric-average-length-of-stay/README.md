# dea:metric-average-length-of-stay

Candidate Performance Metric record for **Average Length of Stay** (ALOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-length-of-stay`
- **Name:** Average Length of Stay
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ALOS

## 2. Definition

Average Length of Stay (ALOS) addresses how efficiently resources are converted into outputs and is a fixture of healthcare reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Total Inpatient Days / Total Discharges - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Healthcare sector.

## 3. Context

The mean days a patient occupies a bed per admission - the canonical throughput metric of hospital operations, and the one that links clinical practice to economics directly: every day removed from average stay releases capacity equivalent to beds without pouring concrete, which is why length-of-stay programs are the classic first move of hospital operations improvement. The strategic content is the case-mix honesty: blended averages move with the admission mix as much as with efficiency, and credible programs follow disease-specific expected-stay benchmarks against which variance is actual efficiency. Read with readmission data as the paired discipline: stays shortened by discharging patients early and unplanned-ly show up as readmissions within weeks, and a length-of-stay program that improves throughput while readmissions rise has moved cost, not reduced it - the classic failure mode of this metric.

## Formula

```
ALOS = Total Inpatient Days / Total Discharges
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 460 (batch 1)
