# dea:metric-psychological-safety-score

Candidate Performance Metric record for **Psychological Safety Score** (PSS-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-psychological-safety-score`
- **Name:** Psychological Safety Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PSS-E

## 2. Definition

Psychological Safety Score (PSS-E) captures the engagement or satisfaction of the people involved for organizations tracking employee wellbeing. The formula is Average Team Psychological Safety Survey Rating - reported in score (points). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The psychological safety score measures the shared belief that interpersonal risk-taking is safe - speaking up with questions, concerns, or mistakes without punishment - and it is the foundation metric of team learning and safety culture: research (Amy Edmondson's original nursing-error finding and the wider literature since) shows that psychologically safe teams report more errors while committing fewer, because reporting is the mechanism of learning. Its honest measurement uses validated team-level instruments, and its reading is team-level by design: psychological safety is a property of the team climate, not the individual, so organizational averages conceal the real variance. The metric's predictive reach is broad: it predicts incident reporting, learning behavior, and innovation participation. Read with error-reporting rates (the validation pair: high safety plus rising reported-error counts is health), speak-up behavior in meetings as observed, and leader-behavior drivers (the fix is leadership conduct, not posters).

## Formula

```
Average Team Psychological Safety Survey Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** employee_wellbeing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1233 (batch 4)
