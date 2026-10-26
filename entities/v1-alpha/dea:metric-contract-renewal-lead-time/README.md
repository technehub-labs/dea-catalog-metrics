# dea:metric-contract-renewal-lead-time

Candidate Performance Metric record for **Contract Renewal Lead Time** (CRLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-renewal-lead-time`
- **Name:** Contract Renewal Lead Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRLT

## 2. Definition

Contract Renewal Lead Time (CRLT) captures how efficiently resources are converted into outputs for organizations tracking outsourcing & vendor management. The formula is Days before Expiry that Renewal is Completed - reported in days. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how far ahead of expiry vendor contracts are renewed. It matters because last-minute renewals destroy negotiating leverage and cause service gaps. Lead time can be gamed by auto-renewing contracts to claim continuity without real negotiation. Read with Vendor Dispute Resolution Time and Contract Renewal Leakage to confirm renewals are well-managed.

## Formula

```
Days before Expiry that Renewal is Completed
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1126 (batch 4)
