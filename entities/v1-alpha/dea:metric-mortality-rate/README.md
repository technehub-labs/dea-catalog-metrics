# dea:metric-mortality-rate

Candidate Performance Metric record for **Mortality Rate** (MR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mortality-rate`
- **Name:** Mortality Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MR

## 2. Definition

Within Healthcare, Mortality Rate (MR) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Deaths / Discharges, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## 3. Context

Deaths as a share of the relevant population - in hospital use, conventionally the inpatient or risk-adjusted mortality index that compares observed deaths against the expected count for the case mix treated. Its strategic weight is the severity of what it measures: mortality is the outcome of last resort, the number that quality reporting, regulator inspection, and public trust all ultimately gravitate toward, and the risk adjustment is what makes the metric usable at all - unadjusted rates punish the hospitals that take the sickest patients. The honest analysis looks for the contribution structure: mortality review programs find that a substantial share of deaths have modifiable factors (recognition delay, treatment escalation failures), which is precisely what makes the metric actionable rather than merely descriptive. Read with volume-outcome context: for high-risk procedures the volume-outcome literature is among the strongest in health services research, and mortality data feeds directly into service-line and referral decisions.

## Formula

```
Deaths / Discharges
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 467 (batch 1)
