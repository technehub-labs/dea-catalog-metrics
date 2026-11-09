# dea:metric-claim-denial-rate-healthcare

Candidate Performance Metric record for **Claim Denial Rate (Healthcare)** (CDR-H) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-denial-rate-healthcare`
- **Name:** Claim Denial Rate (Healthcare)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDR-H

## 2. Definition

Claim Denial Rate (Healthcare) (CDR-H) addresses how efficiently resources are converted into outputs and is a fixture of healthcare reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Denied Claims / Claims Submitted - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Healthcare sector.

## 3. Context

Measures the share of claims denied by payers on first submission. It matters because denials delay cash, cost rework, and signal coding and authorization process failures. Teams can cut it by avoiding complex cases or writing off denials instead of appealing them, which hides revenue loss. Read with Denial Overturn Rate and Charge Capture Accuracy to judge whether denial performance is improving or being relabeled.

## Formula

```
CDR-H = Denied Claims / Claims Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 477 (batch 1)
