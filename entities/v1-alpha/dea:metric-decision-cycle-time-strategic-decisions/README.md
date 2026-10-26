# dea:metric-decision-cycle-time-strategic-decisions

Candidate Performance Metric record for **Decision Cycle Time - Strategic Decisions** (DCTSD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-decision-cycle-time-strategic-decisions`
- **Name:** Decision Cycle Time - Strategic Decisions
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCTSD

## 2. Definition

Decision Cycle Time - Strategic Decisions (DCTSD) addresses how efficiently resources are converted into outputs and is a fixture of enterprise decision effectiveness & governance monitoring reporting. The formula is Days from Decision Request to Final Decision - reported in days. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures elapsed time from strategic issue identification to decision. Slow strategic decisions compound: market windows close while analysis cycles. Cycle time is gameable by back-dating when issues were raised. Read with strategic initiative decision latency and decision rights clarity score.

## Formula

```
DCTSD = Days from Decision Request to Final Decision
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3134 (batch 7)
