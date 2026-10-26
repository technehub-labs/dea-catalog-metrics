# dea:metric-related-party-transaction-approval-rate

Candidate Performance Metric record for **Related-Party Transaction Approval Rate** (RPTA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-related-party-transaction-approval-rate`
- **Name:** Related-Party Transaction Approval Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RPTA

## 2. Definition

Related-Party Transaction Approval Rate (RPTA) measures conformance to standards, plans, or obligations in the Corporate Governance domain. The formula is Related-Party Transactions Approved per Policy / Total Related-Party Transactions - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Related-party transaction approval rate measures the share of transactions with connected parties (management, directors, their families, affiliates) that received proper independent review and approval, and it is the conflict-of-interest control metric of governance - related-party transactions are the classic tunneling mechanism, moving value out of the company through non-arm's-length deals. The regulatory architecture is explicit: listing rules require audit-committee review of material related-party transactions, and disclosure regimes require them to be identified and justified. The metric's honest version is exception-hunting, not rate-watching: one unapproved material transaction matters more than a 99 percent approval rate suggests, and the pattern to watch is approval-quantity drift (many small transactions that individually fall below thresholds but collectively extract value). Read with the materiality-threshold policy itself (companies set their own thresholds in some regimes), transaction-value trend with related parties, and audit-committee dissent or questioning record.

## Formula

```
Related-Party Transactions Approved per Policy / Total Related-Party Transactions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1044 (batch 4)
