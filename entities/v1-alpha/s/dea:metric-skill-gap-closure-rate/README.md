# dea:metric-skill-gap-closure-rate

Candidate Performance Metric record for **Skill Gap Closure Rate** (SGCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-skill-gap-closure-rate`
- **Name:** Skill Gap Closure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SGCR

## 2. Definition

A Learning & Development indicator, Skill Gap Closure Rate (SGCR) quantifies capability maturity or development. It is computed as Closed Skill Gaps / Identified Skill Gaps, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Skill gap closure rate tracks progress against a defined skills taxonomy - the share of identified critical-skill gaps that have been closed through hiring, development, or redeployment. Its honesty depends entirely on taxonomy quality: a skills model that is stale (technology half-lives now run 2-3 years for many digital skills) produces a closure rate that measures progress toward yesterday's requirements. The strategic value comes from making capability planning forward-looking - reading closure rate against projected need, not current-state gap. Also watch coverage: a high closure rate on a narrow skill set while critical adjacent gaps go unmeasured is false comfort. Read with time-to-close by skill category, external hiring versus internal development mix, and critical-role vacancy duration.

## Formula

```
SGCR = Closed Skill Gaps / Identified Skill Gaps
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 796 (batch 2)
