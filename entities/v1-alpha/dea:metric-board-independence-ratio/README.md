# dea:metric-board-independence-ratio

Candidate Performance Metric record for **Board Independence Ratio** (BIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-board-independence-ratio`
- **Name:** Board Independence Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BIR

## 2. Definition

Board Independence Ratio (BIR) measures conformance to standards, plans, or obligations in the Corporate Governance domain. Its calculation is Independent Directors / Total Board Seats, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Board independence ratio measures the share of directors without material relationships to the company, and it is the structural-metric of governance quality - listing standards (NYSE and NASDAQ both) require majority-independent boards, and proxy advisors use the ratio as a screening threshold. The metric's honest reading requires skepticism about definitional capture: independence is determined by bright-line tests (former-employee cooling-off periods, fee thresholds, related-party exposure), so directors can be technically independent while deeply socially embedded - the distinction between structural and behavioral independence is real. Research findings are humbling for the metric's predictive value: board independence correlates weakly with firm performance in most studies, though it correlates more credibly with oversight outcomes like CEO-dismissal sensitivity. Read with committee independence (audit committee independence is separately mandated and more consequential), average director tenure (long tenure erodes independence in practice), and interlocking directorship exposure.

## Formula

```
Independent Directors / Total Board Seats
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1041 (batch 4)
