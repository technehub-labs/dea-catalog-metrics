# dea:metric-disclosure-timeliness

Candidate Performance Metric record for **Disclosure Timeliness** (DTM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-disclosure-timeliness`
- **Name:** Disclosure Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DTM

## 2. Definition

Disclosure Timeliness (DTM) measures conformance to standards, plans, or obligations in the Investor Relations & Capital Markets domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Required Disclosures Made by Deadline / Disclosures Due; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Listed companies, it is a recognized element of the standard performance toolkit.

## 3. Context

The speed of releasing required information against deadlines - the compliance-and-credibility metric of the disclosure function, whose strategic significance is asymmetric consequence: late filings trigger regulatory consequence directly, but the subtler cost is the inference problem - a company that delays a disclosure the market expected punctually invites the assumption that the news was bad, whatever the news was. The honest metric measures against both the regulatory deadline and the peer norm, since meeting the deadline at the last hour while peers report in weeks is technically compliant and communicatively slow. Read with the internal-signature dimension: timeliness is downstream of the close process and the disclosure-committee machinery, so deterioration here is usually a symptom of reporting-process strain - new standards, acquisition integration, control remediation - and the fix is upstream, not in the press office.

## Formula

```
Required Disclosures Made by Deadline / Disclosures Due
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
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 625 (batch 2)
