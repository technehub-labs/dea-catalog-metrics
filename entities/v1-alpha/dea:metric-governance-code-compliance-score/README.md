# dea:metric-governance-code-compliance-score

Candidate Performance Metric record for **Governance Code Compliance Score** (GCCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-governance-code-compliance-score`
- **Name:** Governance Code Compliance Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GCCS

## 2. Definition

Governance Code Compliance Score (GCCS) measures conformance to standards, plans, or obligations in the Corporate Governance domain. It is computed as Complied Code Provisions / Applicable Provisions, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Governance code compliance scores measure adherence to the national or listing governance code - UK Corporate Governance Code, OECD principles, or local equivalents - and they are the structural-framework metric of governance disclosure. Most codes are comply-or-explain rather than mandatory, so the honest score distinguishes compliant from explained: an explanation can be a substantive, situation-specific justification (the code's intended flexibility) or boilerplate evasion, and treating both as equal makes the score meaningless. The measurement risk is checklist-theater: codes define structures (committees, independence, refresh policies), and research shows weak correlation between structural compliance and governance outcomes like fraud prevention or performance. Read with the quality of explanations for non-compliance, substantive-outcome metrics (restatements, disclosure quality, enforcement actions), and code-version drift as codes update.

## Formula

```
Complied Code Provisions / Applicable Provisions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1046 (batch 4)
