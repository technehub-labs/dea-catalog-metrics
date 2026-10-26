# dea:metric-repeat-regulatory-findings-rate

Candidate Performance Metric record for **Repeat Regulatory Findings Rate** (RRFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-regulatory-findings-rate`
- **Name:** Repeat Regulatory Findings Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRFR

## 2. Definition

A Regulatory Affairs & Compliance Operations indicator, Repeat Regulatory Findings Rate (RRFR) quantifies the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Findings Recurring across Cycles / Findings - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of regulatory findings that recur after prior remediation. It is the sharpest accountability metric in compliance: a repeat finding tells the regulator that remediation was cosmetic, and it materially raises penalty exposure. Root-cause discipline distinguishes control failure from control design failure, which need different fixes. Read with remediation aging and regulatory engagement success rate.

## Formula

```
Findings Recurring across Cycles / Findings
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1592 (batch 6)
