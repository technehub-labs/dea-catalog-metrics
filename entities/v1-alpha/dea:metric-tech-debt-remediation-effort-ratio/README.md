# dea:metric-tech-debt-remediation-effort-ratio

Candidate Performance Metric record for **Tech Debt Remediation Effort Ratio** (TDREM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tech-debt-remediation-effort-ratio`
- **Name:** Tech Debt Remediation Effort Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TDREM

## 2. Definition

Tech Debt Remediation Effort Ratio (TDREM) addresses how efficiently resources are converted into outputs and is a fixture of code quality & static analysis reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Estimated Remediation Hours / Development Hours, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Software practice.

## 3. Context

Measures engineering capacity consumed by remediation versus new development. Debt service quietly consumes the majority of capacity in mature estates. Remediation effort counted only when tickets are labeled debt understates. Read with technical debt remediation progress and change failure rate.

## Formula

```
Estimated Remediation Hours / Development Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4191 (batch 9)
