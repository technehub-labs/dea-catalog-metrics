# dea:metric-threat-landscape-coverage-score

Candidate Performance Metric record for **Threat Landscape Coverage Score** (TLCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-landscape-coverage-score`
- **Name:** Threat Landscape Coverage Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TLCS

## 2. Definition

Threat Landscape Coverage Score (TLCS) addresses exposure to adverse outcomes and is a fixture of threat intelligence & red team reporting. Its calculation is Coverage of Industry-Threat Scenarios with Playbooks, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how well monitoring and defenses cover the threats most relevant to your sector and crown jewels. Generic coverage scores well while leaving your actual attackers' techniques unaddressed. Coverage scored by framework checkboxes overstates real readiness. Read with threat intelligence integration coverage and red team detection rate.

## Formula

```
TLCS = Coverage of Industry-Threat Scenarios with Playbooks
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3293 (batch 7)
