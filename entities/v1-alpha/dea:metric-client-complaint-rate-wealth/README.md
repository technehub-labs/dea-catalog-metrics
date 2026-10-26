# dea:metric-client-complaint-rate-wealth

Candidate Performance Metric record for **Client Complaint Rate (Wealth)** (CCR-W) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-complaint-rate-wealth`
- **Name:** Client Complaint Rate (Wealth)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCR-W

## 2. Definition

A Wealth Management indicator, Client Complaint Rate (Wealth) (CCR-W) quantifies the quality of outputs and outcomes. It is computed as Complaints / 1,000 Client Relationships, expressed in events per thousand or million (scaled). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Wealth management.

## 3. Context

Client complaint rate measures formal grievances per client or per account, and in wealth it is the early-warning conduct metric - regulators treat complaint patterns as a diagnostic of firm culture and process quality, and complaint clusters frequently precede enforcement actions. The measurement issue is capture honesty: firms with easy complaint channels look worse than firms that make complaining hard, so a low rate can mean suppressed reporting rather than satisfied clients - which is why regulators increasingly focus on complaint-handling quality, not just volume. Root-cause distribution is the management information: fees, suitability, and service-failure complaints each point at different process fixes. Read with resolution timeliness and fairness (repeat complaints about the same issue signal failed resolution), compensation paid trend, and regulatory-reportable complaint counts.

## Formula

```
Complaints / 1,000 Client Relationships
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1143 (batch 4)
