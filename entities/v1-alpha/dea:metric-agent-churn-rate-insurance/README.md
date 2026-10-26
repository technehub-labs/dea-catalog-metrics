# dea:metric-agent-churn-rate-insurance

Candidate Performance Metric record for **Agent Churn Rate (Insurance)** (ACR-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agent-churn-rate-insurance`
- **Name:** Agent Churn Rate (Insurance)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACR-I

## 2. Definition

Agent Churn Rate (Insurance) (ACR-I) captures the retention of customers, users, or assets over time for organizations tracking insurance distribution & agency management. It is computed as Agents Terminating / Appointed Agents, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Insurance.

## 3. Context

Measures producer departures, failures to license, or inactivity. Agent churn destroys the very relationships distribution economics depend on: orphaned policies lapse at elevated rates and acquisition costs never amortize. Distinguish regretted (productive) churn from low-producer attrition, which is healthy culling. Read with orphan policy lapse rates and new-agent survival curves.

## Formula

```
Agents Terminating / Appointed Agents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1738 (batch 6)
