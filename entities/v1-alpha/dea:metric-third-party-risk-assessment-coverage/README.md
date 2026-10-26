# dea:metric-third-party-risk-assessment-coverage

Candidate Performance Metric record for **Third-Party Risk Assessment Coverage** (TPRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-third-party-risk-assessment-coverage`
- **Name:** Third-Party Risk Assessment Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TPRC

## 2. Definition

Within Risk & Compliance, Third-Party Risk Assessment Coverage (TPRC) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Critical Vendors Assessed / Critical Vendors, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of vendors and partners in scope that have completed risk assessment - the completeness metric of third-party risk management, a discipline that grew from the recognition that outsourcing moved risk to parties the regulator cannot examine but the firm cannot escape. Its strategic weight is accountability transfer without responsibility transfer: under most regulatory regimes, the firm answers for its vendors' failures as if they were its own, and this coverage metric is the primary evidence of due diligence when the failure arrives. The honest construction is tiered - critical vendors assessed deeply and annually, long-tail vendors assessed by questionnaire - since assessing all vendors identically produces shallow coverage of the ones that matter. Read with the contract-protection rate: assessment without contractual audit rights, breach notification, and exit clauses is observation without control.

## Formula

```
Critical Vendors Assessed / Critical Vendors
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** risk_compliance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 385 (batch 1)
