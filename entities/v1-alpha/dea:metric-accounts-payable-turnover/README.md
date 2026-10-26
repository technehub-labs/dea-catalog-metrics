# dea:metric-accounts-payable-turnover

Candidate Performance Metric record for **Accounts Payable Turnover** (APT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-accounts-payable-turnover`
- **Name:** Accounts Payable Turnover
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APT

## 2. Definition

Accounts Payable Turnover (APT) addresses how efficiently resources are converted into outputs and is a fixture of finance & accounting reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Total Supply Purchases / Average Accounts Payable, measured in times per period. The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Total Supply Purchases / Average Accounts Payable
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 26 (batch 1)
