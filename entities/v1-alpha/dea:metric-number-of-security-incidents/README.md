# dea:metric-number-of-security-incidents

Candidate Performance Metric record for **Number of Security Incidents** (NSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-number-of-security-incidents`
- **Name:** Number of Security Incidents
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NSI

## 2. Definition

Number of Security Incidents (NSI) addresses exposure to adverse outcomes and is a fixture of cybersecurity reporting. The formula is Confirmed Security Incidents per Period - reported in count (items per period). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The count of detected security events that triggered response - the raw frequency measure of the threat landscape an organization actually faces. Its strategic content is the paradox that rising counts often mean improving defense: better detection surfaces incidents that were previously occurring invisibly, so a jump in incident count after a monitoring investment is success wearing alarming clothes. The honest analysis is severity-classified: the count of critical incidents is the number that carries risk information, while the total mostly measures the noise of commodity attacks. The metric matters commercially as the denominator of all response metrics and as a reporting signal to boards, where trend-by-severity is the presentation that avoids both complacency and alarmism.

## Formula

```
Confirmed Security Incidents per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 325 (batch 1)
