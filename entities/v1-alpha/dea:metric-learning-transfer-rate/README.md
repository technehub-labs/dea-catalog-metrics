# dea:metric-learning-transfer-rate

Candidate Performance Metric record for **Learning Transfer Rate** (LTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-learning-transfer-rate`
- **Name:** Learning Transfer Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTR

## 2. Definition

Learning Transfer Rate (LTR) measures how effectively a process or entity achieves its intended outcome in the Learning & Development domain. The formula is Learners Applying Skills on Job after Training / Learners Trained - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Learning transfer rate measures the share of trained knowledge and skills that actually show up in on-the-job behavior, and it is the metric that exposes the training industry's dirty secret: studies consistently find a large majority of training content never transfers to work, making training spend one of the least-audited cost centers in corporate budgets. Transfer depends less on instructional quality than on the environment: manager reinforcement, opportunity to apply, and alignment with performance expectations. Kirkpatrick level 3 (behavior) measurement is hard but the only one that matters here - level 1 evaluations (satisfaction) correlate with almost nothing. Read with manager-reinforcement rates, application opportunity logs, and downstream performance indicators for the trained skill.

## Formula

```
LTR = Learners Applying Skills on Job after Training / Learners Trained
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** learning_development

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 795 (batch 2)
