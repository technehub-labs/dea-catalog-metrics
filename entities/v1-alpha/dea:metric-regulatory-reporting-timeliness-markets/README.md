# dea:metric-regulatory-reporting-timeliness-markets

Candidate Performance Metric record for **Regulatory Reporting Timeliness (Markets)** (RRT-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-reporting-timeliness-markets`
- **Name:** Regulatory Reporting Timeliness (Markets)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRT-M

## 2. Definition

Regulatory Reporting Timeliness (Markets) (RRT-M) captures conformance to standards, plans, or obligations for organizations tracking investment banking & capital markets. Its calculation is Reports Filed by Deadline / Reports Required, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Investment banking practice.

## 3. Context

Regulatory reporting timeliness measures adherence to submission deadlines for transaction, position, and conduct reports to market regulators (best-execution reports, short-position disclosures, trade and transaction reporting under EMIR and MiFID), and it is the infrastructure metric of market operations - reporting failures are strict-liability exposure with per-record fine mechanics, so high volumes make even small error rates expensive. The metric is a floor rather than a performance goal: 99.5 percent sounds high until applied to millions of records, where it means thousands of daily failures. The timeliness decomposition distinguishes submission latency (technical throughput) from data quality (a report submitted on time that fails validation is a failure anyway). Read with rejection and correction rates, end-to-end latency distribution versus deadline, and reconciliation breaks between internal books and reported positions.

## Formula

```
Reports Filed by Deadline / Reports Required
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_banking_capital_markets
- **Sector:** investment_banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1153 (batch 4)
