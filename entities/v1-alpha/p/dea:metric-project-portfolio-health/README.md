# dea:metric-project-portfolio-health

Candidate Performance Metric record for **Project Portfolio Health** (PPH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-project-portfolio-health`
- **Name:** Project Portfolio Health
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PPH

## 2. Definition

Project Portfolio Health (PPH) measures exposure to adverse outcomes in the Project Management domain. The formula is Projects on Green Status / Total Projects - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

A composite assessment of the project portfolio across delivery confidence, budget health, benefit trajectory, and risk exposure - typically expressed as the share of initiatives flagged red, amber, and green. Its strategic value is that it is the only view that sees interdependencies: individual projects can each be amber while the portfolio is red, because shared resources, cumulative change load on the same business units, and benefit collisions do not appear in any single project's status. The honest composite resists optimism bias - the endemic tendency of project owners to report one shade better than reality - which is why mature organizations define the RAG thresholds mechanically from schedule and cost variance rather than letting status be a feeling. The trend in the red share is the metric boards actually act on.

## Formula

```
PPH = Projects on Green Status / Total Projects
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 360 (batch 1)
