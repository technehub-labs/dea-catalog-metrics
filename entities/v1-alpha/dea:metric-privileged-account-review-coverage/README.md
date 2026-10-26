# dea:metric-privileged-account-review-coverage

Candidate Performance Metric record for **Privileged Account Review Coverage** (PARC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-privileged-account-review-coverage`
- **Name:** Privileged Account Review Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PARC

## 2. Definition

Privileged Account Review Coverage (PARC) measures conformance to standards, plans, or obligations in the Cybersecurity domain. It is defined as Privileged Accounts Reviewed / Privileged Accounts; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of privileged accounts reviewed within the required period. It matters because stale privileged access is a top audit finding and lateral-movement risk. Reviews can be rubber-stamped en masse without actually checking entitlements. Read with Access Review findings and Segregation of Duties violations to confirm reviews remove access rather than confirm it.

## Formula

```
Privileged Accounts Reviewed / Privileged Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 326 (batch 1)
