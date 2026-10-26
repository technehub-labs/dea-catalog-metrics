# dea:metric-delegation-of-authority-compliance-clm

Candidate Performance Metric record for **Delegation of Authority Compliance (CLM)** (DOAC-CL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delegation-of-authority-compliance-clm`
- **Name:** Delegation of Authority Compliance (CLM)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DOAC-CL

## 2. Definition

A Contract Lifecycle Management indicator, Delegation of Authority Compliance (CLM) (DOAC-CL) quantifies conformance to standards, plans, or obligations. It is computed as Contracts Signed per Authority Matrix / Contracts Sampled, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether contract commitments match the authority matrix for the signing parties. DoA violations in contracts are binding: they cannot be undone after signature. Compliance checked at signature but not amendment misses mid-life drift. Read with delegation of authority compliance and contract approval cycle time.

## Formula

```
Contracts Signed per Authority Matrix / Contracts Sampled
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3704 (batch 8)
