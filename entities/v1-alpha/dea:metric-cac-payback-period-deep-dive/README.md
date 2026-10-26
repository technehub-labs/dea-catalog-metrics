# dea:metric-cac-payback-period-deep-dive

Candidate Performance Metric record for **CAC Payback Period (Deep Dive)** (CACPB-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cac-payback-period-deep-dive`
- **Name:** CAC Payback Period (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CACPB-D

## 2. Definition

CAC Payback Period (Deep Dive) (CACPB-D) addresses how efficiently resources are converted into outputs and is a fixture of startup & venture-backed business reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as CAC / Monthly Gross Margin per Customer, expressed in months. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures months to recover customer acquisition cost from gross profit. It is the discipline metric of startup growth economics: growth funded by CAC that never pays back is a treadmill that consumes runway, and payback periods determine whether growth spending is investment or consumption. Blended CAC across organic-heavy and paid-heavy cohorts hides paid-acquisition deterioration, so read paid separately. Read with burn efficiency and cohort gross-margin development.

## Formula

```
CAC / Monthly Gross Margin per Customer
```

## Unit

- **Unit reference:** `dea:unit-months`
- **Unit:** months
- **Unit label (as published):** months

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2443 (batch 6)
