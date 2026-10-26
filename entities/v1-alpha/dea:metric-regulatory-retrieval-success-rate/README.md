# dea:metric-regulatory-retrieval-success-rate

Candidate Performance Metric record for **Regulatory Retrieval Success Rate** (RRSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-retrieval-success-rate`
- **Name:** Regulatory Retrieval Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRSR

## 2. Definition

Regulatory Retrieval Success Rate (RRSR) measures conformance to standards, plans, or obligations in the Records & Information Management domain. Its calculation is Records Retrieved within Regulatory Deadline / Requests, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether required records can be retrieved within mandated response windows. Discovery failures convert records problems into legal problems. Retrieval tested only on indexed, organized records misses the backlog. Read with freedom of information response timeliness and e-discovery readiness.

## Formula

```
Records Retrieved within Regulatory Deadline / Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3693 (batch 8)
