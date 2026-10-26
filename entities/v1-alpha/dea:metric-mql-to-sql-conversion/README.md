# dea:metric-mql-to-sql-conversion

Candidate Performance Metric record for **MQL to SQL Conversion** (MQL2SQL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mql-to-sql-conversion`
- **Name:** MQL to SQL Conversion
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MQL2SQL

## 2. Definition

Within Marketing, MQL to SQL Conversion (MQL2SQL) is used to gauge how effectively a process or entity achieves its intended outcome. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Sales Qualified Leads / Marketing Qualified Leads, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of marketing-qualified leads that sales accepts as sales-qualified. It matters as the clearest test of lead quality and marketing-sales alignment. It can be gamed by sales rubber-stamping leads to avoid conflict, or by marketing narrowing criteria until conversion looks high while volume collapses. Read with Lead Conversion Rate and Marketing Qualified Lead Volume to see both sides of the quality-volume trade.

## Formula

```
MQL2SQL = Sales Qualified Leads / Marketing Qualified Leads
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 106 (batch 1)
