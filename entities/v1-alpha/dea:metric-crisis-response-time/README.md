# dea:metric-crisis-response-time

Candidate Performance Metric record for **Crisis Response Time** (CRT-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crisis-response-time`
- **Name:** Crisis Response Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRT-C

## 2. Definition

Crisis Response Time (CRT-C) captures exposure to adverse outcomes for organizations tracking corporate communications & pr. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Hours from Crisis Trigger to Public Response - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Crisis response time measures elapsed time from incident detection to public response, and in crisis communications the first hours set the narrative frame permanently - the infamous golden hour logic means that whoever defines the story first usually keeps it. The metric deserves regime awareness: routine issue response (24-hour standard) and acute crisis response (15-60 minutes for social-driven events) are different disciplines. Detection lag is usually the bigger failure point than response drafting, so response time should be measured from event occurrence, not from when comms learned of it. Read with share of coverage in the first news cycle that used company framing, correction/retraction rates, and sentiment recovery slope after the response.

## Formula

```
CRT-C = Hours from Crisis Trigger to Public Response
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_communications_pr

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 790 (batch 2)
