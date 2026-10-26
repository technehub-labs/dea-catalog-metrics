# dea:metric-schedule-buffer-consumption-rate

Candidate Performance Metric record for **Schedule Buffer Consumption Rate** (SBCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-buffer-consumption-rate`
- **Name:** Schedule Buffer Consumption Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SBCR

## 2. Definition

Schedule Buffer Consumption Rate (SBCR) addresses exposure to adverse outcomes and is a fixture of project risk & issue management reporting. It is defined as Buffer Consumed / Buffer Planned; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Buffer Consumed / Buffer Planned
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** project_risk_issue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3425 (batch 7)
