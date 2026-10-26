# dea:metric-whistleblower-report-resolution-time

Candidate Performance Metric record for **Whistleblower Report Resolution Time** (WRRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-whistleblower-report-resolution-time`
- **Name:** Whistleblower Report Resolution Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRRT

## 2. Definition

Whistleblower Report Resolution Time (WRRT) captures conformance to standards, plans, or obligations for organizations tracking risk & compliance. It is defined as Days from Report to Case Closure; the result is stated in days. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average time to investigate and resolve whistleblower reports. It matters because slow handling deters future reporting and compounds retaliation and legal risk. Gaming risk includes quick superficial closures that protect the accused rather than the reporter. Read with Employee Engagement Survey psychological safety scores and retaliation claim rates to test whether resolution is real.

## Formula

```
WRRT = Days from Report to Case Closure
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 386 (batch 1)
