# dea:metric-digital-application-share

Candidate Performance Metric record for **Digital Application Share** (DAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-application-share`
- **Name:** Digital Application Share
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DAS

## 2. Definition

Within Insurance Distribution & Brokerage, Digital Application Share (DAS) is used to gauge how efficiently resources are converted into outputs. The formula is Applications Submitted Digitally / Total Applications - reported in percent (%). It is a standard measure in the Insurance distribution sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Digital application share measures the proportion of insurance applications initiated and completed through digital channels, and it is the cost-structure transformation metric of distribution - digital applications carry lower acquisition cost, faster cycle time, and better data quality (structured intake beats keyed data), which is why carriers push it. The gaming risk is forced migration: pushing applicants to digital by starving the assisted channel degrades the experience for the complex-case segment that genuinely needs human help. The metric should be read with completion rate - an application started digitally and abandoned is worse than one initiated assisted. Read with digital completion versus abandonment rates, straight-through-processing rate on digital applications (the payoff), complexity-segment migration patterns, and underwriting-quality differences by channel.

## Formula

```
Applications Submitted Digitally / Total Applications
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1162 (batch 4)
