# dea:metric-supply-chain-integrity-verification-rate

Candidate Performance Metric record for **Supply Chain Integrity Verification Rate** (SCIVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-chain-integrity-verification-rate`
- **Name:** Supply Chain Integrity Verification Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCIVR

## 2. Definition

Supply Chain Integrity Verification Rate (SCIVR) measures exposure to adverse outcomes in the DevSecOps & Application Security Engineering domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Artifacts Verified via Signature or Provenance / Artifacts, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of artifacts and dependencies verified against signed provenance before build or deployment. After a run of high-profile supply chain attacks, unsigned artifacts are unmanaged risk. Verification that checks signatures but not provenance lineage (SLSA levels) is partial protection. Read with SBOM coverage and security gate enforcement rate.

## Formula

```
Artifacts Verified via Signature or Provenance / Artifacts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2767 (batch 7)
