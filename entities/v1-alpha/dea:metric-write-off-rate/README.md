# dea:metric-write-off-rate

Candidate Performance Metric record for **Write-Off Rate** (WOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-write-off-rate`
- **Name:** Write-Off Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WOR

## 2. Definition

Write-Off Rate (WOR) addresses exposure to adverse outcomes and is a fixture of professional services reporting. The formula is Billed but Uncollected Fees / Standard Fees - reported in percent (%). It is a standard measure in the Professional services sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of receivables written off as uncollectible. It matters because write-offs are the final bill for broken credit or collection processes. Teams can defer write-offs to future periods, temporarily shrinking the rate while aging debt accumulates. Read with Collection Effectiveness Index and Accounts Receivable Aging trends to check for deferred recognition.

## Formula

```
Billed but Uncollected Fees / Standard Fees
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 682 (batch 2)
