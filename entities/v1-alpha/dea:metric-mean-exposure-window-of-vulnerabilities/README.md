# dea:metric-mean-exposure-window-of-vulnerabilities

Candidate Performance Metric record for **Mean Exposure Window of Vulnerabilities** (MEV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-exposure-window-of-vulnerabilities`
- **Name:** Mean Exposure Window of Vulnerabilities
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MEV

## 2. Definition

Mean Exposure Window of Vulnerabilities (MEV) addresses exposure to adverse outcomes and is a fixture of cybersecurity reporting. The formula is Mean Days Critical Vulnerabilities Remain Unpatched - reported in days. It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average time vulnerabilities remain exploitable before remediation. It matters because it converts remediation effort into risk-felt time at risk. It can be gamed by not scanning for hard-to-fix classes of issues, which shrinks the window by shrinking the count. Read with Vulnerability Remediation Time and Critical Patch Compliance to confirm the window is closing across all severity tiers.

## Formula

```
Mean Days Critical Vulnerabilities Remain Unpatched
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 332 (batch 1)
