# dea:metric-escalation-rate-to-executive

Candidate Performance Metric record for **Escalation Rate to Executive** (ERE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-escalation-rate-to-executive`
- **Name:** Escalation Rate to Executive
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERE

## 2. Definition

Escalation Rate to Executive (ERE) measures how efficiently resources are converted into outputs in the Operating Model & Decision Effectiveness domain. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Decisions Escalated to Executive Level / Decisions Raised; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how often decisions escalate beyond their designated authority level. It matters because chronic escalation means the operating model is failing to empower the right levels. Escalations can be hidden by pre-clearing decisions informally before formal meetings. Read with RACI Clarity Index and decision latency to confirm decisions happen where they should.

## Formula

```
ERE = Decisions Escalated to Executive Level / Decisions Raised
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1302 (batch 5)
