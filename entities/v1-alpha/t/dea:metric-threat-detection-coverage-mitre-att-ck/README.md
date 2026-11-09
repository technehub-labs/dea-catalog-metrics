# dea:metric-threat-detection-coverage-mitre-att-ck

Candidate Performance Metric record for **Threat Detection Coverage (MITRE ATT&CK)** (TDCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-detection-coverage-mitre-att-ck`
- **Name:** Threat Detection Coverage (MITRE ATT&CK)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TDCA

## 2. Definition

Within Threat Intelligence & Red Team, Threat Detection Coverage (MITRE ATT&CK) (TDCA) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Techniques with Detectable Coverage / Prioritized Techniques, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Detection coverage against MITRE ATT&CK measures the share of prioritized adversary techniques for which the organization has a working detection - tested, not merely logged. ATT&CK is the industry's shared language for adversary behavior, which makes this the standard way to answer how good is our coverage honestly. The discipline: score coverage against techniques relevant to your threat profile, verify detections fire in purple-team exercises, and treat data-source gaps as the root cause of most holes. Coverage numbers without validation are aspiration, not capability.

## Formula

```
TDCA = Techniques with Detectable Coverage / Prioritized Techniques
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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

- **Source credit:** MITRE ATT&CK framework

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3283 (batch 7)
