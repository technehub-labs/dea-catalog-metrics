# dea:metric-loan-portfolio-growth-rate

Candidate Performance Metric record for **Loan Portfolio Growth Rate** (LPGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-portfolio-growth-rate`
- **Name:** Loan Portfolio Growth Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LPGR

## 2. Definition

Loan Portfolio Growth Rate (LPGR) addresses growth over time and is a fixture of retail banking & lending reporting. Its calculation is (Loan Portfolio_current - Portfolio_prior) / Portfolio_prior, measured in percent (%). It originates from and is most used in Banking practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Loan portfolio growth rate measures the expansion of outstanding credit, and it is the growth-versus-credit-quality tension in a single number - lenders that grow faster than their market are usually either winning share through superior efficiency or buying volume through looser underwriting, and history (2008 most notably) shows which is more common in booms. Growth quality shows up with a lag: vintage loss curves take years to reveal whether growth was sound. Growth also carries funding and capital-constraint implications that constrain sustainable rates. Read with yield versus risk-adjusted yield trends (margin compression on new production is a competitive-intensity signal), vintage delinquency curves versus prior cohorts, and growth decomposition by channel and segment.

## Formula

```
(Loan Portfolio_current - Portfolio_prior) / Portfolio_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 841 (batch 3)
