# dea:metric-divestiture-completion-time

Candidate Performance Metric record for **Divestiture Completion Time** (DVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-divestiture-completion-time`
- **Name:** Divestiture Completion Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DVC

## 2. Definition

Divestiture Completion Time (DVC) captures how efficiently resources are converted into outputs for organizations tracking mergers & acquisitions. Its calculation is Days from Decision to Completed Divestiture, measured in days. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures elapsed time from decision to close for disposals and carve-outs. Divestitures carry stranded-cost bleed and management distraction until closed, so time directly destroys value, and carve-out complexity (TSA scoping, systems separation) is the usual cause of drift. Milestone-based tracking beats calendar optimism. Read with stranded cost run-off and TSA exit progress.

## Formula

```
Days from Decision to Completed Divestiture
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1703 (batch 6)
