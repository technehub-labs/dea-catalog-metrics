# dea:metric-export-authorization-compliance-rate

Candidate Performance Metric record for **Export Authorization Compliance Rate** (EACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-export-authorization-compliance-rate`
- **Name:** Export Authorization Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EACR

## 2. Definition

Export Authorization Compliance Rate (EACR) measures conformance to standards, plans, or obligations in the Aerospace & Defense Program Management domain. It is computed as Transfers with Valid Authorization / Transfers, expressed in percent (%). Its use is concentrated in Aerospace & Defense. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures adherence to export control obligations - licensing, classification, end-use documentation - in defense and dual-use programs. Export violations carry uniquely severe consequences (debarment, criminal liability), and compliance failures cluster in fast-moving program environments where urgency outruns process. Sample-test actual shipments against authorizations, not just process conformance. Read with technology control plan audit findings and license condition tracking.

## Formula

```
Transfers with Valid Authorization / Transfers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1787 (batch 6)
