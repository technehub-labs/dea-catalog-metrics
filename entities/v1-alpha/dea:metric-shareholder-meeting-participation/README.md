# dea:metric-shareholder-meeting-participation

Candidate Performance Metric record for **Shareholder Meeting Participation** (SMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shareholder-meeting-participation`
- **Name:** Shareholder Meeting Participation
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SMP

## 2. Definition

Shareholder Meeting Participation (SMP) addresses the engagement or satisfaction of the people involved and is a fixture of corporate governance reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Shares Voted / Shares Outstanding - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Shareholder meeting participation measures the share of shares voting or represented at annual meetings, and it is the engagement-and-legitimacy metric of shareholder democracy - low participation concentrates effective power in whatever bloc does vote, which in practice means passive index funds and activist institutional investors dominate outcomes regardless of the retail majority. The participation landscape has been transformed by retail-direct platforms and by Rule 14a-2 broker-voting restrictions - which banned brokers voting uninstructed retail shares on non-routine items, sharply cutting measured participation and making time-series comparisons treacherous. The metric's real signal is engagement depth: participation without informed voting (robo-vote recommendations) is thin legitimacy. Read with retail-versus-institutional participation split, vote-with-management rates (participation is only meaningful alongside independence of the votes cast), and engagement-outreach program effectiveness.

## Formula

```
Shares Voted / Shares Outstanding
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** corporate_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1045 (batch 4)
