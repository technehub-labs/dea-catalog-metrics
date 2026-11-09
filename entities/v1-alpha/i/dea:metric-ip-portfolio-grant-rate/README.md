# dea:metric-ip-portfolio-grant-rate

Candidate Performance Metric record for **IP Portfolio Grant Rate** (IPGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ip-portfolio-grant-rate`
- **Name:** IP Portfolio Grant Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IPGR

## 2. Definition

A Legal indicator, IP Portfolio Grant Rate (IPGR) quantifies how effectively a process or entity achieves its intended outcome. Its calculation is Granted IP Applications / Applications Filed, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of patent applications that mature into granted patents - the quality metric of the IP function, since filing counts measure activity while the grant rate measures whether the portfolio is built on claims an examiner found novel and non-obvious. Its strategic weight is signal value: a high grant rate suggests the portfolio is credible for licensing, defensive, and financing purposes, while a low rate suggests the filing strategy prioritizes volume - which sometimes is deliberate (defensive flooding) but usually means drafting and prosecution weakness. The comparison requires technical-field honesty, since grant rates differ systematically across technology classes and offices, and a portfolio-wide rate moves with mix as much as quality. Read with citation and maintenance behavior: granted patents that are abandoned at first renewal were never assets, whatever the grant rate said.

## Formula

```
IPGR = Granted IP Applications / Applications Filed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** legal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 395 (batch 1)
