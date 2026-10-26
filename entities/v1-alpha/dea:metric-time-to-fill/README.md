# dea:metric-time-to-fill

Candidate Performance Metric record for **Time to Fill** (TTF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-fill`
- **Name:** Time to Fill
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTF

## 2. Definition

Time to Fill (TTF) measures how efficiently resources are converted into outputs in the Human Resources domain. Its calculation is Days from Job Requisition to Offer Acceptance, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures days from job requisition approval to offer acceptance. It matters because every open seat costs productivity and risks losing candidates to faster competitors. Teams can beat it by lowering the hiring bar or pre-classifying internal moves as instant fills. Read with Quality of Hire and Time to Hire to confirm speed is not bought with weaker selection.

## Formula

```
Days from Job Requisition to Offer Acceptance
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 132 (batch 1)
