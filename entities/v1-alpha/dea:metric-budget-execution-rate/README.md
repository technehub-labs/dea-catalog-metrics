# dea:metric-budget-execution-rate

Candidate Performance Metric record for **Budget Execution Rate** (BER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-execution-rate`
- **Name:** Budget Execution Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BER

## 2. Definition

Within Public Sector & Government, Budget Execution Rate (BER) is used to gauge conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Actual Spend / Approved Budget - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Public sector sector.

## 3. Context

The share of the approved budget actually spent - the topline execution metric of public administration, and the one that matters more than its private-sector equivalent because public budgeting is also the authorization: funds not executed are programs not delivered, and the annual underspend that looks like discipline in a company looks like failure to deliver in a government. Its strategic significance is the credibility cycle: chronically low execution rates feed the case that the administration cannot absorb its allocations, which feeds into next-cycle allocations and donor-confidence decisions. The honest read is composition-aware: underspend concentrated in capital investment (procurement delays, capacity gaps) is a delivery-capability problem, underspend on operations is an absorption or planning problem, and the same headline rate means opposite remedies. Read with the end-of-year spike pattern - the year-end rush that pushes execution into the final quarter is the visible symptom of poor in-year execution planning.

## Formula

```
Actual Spend / Approved Budget
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 632 (batch 2)
