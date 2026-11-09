# dea:metric-decision-reversal-rate

Candidate Performance Metric record for **Decision Reversal Rate** (DRR-GOV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-reversal-rate`
- **Name:** Decision Reversal Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRR-GOV

## 2. Definition

Decision Reversal Rate (DRR-GOV) measures exposure to adverse outcomes in the Enterprise Decision Effectiveness & Governance Monitoring domain. It is computed as Decisions Reversed within Twelve Months / Decisions, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of decisions later overturned or reversed. Reversals indicate either flawed decision inputs or contested decision rights. Reversal of deliberate experiments (designed to be revisited) is different from churn. Read with decision quality audit score and decision right first time rate.

## Formula

```
DRR-GOV = Decisions Reversed within Twelve Months / Decisions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** enterprise_decision_effectiveness_governance_monitoring

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3136 (batch 7)
