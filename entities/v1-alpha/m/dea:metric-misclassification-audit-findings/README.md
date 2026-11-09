# dea:metric-misclassification-audit-findings

Candidate Performance Metric record for **Misclassification Audit Findings** (MAF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-misclassification-audit-findings`
- **Name:** Misclassification Audit Findings
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MAF

## 2. Definition

Misclassification Audit Findings (MAF) captures conformance to standards, plans, or obligations for organizations tracking gig & contingent workforce. It is computed as Worker Classification Violations Detected / Workers Audited, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures findings from audits testing whether gig or contractor workers are legally employees under applicable tests. Each finding carries back-tax, penalty, and co-employment exposure, and findings per audit indicate systemic versus isolated risk. Trend matters more than single-audit counts, as regulators probe repeatedly. Read with contingent workforce ratio and jurisdictional classification methodology currency.

## Formula

```
MAF = Worker Classification Violations Detected / Workers Audited
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** gig_contingent_workforce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1466 (batch 5)
