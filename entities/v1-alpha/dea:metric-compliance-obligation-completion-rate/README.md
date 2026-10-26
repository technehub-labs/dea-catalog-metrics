# dea:metric-compliance-obligation-completion-rate

Candidate Performance Metric record for **Compliance Obligation Completion Rate** (COCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-compliance-obligation-completion-rate`
- **Name:** Compliance Obligation Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** COCR

## 2. Definition

Compliance Obligation Completion Rate (COCR) measures conformance to standards, plans, or obligations in the Regulatory Affairs & Compliance Operations domain. The formula is Obligations Completed by Due Date / Obligations - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures completion of all tracked regulatory obligations - filings, attestations, certifications, controls - by their deadlines. It is the hygiene floor of compliance operations: missed obligations are how ordinary regulatory risk becomes enforcement risk. Integrity depends on the obligation inventory being complete, which is the actual hard part; completion against an incomplete register is theater. Read with compliance risk assessment coverage and repeat regulatory findings rate.

## Formula

```
Obligations Completed by Due Date / Obligations
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** regulatory_affairs_compliance_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1590 (batch 6)
