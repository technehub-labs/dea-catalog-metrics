# dea:metric-false-decline-rate

Candidate Performance Metric record for **False Decline Rate** (FDR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-false-decline-rate`
- **Name:** False Decline Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FDR-P

## 2. Definition

False Decline Rate (FDR-P) addresses exposure to adverse outcomes and is a fixture of payments & fintech reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Legitimate Transactions Declined / Legitimate Attempts - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Payments & fintech sector.

## 3. Context

False decline rate measures legitimate transactions rejected by risk controls, and it is the invisible cost center of payments risk management - customers rarely complain, they just take their business elsewhere, with surveys showing a large share of declined shoppers refusing to return to the merchant. It is structurally hard to measure because ground truth requires knowing the transaction was legitimate, which is only observable through proxies like repeat purchase behavior or issuer data. The optimization trade-off is explicit: tightening fraud rules lowers fraud losses while raising false declines, and the correct setting depends on margins - a 2 percent margin retailer can afford more fraud than a 60 percent margin software vendor. Read with authorization rate by segment and customer repeat-purchase deltas after declines.

## Formula

```
FDR-P = Legitimate Transactions Declined / Legitimate Attempts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 775 (batch 2)
