# dea:metric-whistleblower-report-volume

Candidate Performance Metric record for **Whistleblower Report Volume** (WRV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-whistleblower-report-volume`
- **Name:** Whistleblower Report Volume
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRV

## 2. Definition

Whistleblower Report Volume (WRV) captures conformance to standards, plans, or obligations for organizations tracking corporate governance. The formula is Reports Received per Period per 1,000 Employees - reported in events per thousand or million (scaled). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the count of internal whistleblower reports received. It matters because volume is a proxy for trust in reporting channels, not for wrongdoing per se. Interpreting falling reports as improvement is the classic trap when it may mean fear. Read with Whistleblower Report Resolution Time and anonymous survey speak-up scores to read the trend correctly.

## Formula

```
WRV = Reports Received per Period per 1,000 Employees
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1049 (batch 4)
