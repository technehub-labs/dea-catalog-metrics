# dea:metric-claim-decision-automation-rate

Candidate Performance Metric record for **Claim Decision Automation Rate** (CDAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-decision-automation-rate`
- **Name:** Claim Decision Automation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDAR

## 2. Definition

Within Insurance Claims Deep Dive, Claim Decision Automation Rate (CDAR) is used to gauge how efficiently resources are converted into outputs. Its calculation is Decisions Made by Rules or Models / Decisions, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Insurance practice.

## 3. Context

Measures the share of claim decisions - coverage, valuation, payment - made by rules or models without human review. It extends STP into the judgment layer, so governance matters twice as much: automation bias in claims directly creates wrongful denials and regulatory exposure. Track overturn rates on audit by automation path, and keep explainability evidence for sampled decisions. Read with straight-through claims settlement rate and complaint and litigation rates.

## Formula

```
Decisions Made by Rules or Models / Decisions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1564 (batch 6)
