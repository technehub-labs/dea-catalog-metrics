# dea:metric-cost-per-acquisition

Candidate Performance Metric record for **Cost per Acquisition** (CPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-acquisition`
- **Name:** Cost per Acquisition
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPA

## 2. Definition

Cost per Acquisition (CPA) addresses how efficiently resources are converted into outputs and is a fixture of marketing reporting. The formula is Total Campaign Cost / Acquisitions - reported in currency per unit. It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures total cost to acquire one new customer. It matters because it must stay well below lifetime value for growth to be sustainable. Teams can lower it cosmetically by counting reactivations as new customers or stopping spend on expensive but strategic segments. Read with Customer Lifetime Value and Marketing Campaign ROI to confirm acquisition economics hold at full cost.

## Formula

```
Total Campaign Cost / Acquisitions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 110 (batch 1)
