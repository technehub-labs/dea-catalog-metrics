# dea:metric-quote-conversion-rate-insurance

Candidate Performance Metric record for **Quote Conversion Rate (Insurance)** (QCR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quote-conversion-rate-insurance`
- **Name:** Quote Conversion Rate (Insurance)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** QCR-I

## 2. Definition

Quote Conversion Rate (Insurance) (QCR-I) addresses how effectively a process or entity achieves its intended outcome and is a fixture of insurance distribution & brokerage reporting. Its calculation is Quotes Converted to Bound Policies / Quotes Issued, measured in percent (%). It originates from and is most used in Insurance distribution practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of insurance quotes that become bound policies. It matters because conversion is where distribution efficiency shows. Conversion can be lifted with underpriced quotes that win business at future loss-ratio cost. Read with Loss Ratio of converted cohorts and Quote-to-Bind time to confirm conversion is profitable.

## Formula

```
QCR-I = Quotes Converted to Bound Policies / Quotes Issued
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
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1155 (batch 4)
