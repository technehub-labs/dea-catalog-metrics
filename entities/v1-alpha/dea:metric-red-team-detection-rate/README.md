# dea:metric-red-team-detection-rate

Candidate Performance Metric record for **Red Team Detection Rate** (RTDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-red-team-detection-rate`
- **Name:** Red Team Detection Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RTDR

## 2. Definition

Red Team Detection Rate (RTDR) addresses exposure to adverse outcomes and is a fixture of threat intelligence & red team reporting. The formula is Simulated Attack Techniques Detected by Defenders / Techniques Executed - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of red team attack behaviors detected by blue team defenses during exercises. Detection rate is the most honest measure of defensive readiness available. Scenarios repeated from prior exercises inflate the rate through familiarity. Read with detection rule coverage against MITRE ATT&CK and red team containment time.

## Formula

```
Simulated Attack Techniques Detected by Defenders / Techniques Executed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3284 (batch 7)
