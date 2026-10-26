# dea:metric-assurance-map-coverage

Candidate Performance Metric record for **Assurance Map Coverage** (AMC-GOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assurance-map-coverage`
- **Name:** Assurance Map Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AMC-GOV

## 2. Definition

Assurance Map Coverage (AMC-GOV) measures exposure to adverse outcomes in the Enterprise Decision Effectiveness & Governance Monitoring domain. The formula is Risks with Mapped Assurance Activities / Key Risks - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely key risks are covered by an identified assurance provider across the three lines. Unmapped risks receive assurance by accident or not at all. Maps drawn once and not refreshed decay quickly. Read with three lines model compliance score and regulatory process compliance rate.

## Formula

```
Risks with Mapped Assurance Activities / Key Risks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3146 (batch 7)
