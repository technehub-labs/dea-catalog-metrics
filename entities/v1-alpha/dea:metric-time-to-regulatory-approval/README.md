# dea:metric-time-to-regulatory-approval

Candidate Performance Metric record for **Time to Regulatory Approval** (TTRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-regulatory-approval`
- **Name:** Time to Regulatory Approval
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTRA

## 2. Definition

Time to Regulatory Approval (TTRA) addresses how efficiently resources are converted into outputs and is a fixture of pharmaceuticals & life sciences reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Days from Submission to Approval, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Pharmaceuticals practice.

## 3. Context

Elapsed time from submission to approval - the terminal-phase velocity metric of drug development, where months have visible value: effective patent life runs from approval, so every month of agency review time is a month of lost exclusivity at peak-margin pricing, which is the entire commercial logic of priority-review vouchers and expedited pathways. Its strategic content is the pathway-arithmetic: regulatory regimes offer accelerated designations (breakthrough, priority, accelerated) whose qualifying criteria are partially under the sponsor's control, and choosing to pursue them is a strategic decision with both speed and commitment trade-offs, since expedited programs often carry confirmatory-trial obligations. Read with the submission-quality split: approval time includes agency clock time and sponsor response time, and the split tells a very different story - regulatory back-and-forth driven by data-quality issues is sponsor delay wearing an agency costume.

## Formula

```
TTRA = Days from Submission to Approval
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 479 (batch 1)
