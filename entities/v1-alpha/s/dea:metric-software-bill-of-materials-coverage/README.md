# dea:metric-software-bill-of-materials-coverage

Candidate Performance Metric record for **Software Bill of Materials Coverage** (SBOMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-software-bill-of-materials-coverage`
- **Name:** Software Bill of Materials Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SBOMC

## 2. Definition

A DevSecOps & Application Security Engineering indicator, Software Bill of Materials Coverage (SBOMC) quantifies conformance to standards, plans, or obligations. Its calculation is Artifacts with Generated SBOM / Artifacts, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of applications with a complete, current machine-readable inventory of components and licenses. SBOMs are now a procurement and regulatory expectation, and the only workable basis for responding to the next Log4j-scale event. Manually assembled or stale SBOMs provide compliance theater without response capability. Read with supply chain integrity verification rate and SCA detection rate.

## Formula

```
SBOMC = Artifacts with Generated SBOM / Artifacts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2752 (batch 7)
