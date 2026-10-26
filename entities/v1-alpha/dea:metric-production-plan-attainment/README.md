# dea:metric-production-plan-attainment

Candidate Performance Metric record for **Production Plan Attainment** (PPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-production-plan-attainment`
- **Name:** Production Plan Attainment
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPA

## 2. Definition

Production Plan Attainment (PPA) measures conformance to standards, plans, or obligations in the Manufacturing domain. The formula is Actual Production / Planned Production - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## 3. Context

Measures actual production volume achieved against the planned schedule. It matters because missed plans cascade into stockouts, expedites, and overtime. Teams can hit the number by cutting corners on changeovers or quality checks mid-run. Read with Plan Accuracy and Schedule Adherence to distinguish execution failure from unrealistic planning.

## Formula

```
Actual Production / Planned Production
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 251 (batch 1)
