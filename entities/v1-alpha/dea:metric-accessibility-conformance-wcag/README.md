# dea:metric-accessibility-conformance-wcag

Candidate Performance Metric record for **Accessibility Conformance (WCAG)** (ACW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-accessibility-conformance-wcag`
- **Name:** Accessibility Conformance (WCAG)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACW

## 2. Definition

Accessibility Conformance (WCAG) (ACW) addresses conformance to standards, plans, or obligations and is a fixture of digital product & web operations reporting. It is defined as Criteria Passed / Applicable WCAG Criteria; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Accessibility conformance measures adherence to the Web Content Accessibility Guidelines - the global standard for digital accessibility, with WCAG 2.1 and 2.2 level AA as the de facto legal threshold in many jurisdictions (ADA in the US courts, the European Accessibility Act, EN 301 549) - and it is both a legal-exposure and market-coverage metric: roughly one in five people experience a disability, and inaccessible interfaces exclude that market entirely. The measurement honesty issue is conformance versus lived experience: automated scanners find roughly 30-40 percent of WCAG issues, so a passing automated score is not conformance; manual testing with assistive technology (screen readers like JAWS and NVDA, keyboard-only navigation) and disabled user testing are required for real conformance. Read with audit methodology disclosure, issue-remediation velocity, and legal demand or complaint history.

## Formula

```
Criteria Passed / Applicable WCAG Criteria
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1084 (batch 4)
