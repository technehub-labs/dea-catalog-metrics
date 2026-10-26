# dea:metric-accessibility-conformance-level

Candidate Performance Metric record for **Accessibility Conformance Level** (ACL-UX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-accessibility-conformance-level`
- **Name:** Accessibility Conformance Level
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACL-UX

## 2. Definition

A UX & Design Systems indicator, Accessibility Conformance Level (ACL-UX) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Interfaces Meeting WCAG 2.2 AA / Interfaces in Scope - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Accessibility conformance measures the share of interfaces meeting WCAG 2.2 AA - the legal benchmark in many jurisdictions (EU accessibility acts, ADA settlements, procurement rules). It is expressed as a conformance level, and passing means automated checks plus the manual checks automation cannot do (keyboard traps, focus order, contrast judgment calls). Beyond legal defense, accessible interfaces correlate with quality for everyone - captions, contrast, and semantic markup help low-bandwidth and situational users too. Audit both automated and manual layers; automated tools catch roughly a third of failures alone.

## Formula

```
Interfaces Meeting WCAG 2.2 AA / Interfaces in Scope
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ux_design_systems

## Attribution

- **Source credit:** WCAG 2.2 (W3C Web Accessibility Initiative)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3271 (batch 7)
