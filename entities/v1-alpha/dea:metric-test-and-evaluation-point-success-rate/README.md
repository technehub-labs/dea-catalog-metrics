# dea:metric-test-and-evaluation-point-success-rate

Candidate Performance Metric record for **Test and Evaluation Point Success Rate** (TEPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-and-evaluation-point-success-rate`
- **Name:** Test and Evaluation Point Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TEPS

## 2. Definition

Test and Evaluation Point Success Rate (TEPS) addresses the quality of outputs and outcomes and is a fixture of defense & aerospace reporting. It is computed as Test Points Passed / Test Points Executed, expressed in percent (%). Its use is concentrated in Defense & aerospace. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of defined test points passed during program test and evaluation. It matters because T&E is the objective evidence gate for defense acquisition milestones. Retesting only failed points after fixes can inflate the rate while masking systemic design issues. Read with First-Pass Success Rate and Defect Discovery trends to confirm program maturity honestly.

## Formula

```
Test Points Passed / Test Points Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 977 (batch 3)
