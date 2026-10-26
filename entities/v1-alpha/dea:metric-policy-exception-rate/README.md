# dea:metric-policy-exception-rate

Candidate Performance Metric record for **Policy Exception Rate** (PER-O) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-policy-exception-rate`
- **Name:** Policy Exception Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PER-O

## 2. Definition

Policy Exception Rate (PER-O) captures conformance to standards, plans, or obligations for organizations tracking operating model & decision effectiveness. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Policy Exceptions Granted / Policy Applications - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the frequency of exceptions to established policies. It matters because exception volume is the leading indicator that policy no longer fits reality. Exceptions can be granted silently so they never enter the count. Read with Policy Refresh cadence and Audit findings to confirm exceptions are visible and drive policy updates.

## Formula

```
Policy Exceptions Granted / Policy Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1308 (batch 5)
