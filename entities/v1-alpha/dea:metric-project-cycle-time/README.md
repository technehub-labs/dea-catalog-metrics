# dea:metric-project-cycle-time

Candidate Performance Metric record for **Project Cycle Time** (PCyT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-cycle-time`
- **Name:** Project Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCyT

## 2. Definition

Project Cycle Time (PCyT) addresses how efficiently resources are converted into outputs and is a fixture of project management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Days from Project Start to Closure, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The elapsed time from project start to completion - the velocity metric of the project portfolio, and strategically the one with the compounding payoff: cycle time compresses the feedback loop between investment decision and realized benefit, which shortens the horizon over which the organization learns which bets were good. The research tradition behind lean project management argues that most cycle time is queue time - work waiting for decisions, resources, or dependencies - not working time, which is why cycle-time attacks that add resources fail and attacks that remove waiting work. The honest measurement uses consistent start and end conventions, since projects that start when funded and projects that start when staffed differ by months. Read by project type, because infrastructure, product, and compliance projects have structurally different cycle physics, and a blended number hides all three.

## Formula

```
Days from Project Start to Closure
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** transformation
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 355 (batch 1)
