# dea:metric-recurring-findings-rate

Candidate Performance Metric record for **Recurring Findings Rate** (RFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recurring-findings-rate`
- **Name:** Recurring Findings Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RFR

## 2. Definition

Recurring Findings Rate (RFR) addresses the quality of outputs and outcomes and is a fixture of internal audit reporting. The formula is Findings Repeated from Prior Cycle / Total Findings - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of audit findings that repeat from prior cycles - the metric that measures whether the organization's control problems are being fixed or merely re-described, and the most economical quality signal available to audit committees: it requires no new testing, only the discipline of comparing findings across years. Its strategic significance is the root-cause truth it exposes: a finding that recurs means the corrective action addressed a symptom, the action was never verified, or the fix decayed after closure accountability ended - and each of those is an organizational statement, not a process defect. The analysis that moves the metric is by category: recurrence concentrated in one system or function indicates structural underinvestment (IT general controls being the canonical case), while scattered recurrence indicates a fix-and-decay culture. The remediation discipline that actually works is verification after closure with a stabilization window, since findings marked fixed at go-live recur at a rate the closure report never captured.

## Formula

```
Findings Repeated from Prior Cycle / Total Findings
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 619 (batch 2)
