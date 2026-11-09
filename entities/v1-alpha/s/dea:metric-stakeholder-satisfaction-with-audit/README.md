# dea:metric-stakeholder-satisfaction-with-audit

Candidate Performance Metric record for **Stakeholder Satisfaction with Audit** (SSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stakeholder-satisfaction-with-audit`
- **Name:** Stakeholder Satisfaction with Audit
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSA

## 2. Definition

Within Internal Audit, Stakeholder Satisfaction with Audit (SSA) is used to gauge the engagement or satisfaction of the people involved. The formula is Satisfied Audit Client Survey Responses / Responses - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures auditee and executive satisfaction with the internal audit function. It matters because audit influence depends on trusted relationships, but satisfaction must not be confused with rigor. Scores can drift high when auditors go easy to be liked. Read with Audit Finding Acceptance Rate and repeat-finding trends to confirm satisfaction coexists with spine.

## Formula

```
SSA = Satisfied Audit Client Survey Responses / Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 621 (batch 2)
