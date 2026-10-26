# dea:metric-estimate-accuracy-schedule

Candidate Performance Metric record for **Estimate Accuracy - Schedule** (EAS-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-estimate-accuracy-schedule`
- **Name:** Estimate Accuracy - Schedule
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EAS-PM

## 2. Definition

Estimate Accuracy - Schedule (EAS-PM) addresses the quality of outputs and outcomes and is a fixture of project management (deep dive) reporting. Its calculation is Actual Duration / Estimated Duration at Milestone, measured in ratio (x:1 or x). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the historical reliability of project duration estimates. Chronic under-estimation forces every downstream commitment to be fiction. Accuracy on recent, comparable work is what calibrates future bids. Read with schedule variance percent and estimation bias calibration index.

## Formula

```
EAS-PM = Actual Duration / Estimated Duration at Milestone
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2931 (batch 7)
