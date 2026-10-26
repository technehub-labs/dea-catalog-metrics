# dea:metric-persistency-rate

Candidate Performance Metric record for **Persistency Rate** (PR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-persistency-rate`
- **Name:** Persistency Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PR

## 2. Definition

Persistency Rate (PR) captures the retention of customers, users, or assets over time for organizations tracking insurance. Its calculation is Policies Remaining In Force / Policies Issued, measured in percent (%). It originates from and is most used in Insurance practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of policies that remain in force through a measurement window - the insurance cousin of retention, and the metric that makes life insurance economics work, because the first-year costs of writing a policy are recovered over many years of premium. Low persistency on long-term products means the block never reaches profitability, whatever the sales volume suggests. The strategic reading is by product and channel: high early-duration lapses usually point to suitability mismatches sold for commission, while lapses clustered at renewal after a bad claims experience point at service failure. Because surrender values and policy loans complicate the picture, regulators and rating agencies treat persistency as a leading indicator of both distribution quality and eventual lapse-supported solvency strain.

## Formula

```
Policies Remaining In Force / Policies Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 60 (batch 1)
