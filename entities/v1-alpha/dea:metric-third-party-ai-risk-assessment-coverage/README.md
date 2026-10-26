# dea:metric-third-party-ai-risk-assessment-coverage

Candidate Performance Metric record for **Third-Party AI Risk Assessment Coverage** (TAIRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-third-party-ai-risk-assessment-coverage`
- **Name:** Third-Party AI Risk Assessment Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TAIRA

## 2. Definition

Third-Party AI Risk Assessment Coverage (TAIRA) addresses exposure to adverse outcomes and is a fixture of ai governance & model risk management reporting. Its calculation is Vendor AI Tools Assessed / Tools in Use, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of AI-enabled third-party tools assessed against AI risk standards before and during use. Vendor AI is enterprise AI under most emerging regulatory framings - the deploying company owns outcomes - and unscreened tools concentrate in business-unit purchases that bypass IT governance. Coverage must extend through embedded AI in ordinary software, not just AI-branded products. Read with procurement gate integration and vendor attestation verification sampling.

## Formula

```
Vendor AI Tools Assessed / Tools in Use
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2497 (batch 7)
