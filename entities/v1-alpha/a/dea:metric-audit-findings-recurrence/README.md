# dea:metric-audit-findings-recurrence

Candidate Performance Metric record for **Audit Findings Recurrence** (AFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-findings-recurrence`
- **Name:** Audit Findings Recurrence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AFR

## 2. Definition

Audit Findings Recurrence (AFR) captures the quality of outputs and outcomes for organizations tracking risk & compliance. Its calculation is Repeat Findings / Total Findings, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of audit findings that repeat across cycles - the metric that answers whether the organization fixes problems or documents them. Its strategic weight is what it says about the fix pipeline: a finding repeated means either the corrective action was cosmetic, the root cause was systemic and the action addressed a symptom, or the fix decayed because accountability ended when the action was marked closed. Recurrence is the most economical audit-quality signal available, since it requires no new testing - only tracking. Read with root-cause taxonomy: findings that recur by category (IT general controls are the canonical example) indicate structural underinvestment in that domain, while randomly distributed recurrence indicates process-discipline weakness. The remediation discipline that moves this metric is verification after closure, not more findings.

## Formula

```
AFR = Repeat Findings / Total Findings
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 379 (batch 1)
