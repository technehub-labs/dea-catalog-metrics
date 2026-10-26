# dea:metric-delegation-of-authority-violations

Candidate Performance Metric record for **Delegation of Authority Violations** (DOAV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delegation-of-authority-violations`
- **Name:** Delegation of Authority Violations
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DOAV

## 2. Definition

Delegation of Authority Violations (DOAV) captures conformance to standards, plans, or obligations for organizations tracking corporate governance. It is defined as Decisions outside Approved Authority Levels / Decisions Audited; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures purchases or decisions executed outside authorized approval limits. It matters because DoA violations are control failures that precede fraud. Violations can be under-detected when approval chains are backdated or split to duck limits. Read with Maverick Spend Rate and Internal Audit findings to confirm authority discipline is real, not paperwork-compliant.

## Formula

```
Decisions outside Approved Authority Levels / Decisions Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1051 (batch 4)
